from training_cards.json_store import refresh_library_bundle
from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY


def main() -> None:
    bundle_path = refresh_library_bundle(GOOGLE_DRIVE_LIBRARY.local_cache_dir)
    print(f"Built training-card library bundle: {bundle_path}")


if __name__ == "__main__":
    main()
