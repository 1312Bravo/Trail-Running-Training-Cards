from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from training_cards.card_library_index import validate_card_library_index
from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY
from training_cards.json_store import (
    LIBRARY_BUNDLE_FILE_NAME,
    load_library_bundle_from_json,
    read_json,
)
from training_cards.philosophy_profiles import PHILOSOPHY_PROFILES
from streamlit_app.philosophy_content import (
    load_app_summary,
    load_detailed_note,
    load_reviewed_source_bullets,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
WEB_DATA_PATH = REPOSITORY_ROOT / "vite_app" / "public" / "data" / "library.json"


def build_web_library_data(cache_dir: Path) -> dict[str, Any]:
    """Validate the Drive bundle and add the reviewed philosophy copy for the web UI."""
    bundle_path = cache_dir / LIBRARY_BUNDLE_FILE_NAME
    if not bundle_path.exists():
        raise FileNotFoundError(
            f"Validated card bundle not found at {bundle_path}. "
            "Download the Drive library or build its bundle before preparing the web app."
        )

    bundle = read_json(bundle_path)
    cards, _, _, _, _, card_library_index = load_library_bundle_from_json(bundle_path)
    validate_card_library_index(
        card_library_index,
        cards,
        schema_version=bundle["manifest"]["schema_version"],
        library_version=bundle["manifest"]["library_version"],
    )

    bundle["philosophies"] = {
        profile_id: {
            "name": profile_name,
            "summary": load_app_summary(profile_id),
            "detail": load_detailed_note(profile_id),
            "sources": load_reviewed_source_bullets(profile_id),
        }
        for profile_id, profile_name in PHILOSOPHY_PROFILES.items()
    }
    return bundle


def main() -> None:
    data = build_web_library_data(GOOGLE_DRIVE_LIBRARY.local_cache_dir)
    WEB_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    WEB_DATA_PATH.write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"Prepared public web library: {WEB_DATA_PATH} ({len(data['cards'])} cards)")


if __name__ == "__main__":
    main()
