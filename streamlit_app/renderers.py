from __future__ import annotations

from base64 import b64encode
from dataclasses import asdict, fields as dataclass_fields, is_dataclass
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

DETAIL_HIDDEN_FIELDS = {"id", "slug", "title"}

GITHUB_ICON_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path fill="currentColor" d="M12 .5A12 12 0 0 0 8.2 23.9c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.5-1.3-1.3-1.7-1.3-1.7-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.6.1-3.2 0 0 1-.3 3.3 1.2a11.3 11.3 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.6.2 2.9.1 3.2.8.9 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.1c0 .3.2.7.8.6A12 12 0 0 0 12 .5Z"/>
</svg>
"""


# ----------------------------------------------------------
# Page Styling
# ----------------------------------------------------------
# Keep this function in place for the app shell, but intentionally avoid custom
# styling while we rebuild the UI from a stable native Streamlit baseline.

def css() -> None:
    st.html(
        """
        <style>
        :root {
            --paper: #ffffff;
            --surface: #ffffff;
            --ink: #252525;
            --muted-ink: #737373;
            --line: #d6d6d6;
            --strong-line: #4d4d4d;
            --soft-surface: #f7f7f7;
        }
        [data-testid="stAppViewContainer"],
        .stApp {
            background: var(--paper);
            color: var(--ink);
        }
        [data-testid="stHeader"] {
            background: transparent;
        }
        [data-testid="stMainBlockContainer"],
        .block-container {
            max-width: 92rem;
            padding-top: 2.75rem;
            padding-bottom: 4rem;
        }
        h1 {
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: clamp(2.25rem, 4vw, 3.35rem);
            font-weight: 600;
            letter-spacing: -0.045em;
            line-height: 1.02;
        }
        [data-testid="stCaptionContainer"] {
            color: var(--muted-ink);
        }
        [data-testid="stButton"] > button {
            min-height: 2rem;
            border: 1px solid #bfc0b8;
            background: var(--surface);
            color: var(--ink);
            box-shadow: none;
            transition: background 160ms ease, border-color 160ms ease;
        }
        [data-testid="stButton"] > button:hover {
            border-color: var(--strong-line);
            background: var(--soft-surface);
            color: var(--ink);
        }
        [data-testid="stTextInput"] input,
        [data-testid="stMultiSelect"] div[data-baseweb="select"] > div {
            background: var(--surface);
        }
        [data-testid="stSegmentedControl"] {
            background: var(--surface);
        }
        [data-testid="stDivider"] {
            border-color: var(--line);
        }
        .contact-links {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-end;
            gap: 0.4rem;
            margin-top: 0;
        }
        .contact-links a {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            color: var(--ink);
            text-decoration: none;
            font-size: 0.98rem;
        }
        .contact-icon {
            width: 1.12rem;
            height: 1.12rem;
            display: inline-block;
        }
        .contact-links a:hover {
            text-decoration: underline;
            text-underline-offset: 0.18rem;
        }
        [class*="st-key-philosophy-"] h1 {
            margin: 0 0 0.8rem;
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.35rem;
            font-weight: 600;
            letter-spacing: -0.02em;
        }
        [class*="st-key-philosophy-"] h2 {
            margin: 1rem 0 0.45rem;
            font-size: 1rem;
        }
        [class*="st-key-philosophy-"] p,
        [class*="st-key-philosophy-"] li {
            color: #555555;
        }
        [class*="st-key-tag_"],
        [class*="st-key-selected_tag_"],
        [class*="st-key-pathway_search_terms_"],
        [class*="st-key-today_search_terms_"] {
            margin: 0 !important;
        }
        [class*="st-key-tag_"] button,
        [class*="st-key-selected_tag_"] button,
        [class*="st-key-pathway_search_terms_"] button,
        [class*="st-key-today_search_terms_"] button {
            min-height: 1.65rem;
            padding: 0.1rem 0.45rem;
            background: var(--surface);
            border: 1px solid var(--line);
            color: var(--ink);
            box-shadow: none;
            font-size: 0.86rem;
            font-weight: 400;
        }
        [class*="st-key-selected_tag_"] button {
            background: #e9ece4;
            border-color: #8b9585;
            font-weight: 600;
        }
        [class*="st-key-open-action"] {
            position: sticky;
            top: 0;
            z-index: 2;
            background: var(--paper);
            padding-bottom: 0.25rem;
        }
        [class*="st-key-open_"] button,
        [class*="st-key-select_"] button {
            border: 1px solid #aeb0a7;
            background: var(--soft-surface);
            color: var(--ink);
            font-weight: 600;
            min-height: 1.8rem;
            padding: 0.12rem 0.55rem;
            font-size: 0.8rem;
            box-shadow: none;
        }
        [class*="st-key-pathway_open_"] button,
        [class*="st-key-pathway_change_"] button {
            border: 1px solid var(--line);
            background: var(--surface);
            color: var(--ink);
            font-weight: 400;
            min-height: 1.55rem;
            padding: 0.05rem 0.4rem;
            font-size: 0.78rem;
            box-shadow: none;
        }
        [class*="st-key-pathway-selection"] {
            position: sticky;
            top: 0;
            z-index: 4;
            background: var(--paper);
            padding-bottom: 0.4rem;
        }
        .preview-card-title {
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.3rem;
            font-weight: 600;
            letter-spacing: -0.025em;
            line-height: 1.14;
        }
        .preview-summary {
            margin: 1rem 0 1.1rem;
            color: var(--ink);
            font-size: 1.02rem;
            line-height: 1.58;
        }
        .preview-field {
            margin: 0.65rem 0;
            color: var(--ink);
            line-height: 1.45;
        }
        .preview-field-label {
            color: var(--muted-ink);
            font-weight: 400;
            font-size: 0.9em;
        }
        .preview-tags-title {
            margin: 1rem 0 0.25rem;
            color: #222222;
            font-weight: 400;
        }
        [class*="st-key-card-"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--surface);
            border: 1px solid var(--strong-line) !important;
            border-radius: 10px;
            box-shadow: 0 1px 2px rgb(40 41 35 / 5%);
        }
        [class*="st-key-card-macro"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #788796;
        }
        [class*="st-key-card-mezzo"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #7f8d72;
        }
        [class*="st-key-card-micro"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #a78a59;
        }
        [class*="st-key-card-session"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #8c7780;
        }
        [class*="st-key-pathway-card-"] div[data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--surface);
            border: 1px solid var(--strong-line) !important;
            border-radius: 8px;
        }
        [class*="st-key-pathway-card-macro"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #788796 !important;
        }
        [class*="st-key-pathway-card-mezzo"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #7f8d72 !important;
        }
        [class*="st-key-pathway-card-micro"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #a78a59 !important;
        }
        [class*="st-key-pathway-card-session"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #8c7780 !important;
        }
        </style>
        """
    )


# ----------------------------------------------------------
# Shared Formatting
# ----------------------------------------------------------
# These helpers keep schema values readable without adding visual complexity.

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


def format_field_value(field_name: str, value: Any) -> str:
    text = as_text(value)
    if field_name == "recommended_duration_weeks" and text:
        return f"{text} weeks"
    if field_name == "recommended_duration_days" and text:
        return f"{text} days"
    return text


def field_label(field_name: str, display_config: dict[str, Any]) -> str:
    labels = display_config.get("field_labels", {})
    return labels.get(field_name, field_name.replace("_", " ").title())


def svg_data_uri(svg: str) -> str:
    encoded_svg = b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded_svg}"


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


def card_type_badge_color(card: Any) -> str:
    colors = {
        "macro": "blue",
        "mezzo": "green",
        "micro": "orange",
        "session": "violet",
    }
    return colors.get(str(card.card_type), "gray")


def set_tag_filter(tag: str) -> None:
    current_tags = list(st.session_state.get("tag_filters", []))
    if tag not in current_tags:
        current_tags.append(tag)
    st.session_state.tag_filters = current_tags


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


# ----------------------------------------------------------
# Preview Cards
# ----------------------------------------------------------

def render_preview_field(card: Any, field_name: str, display_config: dict[str, Any]) -> None:
    value = getattr(card, field_name, None)
    if value is None:
        return
    if isinstance(value, str) and not value.strip():
        return
    if isinstance(value, list) and not value:
        return

    label = field_label(field_name, display_config)
    if field_name == "summary":
        st.html(f'<p class="preview-summary">{escape(as_text(value))}</p>')
    elif field_name == "tags" and isinstance(value, list):
        render_tag_buttons(value, f"preview_{card.id}")
    elif field_name == "philosophy_profile_ids" and isinstance(value, list):
        rendered_value = ", ".join(
            philosophy_profile_display_name(profile_id)
            for profile_id in value
        )
        st.html(
            '<p class="preview-field">'
            f'<span class="preview-field-label">{escape(label)}:</span> '
            f'{escape(rendered_value)}'
            '</p>'
        )
    elif isinstance(value, list):
        rendered_value = ", ".join(display_text(item) for item in value)
        st.html(
            '<p class="preview-field">'
            f'<span class="preview-field-label">{escape(label)}:</span> '
            f'{escape(rendered_value)}'
            '</p>'
        )
    else:
        st.html(
            '<p class="preview-field">'
            f'<span class="preview-field-label">{escape(label)}:</span> '
            f'{escape(as_text(value))}'
            '</p>'
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

    with st.container(border=True, key=f"card-{card_type_key}-{key_prefix}-{card.id}", height=400):
        header_cols = st.columns([1, 0.38], vertical_alignment="top")
        with header_cols[0]:
            st.html(f'<div class="preview-card-title">{escape(card.title)}</div>')
        with header_cols[1]:
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
                    on_click=lambda card_id=card.id: st.session_state.__setitem__("active_card_id", card_id),
                )

        st.badge(
            card_type_label(card.card_type, display_config),
            color=card_type_badge_color(card),
        )

        for field_name in ordered_preview_fields:
            render_preview_field(card, field_name, display_config)


# ----------------------------------------------------------
# Detail View
# ----------------------------------------------------------

def render_reference_list(card: Any, card_by_id: dict[str, Any]) -> None:
    if not card.references:
        return

    with st.container(border=True):
        st.markdown("**References**")
        items = []
        for reference in card.references:
            linked = card_by_id.get(reference.card_id)
            linked_title = linked.title if linked else reference.card_id
            tags = f" ({as_list_text(reference.tags)})" if reference.tags else ""
            items.append(f"- {as_text(reference.relationship)}: {linked_title}{tags}")
        st.markdown("\n".join(items))


def render_workout_parts(parts: list[Any]) -> None:
    if not parts:
        return

    with st.container(border=True):
        st.markdown("**Workout parts**")
        lines = []
        for part in parts:
            lines.append(f"- **{part.name}**")
            lines.append(f"  - Duration: {part.duration}")
            lines.append(f"  - RPE: {part.rpe}")
            if part.instructions:
                lines.append(f"  - {part.instructions}")
            if part.terrain_notes:
                lines.append(f"  - Terrain notes: {part.terrain_notes}")
        st.markdown("\n".join(lines))


def render_dataclass_value(field_name: str, value: Any, display_config: dict[str, Any]) -> bool:
    if field_name != "session_family" or not is_dataclass(value):
        return False

    family = asdict(value)
    with st.container(border=True):
        st.markdown(f"**{field_label(field_name, display_config)}**")
        st.write(family.get("title", ""))
        if family.get("summary"):
            st.caption(family["summary"])
        if family.get("description"):
            st.write(family["description"])
        if family.get("tags"):
            st.caption(f"Tags: {', '.join(display_text(tag) for tag in family['tags'])}")
    return True


def render_field(field_name: str, value: Any, display_config: dict[str, Any]) -> None:
    if value is None:
        return
    if isinstance(value, str) and not value.strip():
        return
    if isinstance(value, list) and not value:
        return
    if render_dataclass_value(field_name, value, display_config):
        return

    label = field_label(field_name, display_config)
    with st.container(border=True):
        st.markdown(f"**{label}**")
        if field_name == "tags" and isinstance(value, list):
            render_tag_buttons(value, "detail")
        elif field_name == "philosophy_profile_ids" and isinstance(value, list):
            st.markdown(
                "\n".join(
                    f"- {philosophy_profile_display_name(profile_id)}"
                    for profile_id in value
                )
            )
        elif isinstance(value, list):
            st.markdown("\n".join(f"- {as_text(item)}" for item in value))
        else:
            st.write(format_field_value(field_name, value))


def ordered_detail_fields(card: Any, display_config: dict[str, Any]) -> list[str]:
    configured_fields = (
        display_config.get("system_fields", [])
        + display_config.get("preview_fields", [])
        + display_config.get("detail_field_order", [])
    )
    dataclass_field_names = [field.name for field in dataclass_fields(card)]
    ordered = []
    for field_name in configured_fields + dataclass_field_names:
        if field_name in DETAIL_HIDDEN_FIELDS:
            continue
        if field_name not in ordered and hasattr(card, field_name):
            ordered.append(field_name)
    return ordered


def render_detail(
    card: Any,
    display_config: dict[str, Any],
    card_by_id: dict[str, Any],
    show_header: bool = True,
) -> None:
    if show_header:
        st.subheader(card.title)
        st.caption(card_type_label(card.card_type, display_config))

    for field_name in ordered_detail_fields(card, display_config):
        value = getattr(card, field_name, None)
        if field_name == "workout_parts":
            render_workout_parts(value)
        elif field_name == "references":
            render_reference_list(card, card_by_id)
        else:
            render_field(field_name, value, display_config)


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
