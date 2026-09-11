from __future__ import annotations

from collections.abc import Iterable


MAINSTREAM_ENDURANCE = "mainstream_endurance"
CTS = "cts"
EVOKE_ENDURANCE = "evoke_endurance"
SWAP = "swap"
SHARMAN_ULTRA = "sharman_ultra"
ENDURANCE_80_20 = "80_20_endurance"
LYDIARD = "lydiard"


# This is the canonical controlled vocabulary for card philosophy provenance.
# IDs must match the corresponding coaching/philosophies directory names.
PHILOSOPHY_PROFILES: dict[str, str] = {
    MAINSTREAM_ENDURANCE: "Mainstream Endurance",
    CTS: "CTS",
    EVOKE_ENDURANCE: "Evoke Endurance",
    SWAP: "Some Work, All Play",
    SHARMAN_ULTRA: "Sharman Ultra",
    ENDURANCE_80_20: "80/20 Endurance",
    LYDIARD: "Lydiard",
}

PHILOSOPHY_PROFILE_IDS = frozenset(PHILOSOPHY_PROFILES)


def philosophy_profile_display_name(profile_id: str) -> str:
    return PHILOSOPHY_PROFILES[profile_id]


def validate_philosophy_profile_ids(profile_ids: Iterable[str]) -> None:
    profile_id_list = list(profile_ids)
    unknown_profile_ids = sorted(set(profile_id_list) - PHILOSOPHY_PROFILE_IDS)
    if unknown_profile_ids:
        raise ValueError(
            "Training card philosophy_profile_ids contains unknown profile IDs: "
            + ", ".join(unknown_profile_ids)
        )
