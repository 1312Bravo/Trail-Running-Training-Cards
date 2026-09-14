from __future__ import annotations

from html import escape
from typing import Any

import streamlit as st

from streamlit_app.config import PATHWAY_STEPS
from streamlit_app.data import cards_of_type, related_child_cards
from streamlit_app.filters import cards_matching_philosophies, cards_matching_tags, cards_matching_terms
from streamlit_app.renderers import render_grid
from streamlit_app.state import (
    add_search_term,
    clear_pathway,
    clear_pathway_from,
    select_pathway_card,
    set_active_card,
    state_key_for_level,
)
from streamlit_app.ui import (
    render_active_tag_filters,
    render_paginated_grid,
    render_philosophy_profile_filter,
    render_search_terms,
)


def selected_pathway_cards(card_by_id: dict[str, Any]) -> dict[str, Any | None]:
    return {
        level: card_by_id.get(st.session_state.get(state_key_for_level(level)))
        for level, _ in PATHWAY_STEPS
    }


def next_pathway_step(selected_cards: dict[str, Any | None]) -> tuple[str, str] | None:
    for level, label in PATHWAY_STEPS:
        if selected_cards[level] is None:
            return level, label
    return None


def pathway_candidates(
    cards: list[Any],
    selected_cards: dict[str, Any | None],
    macro_mezzo_reuse_config: dict[str, Any] | None = None,
    mezzo_micro_reuse_config: dict[str, Any] | None = None,
    micro_session_reuse_config: dict[str, Any] | None = None,
) -> tuple[str, str, list[Any]]:
    next_step = next_pathway_step(selected_cards)
    if not next_step:
        return "", "", []

    next_level, next_label = next_step
    step_index = [level for level, _ in PATHWAY_STEPS].index(next_level)
    if step_index == 0:
        return next_level, next_label, cards_of_type(cards, next_level)

    previous_level = PATHWAY_STEPS[step_index - 1][0]
    previous_card = selected_cards[previous_level]
    if previous_card is None:
        return next_level, next_label, []
    return next_level, next_label, related_child_cards(
        cards,
        previous_card,
        next_level,
        macro_mezzo_reuse_config,
        mezzo_micro_reuse_config,
        micro_session_reuse_config,
    )


def render_pathway_selection(
    selected_cards: dict[str, Any | None],
    display_config: dict[str, Any],
) -> None:
    with st.container(border=False, key="pathway-selection"):
        cols = st.columns(4, gap="small")
        for index, (level, label) in enumerate(PATHWAY_STEPS):
            card = selected_cards[level]
            with cols[index]:
                with st.container(border=False, key=f"pathway-card-{level}"):
                    st.html(f'<div class="pathway-level-label">{escape(label)}</div>')
                    st.html('<div class="pathway-level-rule"></div>')
                    if card is None:
                        st.html('<div class="pathway-empty">Not selected</div>')
                        continue
                    st.html(
                        '<div class="pathway-selected-title">'
                        f"{escape(card.title)}"
                        "</div>"
                    )
                    with st.container(horizontal=True, horizontal_alignment="center"):
                        st.button(
                            "Open card",
                            key=f"pathway_open_{level}",
                            width="content",
                            on_click=set_active_card,
                            args=(card.id,),
                        )
                        st.button(
                            "Remove",
                            key=f"pathway_change_{level}",
                            width="content",
                            on_click=clear_pathway_from,
                            args=(level,),
                        )
        st.html('<div class="pathway-summary-footer-rule"></div>')
        with st.container(horizontal=True, horizontal_alignment="center"):
            st.button(
                "Clear pathway",
                key="clear_pathway",
                type="tertiary",
                width="content",
                on_click=clear_pathway,
            )


def render_build_pathway(
    cards: list[Any],
    display_config: dict[str, Any],
    card_by_id: dict[str, Any],
    macro_mezzo_reuse_config: dict[str, Any],
    mezzo_micro_reuse_config: dict[str, Any],
    micro_session_reuse_config: dict[str, Any],
) -> None:
    selected_cards = selected_pathway_cards(card_by_id)
    render_pathway_selection(selected_cards, display_config)

    next_level, next_label, candidates = pathway_candidates(
        cards,
        selected_cards,
        macro_mezzo_reuse_config,
        mezzo_micro_reuse_config,
        micro_session_reuse_config,
    )
    if not next_level:
        st.caption(
            "Pathway complete. Use Open card on any selected card to inspect details, or Remove to revise one step."
        )
        pathway_cards = [
            selected_cards[level]
            for level, _ in PATHWAY_STEPS
            if selected_cards[level] is not None
        ]
        if pathway_cards:
            st.caption("Chosen pathway cards")
            render_grid(pathway_cards, display_config, key_prefix="completed_pathway")
        return

    with st.container(border=False, key="mode-toolbar-pathway"):
        with st.container(border=False, key="pathway-filter-row"):
            controls = st.columns([1, 1], gap="large", vertical_alignment="center")
            with controls[0]:
                st.text_input(
                    "Search current cards",
                    key="pathway_search_input",
                    placeholder=f"Search {next_label.lower()} cards",
                    help="Searches only the cards available for the current pathway step, including tags.",
                    label_visibility="collapsed",
                    width="stretch",
                    on_change=add_search_term,
                    args=("pathway_search_input", "pathway_search_terms"),
                )
            with controls[1]:
                render_philosophy_profile_filter(label_visibility="collapsed")

        filter_controls = st.columns([1.05, 1], gap="large", vertical_alignment="bottom")
        with filter_controls[0]:
            render_active_tag_filters(show_label=False)
        with filter_controls[1]:
            render_search_terms("pathway_search_terms")

    parent_card_id = (
        selected_cards["macro"].id
        if next_level == "mezzo" and selected_cards["macro"]
        else selected_cards["mezzo"].id
        if next_level == "micro" and selected_cards["mezzo"]
        else selected_cards["micro"].id
        if next_level == "session" and selected_cards["micro"]
        else None
    )
    visible_candidates = cards_matching_philosophies(
        cards_matching_tags(
            cards_matching_terms(candidates, st.session_state.pathway_search_terms),
            st.session_state.tag_filters,
        ),
        st.session_state.philosophy_profile_filters,
        macro_mezzo_reuse_config,
        mezzo_micro_reuse_config,
        micro_session_reuse_config,
        parent_card_id,
    )
    if visible_candidates:
        render_paginated_grid(
            visible_candidates,
            display_config,
            state_prefix=f"pathway_{next_level}_cards",
            key_prefix=f"pathway_{next_level}",
            select_label="Select",
            on_select=select_pathway_card,
            select_level=next_level,
        )
    else:
        st.caption(f"No {next_label.lower()} cards match the current pathway search.")
