from __future__ import annotations

from html import escape
from typing import Any

import streamlit as st

from training_cards.philosophy_profiles import (
    PHILOSOPHY_PROFILES,
    philosophy_profile_display_name,
)

from streamlit_app.config import (
    DEFAULT_CARDS_PER_PAGE,
)
from streamlit_app.philosophies import load_detailed_note, load_reviewed_source_bullets
from streamlit_app.renderers import render_detail, render_grid, render_preview_card
from streamlit_app.state import (
    clear_active_card,
    clear_active_library_preview,
    clear_active_philosophy,
    clear_active_philosophy_sources,
    open_full_card_from_library_preview,
    remove_search_term,
    remove_tag_filter,
    set_session_state_value,
)
from streamlit_app.renderers.shared import display_text


def page_signature(cards: list[Any]) -> tuple[str, ...]:
    return tuple(card.id for card in cards)


def render_pagination_controls(
    total_cards: int,
    page_size: int,
    page: int,
    state_prefix: str,
) -> None:
    total_pages = max(1, (total_cards + page_size - 1) // page_size)
    page_state_key = f"{state_prefix}_page"
    start_item = page * page_size + 1 if total_cards else 0
    end_item = min((page + 1) * page_size, total_cards)

    with st.container(key=f"pagination-{state_prefix}"):
        controls = st.columns(
            [1, 0.1, 0.12, 0.1], gap="small", vertical_alignment="center"
        )
        with controls[0]:
            st.html(
                '<div class="pagination-status">'
                f"<span>Showing {start_item}-{end_item}</span>"
                f"<strong>{total_cards} cards</strong>"
                "</div>"
            )
        with controls[1]:
            st.button(
                "Previous",
                key=f"pagination_{state_prefix}_previous_page",
                type="secondary",
                width="content",
                disabled=page <= 0,
                on_click=set_session_state_value,
                args=(page_state_key, max(0, page - 1)),
            )
        with controls[2]:
            st.html(f'<div class="pagination-page">Page {page + 1} / {total_pages}</div>')
        with controls[3]:
            st.button(
                "Next",
                key=f"pagination_{state_prefix}_next_page",
                type="secondary",
                width="stretch",
                disabled=page >= total_pages - 1,
                on_click=set_session_state_value,
                args=(page_state_key, min(total_pages - 1, page + 1)),
            )


def render_paginated_grid(
    cards: list[Any],
    display_config: dict[str, Any],
    state_prefix: str,
    key_prefix: str,
    select_label: str | None = None,
    open_label: str = "Open card",
    on_select: Any | None = None,
    select_level: str | None = None,
) -> None:
    page_key = f"{state_prefix}_page"
    signature_key = f"{state_prefix}_signature"
    st.session_state.setdefault(page_key, 0)
    st.session_state.setdefault(signature_key, ())

    current_signature = page_signature(cards)
    if st.session_state[signature_key] != current_signature:
        st.session_state[signature_key] = current_signature
        st.session_state[page_key] = 0

    page_size = DEFAULT_CARDS_PER_PAGE
    total_pages = max(1, (len(cards) + page_size - 1) // page_size)
    page = min(max(0, int(st.session_state.get(page_key, 0))), total_pages - 1)
    st.session_state[page_key] = page
    page_cards = cards[page * page_size: (page + 1) * page_size]

    render_grid(
        page_cards,
        display_config,
        key_prefix=f"{key_prefix}_page_{page}",
        select_label=select_label,
        open_label=open_label,
        on_select=on_select,
        select_level=select_level,
    )
    render_pagination_controls(len(cards), page_size, page, state_prefix)


def render_search_terms(terms_key: str) -> None:
    terms = st.session_state.get(terms_key, [])
    if not terms:
        return
    with st.container(horizontal=True):
        for term in terms:
            st.button(
                f"{term} ×",
                key=f"{terms_key}_{term}",
                type="secondary",
                width="content",
                on_click=remove_search_term,
                args=(terms_key, term),
            )


def render_active_tag_filters(show_label: bool = True) -> None:
    if not st.session_state.tag_filters:
        return
    if show_label:
        st.caption("Tag filters")
    with st.container(horizontal=True):
        for tag in st.session_state.tag_filters:
            st.button(
                f"{display_text(tag)} ×",
                key=f"selected_tag_{tag}",
                type="secondary",
                width="content",
                on_click=remove_tag_filter,
                args=(tag,),
            )


def render_philosophy_profile_filter(label_visibility: str = "visible") -> None:
    options = list(PHILOSOPHY_PROFILES)
    if not options:
        return
    st.session_state.philosophy_profile_filters = [
        profile_id
        for profile_id in st.session_state.philosophy_profile_filters
        if profile_id in PHILOSOPHY_PROFILES
    ]
    st.multiselect(
        "Coaching philosophy",
        options,
        key="philosophy_profile_filters",
        format_func=philosophy_profile_display_name,
        placeholder="All coaching philosophies",
        help="Show cards shaped by at least one selected coaching philosophy.",
        width="stretch",
        label_visibility=label_visibility,
    )


def open_card_dialog(card: object, display_config: dict[str, object], card_by_id: dict[str, object]) -> None:
    @st.dialog(" ", width="medium", on_dismiss=clear_active_card)
    def dialog_content() -> None:
        render_detail(card, display_config, card_by_id, show_header=True)
    dialog_content()


def open_library_preview_dialog(card: object, display_config: dict[str, object]) -> None:
    @st.dialog(" ", width="medium", on_dismiss=clear_active_library_preview)
    def dialog_content() -> None:
        render_preview_card(
            card,
            display_config,
            key_prefix="library_preview_dialog",
            height=None,
            open_label="Open full card",
            open_callback=open_full_card_from_library_preview,
        )
    dialog_content()


def open_philosophy_dialog(profile_id: str) -> None:
    @st.dialog(" ", width="medium", on_dismiss=clear_active_philosophy)
    def dialog_content() -> None:
        with st.container(border=False, key=f"full-philosophy-{profile_id}"):
            st.markdown(load_detailed_note(profile_id))
    dialog_content()


def open_philosophy_sources_dialog(profile_id: str) -> None:
    @st.dialog(" ", width="medium", on_dismiss=clear_active_philosophy_sources)
    def dialog_content() -> None:
        with st.container(border=False, key=f"philosophy-sources-{profile_id}"):
            st.caption("Reviewed sources used to inform this library's interpretation.")
            st.markdown(load_reviewed_source_bullets(profile_id))
    dialog_content()
