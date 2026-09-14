from __future__ import annotations

from html import escape
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import streamlit as st

from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY

from streamlit_app.config import APP_MODES, APP_TITLE
from streamlit_app.data import card_counts, card_index, load_library, runtime_cache_dir
from streamlit_app.renderers import css, render_author_footer
from streamlit_app.state import clear_open_views, init_state
from streamlit_app.ui import (
    open_card_dialog,
    open_library_preview_dialog,
    open_philosophy_dialog,
    open_philosophy_sources_dialog,
)
from streamlit_app.views.browse import render_browse_cards
from streamlit_app.views.library import render_card_library
from streamlit_app.views.pathway import render_build_pathway
from streamlit_app.views.philosophies import render_coaching_philosophies
from streamlit_app.views.today import render_today_session


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon=":material/style:", layout="wide")
    css()
    init_state()

    try:
        (
            cards,
            display_config,
            macro_mezzo_reuse_config,
            mezzo_micro_reuse_config,
            micro_session_reuse_config,
            card_library_index,
        ) = load_library(runtime_cache_dir())
    except Exception as error:
        st.error(
            "The local card cache could not be loaded. "
            "Run the local cloud-library download command, or configure the "
            "`gcp_service_account` secrets block when running on Streamlit Cloud."
        )
        st.exception(error)
        return

    card_by_id = card_index(cards)
    counts = card_counts(cards)
    count_line = " · ".join(f"{label} {count}" for label, count in counts.items())
    st.title(APP_TITLE)
    st.html(f'<div class="app-card-count">{escape(count_line)}</div>')

    mode_cols = st.columns([0.13, 0.74, 0.13])
    with mode_cols[1]:
        st.segmented_control(
            "Mode",
            APP_MODES,
            key="app_mode",
            selection_mode="single",
            width="stretch",
            label_visibility="collapsed",
            on_change=clear_open_views,
        )
    if st.session_state.app_mode != st.session_state.last_app_mode:
        clear_open_views()
        st.session_state.last_app_mode = st.session_state.app_mode

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

    render_author_footer()

    active_card = card_by_id.get(st.session_state.active_card_id)
    if active_card:
        open_card_dialog(active_card, display_config, card_by_id)

    active_library_preview_card = card_by_id.get(st.session_state.active_library_preview_card_id)
    if active_library_preview_card:
        open_library_preview_dialog(active_library_preview_card, display_config)

    if st.session_state.active_philosophy_profile_id:
        open_philosophy_dialog(st.session_state.active_philosophy_profile_id)

    if st.session_state.active_philosophy_sources_profile_id:
        open_philosophy_sources_dialog(st.session_state.active_philosophy_sources_profile_id)


if __name__ == "__main__":
    main()
