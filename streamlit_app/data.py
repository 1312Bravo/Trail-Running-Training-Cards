from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any

import streamlit as st

from training_cards.json_store import (
    LIBRARY_BUNDLE_FILE_NAME,
    read_json,
    validate_card_library,
    validate_display_config,
    validate_macro_mezzo_reuse_config,
    validate_mezzo_micro_reuse_config,
    validate_micro_session_reuse_config,
)
from training_cards.card_library_index import validate_card_library_index
from training_cards.google_drive_client import GoogleDriveClient
from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY
from training_cards.pathway import build_pathway_index
from training_cards.philosophy_profiles import philosophy_profile_display_name
from training_cards.serialization import card_from_dict
from training_cards.schemas import CardType

from streamlit_app.config import TYPE_ORDER


# ----------------------------------------------------------
# Cached Library Loading
# ----------------------------------------------------------
# The UI reads from the validated local JSON cache rather than reaching into
# the live sync layer directly.

DEPLOYED_CACHE_DIR = Path(tempfile.gettempdir()) / "training_cards_cloud_library"


def download_deployed_library_bundle(
    client: GoogleDriveClient,
    cache_dir: Path,
) -> None:
    """Download the single validated bundle needed by the deployed app."""
    cache_dir.mkdir(parents = True, exist_ok = True)
    bundle_path = cache_dir / LIBRARY_BUNDLE_FILE_NAME
    if bundle_path.exists():
        bundle_path.unlink()

    root_items = client.list_folder(GOOGLE_DRIVE_LIBRARY.root_folder_id)
    bundle = next(
        (
            item
            for item in root_items
            if item.file_or_folder == "file" and item.title == LIBRARY_BUNDLE_FILE_NAME
        ),
        None,
    )
    if bundle is None:
        raise FileNotFoundError(
            f"Google Drive library bundle not found: {LIBRARY_BUNDLE_FILE_NAME}"
        )

    client.download_file(bundle.id, bundle_path)


def load_deployed_library_bundle(
    bundle_path: Path,
) -> tuple[
    list[Any],
    dict[str, Any],
    dict[str, Any],
    dict[str, Any],
    dict[str, Any],
    dict[str, Any],
]:
    """Read and validate the one-file library bundle used by the deployed app."""
    bundle = read_json(bundle_path)
    manifest = bundle["manifest"]
    display_config = bundle["display_config"]
    macro_mezzo_reuse_config = bundle["macro_mezzo_reuse"]
    mezzo_micro_reuse_config = bundle["mezzo_micro_reuse"]
    micro_session_reuse_config = bundle["micro_session_reuse"]
    cards = [card_from_dict(card_data) for card_data in bundle["cards"]]
    card_library_index = bundle["card_library_index"]

    validate_display_config(display_config, manifest)
    validate_macro_mezzo_reuse_config(macro_mezzo_reuse_config, manifest)
    validate_mezzo_micro_reuse_config(mezzo_micro_reuse_config, manifest)
    validate_micro_session_reuse_config(micro_session_reuse_config, manifest)
    validate_card_library(cards, manifest)
    validate_card_library_index(
        card_library_index,
        cards,
        schema_version=manifest["schema_version"],
        library_version=manifest["library_version"],
    )

    return (
        cards,
        display_config,
        macro_mezzo_reuse_config,
        mezzo_micro_reuse_config,
        micro_session_reuse_config,
        card_library_index,
    )


def runtime_cache_dir() -> Path:
    """Return the local cache when available, otherwise a deployable temp path."""
    local_cache_dir = GOOGLE_DRIVE_LIBRARY.local_cache_dir
    if (local_cache_dir / LIBRARY_BUNDLE_FILE_NAME).exists():
        return local_cache_dir
    return DEPLOYED_CACHE_DIR


@st.cache_resource(show_spinner=False)
def ensure_library_cache(cache_dir: str) -> str:
    """Ensure the validated Drive library exists for this app process."""
    cache_path = Path(cache_dir)
    if (cache_path / LIBRARY_BUNDLE_FILE_NAME).exists():
        return str(cache_path)

    credentials_info = None
    if "gcp_service_account" in st.secrets:
        credentials_info = dict(st.secrets["gcp_service_account"])

    download_deployed_library_bundle(
        GoogleDriveClient(credentials_info=credentials_info),
        cache_path,
    )
    return str(cache_path)

@st.cache_data(show_spinner=False)
def load_library(
    cache_dir: Path,
) -> tuple[
    list[Any],
    dict[str, Any],
    dict[str, Any],
    dict[str, Any],
    dict[str, Any],
    dict[str, Any],
]:
    cache_dir = Path(ensure_library_cache(str(cache_dir)))
    return load_deployed_library_bundle(cache_dir / LIBRARY_BUNDLE_FILE_NAME)


# ----------------------------------------------------------
# Filtering and Lookup
# ----------------------------------------------------------
# These helpers keep the Streamlit page logic small and deterministic.

def card_type_label(card_type: CardType, display_config: dict[str, Any]) -> str:
    labels = display_config.get("card_type_labels", {})
    fallback = {
        CardType.MACRO: "Macro",
        CardType.MEZZO: "Mezzo",
        CardType.MICRO: "Micro",
        CardType.SESSION: "Session",
    }
    return fallback.get(card_type, labels.get(str(card_type), str(card_type).title()))


def card_matches_search(card: Any, query: str) -> bool:
    if not query:
        return True

    card_type = getattr(card.card_type, "value", str(card.card_type))
    haystack = " ".join(
        [
            card.title,
            card.slug,
            card_type,
            card.summary,
            card.purpose,
            " ".join(getattr(card, "philosophy_profile_ids", [])),
            " ".join(
                philosophy_profile_display_name(profile_id)
                for profile_id in getattr(card, "philosophy_profile_ids", [])
            ),
            " ".join(
                profile_id.replace("_", " ").replace("-", " ")
                for profile_id in getattr(card, "philosophy_profile_ids", [])
            ),
            " ".join(card.tags),
            " ".join(tag.replace("_", " ") for tag in card.tags),
            " ".join(str(level) for level in card.suitable_levels),
            getattr(card, "additional_information", "") or "",
        ]
    ).lower()
    normalized_query = query.lower().replace("_", " ")
    return query.lower() in haystack or normalized_query in haystack


def filtered_cards(
    cards: list[Any],
    selected_type: str,
    search_query: str,
    tag_filters: list[str] | None = None,
    philosophy_profile_filters: list[str] | None = None,
) -> list[Any]:
    result = [card for card in cards if card_matches_search(card, search_query)]
    if selected_type != "all":
        result = [card for card in result if str(card.card_type) == selected_type]
    if tag_filters:
        result = [card for card in result if all(tag in card.tags for tag in tag_filters)]
    if philosophy_profile_filters:
        result = [
            card
            for card in result
            if any(
                profile_id in getattr(card, "philosophy_profile_ids", [])
                for profile_id in philosophy_profile_filters
            )
        ]
    return sorted(result, key=lambda card: (TYPE_ORDER.index(card.card_type), card.title))


def cards_of_type(cards: list[Any], card_type: str) -> list[Any]:
    return build_pathway_index(cards).cards_of_type(card_type)


def related_child_cards(
    cards: list[Any],
    parent_card: Any,
    child_type: str,
    macro_mezzo_reuse_config: dict[str, Any] | None = None,
    mezzo_micro_reuse_config: dict[str, Any] | None = None,
    micro_session_reuse_config: dict[str, Any] | None = None,
) -> list[Any]:
    return build_pathway_index(
        cards,
        macro_mezzo_reuse_config,
        mezzo_micro_reuse_config,
        micro_session_reuse_config,
    ).children(parent_card.id, child_type)


def reusable_mezzo_ids_for_philosophies(
    macro_mezzo_reuse_config: dict[str, Any] | None,
    parent_card_id: str | None,
    profile_ids: list[str],
) -> set[str]:
    if not macro_mezzo_reuse_config or not parent_card_id or not profile_ids:
        return set()

    return {
        entry["reused_mezzo_card_id"]
        for entry in macro_mezzo_reuse_config.get("entries", [])
        if isinstance(entry, dict)
        and entry.get("macro_card_id") == parent_card_id
        and entry.get("philosophy_profile_id") in profile_ids
        and isinstance(entry.get("reused_mezzo_card_id"), str)
    }


def reusable_micro_ids_for_philosophies(
    mezzo_micro_reuse_config: dict[str, Any] | None,
    parent_card_id: str | None,
    profile_ids: list[str],
) -> set[str]:
    if not mezzo_micro_reuse_config or not parent_card_id or not profile_ids:
        return set()

    return {
        entry["reused_micro_card_id"]
        for entry in mezzo_micro_reuse_config.get("entries", [])
        if isinstance(entry, dict)
        and entry.get("mezzo_card_id") == parent_card_id
        and entry.get("philosophy_profile_id") in profile_ids
        and isinstance(entry.get("reused_micro_card_id"), str)
    }


def reusable_session_ids_for_philosophies(
    micro_session_reuse_config: dict[str, Any] | None,
    parent_card_id: str | None,
    profile_ids: list[str],
) -> set[str]:
    if not micro_session_reuse_config or not parent_card_id or not profile_ids:
        return set()

    return {
        entry["reused_session_card_id"]
        for entry in micro_session_reuse_config.get("entries", [])
        if isinstance(entry, dict)
        and entry.get("micro_card_id") == parent_card_id
        and entry.get("philosophy_profile_id") in profile_ids
        and isinstance(entry.get("reused_session_card_id"), str)
    }


def card_counts(cards: list[Any]) -> dict[str, int]:
    return {
        "All": len(cards),
        "Macro": sum(1 for card in cards if str(card.card_type) == "macro"),
        "Mezzo": sum(1 for card in cards if str(card.card_type) == "mezzo"),
        "Micro": sum(1 for card in cards if str(card.card_type) == "micro"),
        "Session": sum(1 for card in cards if str(card.card_type) == "session"),
    }


def card_index(cards: list[Any]) -> dict[str, Any]:
    return {card.id: card for card in cards}
