from __future__ import annotations

from typing import Any

import streamlit as st

from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY
from training_cards.philosophy_profiles import (
    COMMON_PHILOSOPHY_PROFILE_ID,
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
)


APP_MODES = [
    "Browse cards",
    "Build pathway",
    "Today session",
    "Coaching philosophies",
]
PHILOSOPHY_SUMMARY_HEIGHT = 380
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
    st.session_state.active_card_id = card_id


def clear_active_card() -> None:
    st.session_state.active_card_id = None


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
    st.session_state.setdefault("active_philosophy_profile_id", None)
    st.session_state.setdefault("active_philosophy_sources_profile_id", None)
    st.session_state.setdefault("app_mode", APP_MODES[0])
    st.session_state.setdefault("card_scope_label", None)
    st.session_state.setdefault("tag_filters", [])
    st.session_state.setdefault("philosophy_profile_filters", [])
    for level, _ in PATHWAY_STEPS:
        st.session_state.setdefault(state_key_for_level(level), None)


def open_card_dialog(card: object, display_config: dict[str, object], card_by_id: dict[str, object]) -> None:
    @st.dialog(card.title, width="medium", on_dismiss=clear_active_card)
    def dialog_content() -> None:
        render_detail(card, display_config, card_by_id, show_header=False)

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

    controls = st.columns([0.16, 1.2, 0.08, 0.58, 0.16], vertical_alignment="center")
    with controls[1]:
        with st.container(horizontal_alignment="center"):
            chosen_scope = st.segmented_control(
                "Block",
                scope_labels,
                key="card_scope_label",
                selection_mode="single",
                width="stretch",
                label_visibility="collapsed",
            )
    with controls[3]:
        with st.container(horizontal_alignment="center"):
            st.session_state.search_query = st.text_input(
                "Search",
                value=st.session_state.search_query,
                placeholder=SEARCH_PLACEHOLDER,
                help="Searches across titles, block types, summary, purpose, coaching philosophy, levels, tags, and notes.",
                width="stretch",
                label_visibility="collapsed",
            )
    st.session_state.card_scope = scope_to_value.get(chosen_scope, "all")
    philosophy_profile_options = list(PHILOSOPHY_PROFILES)
    if philosophy_profile_options:
        st.multiselect(
            "Coaching philosophy",
            philosophy_profile_options,
            key="philosophy_profile_filters",
            format_func=philosophy_profile_display_name,
            placeholder="All coaching philosophies",
            help="Show cards shaped by at least one selected coaching philosophy.",
        )
    render_active_tag_filters()

    cards_for_view = filtered_cards(
        cards,
        st.session_state.card_scope,
        st.session_state.search_query,
        tag_filters=st.session_state.tag_filters,
        philosophy_profile_filters=st.session_state.philosophy_profile_filters,
    )
    if cards_for_view:
        render_grid(cards_for_view, display_config, key_prefix=st.session_state.card_scope)
    else:
        st.caption("No cards match the current filters.")


# ----------------------------------------------------------
# Coaching Philosophies Mode
# ----------------------------------------------------------

def render_coaching_philosophies(cards: list[Any]) -> None:
    st.caption(
        "The shared foundation and named profiles explain the coaching reasoning that shapes this card library."
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
                    action_count = (
                        2 if profile_id == COMMON_PHILOSOPHY_PROFILE_ID else 3
                    )
                    actions = st.columns(action_count)
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
                    if profile_id != COMMON_PHILOSOPHY_PROFILE_ID:
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


def render_active_tag_filters() -> None:
    if not st.session_state.tag_filters:
        return

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


def pathway_candidates(cards: list[Any], selected_cards: dict[str, Any | None]) -> tuple[str, str, list[Any]]:
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
    return next_level, next_label, related_child_cards(cards, previous_card, next_level)


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
) -> None:
    selected_cards = selected_pathway_cards(card_by_id)
    render_pathway_selection(selected_cards, display_config)

    next_level, next_label, candidates = pathway_candidates(cards, selected_cards)
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

    step_cols = st.columns([0.18, 1, 0.28, 1, 0.18], gap="small", vertical_alignment="center")
    with step_cols[1]:
        st.caption(f"Choose {next_label.lower()}")
    with step_cols[3]:
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
    render_search_terms("pathway_search_terms")
    render_active_tag_filters()

    visible_candidates = cards_matching_tags(
        cards_matching_terms(candidates, st.session_state.pathway_search_terms),
        st.session_state.tag_filters,
    )
    if visible_candidates:
        render_grid(
            visible_candidates,
            display_config,
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

    cols = st.columns([0.18, 1, 0.28, 1, 0.18], gap="small", vertical_alignment="center")
    with cols[1]:
        st.caption("Quick choose for today")
    with cols[3]:
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
    render_search_terms("today_search_terms")
    render_active_tag_filters()

    visible_sessions = cards_matching_tags(
        cards_matching_terms(session_cards, st.session_state.today_search_terms),
        st.session_state.tag_filters,
    )

    if visible_sessions:
        render_grid(
            visible_sessions,
            display_config,
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
        cards, display_config = load_library(cache_dir)
    except Exception as error:
        st.error(
            "The local card cache could not be loaded. "
            "Run `py -m training_cards.scripts.download_cloud_library` and `py -m training_cards.scripts.validate_cache`."
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
        render_build_pathway(cards, display_config, card_by_id)
    elif st.session_state.app_mode == "Today session":
        render_today_session(cards, display_config)
    elif st.session_state.app_mode == "Coaching philosophies":
        render_coaching_philosophies(cards)
    else:
        render_browse_cards(cards, display_config)

    active_card = card_by_id.get(st.session_state.active_card_id)
    if active_card:
        open_card_dialog(active_card, display_config, card_by_id)

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
