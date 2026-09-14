from __future__ import annotations

from collections import defaultdict
from typing import Any

from training_cards.schemas import BaseTrainingCard

MAINSTREAM_PROFILE_ID = "mainstream_endurance"
DIRECT_SOURCE = "direct"
REUSED_SOURCE = "reused"


def build_card_library_index(
    cards: list[BaseTrainingCard],
    macro_mezzo_reuse_config: dict[str, Any],
    mezzo_micro_reuse_config: dict[str, Any],
    micro_session_reuse_config: dict[str, Any],
    *,
    schema_version: str,
    library_version: str,
    updated_at: str,
) -> dict[str, Any]:
    cards_by_id = {card.id: card for card in cards}
    level_entries: dict[str, dict[str, dict[str, dict[str, Any]]]] = defaultdict(
        lambda: defaultdict(dict)
    )

    for card in cards:
        level = str(card.card_type)
        for profile_id in card.philosophy_profile_ids:
            level_entries[level][profile_id][card.id] = _direct_entry(card)

    _add_reused_entries(
        level_entries,
        cards_by_id,
        "macro",
        _macro_reuse_entries(macro_mezzo_reuse_config),
    )
    _add_reused_entries(
        level_entries,
        cards_by_id,
        "mezzo",
        _card_reuse_entries(macro_mezzo_reuse_config, "reused_mezzo_card_id"),
    )
    _add_reused_entries(
        level_entries,
        cards_by_id,
        "micro",
        _card_reuse_entries(mezzo_micro_reuse_config, "reused_micro_card_id"),
    )
    _add_reused_entries(
        level_entries,
        cards_by_id,
        "session",
        _card_reuse_entries(micro_session_reuse_config, "reused_session_card_id"),
    )

    return {
        "schema_version": schema_version,
        "library_version": library_version,
        "updated_at": updated_at,
        "levels": {
            level: {
                profile_id: sorted(entries.values(), key=_entry_sort_key)
                for profile_id, entries in sorted(profiles.items())
            }
            for level, profiles in sorted(level_entries.items())
        },
    }


def validate_card_library_index(
    index: dict[str, Any],
    cards: list[BaseTrainingCard],
    *,
    schema_version: str,
    library_version: str,
) -> None:
    if index.get("schema_version") != schema_version:
        raise ValueError("card_library_index.json schema_version does not match manifest schema.")
    if index.get("library_version") != library_version:
        raise ValueError("card_library_index.json library_version does not match manifest library.")

    cards_by_id = {card.id: card for card in cards}
    levels = index.get("levels")
    if not isinstance(levels, dict):
        raise ValueError("card_library_index.json must contain a levels object.")

    for level, profiles in levels.items():
        if not isinstance(profiles, dict):
            raise ValueError(f"card_library_index.json level must be an object: {level}")

        for profile_id, entries in profiles.items():
            if not isinstance(entries, list):
                raise ValueError(
                    f"card_library_index.json profile entries must be a list: {level}/{profile_id}"
                )

            seen_ids: set[str] = set()
            for entry in entries:
                _validate_index_entry(entry, cards_by_id, level, profile_id)
                card_id = entry["card_id"]
                if card_id in seen_ids:
                    raise ValueError(
                        f"card_library_index.json has duplicate card {card_id} under {level}/{profile_id}."
                    )
                seen_ids.add(card_id)


def _direct_entry(card: BaseTrainingCard) -> dict[str, Any]:
    return {
        "card_id": card.id,
        "title": card.title,
        "description": _card_description(card),
        "source": DIRECT_SOURCE,
    }


def _reused_entry(card: BaseTrainingCard, source_profile: str) -> dict[str, Any]:
    return {
        "card_id": card.id,
        "title": card.title,
        "description": _card_description(card),
        "source": REUSED_SOURCE,
        "source_profile": source_profile,
    }


def _card_description(card: BaseTrainingCard) -> str:
    return card.summary or card.purpose


def _macro_reuse_entries(config: dict[str, Any]) -> list[tuple[str, str]]:
    return [
        (entry["philosophy_profile_id"], entry["macro_card_id"])
        for entry in config.get("entries", [])
    ]


def _card_reuse_entries(config: dict[str, Any], card_id_field: str) -> list[tuple[str, str]]:
    return [
        (entry["philosophy_profile_id"], entry[card_id_field])
        for entry in config.get("entries", [])
    ]


def _add_reused_entries(
    level_entries: dict[str, dict[str, dict[str, dict[str, Any]]]],
    cards_by_id: dict[str, BaseTrainingCard],
    level: str,
    reuse_entries: list[tuple[str, str]],
) -> None:
    for profile_id, card_id in reuse_entries:
        card = cards_by_id.get(card_id)
        if card is None:
            continue
        if card_id in level_entries[level][profile_id]:
            continue
        level_entries[level][profile_id][card_id] = _reused_entry(
            card,
            _source_profile_for_card(card),
        )


def _source_profile_for_card(card: BaseTrainingCard) -> str:
    if MAINSTREAM_PROFILE_ID in card.philosophy_profile_ids:
        return MAINSTREAM_PROFILE_ID
    return card.philosophy_profile_ids[0]


def _entry_sort_key(entry: dict[str, Any]) -> tuple[str, str]:
    return (entry["title"].casefold(), entry["card_id"])


def _validate_index_entry(
    entry: dict[str, Any],
    cards_by_id: dict[str, BaseTrainingCard],
    level: str,
    profile_id: str,
) -> None:
    required_fields = {"card_id", "title", "description", "source"}
    missing = required_fields - set(entry)
    if missing:
        raise ValueError(
            f"card_library_index.json entry under {level}/{profile_id} is missing {sorted(missing)}."
        )

    card_id = entry["card_id"]
    card = cards_by_id.get(card_id)
    if card is None:
        raise ValueError(f"card_library_index.json references unknown card: {card_id}")
    if str(card.card_type) != level:
        raise ValueError(
            f"card_library_index.json places {card_id} under {level}, but card is {card.card_type}."
        )

    source = entry["source"]
    if source == DIRECT_SOURCE:
        if "source_profile" in entry:
            raise ValueError(f"Direct index entry must not include source_profile: {card_id}")
        if profile_id not in card.philosophy_profile_ids:
            raise ValueError(f"Direct index entry profile does not own card {card_id}: {profile_id}")
        return

    if source == REUSED_SOURCE:
        source_profile = entry.get("source_profile")
        if not source_profile:
            raise ValueError(f"Reused index entry must include source_profile: {card_id}")
        if source_profile not in card.philosophy_profile_ids:
            raise ValueError(
                f"Reused index entry source_profile does not own card {card_id}: {source_profile}"
            )
        return

    raise ValueError(f"Unknown card_library_index source for {card_id}: {source}")
