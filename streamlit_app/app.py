from __future__ import annotations

import streamlit as st

from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY

from streamlit_app.config import APP_TITLE, SEARCH_PLACEHOLDER
from streamlit_app.data import card_counts, card_index, filtered_cards, load_library
from streamlit_app.renderers import css, render_contact_footer, render_detail, render_grid


# ----------------------------------------------------------
# Session State
# ----------------------------------------------------------
# The app only needs a search query and the currently opened card.

def set_active_card(card_id: str) -> None:
    st.session_state.active_card_id = card_id


def clear_active_card() -> None:
    st.session_state.active_card_id = None


def init_state() -> None:
    st.session_state.setdefault("search_query", "")
    st.session_state.setdefault("active_card_id", None)
    st.session_state.setdefault("card_scope", "all")


def open_card_dialog(card: object, display_config: dict[str, object], card_by_id: dict[str, object]) -> None:
    @st.dialog(card.title, width="large", on_dismiss=clear_active_card)
    def dialog_content() -> None:
        render_detail(card, display_config, card_by_id, show_header=False)

    dialog_content()


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

    scope_labels = ["All", "Macro", "Mezzo", "Micro", "Session"]
    scope_to_value = {label: label.lower() for label in scope_labels}
    current_scope_label = next(
        (label for label, value in scope_to_value.items() if value == st.session_state.card_scope),
        "All",
    )

    counts = card_counts(cards)
    count_line = " · ".join(f"{label} {count}" for label, count in counts.items())
    st.title(APP_TITLE)
    st.caption(count_line)

    controls = st.columns([1, 1], vertical_alignment="bottom")
    with controls[0]:
        chosen_scope = st.segmented_control(
            "Block",
            scope_labels,
            default=current_scope_label,
            selection_mode="single",
            width="stretch",
        )
    with controls[1]:
        st.session_state.search_query = st.text_input(
            "Search",
            value=st.session_state.search_query,
            placeholder=SEARCH_PLACEHOLDER,
        )
    st.session_state.card_scope = scope_to_value[chosen_scope or "All"]

    cards_for_view = filtered_cards(
        cards,
        st.session_state.card_scope,
        st.session_state.search_query,
    )
    if cards_for_view:
        render_grid(cards_for_view, display_config, key_prefix=st.session_state.card_scope)
    else:
        st.info("No cards match the current filters.")

    active_card = card_by_id.get(st.session_state.active_card_id)
    if active_card:
        open_card_dialog(active_card, display_config, card_by_id)

    render_contact_footer()


if __name__ == "__main__":
    main()
