from __future__ import annotations

from html import escape
from typing import Any

import streamlit as st

from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY
from training_cards.philosophy_profiles import (
    PHILOSOPHY_PROFILES,
    philosophy_profile_display_name,
)

from streamlit_app.config import (
    APP_TITLE,
    SEARCH_PLACEHOLDER,
)
from streamlit_app.data import (
    card_matches_search,
    card_counts,
    card_index,
    cards_of_type,
    filtered_cards,
    load_library,
    related_child_cards,
    reusable_micro_ids_for_philosophies,
    reusable_mezzo_ids_for_philosophies,
    reusable_session_ids_for_philosophies,
)
from streamlit_app.philosophies import (
    load_app_summary,
    load_detailed_note,
    load_reviewed_source_bullets,
)
from streamlit_app.renderers import (
    css,
    display_text,
    render_contact_links,
    render_detail,
    render_grid,
    render_preview_card,
)


APP_MODES = [
    "Browse cards",
    "Card library",
    "Build pathway",
    "Today session",
    "Coaching philosophies",
]
PHILOSOPHY_SUMMARY_HEIGHT = 380
DEFAULT_CARDS_PER_PAGE = 8
CARD_PAGE_SIZE_OPTIONS = [6, 8, 12]
PATHWAY_STEPS = [
    ("macro", "Macro"),
    ("mezzo", "Mezzo"),
    ("micro", "Micro"),
    ("session", "Session"),
]


# ----------------------------------------------------------
# Session State
# ----------------------------------------------------------
# The app only needs a search query and the currently opened card.

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
    st.session_state.active_library_preview_card_id = card_id


def clear_active_library_preview() -> None:
    st.session_state.active_library_preview_card_id = None


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


def browse_philosophy_cards(profile_id: str) -> None:
    st.session_state.app_mode = "Browse cards"
    st.session_state.card_scope_label = None
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
    return [
        card
        for card in cards
        if all(tag in card.tags for tag in tags)
    ]


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
        macro_mezzo_reuse_config,
        parent_card_id,
        profile_ids,
    )
    reused_micro_ids = reusable_micro_ids_for_philosophies(
        mezzo_micro_reuse_config,
        parent_card_id,
        profile_ids,
    )
    reused_session_ids = reusable_session_ids_for_philosophies(
        micro_session_reuse_config,
        parent_card_id,
        profile_ids,
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


def remove_tag_filter(tag: str) -> None:
    st.session_state.tag_filters = [
        selected_tag
        for selected_tag in st.session_state.tag_filters
        if selected_tag != tag
    ]


def init_state() -> None:
    st.session_state.setdefault("search_query", "")
    st.session_state.setdefault("pathway_search_input", "")
    st.session_state.setdefault("pathway_search_terms", [])
    st.session_state.setdefault("today_search_input", "")
    st.session_state.setdefault("today_search_terms", [])
    st.session_state.setdefault("active_card_id", None)
    st.session_state.setdefault("active_library_preview_card_id", None)
    st.session_state.setdefault("active_card_history", [])
    st.session_state.setdefault("active_philosophy_profile_id", None)
    st.session_state.setdefault("active_philosophy_sources_profile_id", None)
    st.session_state.setdefault("app_mode", APP_MODES[0])
    st.session_state.setdefault("card_scope_label", None)
    st.session_state.setdefault("tag_filters", [])
    st.session_state.setdefault("philosophy_profile_filters", [])
    st.session_state.setdefault("library_level_label", "Macro")
    st.session_state.setdefault("library_search_query", "")
    st.session_state.setdefault("library_profile_filters", [])
    for level, _ in PATHWAY_STEPS:
        st.session_state.setdefault(state_key_for_level(level), None)


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
        controls = st.columns([0.28, 1, 0.26, 0.22, 0.26], gap="small", vertical_alignment="center")
        with controls[0]:
            st.segmented_control(
                "Cards per page",
                CARD_PAGE_SIZE_OPTIONS,
                key=f"{state_prefix}_page_size",
                selection_mode="single",
                width="stretch",
                label_visibility="collapsed",
            )
        with controls[1]:
            st.html(
                '<div class="pagination-status">'
                f'<span>Showing {start_item}-{end_item}</span>'
                f'<strong>{total_cards} cards</strong>'
                '</div>'
            )
        with controls[2]:
            st.button(
                "Previous",
                key=f"pagination_{state_prefix}_previous_page",
                type="secondary",
                width="stretch",
                disabled=page <= 0,
                on_click=set_session_state_value,
                args=(page_state_key, max(0, page - 1)),
            )
        with controls[3]:
            st.html(f'<div class="pagination-page">Page {page + 1} / {total_pages}</div>')
        with controls[4]:
            st.button(
                "Next",
                key=f"pagination_{state_prefix}_next_page",
                type="secondary",
                width="stretch",
                disabled=page >= total_pages - 1,
                on_click=set_session_state_value,
                args=(page_state_key, min(total_pages - 1, page + 1)),
            )


def set_session_state_value(key: str, value: Any) -> None:
    st.session_state[key] = value


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
    page_size_key = f"{state_prefix}_page_size"
    page_key = f"{state_prefix}_page"
    signature_key = f"{state_prefix}_signature"

    st.session_state.setdefault(page_size_key, DEFAULT_CARDS_PER_PAGE)
    st.session_state.setdefault(page_key, 0)
    st.session_state.setdefault(signature_key, ())

    current_signature = page_signature(cards)
    if st.session_state[signature_key] != current_signature:
        st.session_state[signature_key] = current_signature
        st.session_state[page_key] = 0

    page_size = int(st.session_state.get(page_size_key) or DEFAULT_CARDS_PER_PAGE)
    total_pages = max(1, (len(cards) + page_size - 1) // page_size)
    page = min(max(0, int(st.session_state.get(page_key, 0))), total_pages - 1)
    st.session_state[page_key] = page

    start = page * page_size
    end = start + page_size
    page_cards = cards[start:end]

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


def open_card_dialog(card: object, display_config: dict[str, object], card_by_id: dict[str, object]) -> None:
    @st.dialog(" ", width="medium", on_dismiss=clear_active_card)
    def dialog_content() -> None:
        render_detail(card, display_config, card_by_id, show_header=True)

    dialog_content()


def open_library_preview_dialog(card: object, display_config: dict[str, object]) -> None:
    @st.dialog("Card preview", width="medium", on_dismiss=clear_active_library_preview)
    def dialog_content() -> None:
        render_preview_card(
            card,
            display_config,
            key_prefix="library_preview_dialog",
            open_label="Open full card",
        )

    dialog_content()


def open_philosophy_dialog(profile_id: str) -> None:
    profile_name = philosophy_profile_display_name(profile_id)

    @st.dialog(f"{profile_name} philosophy", width="large", on_dismiss=clear_active_philosophy)
    def dialog_content() -> None:
        st.markdown(load_detailed_note(profile_id))

    dialog_content()


def open_philosophy_sources_dialog(profile_id: str) -> None:
    profile_name = philosophy_profile_display_name(profile_id)

    @st.dialog(
        f"{profile_name} reviewed sources",
        width="large",
        on_dismiss=clear_active_philosophy_sources,
    )
    def dialog_content() -> None:
        st.caption(
            "Reviewed official material used to inform this library's interpretation."
        )
        st.markdown(load_reviewed_source_bullets(profile_id))

    dialog_content()


# ----------------------------------------------------------
# Browse Mode
# ----------------------------------------------------------

def render_browse_cards(cards: list[Any], display_config: dict[str, Any]) -> None:
    scope_labels = ["Macro", "Mezzo", "Micro", "Session"]
    scope_to_value = {label: label.lower() for label in scope_labels}
    if st.session_state.card_scope_label not in scope_labels:
        st.session_state.card_scope_label = None

    with st.container(border=False, key="browse-toolbar"):
        controls = st.columns([1.05, 1], gap="large", vertical_alignment="center")
        with controls[0]:
            chosen_scope = st.segmented_control(
                "Block",
                scope_labels,
                key="card_scope_label",
                selection_mode="single",
                width="stretch",
                label_visibility="collapsed",
            )
        with controls[1]:
            st.session_state.search_query = st.text_input(
                "Search",
                value=st.session_state.search_query,
                placeholder=SEARCH_PLACEHOLDER,
                help="Searches across titles, block types, summary, purpose, coaching philosophy, levels, tags, and notes.",
                width="stretch",
                label_visibility="collapsed",
            )

        filter_controls = st.columns([1.05, 1], gap="large", vertical_alignment="bottom")
        with filter_controls[0]:
            render_active_tag_filters(show_label=False)
        with filter_controls[1]:
            render_philosophy_profile_filter(label_visibility="collapsed")
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


# ----------------------------------------------------------
# Card Library Mode
# ----------------------------------------------------------

def render_card_library(card_library_index: dict[str, Any]) -> None:
    level_labels = ["All", "Macro", "Mezzo", "Micro", "Session"]
    level_to_value = {label: label.lower() for label in level_labels if label != "All"}
    if st.session_state.library_level_label not in level_labels:
        st.session_state.library_level_label = "All"

    st.caption(
        "Compact library index. Direct cards belong to the selected philosophy; reused cards are shown with their source profile."
    )
    controls = st.columns([0.75, 1, 1], gap="large", vertical_alignment="center")
    with controls[0]:
        chosen_level = st.segmented_control(
            "Library level",
            level_labels,
            key="library_level_label",
            selection_mode="single",
            width="stretch",
            label_visibility="collapsed",
        )
    selected_level = level_to_value.get(chosen_level)
    levels_index = card_library_index.get("levels", {})
    level_names = [selected_level] if selected_level else ["macro", "mezzo", "micro", "session"]
    level_index = _combine_library_levels(levels_index, level_names)
    profile_ids = [
        profile_id
        for profile_id in PHILOSOPHY_PROFILES
        if profile_id in level_index
    ]
    st.session_state.library_profile_filters = [
        profile_id
        for profile_id in st.session_state.library_profile_filters
        if profile_id in profile_ids
    ]

    with controls[1]:
        st.multiselect(
            "Philosophy",
            profile_ids,
            key="library_profile_filters",
            format_func=philosophy_profile_display_name,
            placeholder="All philosophies",
            label_visibility="collapsed",
            width="stretch",
        )
    with controls[2]:
        st.text_input(
            "Search library",
            key="library_search_query",
            placeholder="Search titles, descriptions, IDs, or source",
            label_visibility="collapsed",
            width="stretch",
        )

    selected_profiles = st.session_state.library_profile_filters or profile_ids
    total_visible = 0
    for profile_id in selected_profiles:
        entries = _filtered_library_entries(
            level_index.get(profile_id, []),
            st.session_state.library_search_query,
        )
        if not entries:
            continue
        total_visible += len(entries)
        direct_count = sum(entry.get("source") == "direct" for entry in entries)
        reused_count = len(entries) - direct_count
        with st.expander(
            f"{philosophy_profile_display_name(profile_id)} · {len(entries)} cards",
            expanded=bool(st.session_state.library_profile_filters),
        ):
            st.caption(f"{direct_count} direct · {reused_count} reused")
            render_library_header()
            for entry in entries:
                render_library_entry(entry, profile_id)

    if total_visible == 0:
        st.caption("No library entries match the current filters.")


def render_library_entry(entry: dict[str, Any], profile_id: str) -> None:
    source = entry.get("source", "direct")
    source_profile = entry.get("source_profile")
    source_label = ""
    if source == "reused" and source_profile:
        source_label = f"reused from {philosophy_profile_display_name(source_profile)}"
    elif source == "direct":
        source_label = "direct"

    row = st.columns([0.03, 0.28, 0.49, 0.12, 0.08], gap="small", vertical_alignment="center")
    with row[0]:
        st.html('<div class="library-bullet">•</div>')
    with row[1]:
        st.button(
            entry["title"],
            key=f"library_open_{profile_id}_{entry['card_id']}",
            type="secondary",
            width="stretch",
            on_click=set_active_card,
            args=(entry["card_id"],),
        )
    with row[2]:
        st.html(
            '<div class="library-description">'
            f'{escape(entry.get("description", ""))}'
            '</div>'
        )
    with row[3]:
        st.html(
            '<div class="library-source">'
            f'{escape(source_label)}'
            '</div>'
        )
    with row[4]:
        st.html(
            '<div class="library-level">'
            f'{escape(display_text(entry.get("level", "")))}'
            '</div>'
        )


def render_library_header() -> None:
    row = st.columns([0.03, 0.28, 0.49, 0.12, 0.08], gap="small")
    labels = ["", "Title", "Description", "Source", "Block"]
    for column, label in zip(row, labels, strict=True):
        with column:
            st.html(f'<div class="library-header">{escape(label)}</div>')


def _combine_library_levels(
    levels_index: dict[str, dict[str, list[dict[str, Any]]]],
    level_names: list[str],
) -> dict[str, list[dict[str, Any]]]:
    combined: dict[str, list[dict[str, Any]]] = {}
    for level_name in level_names:
        for profile_id, entries in levels_index.get(level_name, {}).items():
            combined.setdefault(profile_id, []).extend(
                dict(entry, level=level_name)
                for entry in entries
            )
    return combined


def _filtered_library_entries(entries: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    normalized_query = query.strip().lower().replace("_", " ")
    if not normalized_query:
        return entries

    return [
        entry
        for entry in entries
        if normalized_query in _library_entry_search_text(entry)
    ]


def _library_entry_search_text(entry: dict[str, Any]) -> str:
    values = [
        entry.get("card_id", ""),
        entry.get("title", ""),
        entry.get("description", ""),
        entry.get("source", ""),
        entry.get("source_profile", ""),
        entry.get("source_profile", "").replace("_", " "),
    ]
    return " ".join(values).lower()


# ----------------------------------------------------------
# Coaching Philosophies Mode
# ----------------------------------------------------------

def render_coaching_philosophies(cards: list[Any]) -> None:
    st.caption(
        "Every card follows the shared coaching foundation. These profiles show the training methods that shape card content."
    )
    profile_ids = list(PHILOSOPHY_PROFILES)

    for row_start in range(0, len(profile_ids), 2):
        cols = st.columns([0.12, 1, 0.18, 1, 0.12], gap="small")
        for offset, profile_id in enumerate(profile_ids[row_start: row_start + 2]):
            with cols[1 + offset * 2]:
                with st.container(border=True, key=f"philosophy-{profile_id}"):
                    with st.container(
                        height=PHILOSOPHY_SUMMARY_HEIGHT,
                        border=False,
                        key=f"philosophy-summary-{profile_id}",
                    ):
                        st.markdown(load_app_summary(profile_id))
                    st.divider()
                    card_count = sum(
                        profile_id in getattr(card, "philosophy_profile_ids", [])
                        for card in cards
                    )
                    st.caption(f"{card_count} cards in this profile")
                    actions = st.columns(3)
                    with actions[0]:
                        st.button(
                            "Show cards",
                            key=f"philosophy_show_cards_{profile_id}",
                            type="secondary",
                            width="stretch",
                            on_click=browse_philosophy_cards,
                            args=(profile_id,),
                        )
                    with actions[1]:
                        st.button(
                            "Read full philosophy",
                            key=f"philosophy_read_{profile_id}",
                            type="secondary",
                            width="stretch",
                            on_click=set_active_philosophy,
                            args=(profile_id,),
                        )
                    with actions[2]:
                        st.button(
                            "View sources",
                            key=f"philosophy_sources_{profile_id}",
                            type="secondary",
                            width="stretch",
                            on_click=set_active_philosophy_sources,
                            args=(profile_id,),
                        )


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
    philosophy_profile_options = list(PHILOSOPHY_PROFILES)
    if not philosophy_profile_options:
        return
    st.session_state.philosophy_profile_filters = [
        profile_id
        for profile_id in st.session_state.philosophy_profile_filters
        if profile_id in PHILOSOPHY_PROFILES
    ]

    st.multiselect(
        "Coaching philosophy",
        philosophy_profile_options,
        key="philosophy_profile_filters",
        format_func=philosophy_profile_display_name,
        placeholder="All coaching philosophies",
        help="Show cards shaped by at least one selected coaching philosophy.",
        width="stretch",
        label_visibility=label_visibility,
    )


# ----------------------------------------------------------
# Pathway Mode
# ----------------------------------------------------------

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


def render_pathway_selection(selected_cards: dict[str, Any | None], display_config: dict[str, Any]) -> None:
    with st.container(border=True, key="pathway-selection"):
        top_cols = st.columns([1, 0.12], vertical_alignment="center")
        with top_cols[0]:
            st.caption("Selected pathway")
        with top_cols[1]:
            st.button("Clear", key="clear_pathway", width="stretch", on_click=clear_pathway)

        cols = st.columns(4, gap="small")
        for index, (level, label) in enumerate(PATHWAY_STEPS):
            card = selected_cards[level]
            with cols[index]:
                with st.container(border=True, height=135, key=f"pathway-card-{level}"):
                    st.caption(label)
                    if card is None:
                        st.caption("Not selected")
                        continue
                    st.markdown(f"**{card.title}**")
                    with st.container(horizontal=True):
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
        st.caption("Pathway complete. Use Open card on any selected card to inspect details, or Remove to revise one step.")
        pathway_cards = [
            selected_cards[level]
            for level, _ in PATHWAY_STEPS
            if selected_cards[level] is not None
        ]
        if pathway_cards:
            st.caption("Chosen pathway cards")
            render_grid(
                pathway_cards,
                display_config,
                key_prefix="completed_pathway",
            )
        return

    with st.container(border=False, key="mode-toolbar-pathway"):
        controls = st.columns([1.05, 1], gap="large", vertical_alignment="center")
        with controls[0]:
            st.caption(f"Choose {next_label.lower()}")
        with controls[1]:
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

        filter_controls = st.columns([1.05, 1], gap="large", vertical_alignment="bottom")
        with filter_controls[0]:
            render_active_tag_filters(show_label=False)
        with filter_controls[1]:
            render_search_terms("pathway_search_terms")
            render_philosophy_profile_filter(label_visibility="collapsed")

    visible_candidates = cards_matching_philosophies(
        cards_matching_tags(
            cards_matching_terms(candidates, st.session_state.pathway_search_terms),
            st.session_state.tag_filters,
        ),
        st.session_state.philosophy_profile_filters,
        macro_mezzo_reuse_config,
        mezzo_micro_reuse_config,
        micro_session_reuse_config,
        (
            selected_cards["macro"].id
            if next_level == "mezzo" and selected_cards["macro"]
            else selected_cards["mezzo"].id
            if next_level == "micro" and selected_cards["mezzo"]
            else selected_cards["micro"].id
            if next_level == "session" and selected_cards["micro"]
            else None
        ),
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


# ----------------------------------------------------------
# Today Session Mode
# ----------------------------------------------------------

def render_today_session(cards: list[Any], display_config: dict[str, Any]) -> None:
    session_cards = cards_of_type(cards, "session")

    with st.container(border=False, key="mode-toolbar-today"):
        controls = st.columns([1.05, 1], gap="large", vertical_alignment="center")
        with controls[0]:
            st.caption("Quick choose for today")
        with controls[1]:
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

        filter_controls = st.columns([1.05, 1], gap="large", vertical_alignment="bottom")
        with filter_controls[0]:
            render_active_tag_filters(show_label=False)
        with filter_controls[1]:
            render_search_terms("today_search_terms")
            render_philosophy_profile_filter(label_visibility="collapsed")

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


# ----------------------------------------------------------
# Page Shell
# ----------------------------------------------------------
# Keep the page composition here so the render helpers remain reusable.

def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon=":material/style:", layout="wide")
    css()
    init_state()

    cache_dir = GOOGLE_DRIVE_LIBRARY.local_cache_dir

    try:
        (
            cards,
            display_config,
            macro_mezzo_reuse_config,
            mezzo_micro_reuse_config,
            micro_session_reuse_config,
            card_library_index,
        ) = load_library(cache_dir)
    except Exception as error:
        st.error(
            "The local card cache could not be loaded. "
            "Run `py -m training_cards.scripts.cloud.download_cloud_library` and `py -m training_cards.scripts.cache.validate_cache`."
        )
        st.exception(error)
        return

    card_by_id = card_index(cards)

    counts = card_counts(cards)
    count_line = " · ".join(f"{label} {count}" for label, count in counts.items())
    header_cols = st.columns([2, 1], vertical_alignment="center")
    with header_cols[0]:
        st.title(APP_TITLE)
        st.caption(count_line)
    with header_cols[1]:
        render_contact_links()

    mode_cols = st.columns([0.13, 0.74, 0.13])
    with mode_cols[1]:
        st.segmented_control(
            "Mode",
            APP_MODES,
            key="app_mode",
            selection_mode="single",
            width="stretch",
            label_visibility="collapsed",
        )

    if st.session_state.app_mode == "Build pathway":
        render_build_pathway(
            cards,
            display_config,
            card_by_id,
            macro_mezzo_reuse_config,
            mezzo_micro_reuse_config,
            micro_session_reuse_config,
        )
    elif st.session_state.app_mode == "Card library":
        render_card_library(card_library_index)
    elif st.session_state.app_mode == "Today session":
        render_today_session(cards, display_config)
    elif st.session_state.app_mode == "Coaching philosophies":
        render_coaching_philosophies(cards)
    else:
        render_browse_cards(cards, display_config)

    active_card = card_by_id.get(st.session_state.active_card_id)
    if active_card:
        open_card_dialog(active_card, display_config, card_by_id)

    active_library_preview_card = card_by_id.get(st.session_state.active_library_preview_card_id)
    if active_library_preview_card:
        open_library_preview_dialog(active_library_preview_card, display_config)

    active_philosophy_profile_id = st.session_state.active_philosophy_profile_id
    if active_philosophy_profile_id:
        open_philosophy_dialog(active_philosophy_profile_id)

    active_philosophy_sources_profile_id = (
        st.session_state.active_philosophy_sources_profile_id
    )
    if active_philosophy_sources_profile_id:
        open_philosophy_sources_dialog(active_philosophy_sources_profile_id)


if __name__ == "__main__":
    main()
