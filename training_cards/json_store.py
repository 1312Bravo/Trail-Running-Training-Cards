from __future__ import annotations
import json
from pathlib import Path
from typing import Any

from training_cards.serialization import card_from_dict, card_to_dict
from training_cards.schemas import BaseTrainingCard

MANIFEST_FILE_NAME = "manifest.json"
DISPLAY_CONFIG_FILE_NAME = "display_config.json"
LIBRARY_ID = "running_training_cards"
SCHEMA_VERSION = "1.0.0"
LIBRARY_VERSION = "0.1.0"
LAST_UPDATED = "2026-08-01"
CARDS_ROOT = "cards"

CARD_TYPE_FOLDER = {
    "macro": "macro",
    "mezzo": "mezzo",
    "micro": "micro",
    "session": "session",
}

# Define how consumers should present the card library without owning card meaning.
def build_display_config() -> dict[str, Any]:
    return {
        "display_config_version": "1.0.0",
        "schema_version": SCHEMA_VERSION,
        "system_fields": [
            "id",
            "slug",
        ],
        "preview_fields": [
            "title",
            "card_type",
            "summary",
            "purpose",
            "suitable_levels",
            "tags",
        ],
        "preview_field_rules": {
            "summary": {
                "max_sentences": 1,
                "target_words": "12-22",
                "role": "Concise preview sentence for quick card comparison.",
            },
        },
        "detail_field_order": [
            "detailed_description",
            "recommended_duration_weeks",
            "recommended_duration_days",
            "typical_duration",
            "goal_race_context",
            "when_to_choose",
            "when_not_to_choose",
            "expected_adaptations",
            "training_characteristics",
            "terrain_demands",
            "common_mistakes",
            "warning_signs",
            "progression_rules",
            "regression_rules",
            "workout_parts",
            "references",
        ],
        "field_labels": {
            "id": "Card ID",
            "slug": "Slug",
            "title": "Title",
            "card_type": "Planning level",
            "summary": "Summary",
            "purpose": "Purpose",
            "suitable_levels": "Suitable for",
            "tags": "Tags",
            "detailed_description": "Detailed description",
            "recommended_duration_weeks": "Recommended duration",
            "recommended_duration_days": "Recommended duration",
            "typical_duration": "Typical duration",
            "goal_race_context": "Goal race context",
            "when_to_choose": "When to choose",
            "when_not_to_choose": "When not to choose",
            "expected_adaptations": "Expected adaptations",
            "training_characteristics": "Training characteristics",
            "terrain_demands": "Terrain demands",
            "common_mistakes": "Common mistakes",
            "warning_signs": "Warning signs",
            "progression_rules": "Progression rules",
            "regression_rules": "Regression rules",
            "workout_parts": "Workout guide",
            "references": "Linked cards",
        },
        "card_type_labels": {
            "macro": "Macro phases",
            "mezzo": "Mezzo blocks",
            "micro": "Micro weeks",
            "session": "Sessions",
        },
    }

# Write formatted JSON in the same style for manifest and card files.
def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents = True, exist_ok = True)
    path.write_text(
        json.dumps(data, indent = 2, ensure_ascii = False) + "\n",
        encoding = "utf-8",
    )


# Read one JSON file.
def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding = "utf-8"))


# Build the table of contents for the cloud/local JSON card library.
def build_manifest(cards: list[BaseTrainingCard]) -> dict[str, Any]:
    card_items = [
        {
            "id": card.id,
            "slug": card.slug,
            "card_type": str(card.card_type),
            "title": card.title,
        }
        for card in sorted(cards, key = lambda card: card.id)
    ]

    return {
        "library_id": LIBRARY_ID,
        "schema_version": SCHEMA_VERSION,
        "library_version": LIBRARY_VERSION,
        "updated_at": LAST_UPDATED,
        "cards_root": CARDS_ROOT,
        "card_count": len(card_items),
        "cards": card_items,
    }

# Read a manifest file from a local cloud-library cache.
def load_manifest(input_dir: Path) -> dict[str, Any]:
    return read_json(input_dir / MANIFEST_FILE_NAME)

# Read display rules from a local cloud-library cache.
def load_display_config(input_dir: Path) -> dict[str, Any]:
    return read_json(input_dir / DISPLAY_CONFIG_FILE_NAME)

# Check that display metadata matches the active card schema.
def validate_display_config(display_config: dict[str, Any], manifest: dict[str, Any]) -> None:
    if display_config["schema_version"] != manifest["schema_version"]:
        raise ValueError(
            "Display config schema_version does not match manifest schema_version."
        )

# Check the manifest and card objects before the app trusts the library.
def validate_card_library(cards: list[BaseTrainingCard], manifest: dict[str, Any]) -> None:
    if manifest["library_id"] != LIBRARY_ID:
        raise ValueError(f"Unexpected card library id: {manifest['library_id']}")
    if manifest["schema_version"] != SCHEMA_VERSION:
        raise ValueError(f"Unsupported card schema version: {manifest['schema_version']}")
    if manifest["card_count"] != len(cards):
        raise ValueError(f"Manifest expects {manifest['card_count']} cards, but loaded {len(cards)}.")

    ids = [card.id for card in cards]
    slugs = [card.slug for card in cards]
    manifest_ids = [card["id"] for card in manifest["cards"]]

    if len(ids) != len(set(ids)):
        raise ValueError("Training card library contains duplicate card IDs.")
    if len(slugs) != len(set(slugs)):
        raise ValueError("Training card library contains duplicate card slugs.")
    if set(ids) != set(manifest_ids):
        raise ValueError("Training card IDs do not match manifest card IDs.")

    missing_references = sorted(
        {
            reference.card_id
            for card in cards
            for reference in card.references
            if reference.card_id not in ids
        }
    )
    if missing_references:
        raise ValueError(f"Training card library has broken references: {missing_references}")

# Write cards as one JSON file per card, grouped by planning level.
# This is used for local cache/export now and can support cloud upload later.
def export_cards_to_json(cards: list[BaseTrainingCard], output_dir: Path) -> None:
    for card in cards:
        type_dir = output_dir / CARD_TYPE_FOLDER[str(card.card_type)]
        write_json(type_dir / f"{card.slug}.json", card_to_dict(card))

# Write a complete local copy of the cloud-style library: manifest plus cards.
def export_card_library_to_json(cards: list[BaseTrainingCard], output_dir: Path) -> None:
    manifest = build_manifest(cards)

    write_json(output_dir / MANIFEST_FILE_NAME, manifest)
    write_json(output_dir / DISPLAY_CONFIG_FILE_NAME, build_display_config())
    export_cards_to_json(cards, output_dir / CARDS_ROOT)

# Load JSON card files under macro/mezzo/micro/session folders and validate
# them by rebuilding the dataclass objects.
def load_cards_from_json(input_dir: Path) -> list[BaseTrainingCard]:
    cards = []

    for path in sorted(input_dir.glob("*/*.json")):
        cards.append(card_from_dict(read_json(path)))

    return cards

# Load a complete local cloud-library cache and validate it against manifest.json.
def load_card_library_from_json(input_dir: Path) -> list[BaseTrainingCard]:
    manifest = load_manifest(input_dir)
    display_config = load_display_config(input_dir)
    cards = load_cards_from_json(input_dir / manifest["cards_root"])

    validate_display_config(display_config, manifest)
    validate_card_library(cards, manifest)

    return cards

