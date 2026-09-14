from __future__ import annotations

from typing import Any

import streamlit as st

from streamlit_app.config import SEARCH_PLACEHOLDER
from streamlit_app.data import filtered_cards
from streamlit_app.renderers import render_grid
from streamlit_app.state import set_card_scope
from streamlit_app.ui import render_active_tag_filters, render_paginated_grid, render_philosophy_profile_filter


def render_browse_cards(cards: list[Any], display_config: dict[str, Any]) -> None:
    scope_labels = ["All", "Macro", "Mezzo", "Micro", "Session"]
    scope_to_value = {label: label.lower() for label in scope_labels if label != "All"}
    if st.session_state.card_scope_label not in scope_labels:
        st.session_state.card_scope_label = "All"

    with st.container(border=False, key="browse-toolbar"):
        with st.container(border=False, key="browse-scope-row"):
            with st.container(horizontal=True, key="browse-scope-links"):
                for label in scope_labels:
                    selected_prefix = "selected-" if st.session_state.card_scope_label == label else ""
                    st.button(
                        label,
                        key=f"browse-scope-{selected_prefix}{label.lower()}",
                        type="tertiary",
                        width="content",
                        on_click=set_card_scope,
                        args=(label,),
                    )
            chosen_scope = st.session_state.card_scope_label

        with st.container(border=False, key="browse-filter-row"):
            controls = st.columns([1, 1], gap="large", vertical_alignment="center")
            with controls[0]:
                st.session_state.search_query = st.text_input(
                    "Search",
                    value=st.session_state.search_query,
                    placeholder=SEARCH_PLACEHOLDER,
                    help="Searches across titles, block types, summary, purpose, coaching philosophy, levels, tags, and notes.",
                    width="stretch",
                    label_visibility="collapsed",
                )
            with controls[1]:
                render_philosophy_profile_filter(label_visibility="collapsed")
        render_active_tag_filters(show_label=False)

    st.session_state.card_scope = scope_to_value.get(chosen_scope, "all")
    cards_for_view = filtered_cards(
        cards,
        st.session_state.card_scope,
        st.session_state.search_query,
        tag_filters=st.session_state.tag_filters,
        philosophy_profile_filters=st.session_state.philosophy_profile_filters,
    )
    if cards_for_view:
        render_paginated_grid(
            cards_for_view,
            display_config,
            state_prefix="browse_cards",
            key_prefix=st.session_state.card_scope,
        )
    else:
        st.caption("No cards match the current filters.")
