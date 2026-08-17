from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY
from training_cards.json_store import (
    CARDS_ROOT,
    export_card_library_to_json,
    load_card_library_from_json,
    load_cards_from_json,
)


def main() -> None:
    cache_dir = GOOGLE_DRIVE_LIBRARY.local_cache_dir
    cards = load_cards_from_json(cache_dir / CARDS_ROOT)

    # Old card JSON omits the field; schema defaults assign those cards to common.
    export_card_library_to_json(cards, cache_dir)
    load_card_library_from_json(cache_dir)

    print(f"Migrated philosophy_profile_ids for {len(cards)} cached cards.")


if __name__ == "__main__":
    main()
