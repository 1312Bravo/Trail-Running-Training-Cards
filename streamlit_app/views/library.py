from __future__ import annotations

from html import escape
from typing import Any

import streamlit as st

from streamlit_app.config import LIBRARY_DEFAULT_CARDS_PER_PAGE
from streamlit_app.filters import filtered_library_entries
from streamlit_app.renderers import display_text
from streamlit_app.state import set_active_library_preview, set_session_state_value
from streamlit_app.ui import render_pagination_controls


def render_card_library(card_library_index: dict[str, Any]) -> None:
    level_labels = ["All", "Macro", "Mezzo", "Micro", "Session"]
    level_to_value = {label: label.lower() for label in level_labels if label != "All"}
    if st.session_state.library_level_label not in level_labels:
        st.session_state.library_level_label = "All"

    controls = st.columns([1.25, 1], gap="large", vertical_alignment="center")
    with controls[0]:
        with st.container(horizontal=True, key="library-level-links"):
            for label in level_labels:
                selected_prefix = "selected-" if st.session_state.library_level_label == label else ""
                st.button(
                    label,
                    key=f"library-level-{selected_prefix}{label.lower()}",
                    type="tertiary",
                    width="content",
                    on_click=set_session_state_value,
                    args=("library_level_label", label),
                )
        chosen_level = st.session_state.library_level_label

    levels_index = card_library_index.get("levels", {})
    selected_level = level_to_value.get(chosen_level)
    level_names = [selected_level] if selected_level else ["macro", "mezzo", "micro", "session"]

    with controls[1]:
        st.text_input(
            "Search library",
            key="library_search_query",
            placeholder="Search titles, descriptions, IDs, or level",
            label_visibility="collapsed",
            width="stretch",
        )

    entries = filtered_library_entries(
        flattened_library_entries(levels_index, level_names),
        st.session_state.library_search_query,
    )
    if not entries:
        st.info("No cards match the current library filters.")
        return

    title = "All cards" if chosen_level == "All" else f"{chosen_level} cards"
    with st.container(border=False, key="library-expanded-all-cards"):
        st.html(f'<div class="library-expanded-title">{escape(title)}</div>')
        st.caption(f"{len(entries)} cards")
        header = st.columns([1.35, 2.45, 0.8], gap="medium")
        for column, heading in zip(header, ("Card", "Description", "Level")):
            with column:
                st.html(f'<div class="library-table-heading">{heading}</div>')
        render_paginated_library_entries(entries, "all_cards")


def flattened_library_entries(
    levels_index: dict[str, dict[str, list[dict[str, Any]]]],
    level_names: list[str],
) -> list[dict[str, Any]]:
    entries_by_card: dict[tuple[str, str], dict[str, Any]] = {}
    for level_name in level_names:
        for profile_entries in levels_index.get(level_name, {}).values():
            for entry in profile_entries:
                card_id = entry.get("card_id", "")
                key = (level_name, card_id)
                entries_by_card.setdefault(key, dict(entry, level=level_name))
    return sorted(entries_by_card.values(), key=library_entry_sort_key)


def library_entry_sort_key(entry: dict[str, Any]) -> tuple[int, str, str]:
    level_order = {"macro": 0, "mezzo": 1, "micro": 2, "session": 3}
    level = str(entry.get("level", ""))
    return (
        level_order.get(level, len(level_order)),
        str(entry.get("title", "")).casefold(),
        str(entry.get("card_id", "")),
    )


def render_library_entry(entry: dict[str, Any], entry_key: str) -> None:
    with st.container(key=f"library-entry-{entry_key}-{entry['card_id']}"):
        row = st.columns([1.35, 2.45, 0.8], gap="medium", vertical_alignment="center")
        with row[0]:
            st.button(
                entry["title"],
                key=f"library_open_{entry_key}_{entry['card_id']}",
                type="tertiary",
                width="content",
                on_click=set_active_library_preview,
                args=(entry["card_id"],),
            )
        with row[1]:
            st.html(f'<div class="library-description">{escape(entry.get("description", ""))}</div>')
        with row[2]:
            st.html(
                '<div class="library-meta">'
                f'{escape(display_text(entry.get("level", "")).title())}'
                "</div>"
            )


def render_paginated_library_entries(
    entries: list[dict[str, Any]],
    entry_key: str,
) -> None:
    state_prefix = f"library_{entry_key}"
    page_key = f"{state_prefix}_page"
    signature_key = f"{state_prefix}_signature"
    st.session_state.setdefault(page_key, 0)
    st.session_state.setdefault(signature_key, ())

    current_signature = tuple(entry.get("card_id", "") for entry in entries)
    if st.session_state[signature_key] != current_signature:
        st.session_state[signature_key] = current_signature
        st.session_state[page_key] = 0

    page_size = LIBRARY_DEFAULT_CARDS_PER_PAGE
    total_pages = max(1, (len(entries) + page_size - 1) // page_size)
    page = min(max(0, int(st.session_state.get(page_key, 0))), total_pages - 1)
    st.session_state[page_key] = page
    for entry in entries[page * page_size: (page + 1) * page_size]:
        render_library_entry(entry, entry_key)
    render_pagination_controls(len(entries), page_size, page, state_prefix)
