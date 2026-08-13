from __future__ import annotations

from dataclasses import asdict, is_dataclass
from typing import Any

import streamlit as st

from streamlit_app.config import DETAIL_SKIP_FIELDS
from streamlit_app.data import card_type_label


# ----------------------------------------------------------
# Page Styling
# ----------------------------------------------------------
# Keep this function in place for the app shell, but intentionally avoid custom
# styling while we rebuild the UI from a stable native Streamlit baseline.

def css() -> None:
    st.html(
        """
        <style>
        [class*="st-key-card-macro"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #8f98a3;
        }
        [class*="st-key-card-mezzo"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #9aa58f;
        }
        [class*="st-key-card-micro"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #b0a27e;
        }
        [class*="st-key-card-session"] div[data-testid="stVerticalBlockBorderWrapper"] {
            border-left: 4px solid #9b8f9f;
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


# ----------------------------------------------------------
# Contact Links
# ----------------------------------------------------------

def render_contact_links() -> None:
    with st.container(horizontal=True, horizontal_alignment="right"):
        st.link_button(
            "Mail",
            "mailto:pecek.urh@gmail.com",
            icon=":material/mail:",
            type="tertiary",
            width="content",
        )
        st.link_button(
            "GitHub",
            "https://github.com/1312Bravo/Trail-Running-Training-Cards",
            icon=":material/code:",
            type="tertiary",
            width="content",
        )


def card_type_badge_color(card: Any) -> str:
    colors = {
        "macro": "blue",
        "mezzo": "green",
        "micro": "orange",
        "session": "violet",
    }
    return colors.get(str(card.card_type), "gray")


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
        st.write(value)
    elif field_name == "tags" and isinstance(value, list):
        st.caption(label)
        with st.container(horizontal=True):
            for tag in value:
                st.badge(as_text(tag), color="gray")
    elif isinstance(value, list):
        st.markdown(f"**{label}:** {as_list_text(value)}")
    else:
        st.markdown(f"**{label}:** {as_text(value)}")


def render_preview_card(card: Any, display_config: dict[str, Any], key_prefix: str) -> None:
    preview_fields = display_config.get("preview_fields", [])
    card_type_key = str(card.card_type).replace("_", "-")

    with st.container(border=True, key=f"card-{card_type_key}-{key_prefix}-{card.id}", height=350):
        st.markdown(f"**{card.title}**")
        st.badge(
            card_type_label(card.card_type, display_config),
            color=card_type_badge_color(card),
        )

        for field_name in preview_fields:
            if field_name in {"title", "card_type"}:
                continue
            render_preview_field(card, field_name, display_config)

        with st.container(horizontal_alignment="right"):
            st.button(
                "Open card",
                key=f"open_{key_prefix}_{card.id}",
                type="tertiary",
                width="content",
                on_click=lambda card_id=card.id: st.session_state.__setitem__("active_card_id", card_id),
            )


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

    st.markdown("**Workout parts**")
    st.dataframe(
        [
            {
                "Part": part.name,
                "Duration": part.duration,
                "RPE": part.rpe,
                "Instructions": part.instructions or "",
                "Terrain notes": part.terrain_notes or "",
            }
            for part in parts
        ],
        hide_index=True,
    )


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
            st.caption(f"Tags: {as_list_text(family['tags'])}")
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
        if isinstance(value, list):
            st.markdown("\n".join(f"- {as_text(item)}" for item in value))
        else:
            st.write(format_field_value(field_name, value))


def render_detail(
    card: Any,
    display_config: dict[str, Any],
    card_by_id: dict[str, Any],
    show_header: bool = True,
) -> None:
    detail_order = display_config.get("detail_field_order", [])
    preview_fields = display_config.get("preview_fields", [])

    if show_header:
        st.subheader(card.title)
        st.caption(card_type_label(card.card_type, display_config))

    for field_name in preview_fields:
        if field_name in DETAIL_SKIP_FIELDS:
            continue
        render_field(field_name, getattr(card, field_name, None), display_config)

    for field_name in detail_order:
        if field_name in preview_fields or field_name in DETAIL_SKIP_FIELDS:
            continue
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

def render_grid(cards: list[Any], display_config: dict[str, Any], key_prefix: str) -> None:
    cols = st.columns(2)
    for index, card in enumerate(cards):
        with cols[index % 2]:
            render_preview_card(card, display_config, f"{key_prefix}_{index}")
