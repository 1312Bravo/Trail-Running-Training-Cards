from __future__ import annotations

from dataclasses import asdict, dataclass

from training_cards.macro_mezzo_reuse import VALID_REUSE_TYPES
from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE, validate_philosophy_profile_ids
from training_cards.schemas import BaseTrainingCard, CardRelationship, CardType


MEZZO_MICRO_REUSE_VERSION = "1.0.0"


@dataclass(frozen=True, slots=True)
class MezzoMicroReuse:
    philosophy_profile_id: str
    mezzo_card_id: str
    mezzo_card_name: str
    reused_micro_card_id: str
    reused_micro_card_name: str
    reuse_type: str

    def __post_init__(self) -> None:
        validate_philosophy_profile_ids([self.philosophy_profile_id])
        if not self.mezzo_card_id.strip():
            raise ValueError("MezzoMicroReuse mezzo_card_id cannot be empty.")
        if not self.mezzo_card_name.strip():
            raise ValueError("MezzoMicroReuse mezzo_card_name cannot be empty.")
        if not self.reused_micro_card_id.strip():
            raise ValueError("MezzoMicroReuse reused_micro_card_id cannot be empty.")
        if not self.reused_micro_card_name.strip():
            raise ValueError("MezzoMicroReuse reused_micro_card_name cannot be empty.")
        if self.reuse_type not in VALID_REUSE_TYPES:
            raise ValueError(f"Unknown mezzo-micro reuse type: {self.reuse_type}")


def mezzo_micro_reuse_to_dict(reuse: MezzoMicroReuse) -> dict[str, str]:
    return asdict(reuse)


def build_mezzo_micro_reuse_config(
    schema_version: str,
    *,
    cards: list[BaseTrainingCard],
    macro_mezzo_reuse_config: dict[str, object],
) -> dict[str, object]:
    cards_by_id = {card.id: card for card in cards}
    mainstream_micros_by_parent = _mainstream_micros_by_parent(cards)
    entries: list[MezzoMicroReuse] = []
    seen_keys: set[tuple[str, str, str, str]] = set()

    for macro_mezzo_entry in macro_mezzo_reuse_config.get("entries", []):
        philosophy_profile_id = str(macro_mezzo_entry["philosophy_profile_id"])
        mezzo_card_id = str(macro_mezzo_entry["reused_mezzo_card_id"])
        reuse_type = str(macro_mezzo_entry["reuse_type"])
        mezzo_card = cards_by_id.get(mezzo_card_id)
        if mezzo_card is None:
            continue

        for micro_card in mainstream_micros_by_parent.get(mezzo_card_id, ()):
            key = (philosophy_profile_id, mezzo_card_id, micro_card.id, reuse_type)
            if key in seen_keys:
                continue
            seen_keys.add(key)
            entries.append(
                MezzoMicroReuse(
                    philosophy_profile_id=philosophy_profile_id,
                    mezzo_card_id=mezzo_card_id,
                    mezzo_card_name=mezzo_card.title,
                    reused_micro_card_id=micro_card.id,
                    reused_micro_card_name=micro_card.title,
                    reuse_type=reuse_type,
                )
            )

    entries.sort(
        key=lambda entry: (
            entry.philosophy_profile_id,
            entry.mezzo_card_id,
            entry.reused_micro_card_id,
            entry.reuse_type,
        )
    )

    return {
        "mezzo_micro_reuse_version": MEZZO_MICRO_REUSE_VERSION,
        "schema_version": schema_version,
        "entry_count": len(entries),
        "entries": [mezzo_micro_reuse_to_dict(entry) for entry in entries],
    }


def _mainstream_micros_by_parent(
    cards: list[BaseTrainingCard],
) -> dict[str, tuple[BaseTrainingCard, ...]]:
    grouped: dict[str, list[BaseTrainingCard]] = {}
    for card in cards:
        if card.card_type != CardType.MICRO:
            continue
        if card.philosophy_profile_ids != [MAINSTREAM_ENDURANCE]:
            continue
        for reference in card.references:
            if reference.relationship == CardRelationship.PARENT:
                grouped.setdefault(reference.card_id, []).append(card)

    return {
        parent_id: tuple(sorted(parent_cards, key=lambda card: card.id))
        for parent_id, parent_cards in grouped.items()
    }
