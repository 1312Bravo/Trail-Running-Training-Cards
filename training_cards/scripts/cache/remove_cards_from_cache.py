from __future__ import annotations

import argparse

from training_cards.card_cache_editor import remove_cards_from_cache


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove cards from the downloaded local cache by card ID."
    )
    parser.add_argument("card_ids", nargs="+", help="Card IDs to remove from the local cache.")
    args = parser.parse_args()

    result = remove_cards_from_cache(args.card_ids)
    print(f"Cache: {result['cache_dir']}")
    print(f"Removed: {', '.join(result['removed']) or '-'}")
    print(f"Missing: {', '.join(result['missing']) or '-'}")


if __name__ == "__main__":
    main()
