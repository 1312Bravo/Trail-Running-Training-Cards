from __future__ import annotations

from base64 import b64encode
from html import escape
from typing import Any

import streamlit as st

from training_cards.philosophy_profiles import philosophy_profile_display_name
from streamlit_app.data import card_type_label


MAIL_ICON_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path fill="currentColor" d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm-.4 4.25-7.07 4.42a1 1 0 0 1-1.06 0L4.4 8.25 5.46 6.55 12 10.64l6.54-4.09 1.06 1.7Z"/>
</svg>
"""

DETAIL_HIDDEN_FIELDS = {"id", "slug", "title", "card_type"}
DETAIL_KEY_FACT_FIELDS = {
    "suitable_levels",
    "recommended_duration_weeks",
    "recommended_duration_days",
    "typical_duration",
    "philosophy_profile_ids",
}

GITHUB_ICON_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path fill="currentColor" d="M12 .5A12 12 0 0 0 8.2 23.9c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.5-1.3-1.3-1.7-1.3-1.7-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.6.1-3.2 0 0 1-.3 3.3 1.2a11.3 11.3 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.6.2 2.9.1 3.2.8.9 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.1c0 .3.2.7.8.6A12 12 0 0 0 12 .5Z"/>
</svg>
"""

CARD_TYPE_PIP_COUNTS = {
    "macro": 4,
    "mezzo": 3,
    "micro": 2,
    "session": 1,
}

LABEL_TEXT_OVERRIDES = {
    "cts": "CTS",
    "rpe": "RPE",
    "utmb": "UTMB",
    "vo2max": "VO2max",
}


# ----------------------------------------------------------
# Shared Formatting And Controls
# ----------------------------------------------------------

def as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if hasattr(value, "value"):
        return str(value.value)
    return str(value)


def as_list_text(values: list[Any]) -> str:
    return ", ".join(as_text(value) for value in values)


def display_text(value: Any) -> str:
    return as_text(value).replace("_", " ")


def display_label_text(value: Any) -> str:
    text = display_text(value).replace("-", " ").strip()
    words = []
    for word in text.split():
        words.append(LABEL_TEXT_OVERRIDES.get(word.lower(), word[:1].upper() + word[1:]))
    return " ".join(words)


def format_field_value(field_name: str, value: Any) -> str:
    text = as_text(value)
    if field_name == "recommended_duration_weeks" and text:
        if "week" in text.lower():
            return text
        return f"{text} weeks"
    if field_name == "recommended_duration_days" and text:
        if "day" in text.lower():
            return text
        return f"{text} days"
    return text


def field_label(field_name: str, display_config: dict[str, Any]) -> str:
    labels = display_config.get("field_labels", {})
    return labels.get(field_name, field_name.replace("_", " ").title())


def svg_data_uri(svg: str) -> str:
    encoded_svg = b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded_svg}"


def preview_card_pips_html(card_type_key: str) -> str:
    pip_count = CARD_TYPE_PIP_COUNTS.get(card_type_key, 0)
    if pip_count <= 0:
        return ""
    pips = "".join('<span class="preview-card-pip">★</span>' for _ in range(pip_count))
    return f'<span class="preview-card-pips" aria-hidden="true">{pips}</span>'


def preview_card_meta_text(card: Any, display_config: dict[str, Any]) -> str:
    card_type = card_type_label(card.card_type, display_config)
    values = [card_type]
    philosophy_ids = getattr(card, "philosophy_profile_ids", [])
    if philosophy_ids:
        values.append(philosophy_profile_display_name(philosophy_ids[0]))
    return " | ".join(display_label_text(value) for value in values)


# ----------------------------------------------------------
# Contact Links
# ----------------------------------------------------------

def render_contact_links() -> None:
    mail_icon = svg_data_uri(MAIL_ICON_SVG)
    github_icon = svg_data_uri(GITHUB_ICON_SVG)
    st.html(
        f"""
        <div class="contact-links">
            <a href="mailto:pecek.urh@gmail.com">
                <img class="contact-icon" src="{mail_icon}" alt="">
                <span>pecek.urh@gmail.com</span>
            </a>
            <a href="https://github.com/1312Bravo/Trail-Running-Training-Cards" target="_blank">
                <img class="contact-icon" src="{github_icon}" alt="">
                <span>GitHub</span>
            </a>
        </div>
        """
    )


def set_tag_filter(tag: str) -> None:
    current_tags = list(st.session_state.get("tag_filters", []))
    if tag not in current_tags:
        current_tags.append(tag)
    st.session_state.tag_filters = current_tags


def open_card(card_id: str) -> None:
    st.session_state.active_card_id = card_id
    st.session_state.active_card_history = []


def render_card_history_back(card_by_id: dict[str, Any]) -> None:
    history = list(st.session_state.get("active_card_history", []))
    if not history:
        return

    previous_card_id = history[-1]
    previous_card = card_by_id.get(previous_card_id)
    previous_title = previous_card.title if previous_card else previous_card_id

    if st.button(
        f"Back to {previous_title}",
        key=f"detail-history-back-{previous_card_id}",
        type="secondary",
        width="content",
    ):
        st.session_state.active_card_history = history[:-1]
        st.session_state.active_card_id = previous_card_id
        st.rerun(scope="app")


def render_tag_buttons(tags: list[Any], key_prefix: str) -> None:
    if not tags:
        return

    with st.container(horizontal=True):
        for tag in tags:
            tag_text = as_text(tag)
            st.button(
                display_text(tag_text),
                key=f"tag_{key_prefix}_{tag_text}",
                type="secondary",
                width="content",
                on_click=set_tag_filter,
                args=(tag_text,),
            )


def render_preview_tag_labels(tags: list[Any], key_prefix: str) -> None:
    if not tags:
        return

    with st.container(horizontal=True, key=f"preview-tags-{key_prefix}"):
        for tag in tags:
            tag_text = as_text(tag)
            st.button(
                display_label_text(tag_text),
                key=f"tag_preview_{key_prefix}_{tag_text}",
                type="secondary",
                width="content",
                on_click=set_tag_filter,
                args=(tag_text,),
            )


def render_preview_footer_tag_labels(tags: list[Any], key_prefix: str) -> None:
    if not tags:
        return

    with st.container(
        horizontal=True,
        horizontal_alignment="right",
        key=f"preview-footer-tags-{key_prefix}",
    ):
        for tag in tags:
            tag_text = as_text(tag)
            st.button(
                display_label_text(tag_text),
                key=f"tag_preview_footer_{key_prefix}_{tag_text}",
                type="secondary",
                width="content",
                on_click=set_tag_filter,
                args=(tag_text,),
            )
