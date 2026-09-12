from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Iterable, Any

from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY, GoogleDriveLibraryConfig
from training_cards.json_store import (
    export_card_library_to_json,
    load_card_library_from_json,
    read_json,
    refresh_library_bundle,
    card_storage_path,
)
from training_cards.pathway import validate_pathway_publish_ready
from training_cards.schemas import BaseTrainingCard
from training_cards.serialization import card_from_dict


def load_authored_cards_from_files(paths: Iterable[Path]) -> list[BaseTrainingCard]:
    cards: list[BaseTrainingCard] = []
    for path in paths:
        path = path.resolve()
        if path.suffix == ".json":
            cards.extend(_load_cards_from_json_file(path))
        elif path.suffix == ".py":
            cards.extend(_load_cards_from_python_file(path))
        else:
            raise ValueError(f"Unsupported card authoring file type: {path}")

    return cards


def add_or_update_cards_in_cache(
    new_cards: list[BaseTrainingCard],
    config: GoogleDriveLibraryConfig = GOOGLE_DRIVE_LIBRARY,
) -> dict[str, list[str] | str]:
    if not new_cards:
        raise ValueError("No cards supplied.")

    existing_cards = load_card_library_from_json(config.local_cache_dir)
    existing_by_id = {card.id: card for card in existing_cards}
    replacement_paths = {
        card_storage_path(existing_by_id[card.id])
        for card in new_cards
        if card.id in existing_by_id
    }

    merged_by_id = existing_by_id | {card.id: card for card in new_cards}
    merged_cards = list(merged_by_id.values())
    validate_pathway_publish_ready(merged_cards)

    for relative_path in replacement_paths:
        path = config.local_cache_dir / "cards" / relative_path
        if path.exists():
            path.unlink()

    export_card_library_to_json(merged_cards, config.local_cache_dir)
    refresh_library_bundle(config.local_cache_dir)

    added = sorted(card.id for card in new_cards if card.id not in existing_by_id)
    updated = sorted(card.id for card in new_cards if card.id in existing_by_id)
    return {
        "cache_dir": str(config.local_cache_dir),
        "added": added,
        "updated": updated,
    }


def remove_cards_from_cache(
    card_ids: Iterable[str],
    config: GoogleDriveLibraryConfig = GOOGLE_DRIVE_LIBRARY,
) -> dict[str, list[str] | str]:
    ids_to_remove = set(card_ids)
    if not ids_to_remove:
        raise ValueError("No card IDs supplied.")

    existing_cards = load_card_library_from_json(config.local_cache_dir)
    existing_by_id = {card.id: card for card in existing_cards}
    missing = sorted(ids_to_remove - set(existing_by_id))
    removed_cards = [existing_by_id[card_id] for card_id in ids_to_remove if card_id in existing_by_id]
    remaining_cards = [
        card
        for card in existing_cards
        if card.id not in ids_to_remove
    ]

    validate_pathway_publish_ready(remaining_cards)

    for card in removed_cards:
        path = config.local_cache_dir / "cards" / card_storage_path(card)
        if path.exists():
            path.unlink()

    export_card_library_to_json(remaining_cards, config.local_cache_dir)
    refresh_library_bundle(config.local_cache_dir)

    return {
        "cache_dir": str(config.local_cache_dir),
        "removed": sorted(card.id for card in removed_cards),
        "missing": missing,
    }


def _load_cards_from_json_file(path: Path) -> list[BaseTrainingCard]:
    data = read_json(path)
    if isinstance(data, list):
        return [card_from_dict(card_data) for card_data in data]
    if isinstance(data, dict) and isinstance(data.get("cards"), list):
        return [card_from_dict(card_data) for card_data in data["cards"]]
    if isinstance(data, dict):
        return [card_from_dict(data)]

    raise ValueError(f"Card JSON must contain an object, a list, or a cards list: {path}")


def _load_cards_from_python_file(path: Path) -> list[BaseTrainingCard]:
    module_name = f"_authored_cards_{path.stem}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ValueError(f"Cannot import Python card file: {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    authored_cards = _get_authored_cards_from_module(module.__dict__, path)
    return [_validate_authored_card(card, path) for card in authored_cards]


def _get_authored_cards_from_module(module_vars: dict[str, Any], path: Path) -> list[Any]:
    if "AUTHORED_CARDS" in module_vars:
        return list(module_vars["AUTHORED_CARDS"])
    if "AUTHORED_CARD" in module_vars:
        return [module_vars["AUTHORED_CARD"]]

    raise ValueError(
        f"Python card file must define AUTHORED_CARD or AUTHORED_CARDS: {path}"
    )


def _validate_authored_card(card: Any, path: Path) -> BaseTrainingCard:
    if not isinstance(card, BaseTrainingCard):
        raise TypeError(f"Authored object is not a BaseTrainingCard in {path}: {type(card)}")
    return card
