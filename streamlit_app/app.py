from __future__ import annotations

from pathlib import Path

import streamlit as st

from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY

from streamlit_app.config import APP_SUBTITLE, APP_TITLE, SEARCH_PLACEHOLDER
from streamlit_app.data import card_counts, card_index, filtered_cards, load_library
from streamlit_app.renderers import css, render_detail, render_grid


# ----------------------------------------------------------
# Session State
# ----------------------------------------------------------
# The app only needs a search query and the currently opened card.

def set_active_card(card_id: str) -> None:
    st.session_state.active_card_id = card_id


def init_state() -> None:
    st.session_state.setdefault("search_query", "")
    st.session_state.setdefault("active_card_id", None)


# ----------------------------------------------------------
# Navigation Tabs
# ----------------------------------------------------------
# Each tab is a view over the same card set, filtered by planning level.

def type_tabs(cards: list[object], display_config: dict[str, object]) -> None:
    tabs = st.tabs(["All cards", "Macro", "Mezzo", "Micro", "Session"])
    tab_specs = [
        ("all", tabs[0]),
        ("macro", tabs[1]),
        ("mezzo", tabs[2]),
        ("micro", tabs[3]),
        ("session", tabs[4]),
    ]

    for selected_type, tab in tab_specs:
        with tab:
            cards_for_tab = filtered_cards(cards, selected_type, st.session_state.search_query)
            if not cards_for_tab:
                st.info("No cards match the current filters.")
                continue
            render_grid(cards_for_tab, display_config, key_prefix=selected_type)


# ----------------------------------------------------------
# Page Shell
# ----------------------------------------------------------
# Keep the page composition here so the render helpers remain reusable.

def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon="🏔", layout="wide")
    css()
    init_state()

    st.markdown(
        f"""
        <div class="hero">
            <h1>{APP_TITLE}</h1>
            <p>{APP_SUBTITLE}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

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

    top_cols = st.columns(5)
    for col, (label, count) in zip(top_cols, card_counts(cards).items(), strict=False):
        with col:
            st.metric(label, count)

    st.sidebar.markdown("### Filters")
    st.session_state.search_query = st.sidebar.text_input(
        "Search cards",
        value=st.session_state.search_query,
        placeholder=SEARCH_PLACEHOLDER,
    )
    st.sidebar.caption("Search matches titles, summaries, purposes, tags, and additional coaching notes.")
    st.sidebar.markdown("### Reading order")
    st.sidebar.caption("All cards comes first, then each planning level.")

    st.markdown('<div class="section-label">Preview first</div>', unsafe_allow_html=True)
    st.caption("The preview uses the summary, purpose, suitable levels, and tags. Open any card to see the full coaching view.")

    type_tabs(cards, display_config)

    active_card = card_by_id.get(st.session_state.active_card_id)
    st.divider()
    st.markdown('<div class="section-label">Open card</div>', unsafe_allow_html=True)
    if active_card:
        render_detail(active_card, display_config, card_by_id)
    else:
        st.info("Pick a card from any tab to open the full coaching view here.")


if __name__ == "__main__":
    main()
