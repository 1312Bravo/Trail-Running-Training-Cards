from __future__ import annotations

from typing import Any

import streamlit as st

from streamlit_app.data import cards_of_type
from streamlit_app.filters import cards_matching_philosophies, cards_matching_tags, cards_matching_terms
from streamlit_app.state import add_search_term
from streamlit_app.ui import render_active_tag_filters, render_paginated_grid, render_philosophy_profile_filter, render_search_terms


def render_today_session(cards: list[Any], display_config: dict[str, Any]) -> None:
    session_cards = cards_of_type(cards, "session")

    with st.container(border=False, key="mode-toolbar-today"):
        with st.container(border=False, key="today-filter-row"):
            controls = st.columns([1, 1], gap="large", vertical_alignment="center")
            with controls[0]:
                st.text_input(
                    "Search session cards",
                    key="today_search_input",
                    placeholder="Search today's session",
                    help="Add one or more search terms. Terms combine with AND.",
                    label_visibility="collapsed",
                    width="stretch",
                    on_change=add_search_term,
                    args=("today_search_input", "today_search_terms"),
                )
            with controls[1]:
                render_philosophy_profile_filter(label_visibility="collapsed")

        filter_controls = st.columns([1.05, 1], gap="large", vertical_alignment="bottom")
        with filter_controls[0]:
            render_active_tag_filters(show_label=False)
        with filter_controls[1]:
            render_search_terms("today_search_terms")

    visible_sessions = cards_matching_philosophies(
        cards_matching_tags(
            cards_matching_terms(session_cards, st.session_state.today_search_terms),
            st.session_state.tag_filters,
        ),
        st.session_state.philosophy_profile_filters,
    )

    if visible_sessions:
        render_paginated_grid(
            visible_sessions,
            display_config,
            state_prefix="today_session_cards",
            key_prefix="today_session",
        )
    else:
        st.caption("No session cards match the current search.")
