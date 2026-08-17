from __future__ import annotations

from pathlib import Path
from typing import Any

import streamlit as st

from training_cards.json_store import (
    load_card_library_from_json,
    load_display_config,
)
from training_cards.pathway import build_pathway_index
from training_cards.schemas import CardType

from streamlit_app.config import TYPE_ORDER


# ----------------------------------------------------------
# Cached Library Loading
# ----------------------------------------------------------
# The UI reads from the validated local JSON cache rather than reaching into
# the live sync layer directly.

@st.cache_data(show_spinner=False)
def load_library(cache_dir: Path) -> tuple[list[Any], dict[str, Any]]:
    cards = load_card_library_from_json(cache_dir)
    display_config = load_display_config(cache_dir)
    return cards, display_config


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


def related_child_cards(cards: list[Any], parent_card: Any, child_type: str) -> list[Any]:
    return build_pathway_index(cards).children(parent_card.id, child_type)


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
