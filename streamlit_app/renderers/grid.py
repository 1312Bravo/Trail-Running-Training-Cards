from __future__ import annotations

from typing import Any

import streamlit as st

from .preview import render_preview_card


# ----------------------------------------------------------
# Grid Layout
# ----------------------------------------------------------

def render_grid(
    cards: list[Any],
    display_config: dict[str, Any],
    key_prefix: str,
    select_label: str | None = None,
    open_label: str = "Open card",
    on_select: Any | None = None,
    select_level: str | None = None,
) -> None:
    cards_per_row = 2
    for row_start in range(0, len(cards), cards_per_row):
        cols = st.columns([0.18, 1, 0.28, 1, 0.18], gap="small")
        row_cards = cards[row_start: row_start + cards_per_row]
        for offset, card in enumerate(row_cards):
            index = row_start + offset
            with cols[1 + offset * 2]:
                select_args = (select_level, card.id) if select_level else ()
                render_preview_card(
                    card,
                    display_config,
                    f"{key_prefix}_{index}",
                    select_label=select_label,
                    open_label=open_label,
                    on_select=on_select,
                    select_args=select_args,
                )
