from __future__ import annotations

from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY
from training_cards.json_store import (
    load_card_library_from_json,
    load_macro_mezzo_reuse_config,
    load_mezzo_micro_reuse_config,
)
from training_cards.schemas import (
    BaseTrainingCard,
    CardType,
)

# ----------------------------------------------------------
# Active Card Registry
# ----------------------------------------------------------
# Cloud JSON is the source of truth. The registry loads the downloaded local
# cache, which should be refreshed from Google Drive when card content changes.


# Load and validate the active JSON card library.
def load_active_cards() -> list[BaseTrainingCard]:
    try:
        return load_card_library_from_json(GOOGLE_DRIVE_LIBRARY.local_cache_dir)
    except FileNotFoundError as error:
        raise RuntimeError(
            "Training card JSON cache is missing. Run: py -m training_cards.scripts.download_cloud_library"
        ) from error


ALL_CARDS = load_active_cards()
CARD_BY_ID = {card.id: card for card in ALL_CARDS}
MACRO_MEZZO_REUSE_CONFIG = load_macro_mezzo_reuse_config(GOOGLE_DRIVE_LIBRARY.local_cache_dir)
MEZZO_MICRO_REUSE_CONFIG = load_mezzo_micro_reuse_config(GOOGLE_DRIVE_LIBRARY.local_cache_dir)


# Return a single card by stable ID.
def get_card(card_id: str) -> BaseTrainingCard:
    try:
        return CARD_BY_ID[card_id]
    except KeyError as error:
        raise KeyError(f"Unknown training card id: {card_id}") from error


# Return cards from one planning level, such as macro or session.
def get_cards_by_type(card_type: CardType) -> list[BaseTrainingCard]:
    return [card for card in ALL_CARDS if card.card_type == card_type]


# Return cards that include a free-text tag.
def get_cards_by_tag(tag: str) -> list[BaseTrainingCard]:
    return [card for card in ALL_CARDS if tag in card.tags]


# Return session cards that belong to one named family.
def get_cards_by_session_family(family_id_or_slug: str) -> list[BaseTrainingCard]:
    return [
        card
        for card in ALL_CARDS
        if card.card_type == CardType.SESSION
        and getattr(card, "session_family", None) is not None
        and (
            card.session_family.id == family_id_or_slug
            or card.session_family.slug == family_id_or_slug
        )
    ]


# Follow all structured references from one card to the actual card objects.
def get_referenced_cards(card: BaseTrainingCard) -> list[BaseTrainingCard]:
    return [CARD_BY_ID[reference.card_id] for reference in card.references]


# Return app-facing macro-to-mezzo reuse metadata from the active JSON cache.
def get_macro_mezzo_reuse_config() -> dict[str, object]:
    return MACRO_MEZZO_REUSE_CONFIG


# Return app-facing mezzo-to-micro reuse metadata from the active JSON cache.
def get_mezzo_micro_reuse_config() -> dict[str, object]:
    return MEZZO_MICRO_REUSE_CONFIG


# Return reused mainstream mezzo cards for a profile within a macro context.
def get_reused_mezzo_cards(profile_id: str, macro_card_id: str) -> list[BaseTrainingCard]:
    reused_ids = {
        entry["reused_mezzo_card_id"]
        for entry in MACRO_MEZZO_REUSE_CONFIG.get("entries", [])
        if isinstance(entry, dict)
        and entry.get("philosophy_profile_id") == profile_id
        and entry.get("macro_card_id") == macro_card_id
        and isinstance(entry.get("reused_mezzo_card_id"), str)
    }
    return [CARD_BY_ID[card_id] for card_id in sorted(reused_ids) if card_id in CARD_BY_ID]


# Return reused mainstream micro cards for a profile within a mezzo context.
def get_reused_micro_cards(profile_id: str, mezzo_card_id: str) -> list[BaseTrainingCard]:
    reused_ids = {
        entry["reused_micro_card_id"]
        for entry in MEZZO_MICRO_REUSE_CONFIG.get("entries", [])
        if isinstance(entry, dict)
        and entry.get("philosophy_profile_id") == profile_id
        and entry.get("mezzo_card_id") == mezzo_card_id
        and isinstance(entry.get("reused_micro_card_id"), str)
    }
    return [CARD_BY_ID[card_id] for card_id in sorted(reused_ids) if card_id in CARD_BY_ID]
