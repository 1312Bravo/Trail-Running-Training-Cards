from __future__ import annotations

from html import escape
from typing import Any

import streamlit as st

from training_cards.philosophy_profiles import PHILOSOPHY_PROFILES, philosophy_profile_display_name

from streamlit_app.config import PHILOSOPHY_SUMMARY_HEIGHT
from streamlit_app.philosophies import load_app_summary
from streamlit_app.state import browse_philosophy_cards, set_active_philosophy, set_active_philosophy_sources


def render_coaching_philosophies(cards: list[Any]) -> None:
    profile_ids = list(PHILOSOPHY_PROFILES)

    for row_start in range(0, len(profile_ids), 2):
        with st.container(border=False, key=f"philosophy-grid-row-{row_start}"):
            cols = st.columns([0.12, 1, 0.18, 1, 0.12], gap="small")
            for offset, profile_id in enumerate(profile_ids[row_start: row_start + 2]):
                with cols[1 + offset * 2]:
                    with st.container(border=True, key=f"philosophy-{profile_id}"):
                        with st.container(border=False, key=f"philosophy-summary-{profile_id}"):
                            summary = load_app_summary(profile_id)
                            summary_lines = summary.splitlines()
                            summary_title = (
                                summary_lines[0][2:].strip()
                                if summary_lines and summary_lines[0].startswith("# ")
                                else philosophy_profile_display_name(profile_id)
                            )
                            summary_body = (
                                "\n".join(summary_lines[1:]).lstrip()
                                if summary_lines and summary_lines[0].startswith("# ")
                                else summary
                            )
                            st.html(
                                '<div class="philosophy-card-title">'
                                f"{escape(summary_title)}"
                                "</div>"
                            )
                        with st.container(border=False, key=f"philosophy-actions-{profile_id}"):
                            card_count = sum(
                                profile_id in getattr(card, "philosophy_profile_ids", [])
                                for card in cards
                            )
                            st.html(
                                '<div class="philosophy-card-count">'
                                f"{card_count} cards in this profile"
                                "</div>"
                            )
                            actions = st.columns(3)
                            with actions[0]:
                                st.button(
                                    "Show cards",
                                    key=f"philosophy_show_cards_{profile_id}",
                                    type="tertiary",
                                    width="stretch",
                                    on_click=browse_philosophy_cards,
                                    args=(profile_id,),
                                )
                            with actions[1]:
                                st.button(
                                    "Read full philosophy",
                                    key=f"philosophy_read_{profile_id}",
                                    type="tertiary",
                                    width="stretch",
                                    on_click=set_active_philosophy,
                                    args=(profile_id,),
                                )
                            with actions[2]:
                                st.button(
                                    "View sources",
                                    key=f"philosophy_sources_{profile_id}",
                                    type="tertiary",
                                    width="stretch",
                                    on_click=set_active_philosophy_sources,
                                    args=(profile_id,),
                                )
                        with st.container(
                            height=PHILOSOPHY_SUMMARY_HEIGHT,
                            border=False,
                            key=f"philosophy-summary-content-{profile_id}",
                        ):
                            st.markdown(summary_body)
