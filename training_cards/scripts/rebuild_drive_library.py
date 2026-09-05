from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY
from training_cards.google_drive_client import GoogleDriveClient
from training_cards.rebuild_store import (
    archive_active_library,
    publish_library,
    replace_active_library_contents,
    verify_library,
    verify_raw_library,
    write_rebuild_target,
)
from training_cards.json_store import (
    DISPLAY_CONFIG_FILE_NAME,
    LIBRARY_BUNDLE_FILE_NAME,
    MANIFEST_FILE_NAME,
)


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
WORK_DIR = PACKAGE_ROOT / "local_cache" / "rebuild_work"
STAGING_DIR = PACKAGE_ROOT / "local_cache" / "rebuild_staging"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("archive", "publish", "replace-active", "delete-old"))
    parser.add_argument("--former-root-folder-id")
    parser.add_argument("--source-dir", type=Path, default=STAGING_DIR)
    parser.add_argument("--target-file", type=Path, default=WORK_DIR / "replacement_target.json")
    parser.add_argument("--archive-file", type=Path, default=WORK_DIR / "archive_target.json")
    args = parser.parse_args()
    client = GoogleDriveClient()
    WORK_DIR.mkdir(parents=True, exist_ok=True)

    if args.action == "archive":
        archive_config, archive_dir = archive_active_library(client, GOOGLE_DRIVE_LIBRARY, WORK_DIR)
        verified_count = verify_raw_library(client, archive_config, WORK_DIR / "verified_archive")
        write_rebuild_target(args.archive_file, archive_config)
        print(f"Archived and verified {verified_count} cards: {archive_config.root_folder_url}")
        print(f"Local archive: {archive_dir}")
        return

    if args.action == "publish":
        parent_folder_id = client.get_parent_folder_id(GOOGLE_DRIVE_LIBRARY.root_folder_id)
        if parent_folder_id is None:
            parent_folder_id = GOOGLE_DRIVE_LIBRARY.root_folder_id
            print("Current library parent is not accessible; creating the replacement inside its shared container.")
        replacement_config = publish_library(
            client,
            args.source_dir,
            parent_folder_id,
            f"{GOOGLE_DRIVE_LIBRARY.library_name}_rebuild_{date.today():%Y-%m-%d}",
        )
        verified_count = verify_library(client, replacement_config, WORK_DIR / "verified_replacement")
        write_rebuild_target(args.target_file, replacement_config)
        print(f"Published and verified {verified_count} cards: {replacement_config.root_folder_url}")
        return

    if args.action == "replace-active":
        replacement_config = replace_active_library_contents(
            client,
            args.source_dir,
            GOOGLE_DRIVE_LIBRARY,
        )
        verified_count = verify_library(client, replacement_config, WORK_DIR / "verified_replacement")
        write_rebuild_target(args.target_file, replacement_config)
        print(f"Replaced and verified {verified_count} cards in active library: {replacement_config.root_folder_url}")
        return

    if not args.former_root_folder_id:
        parser.error("delete-old requires --former-root-folder-id")
    if args.former_root_folder_id == GOOGLE_DRIVE_LIBRARY.root_folder_id:
        parser.error("delete-old must target the former library, not the configured active library")

    former_items = client.list_folder(args.former_root_folder_id)
    if any(item.id == GOOGLE_DRIVE_LIBRARY.root_folder_id for item in former_items):
        _delete_nested_former_library_contents(client, former_items)
        print("Permanently deleted the former active library contents from the shared container.")
        return

    client.delete_file(args.former_root_folder_id)
    print("Permanently deleted the former active Google Drive library.")


def _delete_nested_former_library_contents(client, former_items) -> None:
    expected_root_file_names = {
        MANIFEST_FILE_NAME,
        DISPLAY_CONFIG_FILE_NAME,
        LIBRARY_BUNDLE_FILE_NAME,
    }
    legacy_cards_folders = [
        item
        for item in former_items
        if item.file_or_folder == "folder" and item.title == "cards"
    ]
    root_files = [item for item in former_items if item.file_or_folder == "file"]

    if len(legacy_cards_folders) != 1:
        raise ValueError("Expected exactly one former 'cards' folder before nested cleanup.")
    if {item.title for item in root_files} != expected_root_file_names:
        raise ValueError("Shared container has unexpected root files; refusing nested cleanup.")

    for item in [*root_files, legacy_cards_folders[0]]:
        client.delete_file(item.id)


if __name__ == "__main__":
    main()
