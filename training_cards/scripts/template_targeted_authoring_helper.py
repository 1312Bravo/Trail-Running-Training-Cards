from __future__ import annotations

import argparse
from pathlib import Path

from training_cards.cards.examples.macro_example import example_macro_card
from training_cards.cards.examples.mezzo_example import example_mezzo_card
from training_cards.cards.examples.micro_example import example_micro_card
from training_cards.cards.examples.session_example import example_session_card
from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY
from training_cards.json_store import export_card_library_to_json, load_card_library_from_json
from training_cards.pathway import validate_pathway_publish_ready
from training_cards.schemas import BaseTrainingCard


# ---------------------------------------------------------------------------
# Targeted Authoring Template
# ---------------------------------------------------------------------------
# Copy this file or adapt the constants below when a new card batch is easier
# to author with Python classes than by editing JSON directly.

AUTHORED_CARDS: list[BaseTrainingCard] = [
    example_macro_card,
    example_mezzo_card,
    example_micro_card,
    example_session_card,
]

EXAMPLE_OUTPUT_DIR = Path("training_cards/local_cache/authoring_template_output")

UPLOAD_COMMAND_BY_LAYER = {
    "macro": "py -m training_cards.scripts.upload_cache",
    "mezzo": "py -m training_cards.scripts.upload_mezzo_cache",
    "micro": "py -m training_cards.scripts.upload_micro_cache",
    "session": "py -m training_cards.scripts.upload_session_cache",
    "mixed": "py -m training_cards.scripts.upload_cache",
}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Template for class-based targeted card authoring."
    )
    parser.add_argument(
        "--publish-to-cache",
        action="store_true",
        help=(
            "Merge AUTHORED_CARDS into the active local cloud cache. "
            "Refuses example IDs so examples cannot be uploaded by accident."
        ),
    )
    args = parser.parse_args()

    if args.publish_to_cache:
        publish_authored_cards_to_cache(AUTHORED_CARDS)
        return

    export_card_library_to_json(AUTHORED_CARDS, EXAMPLE_OUTPUT_DIR)
    print(f"Exported example authoring library to: {EXAMPLE_OUTPUT_DIR}")
    print_publish_instructions(AUTHORED_CARDS)


def publish_authored_cards_to_cache(cards: list[BaseTrainingCard]) -> None:
    if any(card.id.startswith("example_") or card.slug.startswith("example-") for card in cards):
        raise SystemExit(
            "Refusing to publish example cards into the active cache. "
            "Replace AUTHORED_CARDS with real accepted cards first."
        )

    cache_dir = GOOGLE_DRIVE_LIBRARY.local_cache_dir
    existing_cards = load_card_library_from_json(cache_dir)
    merged_cards = {card.id: card for card in existing_cards}
    merged_cards.update({card.id: card for card in cards})
    final_cards = list(merged_cards.values())

    validate_pathway_publish_ready(final_cards)
    export_card_library_to_json(final_cards, cache_dir)

    print(f"Merged {len(cards)} authored card(s) into active cache: {cache_dir}")
    print_publish_instructions(cards)


def print_publish_instructions(cards: list[BaseTrainingCard]) -> None:
    layers = {str(card.card_type) for card in cards}
    layer = next(iter(layers)) if len(layers) == 1 else "mixed"
    upload_command = UPLOAD_COMMAND_BY_LAYER[layer]

    print("")
    print("Publishing steps for real authored cards:")
    print("1. py -m training_cards.scripts.download_cloud_library")
    print("2. Replace AUTHORED_CARDS in this template with real accepted cards.")
    print("3. py -m training_cards.scripts.template_targeted_authoring_helper --publish-to-cache")
    print("4. py -m training_cards.scripts.validate_cache")
    print("5. py -m training_cards.scripts.build_bundle")
    print(f"6. {upload_command}")
    print("7. For substantial changes, download again and validate the Drive readback.")
    print("")
    print("Do not upload cards from the disposable example output folder.")


if __name__ == "__main__":
    main()
