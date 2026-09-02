from __future__ import annotations

from html import escape
from typing import Any

import streamlit as st

from training_cards.philosophy_profiles import philosophy_profile_display_name
from streamlit_app.config import DETAIL_FIELD_LABEL_OVERRIDES
from streamlit_app.data import card_type_label

from .shared import (
    as_text,
    display_label_text,
    display_text,
    field_label,
    open_card,
    preview_card_pips_html,
    render_preview_footer_tag_labels,
    render_preview_tag_labels,
)


# ----------------------------------------------------------
# Preview Cards
# ----------------------------------------------------------

def render_preview_field(
    card: Any,
    field_name: str,
    display_config: dict[str, Any],
    key_prefix: str,
) -> None:
    value = getattr(card, field_name, None)
    if value is None:
        return
    if isinstance(value, str) and not value.strip():
        return
    if isinstance(value, list) and not value:
        return

    label = DETAIL_FIELD_LABEL_OVERRIDES.get(
        field_name,
        field_label(field_name, display_config),
    )
    if field_name == "summary":
        st.html(f'<p class="preview-summary">{escape(as_text(value))}</p>')
    elif field_name == "tags" and isinstance(value, list):
        render_preview_tag_labels(value, f"{key_prefix}_{card.id}")
    elif field_name == "philosophy_profile_ids" and isinstance(value, list):
        rendered_value = ", ".join(
            philosophy_profile_display_name(profile_id)
            for profile_id in value
        )
        st.html(
            '<div class="preview-field">'
            f'<span class="preview-field-label">{escape(label)}:</span> '
            f'<span class="preview-field-value">{escape(rendered_value)}</span>'
            '</div>'
        )
    elif isinstance(value, list):
        formatter = display_label_text if field_name == "suitable_levels" else display_text
        rendered_value = ", ".join(formatter(item) for item in value)
        st.html(
            '<div class="preview-field">'
            f'<span class="preview-field-label">{escape(label)}:</span> '
            f'<span class="preview-field-value">{escape(rendered_value)}</span>'
            '</div>'
        )
    else:
        st.html(
            '<div class="preview-field">'
            f'<span class="preview-field-label">{escape(label)}:</span> '
            f'<span class="preview-field-value">{escape(as_text(value))}</span>'
            '</div>'
        )


def render_preview_card(
    card: Any,
    display_config: dict[str, Any],
    key_prefix: str,
    select_label: str | None = None,
    open_label: str = "Open card",
    on_select: Any | None = None,
    select_args: tuple[Any, ...] = (),
) -> None:
    preview_fields = display_config.get("preview_fields", [])
    ordered_preview_fields = [
        field_name
        for field_name in ["summary", "purpose", "suitable_levels", "goal_race_context", "training_profile", "philosophy_profile_ids", "tags"]
        if field_name in preview_fields
    ]
    card_type_key = str(card.card_type).replace("_", "-")
    card_type_meta = display_label_text(card_type_label(card.card_type, display_config))

    with st.container(border=True, key=f"card-{card_type_key}-{key_prefix}-{card.id}", height=470):
        st.html(
            '<div class="preview-card-title">'
            f'<span class="preview-card-title-text">{escape(card.title)}</span>'
            f'{preview_card_pips_html(card_type_key)}'
            '</div>'
        )
        meta_cols = st.columns([1, 0.25], vertical_alignment="center")
        with meta_cols[0]:
            st.html(
                '<div class="preview-card-meta '
                f'preview-card-type-{card_type_key}">'
                f'{escape(card_type_meta)}'
                '</div>'
            )
        with meta_cols[1]:
            with st.container(
                key=f"open-action-{key_prefix}-{card.id}",
                horizontal=True,
                horizontal_alignment="right",
            ):
                if select_label and on_select:
                    st.button(
                        select_label,
                        key=f"select_{key_prefix}_{card.id}",
                        type="secondary",
                        width="content",
                        on_click=on_select,
                        args=select_args,
                    )
                st.button(
                    open_label,
                    key=f"open_{key_prefix}_{card.id}",
                    type="secondary",
                    width="content",
                    on_click=open_card,
                    args=(card.id,),
                )

        for field_name in ordered_preview_fields:
            if field_name == "tags":
                continue
            render_preview_field(card, field_name, display_config, key_prefix)

        if "tags" in ordered_preview_fields and card.tags:
            render_preview_footer_tag_labels(card.tags, f"{key_prefix}_{card.id}")
