from __future__ import annotations

from typing import Any

import streamlit as st

from streamlit_app.config import APP_MODES, PATHWAY_STEPS


def set_active_card(card_id: str) -> None:
    st.session_state.active_philosophy_profile_id = None
    st.session_state.active_philosophy_sources_profile_id = None
    st.session_state.active_library_preview_card_id = None
    st.session_state.active_card_id = card_id
    st.session_state.active_card_history = []


def clear_active_card() -> None:
    st.session_state.active_card_id = None
    st.session_state.active_card_history = []


def set_active_library_preview(card_id: str) -> None:
    st.session_state.active_card_id = None
    st.session_state.active_card_history = []
    st.session_state.active_library_preview_card_id = card_id


def clear_active_library_preview() -> None:
    st.session_state.active_library_preview_card_id = None


def open_full_card_from_library_preview(card_id: str) -> None:
    st.session_state.active_library_preview_card_id = None
    st.session_state.active_card_id = card_id
    st.session_state.active_card_history = []
    st.rerun(scope="app")


def set_active_philosophy(profile_id: str) -> None:
    st.session_state.active_card_id = None
    st.session_state.active_philosophy_sources_profile_id = None
    st.session_state.active_philosophy_profile_id = profile_id


def clear_active_philosophy() -> None:
    st.session_state.active_philosophy_profile_id = None


def set_active_philosophy_sources(profile_id: str) -> None:
    st.session_state.active_card_id = None
    st.session_state.active_philosophy_profile_id = None
    st.session_state.active_philosophy_sources_profile_id = profile_id


def clear_active_philosophy_sources() -> None:
    st.session_state.active_philosophy_sources_profile_id = None


def clear_open_views() -> None:
    """Close modal views when the user changes the top-level app mode."""
    st.session_state.active_card_id = None
    st.session_state.active_library_preview_card_id = None
    st.session_state.active_philosophy_profile_id = None
    st.session_state.active_philosophy_sources_profile_id = None
    st.session_state.active_card_history = []


def toggle_library_profile(profile_id: str) -> None:
    if profile_id in st.session_state.library_expanded_profiles:
        st.session_state.library_expanded_profiles = []
    else:
        st.session_state.library_expanded_profiles = [profile_id]


def set_card_scope(scope_label: str) -> None:
    st.session_state.card_scope_label = scope_label


def browse_philosophy_cards(profile_id: str) -> None:
    st.session_state.app_mode = "Browse cards"
    st.session_state.card_scope_label = "All"
    st.session_state.philosophy_profile_filters = [profile_id]


def state_key_for_level(level: str) -> str:
    return f"pathway_{level}_id"


def select_pathway_card(level: str, card_id: str) -> None:
    levels = [step_level for step_level, _ in PATHWAY_STEPS]
    selected_index = levels.index(level)
    st.session_state[state_key_for_level(level)] = card_id
    st.session_state.pathway_search_terms = []
    st.session_state.pathway_search_input = ""
    for later_level in levels[selected_index + 1:]:
        st.session_state[state_key_for_level(later_level)] = None


def clear_pathway_from(level: str) -> None:
    levels = [step_level for step_level, _ in PATHWAY_STEPS]
    selected_index = levels.index(level)
    st.session_state.pathway_search_terms = []
    st.session_state.pathway_search_input = ""
    for later_level in levels[selected_index:]:
        st.session_state[state_key_for_level(later_level)] = None


def clear_pathway() -> None:
    st.session_state.pathway_search_terms = []
    st.session_state.pathway_search_input = ""
    for level, _ in PATHWAY_STEPS:
        st.session_state[state_key_for_level(level)] = None


def add_search_term(input_key: str, terms_key: str) -> None:
    term = st.session_state.get(input_key, "").strip()
    if not term:
        return

    current_terms = list(st.session_state.get(terms_key, []))
    if term not in current_terms:
        current_terms.append(term)
    st.session_state[terms_key] = current_terms
    st.session_state[input_key] = ""


def remove_search_term(terms_key: str, term: str) -> None:
    st.session_state[terms_key] = [
        current_term
        for current_term in st.session_state.get(terms_key, [])
        if current_term != term
    ]


def remove_tag_filter(tag: str) -> None:
    st.session_state.tag_filters = [
        selected_tag
        for selected_tag in st.session_state.tag_filters
        if selected_tag != tag
    ]


def set_session_state_value(key: str, value: Any) -> None:
    st.session_state[key] = value


def init_state() -> None:
    defaults = {
        "search_query": "",
        "pathway_search_input": "",
        "pathway_search_terms": [],
        "today_search_input": "",
        "today_search_terms": [],
        "active_card_id": None,
        "active_library_preview_card_id": None,
        "active_card_history": [],
        "active_philosophy_profile_id": None,
        "active_philosophy_sources_profile_id": None,
        "app_mode": APP_MODES[0],
        "card_scope_label": "All",
        "tag_filters": [],
        "philosophy_profile_filters": [],
        "library_level_label": "All",
        "library_search_query": "",
        "library_expanded_profiles": [],
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)

    if "last_app_mode" not in st.session_state:
        if any(
            st.session_state.get(key)
            for key in (
                "active_card_id",
                "active_library_preview_card_id",
                "active_philosophy_profile_id",
                "active_philosophy_sources_profile_id",
            )
        ):
            clear_open_views()
        st.session_state.last_app_mode = st.session_state.app_mode

    if st.session_state.card_scope_label not in {"All", "Macro", "Mezzo", "Micro", "Session"}:
        st.session_state.card_scope_label = "All"
    for level, _ in PATHWAY_STEPS:
        st.session_state.setdefault(state_key_for_level(level), None)
