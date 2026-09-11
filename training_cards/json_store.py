from __future__ import annotations
import json
from pathlib import Path
from typing import Any

from training_cards.serialization import (
    card_from_dict,
    card_to_dict,
)
from training_cards.macro_mezzo_reuse import (
    VALID_REUSE_TYPES,
    build_macro_mezzo_reuse_config,
)
from training_cards.mezzo_micro_reuse import build_mezzo_micro_reuse_config
from training_cards.micro_session_reuse import build_micro_session_reuse_config
from training_cards.philosophy_profiles import validate_philosophy_profile_ids
from training_cards.schemas import BaseTrainingCard

MANIFEST_FILE_NAME = "manifest.json"
DISPLAY_CONFIG_FILE_NAME = "display_config.json"
MACRO_MEZZO_REUSE_FILE_NAME = "macro_mezzo_reuse.json"
MEZZO_MICRO_REUSE_FILE_NAME = "mezzo_micro_reuse.json"
MICRO_SESSION_REUSE_FILE_NAME = "micro_session_reuse.json"
LIBRARY_BUNDLE_FILE_NAME = "training_cards_library.json"
LIBRARY_ID = "running_training_cards"
SCHEMA_VERSION = "1.3.0"
LIBRARY_VERSION = "0.8.0"
LAST_UPDATED = "2026-09-10"
CARDS_ROOT = "cards"
MULTI_PROFILE_CARD_FOLDER = "multi_profile"

CARD_TYPE_FOLDER = {
    "macro": "macro",
    "mezzo": "mezzo",
    "micro": "micro",
    "session": "session",
}


def card_profile_folder(card: BaseTrainingCard) -> str:
    if len(card.philosophy_profile_ids) == 1:
        return card.philosophy_profile_ids[0]

    return MULTI_PROFILE_CARD_FOLDER


def card_storage_path(card: BaseTrainingCard) -> Path:
    return Path(CARD_TYPE_FOLDER[str(card.card_type)]) / card_profile_folder(card) / f"{card.slug}.json"

# Define how consumers should present the card library without owning card meaning.
def build_display_config() -> dict[str, Any]:
    return {
        "display_config_version": "1.3.0",
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
            "philosophy_profile_ids",
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
            "additional_information",
            "recommended_duration_weeks",
            "recommended_duration_days",
            "typical_duration",
            "timing_guidance",
            "placement_guidance",
            "session_family",
            "week_structure",
            "key_sessions",
            "load_pattern",
            "recovery_requirements",
            "goal_race_context",
            "training_profile",
            "expected_adaptations",
            "watchouts",
            "progression_rules",
            "regression_rules",
            "workout_blocks",
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
            "philosophy_profile_ids": "Coaching philosophy",
            "tags": "Tags",
            "additional_information": "Additional information",
            "recommended_duration_weeks": "Recommended duration",
            "recommended_duration_days": "Recommended duration",
            "typical_duration": "Typical duration",
            "timing_guidance": "Timing guidance",
            "placement_guidance": "Placement guidance",
            "session_family": "Session family",
            "week_structure": "Week structure",
            "key_sessions": "Key sessions",
            "load_pattern": "Load pattern",
            "recovery_requirements": "Recovery requirements",
            "goal_race_context": "Goal race context",
            "training_profile": "Training profile",
            "expected_adaptations": "Expected adaptations",
            "watchouts": "Watchouts",
            "progression_rules": "Progression rules",
            "regression_rules": "Regression rules",
            "workout_blocks": "Workout guide",
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
            "profile_folder": card_profile_folder(card),
            "storage_path": str(card_storage_path(card)).replace("\\", "/"),
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

# Build one complete app-facing bundle from validated card objects.
def build_library_bundle(
    cards: list[BaseTrainingCard],
    manifest: dict[str, Any],
    display_config: dict[str, Any],
    macro_mezzo_reuse_config: dict[str, Any],
    mezzo_micro_reuse_config: dict[str, Any],
    micro_session_reuse_config: dict[str, Any],
) -> dict[str, Any]:
    return {
        "manifest": manifest,
        "display_config": display_config,
        "macro_mezzo_reuse": macro_mezzo_reuse_config,
        "mezzo_micro_reuse": mezzo_micro_reuse_config,
        "micro_session_reuse": micro_session_reuse_config,
        "cards": [
            card_to_dict(card)
            for card in sorted(cards, key = lambda card: card.id)
        ],
    }

# Read a manifest file from a local cloud-library cache.
def load_manifest(input_dir: Path) -> dict[str, Any]:
    return read_json(input_dir / MANIFEST_FILE_NAME)

# Read display rules from a local cloud-library cache.
def load_display_config(input_dir: Path) -> dict[str, Any]:
    return read_json(input_dir / DISPLAY_CONFIG_FILE_NAME)


# Read macro-to-mezzo reuse metadata from a local cloud-library cache.
def load_macro_mezzo_reuse_config(input_dir: Path) -> dict[str, Any]:
    path = input_dir / MACRO_MEZZO_REUSE_FILE_NAME
    if not path.exists():
        return build_macro_mezzo_reuse_config(SCHEMA_VERSION, card_ids=set())

    return read_json(path)


def build_macro_mezzo_reuse_config_for_cards(cards: list[BaseTrainingCard]) -> dict[str, Any]:
    return build_macro_mezzo_reuse_config(
        SCHEMA_VERSION,
        card_ids={card.id for card in cards},
    )


def write_macro_mezzo_reuse_config(output_dir: Path, cards: list[BaseTrainingCard]) -> Path:
    path = output_dir / MACRO_MEZZO_REUSE_FILE_NAME
    write_json(path, build_macro_mezzo_reuse_config_for_cards(cards))
    return path


# Read mezzo-to-micro reuse metadata from a local cloud-library cache.
def load_mezzo_micro_reuse_config(input_dir: Path) -> dict[str, Any]:
    path = input_dir / MEZZO_MICRO_REUSE_FILE_NAME
    if not path.exists():
        return build_mezzo_micro_reuse_config(
            SCHEMA_VERSION,
            cards=[],
            macro_mezzo_reuse_config=build_macro_mezzo_reuse_config_for_cards([]),
        )

    return read_json(path)


def build_mezzo_micro_reuse_config_for_cards(cards: list[BaseTrainingCard]) -> dict[str, Any]:
    return build_mezzo_micro_reuse_config(
        SCHEMA_VERSION,
        cards=cards,
        macro_mezzo_reuse_config=build_macro_mezzo_reuse_config_for_cards(cards),
    )


def write_mezzo_micro_reuse_config(output_dir: Path, cards: list[BaseTrainingCard]) -> Path:
    path = output_dir / MEZZO_MICRO_REUSE_FILE_NAME
    write_json(path, build_mezzo_micro_reuse_config_for_cards(cards))
    return path


# Read micro-to-session reuse metadata from a local cloud-library cache.
def load_micro_session_reuse_config(input_dir: Path) -> dict[str, Any]:
    path = input_dir / MICRO_SESSION_REUSE_FILE_NAME
    if not path.exists():
        return build_micro_session_reuse_config(
            SCHEMA_VERSION,
            cards=[],
            mezzo_micro_reuse_config=build_mezzo_micro_reuse_config_for_cards([]),
        )

    return read_json(path)


def build_micro_session_reuse_config_for_cards(cards: list[BaseTrainingCard]) -> dict[str, Any]:
    return build_micro_session_reuse_config(
        SCHEMA_VERSION,
        cards=cards,
        mezzo_micro_reuse_config=build_mezzo_micro_reuse_config_for_cards(cards),
    )


def write_micro_session_reuse_config(output_dir: Path, cards: list[BaseTrainingCard]) -> Path:
    path = output_dir / MICRO_SESSION_REUSE_FILE_NAME
    write_json(path, build_micro_session_reuse_config_for_cards(cards))
    return path

# Check that display metadata matches the active card schema.
def validate_display_config(display_config: dict[str, Any], manifest: dict[str, Any]) -> None:
    if display_config["schema_version"] != manifest["schema_version"]:
        raise ValueError(
            "Display config schema_version does not match manifest schema_version."
        )


def validate_macro_mezzo_reuse_config(
    macro_mezzo_reuse_config: dict[str, Any],
    manifest: dict[str, Any],
) -> None:
    if macro_mezzo_reuse_config["schema_version"] != manifest["schema_version"]:
        raise ValueError(
            "Macro-mezzo reuse schema_version does not match manifest schema_version."
        )

    manifest_cards = {card["id"]: card for card in manifest["cards"]}
    entries = macro_mezzo_reuse_config.get("entries", [])
    if macro_mezzo_reuse_config.get("entry_count") != len(entries):
        raise ValueError("Macro-mezzo reuse entry_count does not match entries length.")

    required_fields = {
        "philosophy_profile_id",
        "macro_card_id",
        "macro_card_name",
        "reused_mezzo_card_id",
        "reused_mezzo_card_name",
        "reuse_type",
    }
    for entry in entries:
        missing_fields = sorted(required_fields - set(entry))
        if missing_fields:
            raise ValueError(f"Macro-mezzo reuse entry has missing fields: {missing_fields}")
        validate_philosophy_profile_ids([entry["philosophy_profile_id"]])
        if entry["reuse_type"] not in VALID_REUSE_TYPES:
            raise ValueError(
                f"Macro-mezzo reuse entry has unknown reuse_type: {entry['reuse_type']}."
            )

        macro_card = manifest_cards.get(entry["macro_card_id"])
        reused_mezzo_card = manifest_cards.get(entry["reused_mezzo_card_id"])
        if macro_card is None:
            raise ValueError(
                f"Macro-mezzo reuse points to missing macro card {entry['macro_card_id']}."
            )
        if reused_mezzo_card is None:
            raise ValueError(
                "Macro-mezzo reuse points to missing mezzo card "
                f"{entry['reused_mezzo_card_id']}."
            )
        if macro_card["card_type"] != "macro":
            raise ValueError(
                f"Macro-mezzo reuse macro_card_id is not a macro card: {entry['macro_card_id']}."
            )
        if reused_mezzo_card["card_type"] != "mezzo":
            raise ValueError(
                "Macro-mezzo reuse reused_mezzo_card_id is not a mezzo card: "
                f"{entry['reused_mezzo_card_id']}."
            )
        if macro_card["title"] != entry["macro_card_name"]:
            raise ValueError(
                f"Macro-mezzo reuse macro_card_name is stale for {entry['macro_card_id']}."
            )
        if reused_mezzo_card["title"] != entry["reused_mezzo_card_name"]:
            raise ValueError(
                "Macro-mezzo reuse reused_mezzo_card_name is stale for "
                f"{entry['reused_mezzo_card_id']}."
            )


def validate_mezzo_micro_reuse_config(
    mezzo_micro_reuse_config: dict[str, Any],
    manifest: dict[str, Any],
) -> None:
    if mezzo_micro_reuse_config["schema_version"] != manifest["schema_version"]:
        raise ValueError(
            "Mezzo-micro reuse schema_version does not match manifest schema_version."
        )

    manifest_cards = {card["id"]: card for card in manifest["cards"]}
    entries = mezzo_micro_reuse_config.get("entries", [])
    if mezzo_micro_reuse_config.get("entry_count") != len(entries):
        raise ValueError("Mezzo-micro reuse entry_count does not match entries length.")

    required_fields = {
        "philosophy_profile_id",
        "mezzo_card_id",
        "mezzo_card_name",
        "reused_micro_card_id",
        "reused_micro_card_name",
        "reuse_type",
    }
    for entry in entries:
        missing_fields = sorted(required_fields - set(entry))
        if missing_fields:
            raise ValueError(f"Mezzo-micro reuse entry has missing fields: {missing_fields}")
        validate_philosophy_profile_ids([entry["philosophy_profile_id"]])
        if entry["reuse_type"] not in VALID_REUSE_TYPES:
            raise ValueError(
                f"Mezzo-micro reuse entry has unknown reuse_type: {entry['reuse_type']}."
            )

        mezzo_card = manifest_cards.get(entry["mezzo_card_id"])
        reused_micro_card = manifest_cards.get(entry["reused_micro_card_id"])
        if mezzo_card is None:
            raise ValueError(
                f"Mezzo-micro reuse points to missing mezzo card {entry['mezzo_card_id']}."
            )
        if reused_micro_card is None:
            raise ValueError(
                "Mezzo-micro reuse points to missing micro card "
                f"{entry['reused_micro_card_id']}."
            )
        if mezzo_card["card_type"] != "mezzo":
            raise ValueError(
                f"Mezzo-micro reuse mezzo_card_id is not a mezzo card: {entry['mezzo_card_id']}."
            )
        if reused_micro_card["card_type"] != "micro":
            raise ValueError(
                "Mezzo-micro reuse reused_micro_card_id is not a micro card: "
                f"{entry['reused_micro_card_id']}."
            )
        if mezzo_card["title"] != entry["mezzo_card_name"]:
            raise ValueError(
                f"Mezzo-micro reuse mezzo_card_name is stale for {entry['mezzo_card_id']}."
            )
        if reused_micro_card["title"] != entry["reused_micro_card_name"]:
            raise ValueError(
                "Mezzo-micro reuse reused_micro_card_name is stale for "
                f"{entry['reused_micro_card_id']}."
            )


def validate_micro_session_reuse_config(
    micro_session_reuse_config: dict[str, Any],
    manifest: dict[str, Any],
) -> None:
    if micro_session_reuse_config["schema_version"] != manifest["schema_version"]:
        raise ValueError(
            "Micro-session reuse schema_version does not match manifest schema_version."
        )

    manifest_cards = {card["id"]: card for card in manifest["cards"]}
    entries = micro_session_reuse_config.get("entries", [])
    if micro_session_reuse_config.get("entry_count") != len(entries):
        raise ValueError("Micro-session reuse entry_count does not match entries length.")

    required_fields = {
        "philosophy_profile_id",
        "micro_card_id",
        "micro_card_name",
        "reused_session_card_id",
        "reused_session_card_name",
        "reuse_type",
    }
    for entry in entries:
        missing_fields = sorted(required_fields - set(entry))
        if missing_fields:
            raise ValueError(f"Micro-session reuse entry has missing fields: {missing_fields}")
        validate_philosophy_profile_ids([entry["philosophy_profile_id"]])
        if entry["reuse_type"] not in VALID_REUSE_TYPES:
            raise ValueError(
                f"Micro-session reuse entry has unknown reuse_type: {entry['reuse_type']}."
            )

        micro_card = manifest_cards.get(entry["micro_card_id"])
        reused_session_card = manifest_cards.get(entry["reused_session_card_id"])
        if micro_card is None:
            raise ValueError(
                f"Micro-session reuse points to missing micro card {entry['micro_card_id']}."
            )
        if reused_session_card is None:
            raise ValueError(
                "Micro-session reuse points to missing session card "
                f"{entry['reused_session_card_id']}."
            )
        if micro_card["card_type"] != "micro":
            raise ValueError(
                f"Micro-session reuse micro_card_id is not a micro card: {entry['micro_card_id']}."
            )
        if reused_session_card["card_type"] != "session":
            raise ValueError(
                "Micro-session reuse reused_session_card_id is not a session card: "
                f"{entry['reused_session_card_id']}."
            )
        if micro_card["title"] != entry["micro_card_name"]:
            raise ValueError(
                f"Micro-session reuse micro_card_name is stale for {entry['micro_card_id']}."
            )
        if reused_session_card["title"] != entry["reused_session_card_name"]:
            raise ValueError(
                "Micro-session reuse reused_session_card_name is stale for "
                f"{entry['reused_session_card_id']}."
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

# Write the app-facing one-file library bundle.
def write_library_bundle(
    output_dir: Path,
    cards: list[BaseTrainingCard],
    manifest: dict[str, Any] | None = None,
    display_config: dict[str, Any] | None = None,
    macro_mezzo_reuse_config: dict[str, Any] | None = None,
    mezzo_micro_reuse_config: dict[str, Any] | None = None,
    micro_session_reuse_config: dict[str, Any] | None = None,
) -> Path:
    manifest = manifest or build_manifest(cards)
    display_config = display_config or build_display_config()
    macro_mezzo_reuse_config = (
        macro_mezzo_reuse_config or build_macro_mezzo_reuse_config_for_cards(cards)
    )
    mezzo_micro_reuse_config = (
        mezzo_micro_reuse_config or build_mezzo_micro_reuse_config_for_cards(cards)
    )
    micro_session_reuse_config = (
        micro_session_reuse_config or build_micro_session_reuse_config_for_cards(cards)
    )
    bundle = build_library_bundle(
        cards,
        manifest,
        display_config,
        macro_mezzo_reuse_config,
        mezzo_micro_reuse_config,
        micro_session_reuse_config,
    )
    bundle_path = output_dir / LIBRARY_BUNDLE_FILE_NAME

    write_json(bundle_path, bundle)
    return bundle_path

# Write cards as one JSON file per card, grouped by planning level and profile folder.
# This is used for local cache/export now and can support cloud upload later.
def export_cards_to_json(cards: list[BaseTrainingCard], output_dir: Path) -> None:
    for card in cards:
        write_json(output_dir / card_storage_path(card), card_to_dict(card))

# Write a complete local copy of the cloud-style library: manifest plus cards.
def export_card_library_to_json(cards: list[BaseTrainingCard], output_dir: Path) -> None:
    manifest = build_manifest(cards)
    display_config = build_display_config()
    macro_mezzo_reuse_config = build_macro_mezzo_reuse_config_for_cards(cards)
    mezzo_micro_reuse_config = build_mezzo_micro_reuse_config_for_cards(cards)
    micro_session_reuse_config = build_micro_session_reuse_config_for_cards(cards)

    write_json(output_dir / MANIFEST_FILE_NAME, manifest)
    write_json(output_dir / DISPLAY_CONFIG_FILE_NAME, display_config)
    write_json(output_dir / MACRO_MEZZO_REUSE_FILE_NAME, macro_mezzo_reuse_config)
    write_json(output_dir / MEZZO_MICRO_REUSE_FILE_NAME, mezzo_micro_reuse_config)
    write_json(output_dir / MICRO_SESSION_REUSE_FILE_NAME, micro_session_reuse_config)
    export_cards_to_json(cards, output_dir / CARDS_ROOT)
    write_library_bundle(
        output_dir,
        cards,
        manifest,
        display_config,
        macro_mezzo_reuse_config,
        mezzo_micro_reuse_config,
        micro_session_reuse_config,
    )

# Load JSON card files under macro/mezzo/micro/session folders and validate them
# by rebuilding the dataclass objects. Nested profile folders are preferred, but
# this still reads older flat type folders while old archives exist.
def load_cards_from_json(input_dir: Path) -> list[BaseTrainingCard]:
    cards = []

    for path in sorted(input_dir.rglob("*.json")):
        cards.append(card_from_dict(read_json(path)))

    return cards

# Load a complete local cloud-library cache and validate it against manifest.json.
def load_card_library_from_json(input_dir: Path) -> list[BaseTrainingCard]:
    manifest = load_manifest(input_dir)
    display_config = load_display_config(input_dir)
    macro_mezzo_reuse_config = load_macro_mezzo_reuse_config(input_dir)
    mezzo_micro_reuse_config = load_mezzo_micro_reuse_config(input_dir)
    micro_session_reuse_config = load_micro_session_reuse_config(input_dir)
    cards = load_cards_from_json(input_dir / manifest["cards_root"])

    validate_display_config(display_config, manifest)
    validate_macro_mezzo_reuse_config(macro_mezzo_reuse_config, manifest)
    validate_mezzo_micro_reuse_config(mezzo_micro_reuse_config, manifest)
    validate_micro_session_reuse_config(micro_session_reuse_config, manifest)
    validate_card_library(cards, manifest)

    return cards

# Validate the local cache, then refresh the app-facing one-file bundle.
def refresh_library_bundle(input_dir: Path) -> Path:
    cards = load_card_library_from_json(input_dir)
    return write_library_bundle(
        input_dir,
        cards,
        load_manifest(input_dir),
        load_display_config(input_dir),
        load_macro_mezzo_reuse_config(input_dir),
        load_mezzo_micro_reuse_config(input_dir),
        load_micro_session_reuse_config(input_dir),
    )

