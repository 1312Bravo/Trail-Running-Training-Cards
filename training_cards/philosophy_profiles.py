from __future__ import annotations

from collections.abc import Iterable


COMMON_PHILOSOPHY_PROFILE_ID = "common"

# This is the canonical controlled vocabulary for card philosophy provenance.
# IDs must match the corresponding coaching/philosophies directory names.
PHILOSOPHY_PROFILES: dict[str, str] = {
    COMMON_PHILOSOPHY_PROFILE_ID: "Common",
    "cts": "CTS",
    "evoke_endurance": "Evoke Endurance",
    "swap": "Some Work, All Play",
    "sharman_ultra": "Sharman Ultra",
    "80_20_endurance": "80/20 Endurance",
    "lydiard": "Lydiard",
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
    if (
        COMMON_PHILOSOPHY_PROFILE_ID in profile_id_list
        and len(profile_id_list) != 1
    ):
        raise ValueError(
            "Training card philosophy_profile_ids cannot combine common with named profiles."
        )
