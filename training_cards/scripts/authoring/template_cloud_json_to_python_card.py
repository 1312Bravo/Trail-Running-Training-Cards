from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY
from training_cards.cloud_store import load_cached_cloud_library
from training_cards.json_store import card_storage_path
from training_cards.serialization import card_to_dict


# ---------------------------------------------------------------------------
# Cloud JSON -> Local Python Authoring Template
# ---------------------------------------------------------------------------
# Use this when one existing cloud/cache JSON card should become a temporary
# local Python authoring file. Do not use it to recreate the full seed library.

DEFAULT_OUTPUT_DIR = Path("training_cards/local_cache/python_authoring")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a local Python authoring file from one downloaded cloud/cache JSON card."
    )
    selector = parser.add_mutually_exclusive_group(required=True)
    selector.add_argument("--card-id", help="Card ID to convert, for example macro_001.")
    selector.add_argument("--slug", help="Card slug to convert, for example mainstream-base-development.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Folder for the generated temporary Python authoring file.",
    )
    args = parser.parse_args()

    cards = load_cached_cloud_library(GOOGLE_DRIVE_LIBRARY)
    card = next(
        (
            card
            for card in cards
            if (args.card_id and card.id == args.card_id)
            or (args.slug and card.slug == args.slug)
        ),
        None,
    )

    if card is None:
        raise SystemExit("Card not found in local cache. Run download_cloud_library first.")

    output_path = args.output_dir / f"{safe_python_name(card.slug)}.py"
    write_python_authoring_file(output_path, card)

    print(f"Wrote local Python authoring file: {output_path}")
    print("")
    print("Next steps:")
    print("1. Edit the generated CARD_DATA carefully.")
    print("2. Import AUTHORED_CARD from this file in a targeted authoring helper.")
    print("3. Publish the edited card into the local cache.")
    print("4. Validate, build the bundle, and upload the relevant cache files to Drive.")
    print("")
    print(f"Original cloud/cache JSON path: cards/{card_storage_path(card)}")


def write_python_authoring_file(path: Path, card) -> None:
    card_data = card_to_dict(card)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "from training_cards.serialization import card_from_dict",
                "",
                "",
                "# Temporary authoring file generated from downloaded cloud/cache JSON.",
                "# Edit CARD_DATA, then import AUTHORED_CARD in a targeted helper.",
                "CARD_DATA = "
                + json.dumps(card_data, indent=4, ensure_ascii=False).replace("\n", "\n"),
                "",
                "AUTHORED_CARD = card_from_dict(CARD_DATA)",
                "",
            ]
        ),
        encoding="utf-8",
    )


def safe_python_name(slug: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9_]+", "_", slug).strip("_").lower()
    if not name:
        return "authored_card"
    if name[0].isdigit():
        return f"card_{name}"
    return name


if __name__ == "__main__":
    main()
