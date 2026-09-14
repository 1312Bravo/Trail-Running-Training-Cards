from __future__ import annotations

from html import escape
from typing import Any

import streamlit as st

from training_cards.philosophy_profiles import PHILOSOPHY_PROFILES, philosophy_profile_display_name

from streamlit_app.config import LIBRARY_DEFAULT_CARDS_PER_PAGE
from streamlit_app.filters import combine_library_levels, filtered_library_entries
from streamlit_app.renderers import display_text
from streamlit_app.state import set_active_library_preview, set_session_state_value, toggle_library_profile
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

    selected_level = level_to_value.get(chosen_level)
    levels_index = card_library_index.get("levels", {})
    level_names = [selected_level] if selected_level else ["macro", "mezzo", "micro", "session"]
    level_index = combine_library_levels(levels_index, level_names)
    profile_ids = [profile_id for profile_id in PHILOSOPHY_PROFILES if profile_id in level_index]
    st.session_state.library_expanded_profiles = [
        profile_id
        for profile_id in st.session_state.library_expanded_profiles
        if profile_id in profile_ids
    ]

    with controls[1]:
        st.text_input(
            "Search library",
            key="library_search_query",
            placeholder="Search titles, descriptions, IDs, or source",
            label_visibility="collapsed",
            width="stretch",
        )

    expanded_profiles = set(st.session_state.library_expanded_profiles)
    visible_profile_entries: list[tuple[str, list[dict[str, Any]]]] = []
    for profile_id in profile_ids:
        entries = filtered_library_entries(
            level_index.get(profile_id, []),
            st.session_state.library_search_query,
        )
        if entries:
            visible_profile_entries.append((profile_id, entries))

    with st.container(border=False, key="library-profile-grid"):
        profile_columns = st.columns(2, gap="medium")
        for index, (profile_id, entries) in enumerate(visible_profile_entries):
            is_expanded = profile_id in expanded_profiles
            with profile_columns[index % 2]:
                with st.container(border=False, key=f"library-group-{profile_id}"):
                    st.button(
                        f'{"v" if is_expanded else ">"}  '
                        f"{philosophy_profile_display_name(profile_id)} · {len(entries)} cards",
                        key=f"library-group-toggle-{profile_id}",
                        type="tertiary",
                        width="stretch",
                        on_click=toggle_library_profile,
                        args=(profile_id,),
                    )

    for profile_id, entries in visible_profile_entries:
        if profile_id not in expanded_profiles:
            continue
        direct_count = sum(entry.get("source") == "direct" for entry in entries)
        reused_count = len(entries) - direct_count
        with st.container(border=False, key=f"library-expanded-{profile_id}"):
            st.html(
                '<div class="library-expanded-title">'
                f"{escape(philosophy_profile_display_name(profile_id))}"
                "</div>"
            )
            st.caption(f"{direct_count} direct · {reused_count} reused")
            header = st.columns([1.35, 2.45, 0.8, 1], gap="medium")
            for column, heading in zip(header, ("Card", "Description", "Level", "Source")):
                with column:
                    st.html(f'<div class="library-table-heading">{heading}</div>')
            render_paginated_library_entries(entries, profile_id)


def render_library_entry(entry: dict[str, Any], profile_id: str) -> None:
    source = entry.get("source", "direct")
    source_profile = entry.get("source_profile")
    source_label = "Direct"
    if source == "reused" and source_profile:
        source_label = f"From {philosophy_profile_display_name(source_profile)}"

    with st.container(key=f"library-entry-{profile_id}-{entry['card_id']}"):
        row = st.columns([1.35, 2.45, 0.8, 1], gap="medium", vertical_alignment="center")
        with row[0]:
            st.button(
                entry["title"],
                key=f"library_open_{profile_id}_{entry['card_id']}",
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
        with row[3]:
            st.html(f'<div class="library-meta">{escape(source_label)}</div>')


def render_paginated_library_entries(
    entries: list[dict[str, Any]],
    profile_id: str,
) -> None:
    state_prefix = f"library_{profile_id}"
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
        render_library_entry(entry, profile_id)
    render_pagination_controls(len(entries), page_size, page, state_prefix)
