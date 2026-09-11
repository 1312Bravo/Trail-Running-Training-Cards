from __future__ import annotations

import hashlib
from dataclasses import replace
from datetime import date
from pathlib import Path

from training_cards.cloud_config import GoogleDriveLibraryConfig
from training_cards.cloud_store import download_cloud_library
from training_cards.json_store import (
    CARDS_ROOT,
    DISPLAY_CONFIG_FILE_NAME,
    LIBRARY_BUNDLE_FILE_NAME,
    MACRO_MEZZO_REUSE_FILE_NAME,
    MANIFEST_FILE_NAME,
    MEZZO_MICRO_REUSE_FILE_NAME,
    load_card_library_from_json,
    read_json,
    write_json,
)


CARD_TYPE_FOLDERS = ("macro", "mezzo", "micro", "session")
ROOT_LIBRARY_FILE_NAMES = (
    MANIFEST_FILE_NAME,
    DISPLAY_CONFIG_FILE_NAME,
    MACRO_MEZZO_REUSE_FILE_NAME,
    MEZZO_MICRO_REUSE_FILE_NAME,
    LIBRARY_BUNDLE_FILE_NAME,
)


def archive_active_library(
    client,
    active_config: GoogleDriveLibraryConfig,
    work_dir: Path,
) -> tuple[GoogleDriveLibraryConfig, Path]:
    frozen_dir = work_dir / "frozen_active_library"
    archive_dir = work_dir / "local_archive"
    _reset_directory(frozen_dir)
    _reset_directory(archive_dir)
    frozen_config = replace(active_config, local_cache_dir=frozen_dir)
    download_cloud_library(client, frozen_config, validate_download=False)
    card_count = _verify_raw_library(frozen_dir)
    _copy_library(frozen_dir, archive_dir)
    metadata = {
        "archive_created_on": str(date.today()),
        "reason": "pre-rebuild active library archive",
        "source_root_folder_id": active_config.root_folder_id,
        "source_root_folder_url": active_config.root_folder_url,
        "manifest": read_json(frozen_dir / MANIFEST_FILE_NAME),
        "card_count": card_count,
        "checksums": _checksums(archive_dir),
    }
    write_json(archive_dir / "archive_metadata.json", metadata)
    parent_folder_id = client.get_parent_folder_id(active_config.root_folder_id)
    if parent_folder_id is None:
        parent_folder_id = active_config.root_folder_id
    archive_name = f"{active_config.library_name}_archive_{date.today():%Y-%m-%d}_pre_rebuild"
    archive_config = publish_library(
        client,
        archive_dir,
        parent_folder_id,
        archive_name,
        validate_source=False,
    )
    return archive_config, archive_dir


def publish_library(
    client,
    source_dir: Path,
    parent_folder_id: str,
    library_name: str,
    *,
    validate_source: bool = True,
) -> GoogleDriveLibraryConfig:
    if validate_source:
        load_card_library_from_json(source_dir)
    root_folder_id = client.create_folder(library_name, parent_folder_id)
    cards_folder_id = client.create_folder("cards", root_folder_id)
    card_folder_ids = {
        card_type: client.create_folder(card_type, cards_folder_id)
        for card_type in CARD_TYPE_FOLDERS
    }
    for file_name in ROOT_LIBRARY_FILE_NAMES:
        if not (source_dir / file_name).exists():
            continue
        client.upload_file(source_dir / file_name, root_folder_id, file_name, "application/json")
    archive_metadata = source_dir / "archive_metadata.json"
    if archive_metadata.exists():
        client.upload_file(archive_metadata, root_folder_id, archive_metadata.name, "application/json")
    for card_type in CARD_TYPE_FOLDERS:
        folder_cache = {(): card_folder_ids[card_type]}
        for path in sorted((source_dir / "cards" / card_type).rglob("*.json")):
            relative_parent = path.relative_to(source_dir / "cards" / card_type).parent
            parent_parts = relative_parent.parts
            parent_folder_id = _ensure_drive_folder_path(
                client,
                card_folder_ids[card_type],
                parent_parts,
                folder_cache,
            )
            client.upload_file(path, parent_folder_id, path.name, "application/json")
    return GoogleDriveLibraryConfig(
        library_name=library_name,
        root_folder_id=root_folder_id,
        root_folder_url=f"https://drive.google.com/drive/folders/{root_folder_id}",
        cards_folder_id=cards_folder_id,
        macro_folder_id=card_folder_ids["macro"],
        mezzo_folder_id=card_folder_ids["mezzo"],
        micro_folder_id=card_folder_ids["micro"],
        session_folder_id=card_folder_ids["session"],
    )


def replace_active_library_contents(
    client,
    source_dir: Path,
    active_config: GoogleDriveLibraryConfig,
) -> GoogleDriveLibraryConfig:
    load_card_library_from_json(source_dir)
    root_items = client.list_folder(active_config.root_folder_id)
    expected_root_names = {
        *ROOT_LIBRARY_FILE_NAMES,
        CARDS_ROOT,
    }
    replace_items = [
        item
        for item in root_items
        if item.title in expected_root_names
    ]

    unexpected_items = [
        item.title
        for item in root_items
        if item.title not in expected_root_names
    ]
    if unexpected_items:
        raise ValueError(
            "Active library root contains unexpected items; refusing destructive replacement: "
            + ", ".join(sorted(unexpected_items))
        )

    for item in replace_items:
        client.delete_file(item.id)

    cards_folder_id = client.create_folder(CARDS_ROOT, active_config.root_folder_id)
    card_folder_ids = {
        card_type: client.create_folder(card_type, cards_folder_id)
        for card_type in CARD_TYPE_FOLDERS
    }

    for file_name in ROOT_LIBRARY_FILE_NAMES:
        client.upload_file(source_dir / file_name, active_config.root_folder_id, file_name, "application/json")

    for card_type in CARD_TYPE_FOLDERS:
        folder_cache = {(): card_folder_ids[card_type]}
        card_type_dir = source_dir / CARDS_ROOT / card_type

        if not card_type_dir.exists():
            continue

        for path in sorted(card_type_dir.rglob("*.json")):
            relative_parent = path.relative_to(card_type_dir).parent
            parent_folder_id = _ensure_drive_folder_path(
                client,
                card_folder_ids[card_type],
                relative_parent.parts,
                folder_cache,
            )
            client.upload_file(path, parent_folder_id, path.name, "application/json")

    return GoogleDriveLibraryConfig(
        library_name=active_config.library_name,
        root_folder_id=active_config.root_folder_id,
        root_folder_url=active_config.root_folder_url,
        cards_folder_id=cards_folder_id,
        macro_folder_id=card_folder_ids["macro"],
        mezzo_folder_id=card_folder_ids["mezzo"],
        micro_folder_id=card_folder_ids["micro"],
        session_folder_id=card_folder_ids["session"],
    )


def verify_library(client, config: GoogleDriveLibraryConfig, verification_dir: Path) -> int:
    _reset_directory(verification_dir)
    verification_config = replace(config, local_cache_dir=verification_dir)
    download_cloud_library(client, verification_config)
    return len(load_card_library_from_json(verification_dir))


def verify_raw_library(client, config: GoogleDriveLibraryConfig, verification_dir: Path) -> int:
    _reset_directory(verification_dir)
    verification_config = replace(config, local_cache_dir=verification_dir)
    download_cloud_library(client, verification_config, validate_download=False)
    return _verify_raw_library(verification_dir)


def write_rebuild_target(path: Path, config: GoogleDriveLibraryConfig) -> None:
    write_json(
        path,
        {
            "library_name": config.library_name,
            "root_folder_id": config.root_folder_id,
            "root_folder_url": config.root_folder_url,
            "cards_folder_id": config.cards_folder_id,
            "macro_folder_id": config.macro_folder_id,
            "mezzo_folder_id": config.mezzo_folder_id,
            "micro_folder_id": config.micro_folder_id,
            "session_folder_id": config.session_folder_id,
        },
    )


def _copy_library(source_dir: Path, destination_dir: Path) -> None:
    for source_path in source_dir.rglob("*.json"):
        destination_path = destination_dir / source_path.relative_to(source_dir)
        destination_path.parent.mkdir(parents=True, exist_ok=True)
        destination_path.write_bytes(source_path.read_bytes())


def _checksums(root_dir: Path) -> dict[str, str]:
    return {
        str(path.relative_to(root_dir)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root_dir.rglob("*.json"))
    }


def _verify_raw_library(library_dir: Path) -> int:
    manifest = read_json(library_dir / MANIFEST_FILE_NAME)
    card_paths = list((library_dir / manifest["cards_root"]).rglob("*.json"))
    expected_count = manifest.get("card_count")

    if not isinstance(expected_count, int) or expected_count != len(card_paths):
        raise ValueError(
            f"Archive manifest expects {expected_count} cards, but contains {len(card_paths)} JSON card files."
        )

    return len(card_paths)


def _ensure_drive_folder_path(
    client,
    root_folder_id: str,
    path_parts: tuple[str, ...],
    folder_cache: dict[tuple[str, ...], str],
) -> str:
    if path_parts in folder_cache:
        return folder_cache[path_parts]

    current_parts: tuple[str, ...] = ()
    current_folder_id = root_folder_id

    for part in path_parts:
        current_parts = (*current_parts, part)
        if current_parts not in folder_cache:
            current_folder_id = client.create_folder(part, current_folder_id)
            folder_cache[current_parts] = current_folder_id
        else:
            current_folder_id = folder_cache[current_parts]

    return current_folder_id


def _reset_directory(path: Path) -> None:
    if path.exists():
        for child in sorted(path.iterdir(), reverse=True):
            if child.is_dir():
                import shutil
                shutil.rmtree(child)
            else:
                child.unlink()
    path.mkdir(parents=True, exist_ok=True)
