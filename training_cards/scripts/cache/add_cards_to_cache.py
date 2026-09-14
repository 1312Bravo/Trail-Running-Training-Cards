from __future__ import annotations

import argparse
from pathlib import Path

from training_cards.card_cache_editor import (
    add_or_update_cards_in_cache,
    load_authored_cards_from_files,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add or replace authored card JSON/Python files in the downloaded local cache."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="Card JSON files or Python files defining AUTHORED_CARD/AUTHORED_CARDS.",
    )
    args = parser.parse_args()

    cards = load_authored_cards_from_files(args.paths)
    result = add_or_update_cards_in_cache(cards)
    print(f"Cache: {result['cache_dir']}")
    print(f"Added: {', '.join(result['added']) or '-'}")
    print(f"Updated: {', '.join(result['updated']) or '-'}")


if __name__ == "__main__":
    main()
