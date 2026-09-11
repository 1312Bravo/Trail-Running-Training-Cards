from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Iterable

from training_cards.philosophy_profiles import (
    CTS,
    ENDURANCE_80_20,
    EVOKE_ENDURANCE,
    LYDIARD,
    SHARMAN_ULTRA,
    SWAP,
    validate_philosophy_profile_ids,
)


MACRO_MEZZO_REUSE_VERSION = "1.0.0"
INHERIT_MAINSTREAM = "inherit_mainstream"
REUSE_MAINSTREAM = "reuse_mainstream"
VALID_REUSE_TYPES = {INHERIT_MAINSTREAM, REUSE_MAINSTREAM}


@dataclass(frozen=True, slots=True)
class MacroMezzoReuse:
    philosophy_profile_id: str
    macro_card_id: str
    macro_card_name: str
    reused_mezzo_card_id: str
    reused_mezzo_card_name: str
    reuse_type: str

    def __post_init__(self) -> None:
        validate_philosophy_profile_ids([self.philosophy_profile_id])
        if not self.macro_card_id.strip():
            raise ValueError("MacroMezzoReuse macro_card_id cannot be empty.")
        if not self.macro_card_name.strip():
            raise ValueError("MacroMezzoReuse macro_card_name cannot be empty.")
        if not self.reused_mezzo_card_id.strip():
            raise ValueError("MacroMezzoReuse reused_mezzo_card_id cannot be empty.")
        if not self.reused_mezzo_card_name.strip():
            raise ValueError("MacroMezzoReuse reused_mezzo_card_name cannot be empty.")
        if self.reuse_type not in VALID_REUSE_TYPES:
            raise ValueError(f"Unknown macro-mezzo reuse type: {self.reuse_type}")


MAINSTREAM_MACRO_NAMES = {
    "macro_001": "Return To Consistency",
    "macro_002": "Base Development",
    "macro_003": "Capacity Development",
    "macro_004": "Race-Specific Preparation",
    "macro_005": "Peak And Taper",
    "macro_006": "Competition Management",
    "macro_007": "Recovery And Transition",
    "macro_008": "Off-Season",
    "macro_009": "Maintenance",
}

MAINSTREAM_MEZZO_NAMES = {
    "mezzo_001": "Re-Entry Rhythm Block",
    "mezzo_002": "Easy Aerobic Reconditioning Block",
    "mezzo_003": "Movement Strength Reintroduction Block",
    "mezzo_004": "Aerobic Volume Block",
    "mezzo_005": "Long Endurance Development Block",
    "mezzo_006": "Strength And Movement Support Block",
    "mezzo_007": "Threshold Control Block",
    "mezzo_008": "Aerobic Power Block",
    "mezzo_009": "Strength Endurance Block",
    "mezzo_010": "Course Demands Block",
    "mezzo_011": "Race Execution Practice Block",
    "mezzo_012": "Fueling And Hydration Practice Block",
    "mezzo_013": "Taper Freshness Block",
    "mezzo_014": "Sharpening Touchpoint Block",
    "mezzo_015": "Race Readiness Check Block",
    "mezzo_016": "Between-Race Recovery Block",
    "mezzo_017": "Race Season Maintenance Block",
    "mezzo_018": "Competition Learning Block",
    "mezzo_019": "Post-Race Recovery Block",
    "mezzo_020": "Reduced-Load Adaptation Block",
    "mezzo_021": "Transition Bridge Block",
    "mezzo_022": "Low-Pressure Aerobic Rhythm Block",
    "mezzo_023": "General Strength And Mobility Block",
    "mezzo_024": "Movement Variety Block",
    "mezzo_025": "Aerobic Maintenance Block",
    "mezzo_026": "Quality Touchpoint Block",
    "mezzo_027": "Constraint-Friendly Consistency Block",
    "mezzo_028": "Trail Skill And Terrain Familiarity Block",
}

MAINSTREAM_MEZZOS_BY_MACRO = {
    "macro_001": ("mezzo_001", "mezzo_002", "mezzo_003"),
    "macro_002": ("mezzo_004", "mezzo_005", "mezzo_006", "mezzo_028"),
    "macro_003": ("mezzo_007", "mezzo_008", "mezzo_009"),
    "macro_004": ("mezzo_010", "mezzo_011", "mezzo_012"),
    "macro_005": ("mezzo_013", "mezzo_014", "mezzo_015"),
    "macro_006": ("mezzo_016", "mezzo_017", "mezzo_018"),
    "macro_007": ("mezzo_019", "mezzo_020", "mezzo_021"),
    "macro_008": ("mezzo_022", "mezzo_023", "mezzo_024"),
    "macro_009": ("mezzo_025", "mezzo_026", "mezzo_027"),
}


def _macro_mezzos(macro_id: str, *mezzo_ids: str) -> tuple[str, ...]:
    if mezzo_ids:
        return tuple(mezzo_ids)

    return MAINSTREAM_MEZZOS_BY_MACRO[macro_id]


def _entries(
    *,
    philosophy_profile_id: str,
    macro_card_id: str,
    macro_card_name: str,
    reused_mezzo_card_ids: Iterable[str],
    reuse_type: str,
) -> tuple[MacroMezzoReuse, ...]:
    return tuple(
        MacroMezzoReuse(
            philosophy_profile_id=philosophy_profile_id,
            macro_card_id=macro_card_id,
            macro_card_name=macro_card_name,
            reused_mezzo_card_id=mezzo_id,
            reused_mezzo_card_name=MAINSTREAM_MEZZO_NAMES[mezzo_id],
            reuse_type=reuse_type,
        )
        for mezzo_id in reused_mezzo_card_ids
    )


def _inherited(
    philosophy_profile_id: str,
    macro_id: str,
    *mezzo_ids: str,
) -> tuple[MacroMezzoReuse, ...]:
    return _entries(
        philosophy_profile_id=philosophy_profile_id,
        macro_card_id=macro_id,
        macro_card_name=MAINSTREAM_MACRO_NAMES[macro_id],
        reused_mezzo_card_ids=_macro_mezzos(macro_id, *mezzo_ids),
        reuse_type=INHERIT_MAINSTREAM,
    )


def _reused(
    philosophy_profile_id: str,
    macro_id: str,
    macro_name: str,
    *mezzo_ids: str,
) -> tuple[MacroMezzoReuse, ...]:
    return _entries(
        philosophy_profile_id=philosophy_profile_id,
        macro_card_id=macro_id,
        macro_card_name=macro_name,
        reused_mezzo_card_ids=mezzo_ids,
        reuse_type=REUSE_MAINSTREAM,
    )


MACRO_MEZZO_REUSE_ENTRIES: tuple[MacroMezzoReuse, ...] = (
    *_inherited(ENDURANCE_80_20, "macro_001"),
    *_inherited(ENDURANCE_80_20, "macro_005"),
    *_inherited(ENDURANCE_80_20, "macro_007"),
    *_inherited(ENDURANCE_80_20, "macro_008"),
    *_reused(ENDURANCE_80_20, "macro_010", "80/20 Base Development", "mezzo_006", "mezzo_028"),
    *_reused(ENDURANCE_80_20, "macro_012", "80/20 Race-Specific Preparation", "mezzo_011", "mezzo_012"),
    *_reused(ENDURANCE_80_20, "macro_014", "80/20 Competition Management", "mezzo_018"),
    *_reused(ENDURANCE_80_20, "macro_015", "80/20 Maintenance", "mezzo_027"),
    *_inherited(LYDIARD, "macro_001"),
    *_inherited(LYDIARD, "macro_006"),
    *_inherited(LYDIARD, "macro_007", "mezzo_019", "mezzo_021"),
    *_inherited(LYDIARD, "macro_008"),
    *_inherited(LYDIARD, "macro_009"),
    *_reused(LYDIARD, "macro_016", "Lydiard Base Development", "mezzo_006", "mezzo_028"),
    *_reused(LYDIARD, "macro_018", "Lydiard Race-Specific Preparation", "mezzo_012"),
    *_reused(LYDIARD, "macro_019", "Lydiard Peak And Taper", "mezzo_015"),
    *_inherited(CTS, "macro_001"),
    *_inherited(CTS, "macro_005"),
    *_inherited(CTS, "macro_007"),
    *_inherited(CTS, "macro_008"),
    *_inherited(CTS, "macro_009"),
    *_reused(CTS, "macro_020", "CTS Base Development", "mezzo_006", "mezzo_028"),
    *_inherited(EVOKE_ENDURANCE, "macro_001"),
    *_inherited(EVOKE_ENDURANCE, "macro_005"),
    *_inherited(EVOKE_ENDURANCE, "macro_006"),
    *_inherited(EVOKE_ENDURANCE, "macro_007", "mezzo_019", "mezzo_021"),
    *_inherited(EVOKE_ENDURANCE, "macro_008"),
    *_inherited(EVOKE_ENDURANCE, "macro_009"),
    *_reused(EVOKE_ENDURANCE, "macro_024", "Evoke Base Development", "mezzo_028"),
    *_reused(EVOKE_ENDURANCE, "macro_026", "Evoke Race-Specific Preparation", "mezzo_012"),
    *_inherited(SWAP, "macro_005"),
    *_inherited(SWAP, "macro_007", "mezzo_020"),
    *_inherited(SWAP, "macro_009"),
    *_reused(SWAP, "macro_027", "SWAP Return To Consistency", "mezzo_003"),
    *_reused(SWAP, "macro_028", "SWAP Base Development", "mezzo_006", "mezzo_028"),
    *_reused(SWAP, "macro_030", "SWAP Race-Specific Preparation", "mezzo_012"),
    *_reused(SWAP, "macro_034", "SWAP Off-Season", "mezzo_023"),
    *_inherited(SHARMAN_ULTRA, "macro_001"),
    *_inherited(SHARMAN_ULTRA, "macro_002"),
    *_inherited(SHARMAN_ULTRA, "macro_003"),
    *_inherited(SHARMAN_ULTRA, "macro_005"),
    *_inherited(SHARMAN_ULTRA, "macro_007"),
    *_inherited(SHARMAN_ULTRA, "macro_008"),
    *_inherited(SHARMAN_ULTRA, "macro_009"),
    *_reused(SHARMAN_ULTRA, "macro_038", "Sharman Ultra Competition Management", "mezzo_017"),
)


def macro_mezzo_reuse_to_dict(reuse: MacroMezzoReuse) -> dict[str, str]:
    return asdict(reuse)


def build_macro_mezzo_reuse_config(
    schema_version: str,
    *,
    card_ids: set[str] | None = None,
) -> dict[str, object]:
    entries = MACRO_MEZZO_REUSE_ENTRIES
    if card_ids is not None:
        entries = tuple(
            entry
            for entry in entries
            if entry.macro_card_id in card_ids and entry.reused_mezzo_card_id in card_ids
        )

    return {
        "macro_mezzo_reuse_version": MACRO_MEZZO_REUSE_VERSION,
        "schema_version": schema_version,
        "entry_count": len(entries),
        "entries": [macro_mezzo_reuse_to_dict(entry) for entry in entries],
    }
