from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

from training_cards.cloud_config import (
    GOOGLE_DRIVE_LIBRARY,
    GoogleDriveLibraryConfig,
)
from training_cards.json_store import (
    CARDS_ROOT,
    CARD_LIBRARY_INDEX_FILE_NAME,
    DISPLAY_CONFIG_FILE_NAME,
    LIBRARY_BUNDLE_FILE_NAME,
    MACRO_MEZZO_REUSE_FILE_NAME,
    MANIFEST_FILE_NAME,
    MEZZO_MICRO_REUSE_FILE_NAME,
    MICRO_SESSION_REUSE_FILE_NAME,
    build_display_config,
    build_macro_mezzo_reuse_config_for_cards,
    build_mezzo_micro_reuse_config_for_cards,
    build_micro_session_reuse_config_for_cards,
    load_card_library_from_json,
    refresh_library_bundle,
    write_macro_mezzo_reuse_config,
    write_mezzo_micro_reuse_config,
    write_micro_session_reuse_config,
    write_json,
)
from training_cards.pathway import validate_pathway_publish_ready
from training_cards.schemas import BaseTrainingCard


@dataclass(frozen=True, slots=True)
class DriveItem:
    id: str
    title: str
    file_or_folder: str


# Return the canonical Google Drive folder URL for the card library.
def get_cloud_library_url(config: GoogleDriveLibraryConfig = GOOGLE_DRIVE_LIBRARY) -> str:
    return config.root_folder_url


# Load and validate the current local cloud-library cache.
def load_cached_cloud_library(config: GoogleDriveLibraryConfig = GOOGLE_DRIVE_LIBRARY) -> list[BaseTrainingCard]:
    return load_card_library_from_json(config.local_cache_dir)


# Download the Drive library into local cache through a concrete Drive client.
def download_cloud_library(
    client,
    config: GoogleDriveLibraryConfig = GOOGLE_DRIVE_LIBRARY,
    *,
    validate_download: bool = True,
) -> Path:
    config.local_cache_dir.mkdir(parents = True, exist_ok = True)
    _clear_cached_json_files(config.local_cache_dir)

    cards_dir = config.local_cache_dir / CARDS_ROOT
    cards_dir.mkdir(parents = True, exist_ok = True)

    manifest = _find_drive_item(client.list_folder(config.root_folder_id), MANIFEST_FILE_NAME)
    client.download_file(manifest.id, config.local_cache_dir / MANIFEST_FILE_NAME)

    root_items = client.list_folder(config.root_folder_id)
    display_config = _maybe_find_drive_item(root_items, DISPLAY_CONFIG_FILE_NAME)

    if display_config is None:
        write_json(config.local_cache_dir / DISPLAY_CONFIG_FILE_NAME, build_display_config())
    else:
        client.download_file(display_config.id, config.local_cache_dir / DISPLAY_CONFIG_FILE_NAME)

    macro_mezzo_reuse = _maybe_find_drive_item(root_items, MACRO_MEZZO_REUSE_FILE_NAME)
    if macro_mezzo_reuse is None:
        write_json(
            config.local_cache_dir / MACRO_MEZZO_REUSE_FILE_NAME,
            build_macro_mezzo_reuse_config_for_cards([]),
        )
    else:
        client.download_file(macro_mezzo_reuse.id, config.local_cache_dir / MACRO_MEZZO_REUSE_FILE_NAME)

    mezzo_micro_reuse = _maybe_find_drive_item(root_items, MEZZO_MICRO_REUSE_FILE_NAME)
    if mezzo_micro_reuse is None:
        write_json(
            config.local_cache_dir / MEZZO_MICRO_REUSE_FILE_NAME,
            build_mezzo_micro_reuse_config_for_cards([]),
        )
    else:
        client.download_file(mezzo_micro_reuse.id, config.local_cache_dir / MEZZO_MICRO_REUSE_FILE_NAME)

    micro_session_reuse = _maybe_find_drive_item(root_items, MICRO_SESSION_REUSE_FILE_NAME)
    if micro_session_reuse is None:
        write_json(
            config.local_cache_dir / MICRO_SESSION_REUSE_FILE_NAME,
            build_micro_session_reuse_config_for_cards([]),
        )
    else:
        client.download_file(micro_session_reuse.id, config.local_cache_dir / MICRO_SESSION_REUSE_FILE_NAME)

    card_library_index = _maybe_find_drive_item(root_items, CARD_LIBRARY_INDEX_FILE_NAME)
    if card_library_index is not None:
        client.download_file(card_library_index.id, config.local_cache_dir / CARD_LIBRARY_INDEX_FILE_NAME)

    for card_type, folder_id in config.card_type_folder_ids.items():
        type_dir = cards_dir / card_type
        type_dir.mkdir(parents = True, exist_ok = True)

        for item in client.list_folder(folder_id):
            if item.file_or_folder == "file" and item.title.endswith(".json"):
                client.download_file(item.id, type_dir / item.title)
            elif item.file_or_folder == "folder":
                profile_dir = type_dir / item.title
                profile_dir.mkdir(parents = True, exist_ok = True)
                for profile_item in client.list_folder(item.id):
                    if profile_item.file_or_folder == "file" and profile_item.title.endswith(".json"):
                        client.download_file(profile_item.id, profile_dir / profile_item.title)

    if validate_download:
        refresh_library_bundle(config.local_cache_dir)

    return config.local_cache_dir


# Upload local cache files to Drive, updating existing files and creating missing ones.
def upload_cached_library(client, config: GoogleDriveLibraryConfig = GOOGLE_DRIVE_LIBRARY) -> None:
    display_config_path = config.local_cache_dir / DISPLAY_CONFIG_FILE_NAME
    macro_mezzo_reuse_path = config.local_cache_dir / MACRO_MEZZO_REUSE_FILE_NAME
    mezzo_micro_reuse_path = config.local_cache_dir / MEZZO_MICRO_REUSE_FILE_NAME
    micro_session_reuse_path = config.local_cache_dir / MICRO_SESSION_REUSE_FILE_NAME

    if not display_config_path.exists():
        write_json(display_config_path, build_display_config())

    cards = load_cached_cloud_library(config)
    if not macro_mezzo_reuse_path.exists():
        write_macro_mezzo_reuse_config(config.local_cache_dir, cards)
    if not mezzo_micro_reuse_path.exists():
        write_mezzo_micro_reuse_config(config.local_cache_dir, cards)
    if not micro_session_reuse_path.exists():
        write_micro_session_reuse_config(config.local_cache_dir, cards)

    validate_pathway_publish_ready(cards)
    refresh_library_bundle(config.local_cache_dir)
    root_items = client.list_folder(config.root_folder_id)

    _upsert_root_library_files(client, config, root_items)

    for card_type, folder_id in config.card_type_folder_ids.items():
        _upload_card_type_files(client, config, card_type, folder_id)


# Upload only root metadata files, leaving all remote card JSON files untouched.
def upload_cached_root_metadata(client, config: GoogleDriveLibraryConfig = GOOGLE_DRIVE_LIBRARY) -> None:
    display_config_path = config.local_cache_dir / DISPLAY_CONFIG_FILE_NAME
    macro_mezzo_reuse_path = config.local_cache_dir / MACRO_MEZZO_REUSE_FILE_NAME
    mezzo_micro_reuse_path = config.local_cache_dir / MEZZO_MICRO_REUSE_FILE_NAME
    micro_session_reuse_path = config.local_cache_dir / MICRO_SESSION_REUSE_FILE_NAME

    if not display_config_path.exists():
        write_json(display_config_path, build_display_config())

    cards = load_cached_cloud_library(config)
    if not macro_mezzo_reuse_path.exists():
        write_macro_mezzo_reuse_config(config.local_cache_dir, cards)
    if not mezzo_micro_reuse_path.exists():
        write_mezzo_micro_reuse_config(config.local_cache_dir, cards)
    if not micro_session_reuse_path.exists():
        write_micro_session_reuse_config(config.local_cache_dir, cards)

    validate_pathway_publish_ready(cards)
    refresh_library_bundle(config.local_cache_dir)
    root_items = client.list_folder(config.root_folder_id)

    _upsert_root_library_files(client, config, root_items)


# Upload root metadata plus only mezzo card files, leaving existing macro files untouched.
def upload_cached_mezzo_library(client, config: GoogleDriveLibraryConfig = GOOGLE_DRIVE_LIBRARY) -> None:
    display_config_path = config.local_cache_dir / DISPLAY_CONFIG_FILE_NAME
    macro_mezzo_reuse_path = config.local_cache_dir / MACRO_MEZZO_REUSE_FILE_NAME
    mezzo_micro_reuse_path = config.local_cache_dir / MEZZO_MICRO_REUSE_FILE_NAME
    micro_session_reuse_path = config.local_cache_dir / MICRO_SESSION_REUSE_FILE_NAME

    if not display_config_path.exists():
        write_json(display_config_path, build_display_config())

    cards = load_cached_cloud_library(config)
    if not macro_mezzo_reuse_path.exists():
        write_macro_mezzo_reuse_config(config.local_cache_dir, cards)
    if not mezzo_micro_reuse_path.exists():
        write_mezzo_micro_reuse_config(config.local_cache_dir, cards)
    if not micro_session_reuse_path.exists():
        write_micro_session_reuse_config(config.local_cache_dir, cards)

    validate_pathway_publish_ready(cards)
    refresh_library_bundle(config.local_cache_dir)
    root_items = client.list_folder(config.root_folder_id)

    _upsert_root_library_files(client, config, root_items)
    _upload_card_type_files(client, config, "mezzo", config.mezzo_folder_id)


# Upload root metadata plus only micro card files, leaving existing macro/mezzo files untouched.
def upload_cached_micro_library(client, config: GoogleDriveLibraryConfig = GOOGLE_DRIVE_LIBRARY) -> None:
    display_config_path = config.local_cache_dir / DISPLAY_CONFIG_FILE_NAME
    macro_mezzo_reuse_path = config.local_cache_dir / MACRO_MEZZO_REUSE_FILE_NAME
    mezzo_micro_reuse_path = config.local_cache_dir / MEZZO_MICRO_REUSE_FILE_NAME
    micro_session_reuse_path = config.local_cache_dir / MICRO_SESSION_REUSE_FILE_NAME

    if not display_config_path.exists():
        write_json(display_config_path, build_display_config())

    cards = load_cached_cloud_library(config)
    if not macro_mezzo_reuse_path.exists():
        write_macro_mezzo_reuse_config(config.local_cache_dir, cards)
    if not mezzo_micro_reuse_path.exists():
        write_mezzo_micro_reuse_config(config.local_cache_dir, cards)
    if not micro_session_reuse_path.exists():
        write_micro_session_reuse_config(config.local_cache_dir, cards)

    validate_pathway_publish_ready(cards)
    refresh_library_bundle(config.local_cache_dir)
    root_items = client.list_folder(config.root_folder_id)

    _upsert_root_library_files(client, config, root_items)
    _upload_card_type_files(client, config, "micro", config.micro_folder_id)


# Upload root metadata plus only session card files, leaving existing macro/mezzo/micro files untouched.
def upload_cached_session_library(client, config: GoogleDriveLibraryConfig = GOOGLE_DRIVE_LIBRARY) -> None:
    display_config_path = config.local_cache_dir / DISPLAY_CONFIG_FILE_NAME
    macro_mezzo_reuse_path = config.local_cache_dir / MACRO_MEZZO_REUSE_FILE_NAME
    mezzo_micro_reuse_path = config.local_cache_dir / MEZZO_MICRO_REUSE_FILE_NAME
    micro_session_reuse_path = config.local_cache_dir / MICRO_SESSION_REUSE_FILE_NAME

    if not display_config_path.exists():
        write_json(display_config_path, build_display_config())

    cards = load_cached_cloud_library(config)
    if not macro_mezzo_reuse_path.exists():
        write_macro_mezzo_reuse_config(config.local_cache_dir, cards)
    if not mezzo_micro_reuse_path.exists():
        write_mezzo_micro_reuse_config(config.local_cache_dir, cards)
    if not micro_session_reuse_path.exists():
        write_micro_session_reuse_config(config.local_cache_dir, cards)

    validate_pathway_publish_ready(cards)
    refresh_library_bundle(config.local_cache_dir)
    root_items = client.list_folder(config.root_folder_id)

    _upsert_root_library_files(client, config, root_items)
    _upload_card_type_files(client, config, "session", config.session_folder_id)


def _find_drive_item(items: list[DriveItem], title: str) -> DriveItem:
    for item in items:
        if item.title == title:
            return item

    raise FileNotFoundError(f"Google Drive item not found: {title}")

def _maybe_find_drive_item(items: list[DriveItem], title: str) -> DriveItem | None:
    for item in items:
        if item.title == title:
            return item

    return None


def _upsert_root_library_files(
    client,
    config: GoogleDriveLibraryConfig,
    root_items: list[DriveItem],
) -> None:
    root_file_names = (
        MANIFEST_FILE_NAME,
        DISPLAY_CONFIG_FILE_NAME,
        MACRO_MEZZO_REUSE_FILE_NAME,
        MEZZO_MICRO_REUSE_FILE_NAME,
        MICRO_SESSION_REUSE_FILE_NAME,
        CARD_LIBRARY_INDEX_FILE_NAME,
        LIBRARY_BUNDLE_FILE_NAME,
    )
    for file_name in root_file_names:
        _upsert_file(
            client,
            config.local_cache_dir / file_name,
            config.root_folder_id,
            file_name,
            root_items,
        )


def _upload_card_type_files(
    client,
    config: GoogleDriveLibraryConfig,
    card_type: str,
    folder_id: str,
) -> None:
    cards_dir = config.local_cache_dir / CARDS_ROOT
    folder_items = client.list_folder(folder_id)
    profile_folder_ids = {
        item.title: item.id
        for item in folder_items
        if item.file_or_folder == "folder"
    }

    for path in sorted((cards_dir / card_type).rglob("*.json")):
        relative_path = path.relative_to(cards_dir / card_type)
        parent_folder_id = folder_id
        existing_items = folder_items

        if len(relative_path.parts) > 1:
            profile_folder_name = relative_path.parts[0]
            parent_folder_id = profile_folder_ids.get(profile_folder_name)
            if parent_folder_id is None:
                parent_folder_id = client.create_folder(profile_folder_name, folder_id)
                profile_folder_ids[profile_folder_name] = parent_folder_id
            existing_items = client.list_folder(parent_folder_id)

        _upsert_file(client, path, parent_folder_id, path.name, existing_items)


# Remove old local JSON before downloading a fresh cloud copy.
def _clear_cached_json_files(cache_dir: Path) -> None:
    manifest_path = cache_dir / MANIFEST_FILE_NAME
    display_config_path = cache_dir / DISPLAY_CONFIG_FILE_NAME
    macro_mezzo_reuse_path = cache_dir / MACRO_MEZZO_REUSE_FILE_NAME
    mezzo_micro_reuse_path = cache_dir / MEZZO_MICRO_REUSE_FILE_NAME
    micro_session_reuse_path = cache_dir / MICRO_SESSION_REUSE_FILE_NAME
    card_library_index_path = cache_dir / CARD_LIBRARY_INDEX_FILE_NAME
    bundle_path = cache_dir / LIBRARY_BUNDLE_FILE_NAME

    if manifest_path.exists():
        manifest_path.unlink()

    if display_config_path.exists():
        display_config_path.unlink()

    if macro_mezzo_reuse_path.exists():
        macro_mezzo_reuse_path.unlink()

    if mezzo_micro_reuse_path.exists():
        mezzo_micro_reuse_path.unlink()

    if micro_session_reuse_path.exists():
        micro_session_reuse_path.unlink()

    if card_library_index_path.exists():
        card_library_index_path.unlink()

    if bundle_path.exists():
        bundle_path.unlink()

    for path in (cache_dir / CARDS_ROOT).rglob("*.json"):
        path.unlink()


def _upsert_file(client, local_path: Path, folder_id: str, file_name: str, existing_items: list[DriveItem]) -> None:
    existing_file = next(
        (item for item in existing_items if item.file_or_folder == "file" and item.title == file_name),
        None,
    )

    if existing_file is None:
        client.upload_file(local_path, folder_id, file_name, "application/json")
        return

    client.update_file(existing_file.id, local_path, "application/json")
