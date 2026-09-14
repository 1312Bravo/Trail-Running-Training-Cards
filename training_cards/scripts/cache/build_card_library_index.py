from __future__ import annotations

from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY
from training_cards.json_store import CARD_LIBRARY_INDEX_FILE_NAME, refresh_library_bundle


def main() -> None:
    refresh_library_bundle(GOOGLE_DRIVE_LIBRARY.local_cache_dir)
    print(GOOGLE_DRIVE_LIBRARY.local_cache_dir / CARD_LIBRARY_INDEX_FILE_NAME)


if __name__ == "__main__":
    main()
