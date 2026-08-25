from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any


# Artwork stays outside the training-card schema. Cards connect to these
# assets only through their stable card id.
ART_ROOT = Path(__file__).resolve().parents[1] / "art_work"
DEFAULT_CATALOG_PATH = ART_ROOT / "catalog.json"
DEFAULT_FALLBACK_ASSET_PATH = ART_ROOT / "assets" / "prototype" / "fallback" / "fallback_avatar.svg"
VALID_LEVELS = {"macro", "mezzo", "micro", "session"}


@dataclass(frozen=True)
class ArtworkAsset:
    level: str
    asset_path: Path
    alt_text: str
    tags: tuple[str, ...] = ()
    is_fallback: bool = False


def artwork_for_card(card_id: str, use_fallback: bool = True) -> ArtworkAsset | None:
    artwork = load_artwork_catalog().get(card_id)
    if artwork is not None:
        return artwork
    if not use_fallback:
        return None
    return fallback_artwork()


def fallback_artwork(
    asset_path: Path = DEFAULT_FALLBACK_ASSET_PATH,
) -> ArtworkAsset | None:
    resolved_asset_path = asset_path.resolve()
    if not _is_relative_to(resolved_asset_path, ART_ROOT):
        return None
    if not resolved_asset_path.is_file():
        return None

    return ArtworkAsset(
        level="fallback",
        asset_path=resolved_asset_path,
        alt_text="Unassigned training-card avatar",
        tags=("fallback", "unassigned"),
        is_fallback=True,
    )


def clear_artwork_catalog_cache() -> None:
    _load_artwork_catalog.cache_clear()


def load_artwork_catalog(catalog_path: Path = DEFAULT_CATALOG_PATH) -> dict[str, ArtworkAsset]:
    catalog_path = catalog_path.resolve()
    try:
        modified_at = catalog_path.stat().st_mtime_ns
    except OSError:
        modified_at = 0

    # Include the file timestamp in the cache key so local catalog edits refresh
    # without rereading JSON for every card render.
    return _load_artwork_catalog(catalog_path, modified_at)


@lru_cache(maxsize=8)
def _load_artwork_catalog(catalog_path: Path, modified_at: int) -> dict[str, ArtworkAsset]:
    art_root = catalog_path.parent

    try:
        raw_catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

    if not isinstance(raw_catalog, dict):
        return {}

    catalog: dict[str, ArtworkAsset] = {}
    for card_id, raw_entry in raw_catalog.items():
        if not isinstance(card_id, str) or not isinstance(raw_entry, dict):
            continue

        artwork = _parse_artwork_entry(raw_entry, art_root)
        if artwork is not None:
            catalog[card_id] = artwork

    return catalog


def _parse_artwork_entry(raw_entry: dict[str, Any], art_root: Path) -> ArtworkAsset | None:
    level = raw_entry.get("level")
    asset_path = raw_entry.get("asset_path")
    alt_text = raw_entry.get("alt_text")
    tags = raw_entry.get("tags", [])

    if level not in VALID_LEVELS:
        return None
    if not isinstance(asset_path, str) or not asset_path:
        return None
    if not isinstance(alt_text, str) or not alt_text:
        return None
    if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
        return None

    resolved_asset_path = (art_root / asset_path).resolve()
    if not _is_relative_to(resolved_asset_path, art_root):
        return None
    if not resolved_asset_path.is_file():
        return None

    return ArtworkAsset(
        level=level,
        asset_path=resolved_asset_path,
        alt_text=alt_text,
        tags=tuple(tags),
    )


def _is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True
