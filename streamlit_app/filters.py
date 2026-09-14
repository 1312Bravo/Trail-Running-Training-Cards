from __future__ import annotations

from typing import Any

from training_cards.philosophy_profiles import philosophy_profile_display_name

from streamlit_app.data import (
    card_matches_search,
    reusable_micro_ids_for_philosophies,
    reusable_mezzo_ids_for_philosophies,
    reusable_session_ids_for_philosophies,
)


def cards_matching_terms(cards: list[Any], terms: list[str]) -> list[Any]:
    if not terms:
        return cards
    return [
        card
        for card in cards
        if all(card_matches_search(card, term) for term in terms)
    ]


def cards_matching_tags(cards: list[Any], tags: list[str]) -> list[Any]:
    if not tags:
        return cards
    return [card for card in cards if all(tag in card.tags for tag in tags)]


def cards_matching_philosophies(
    cards: list[Any],
    profile_ids: list[str],
    macro_mezzo_reuse_config: dict[str, Any] | None = None,
    mezzo_micro_reuse_config: dict[str, Any] | None = None,
    micro_session_reuse_config: dict[str, Any] | None = None,
    parent_card_id: str | None = None,
) -> list[Any]:
    if not profile_ids:
        return cards
    reused_mezzo_ids = reusable_mezzo_ids_for_philosophies(
        macro_mezzo_reuse_config, parent_card_id, profile_ids
    )
    reused_micro_ids = reusable_micro_ids_for_philosophies(
        mezzo_micro_reuse_config, parent_card_id, profile_ids
    )
    reused_session_ids = reusable_session_ids_for_philosophies(
        micro_session_reuse_config, parent_card_id, profile_ids
    )
    return [
        card
        for card in cards
        if card.id in reused_mezzo_ids
        or card.id in reused_micro_ids
        or card.id in reused_session_ids
        or any(
            profile_id in getattr(card, "philosophy_profile_ids", [])
            for profile_id in profile_ids
        )
    ]


def combine_library_levels(
    levels_index: dict[str, dict[str, list[dict[str, Any]]]],
    level_names: list[str],
) -> dict[str, list[dict[str, Any]]]:
    combined: dict[str, list[dict[str, Any]]] = {}
    for level_name in level_names:
        for profile_id, entries in levels_index.get(level_name, {}).items():
            combined.setdefault(profile_id, []).extend(
                dict(entry, level=level_name) for entry in entries
            )
    return combined


def filtered_library_entries(
    entries: list[dict[str, Any]], query: str
) -> list[dict[str, Any]]:
    normalized_query = query.strip().lower().replace("_", " ")
    if not normalized_query:
        return entries
    return [
        entry
        for entry in entries
        if normalized_query in library_entry_search_text(entry)
    ]


def library_entry_search_text(entry: dict[str, Any]) -> str:
    values = [
        entry.get("card_id", ""),
        entry.get("title", ""),
        entry.get("description", ""),
        entry.get("source", ""),
        entry.get("source_profile", ""),
        entry.get("source_profile", "").replace("_", " "),
    ]
    return " ".join(values).lower()
