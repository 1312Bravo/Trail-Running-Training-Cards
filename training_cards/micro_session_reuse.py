from __future__ import annotations

from dataclasses import asdict, dataclass

from training_cards.macro_mezzo_reuse import REUSE_MAINSTREAM, VALID_REUSE_TYPES
from training_cards.philosophy_profiles import MAINSTREAM_ENDURANCE, validate_philosophy_profile_ids
from training_cards.schemas import BaseTrainingCard, CardRelationship, CardType


MICRO_SESSION_REUSE_VERSION = "1.0.0"


@dataclass(frozen=True, slots=True)
class MicroSessionReuse:
    philosophy_profile_id: str
    micro_card_id: str
    micro_card_name: str
    reused_session_card_id: str
    reused_session_card_name: str
    reuse_type: str

    def __post_init__(self) -> None:
        validate_philosophy_profile_ids([self.philosophy_profile_id])
        if not self.micro_card_id.strip():
            raise ValueError("MicroSessionReuse micro_card_id cannot be empty.")
        if not self.micro_card_name.strip():
            raise ValueError("MicroSessionReuse micro_card_name cannot be empty.")
        if not self.reused_session_card_id.strip():
            raise ValueError("MicroSessionReuse reused_session_card_id cannot be empty.")
        if not self.reused_session_card_name.strip():
            raise ValueError("MicroSessionReuse reused_session_card_name cannot be empty.")
        if self.reuse_type not in VALID_REUSE_TYPES:
            raise ValueError(f"Unknown micro-session reuse type: {self.reuse_type}")


MICRO_SESSION_REUSE_BY_MICRO: dict[str, tuple[str, ...]] = {
    "micro_065": ("session_010", "session_015"),
    "micro_066": ("session_010", "session_011"),
    "micro_067": ("session_001", "session_003", "session_008", "session_010"),
    "micro_068": ("session_010", "session_011"),
    "micro_069": ("session_001", "session_003", "session_008", "session_010"),
    "micro_070": ("session_010",),
    "micro_071": ("session_010",),
    "micro_072": ("session_001", "session_003", "session_008", "session_010"),
    "micro_073": ("session_009", "session_010"),
    "micro_074": ("session_001", "session_010"),
    "micro_075": ("session_001", "session_009", "session_010", "session_031"),
    "micro_076": ("session_004", "session_009", "session_010"),
    "micro_077": ("session_010", "session_011"),
    "micro_078": ("session_002", "session_003", "session_009", "session_030"),
    "micro_079": ("session_009", "session_010", "session_040"),
    "micro_080": ("session_001", "session_002", "session_003", "session_009", "session_010"),
    "micro_081": ("session_009", "session_010", "session_012"),
    "micro_082": ("session_009", "session_010"),
    "micro_083": ("session_003", "session_010"),
    "micro_084": ("session_001", "session_008", "session_010"),
    "micro_085": ("session_009", "session_010"),
    "micro_086": ("session_001", "session_003", "session_009", "session_031"),
    "micro_087": ("session_011", "session_012"),
    "micro_088": ("session_010",),
    "micro_089": ("session_003", "session_010"),
    "micro_090": ("session_010", "session_011"),
    "micro_091": ("session_010", "session_011"),
    "micro_092": ("session_001", "session_003", "session_009"),
    "micro_093": ("session_003", "session_009", "session_018"),
    "micro_094": ("session_011", "session_012"),
    "micro_095": ("session_009", "session_010", "session_018"),
    "micro_096": ("session_001", "session_003", "session_009", "session_030"),
    "micro_097": ("session_009", "session_011", "session_012", "session_022", "session_024", "session_032"),
    "micro_098": ("session_009", "session_010"),
    "micro_099": ("session_009", "session_010"),
    "micro_100": ("session_001", "session_003", "session_008", "session_031"),
    "micro_101": ("session_003", "session_009", "session_010", "session_012"),
    "micro_102": ("session_009", "session_010", "session_012"),
    "micro_103": ("session_001", "session_003", "session_009", "session_011"),
    "micro_104": ("session_010", "session_011"),
    "micro_105": ("session_003", "session_006", "session_009", "session_014", "session_040"),
    "micro_106": ("session_001", "session_003", "session_009", "session_011"),
    "micro_107": ("session_010", "session_011"),
    "micro_108": ("session_003", "session_009", "session_010", "session_023", "session_025", "session_032"),
    "micro_109": ("session_006", "session_009"),
    "micro_110": ("session_010", "session_011"),
    "micro_111": ("session_001", "session_002", "session_003", "session_009"),
    "micro_112": ("session_010", "session_011"),
    "micro_113": ("session_003", "session_009", "session_010"),
    "micro_114": ("session_010", "session_034"),
    "micro_115": ("session_009", "session_010"),
    "micro_116": ("session_009", "session_010"),
    "micro_117": ("session_010", "session_034", "session_035"),
    "micro_118": ("session_010", "session_036", "session_037"),
    "micro_119": ("session_010", "session_035", "session_037"),
    "micro_120": ("session_001", "session_002", "session_003", "session_009", "session_010"),
    "micro_121": ("session_001", "session_009", "session_010", "session_032", "session_043"),
    "micro_122": ("session_009", "session_010", "session_043", "session_044"),
    "micro_123": ("session_001", "session_003", "session_009", "session_010"),
    "micro_124": ("session_009", "session_010", "session_012"),
    "micro_125": ("session_009", "session_010", "session_012"),
    "micro_126": ("session_001", "session_003", "session_009", "session_010"),
    "micro_127": ("session_003", "session_009"),
    "micro_128": ("session_009", "session_010", "session_017"),
    "micro_129": ("session_003", "session_004", "session_009"),
    "micro_130": ("session_009", "session_010"),
    "micro_131": ("session_009", "session_012"),
    "micro_132": ("session_001", "session_009", "session_010"),
    "micro_133": ("session_009", "session_010"),
    "micro_134": ("session_010", "session_011"),
    "micro_135": ("session_001", "session_002", "session_003", "session_009"),
    "micro_136": ("session_001", "session_002", "session_003", "session_009"),
    "micro_137": ("session_010", "session_011"),
    "micro_138": ("session_010", "session_034", "session_036"),
    "micro_139": ("session_001", "session_003", "session_008", "session_009", "session_032"),
    "micro_140": ("session_001", "session_002", "session_003", "session_010", "session_015"),
    "micro_141": ("session_001", "session_002", "session_003", "session_008"),
    "micro_142": ("session_009", "session_010", "session_015"),
    "micro_143": ("session_010", "session_012"),
    "micro_144": ("session_003", "session_006", "session_010"),
    "micro_145": ("session_010", "session_011"),
    "micro_146": ("session_002", "session_009", "session_010"),
    "micro_147": ("session_001", "session_002", "session_003", "session_009", "session_010"),
    "micro_148": ("session_003", "session_009", "session_018"),
    "micro_149": ("session_009", "session_010"),
    "micro_150": ("session_009", "session_010"),
    "micro_151": ("session_010", "session_011"),
    "micro_152": ("session_001", "session_003", "session_009", "session_031"),
    "micro_153": ("session_009", "session_010"),
    "micro_154": ("session_001", "session_003", "session_009", "session_011"),
    "micro_155": ("session_010", "session_011"),
    "micro_156": ("session_003", "session_010", "session_011"),
    "micro_157": ("session_010", "session_011"),
    "micro_158": ("session_009", "session_010"),
    "micro_159": ("session_010", "session_011"),
    "micro_160": ("session_009", "session_010", "session_044"),
    "micro_161": ("session_001", "session_002", "session_003", "session_010"),
    "micro_162": ("session_003", "session_006", "session_010"),
    "micro_163": ("session_009", "session_010", "session_032"),
    "micro_164": ("session_001", "session_009", "session_010", "session_032"),
    "micro_165": ("session_001", "session_009"),
    "micro_166": ("session_001", "session_003", "session_009", "session_016"),
    "micro_167": ("session_010", "session_011"),
    "micro_168": ("session_011", "session_019", "session_034"),
    "micro_169": ("session_010", "session_011"),
    "micro_170": ("session_009", "session_010"),
    "micro_171": ("session_009", "session_010"),
    "micro_172": ("session_009", "session_012"),
    "micro_173": ("session_010", "session_011"),
    "micro_174": ("session_001", "session_002", "session_003", "session_010", "session_015"),
    "micro_175": ("session_003", "session_008", "session_010", "session_032", "session_043"),
    "micro_176": ("session_001", "session_003", "session_044", "session_045"),
    "micro_177": ("session_010", "session_011", "session_044"),
}


def micro_session_reuse_to_dict(reuse: MicroSessionReuse) -> dict[str, str]:
    return asdict(reuse)


def build_micro_session_reuse_config(
    schema_version: str,
    *,
    cards: list[BaseTrainingCard],
    mezzo_micro_reuse_config: dict[str, object],
) -> dict[str, object]:
    cards_by_id = {card.id: card for card in cards}
    mainstream_sessions_by_parent = _mainstream_sessions_by_parent(cards)
    entries: list[MicroSessionReuse] = []
    seen_keys: set[tuple[str, str, str, str]] = set()

    for mezzo_micro_entry in mezzo_micro_reuse_config.get("entries", []):
        philosophy_profile_id = str(mezzo_micro_entry["philosophy_profile_id"])
        micro_card_id = str(mezzo_micro_entry["reused_micro_card_id"])
        reuse_type = str(mezzo_micro_entry["reuse_type"])
        micro_card = cards_by_id.get(micro_card_id)
        if micro_card is None:
            continue

        for session_card in mainstream_sessions_by_parent.get(micro_card_id, ()):
            _append_entry(
                entries,
                seen_keys,
                philosophy_profile_id=philosophy_profile_id,
                micro_card=micro_card,
                session_card=session_card,
                reuse_type=reuse_type,
            )

    for micro_card_id, session_card_ids in MICRO_SESSION_REUSE_BY_MICRO.items():
        micro_card = cards_by_id.get(micro_card_id)
        if micro_card is None or micro_card.card_type != CardType.MICRO:
            continue
        if micro_card.philosophy_profile_ids == [MAINSTREAM_ENDURANCE]:
            continue
        philosophy_profile_id = micro_card.philosophy_profile_ids[0]
        for session_card_id in session_card_ids:
            session_card = cards_by_id.get(session_card_id)
            if session_card is None:
                continue
            _append_entry(
                entries,
                seen_keys,
                philosophy_profile_id=philosophy_profile_id,
                micro_card=micro_card,
                session_card=session_card,
                reuse_type=REUSE_MAINSTREAM,
            )

    entries.sort(
        key=lambda entry: (
            entry.philosophy_profile_id,
            entry.micro_card_id,
            entry.reused_session_card_id,
            entry.reuse_type,
        )
    )

    return {
        "micro_session_reuse_version": MICRO_SESSION_REUSE_VERSION,
        "schema_version": schema_version,
        "entry_count": len(entries),
        "entries": [micro_session_reuse_to_dict(entry) for entry in entries],
    }


def _append_entry(
    entries: list[MicroSessionReuse],
    seen_keys: set[tuple[str, str, str, str]],
    *,
    philosophy_profile_id: str,
    micro_card: BaseTrainingCard,
    session_card: BaseTrainingCard,
    reuse_type: str,
) -> None:
    if session_card.card_type != CardType.SESSION:
        return
    if session_card.philosophy_profile_ids != [MAINSTREAM_ENDURANCE]:
        return

    key = (philosophy_profile_id, micro_card.id, session_card.id, reuse_type)
    if key in seen_keys:
        return
    seen_keys.add(key)
    entries.append(
        MicroSessionReuse(
            philosophy_profile_id=philosophy_profile_id,
            micro_card_id=micro_card.id,
            micro_card_name=micro_card.title,
            reused_session_card_id=session_card.id,
            reused_session_card_name=session_card.title,
            reuse_type=reuse_type,
        )
    )


def _mainstream_sessions_by_parent(
    cards: list[BaseTrainingCard],
) -> dict[str, tuple[BaseTrainingCard, ...]]:
    grouped: dict[str, list[BaseTrainingCard]] = {}
    for card in cards:
        if card.card_type != CardType.SESSION:
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
