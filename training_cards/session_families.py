from __future__ import annotations

from training_cards.schemas.session_family import SessionFamily

# ----------------------------------------------------------
# Session Family Registry
# ----------------------------------------------------------
# These objects define the reusable session-family taxonomy used by session
# cards. Cards reference these shared definitions rather than free-text labels.

EASY_SESSION_FAMILY = SessionFamily(
    id="session_family_easy",
    slug="easy",
    title="Easy",
    summary="Low-intensity aerobic running that builds volume and supports recovery.",
    description="Easy running is the backbone of most training plans. It should stay conversational and recoverable.",
    tags=["aerobic", "easy", "volume", "recovery"],
)

RECOVERY_SESSION_FAMILY = SessionFamily(
    id="session_family_recovery",
    slug="recovery",
    title="Recovery",
    summary="Very easy movement used to promote freshness without adding meaningful training stress.",
    description="Recovery running should feel almost too easy and should not become hidden training.",
    tags=["recovery", "easy", "low_load"],
)

ENDURANCE_SESSION_FAMILY = SessionFamily(
    id="session_family_endurance",
    slug="endurance",
    title="Endurance",
    summary="Longer aerobic running used to extend stamina, fueling practice, and time-on-feet.",
    description="Endurance sessions stretch the athlete's ability to stay aerobically steady for longer periods.",
    tags=["endurance", "long_run", "aerobic"],
)

CONTROLLED_QUALITY_SESSION_FAMILY = SessionFamily(
    id="session_family_controlled_quality",
    slug="controlled_quality",
    title="Controlled Quality",
    summary="Moderate quality work that stays clearly controlled and supports stamina without overreaching.",
    description="Controlled quality sits between easy running and hard workouts, with a strong emphasis on restraint.",
    tags=["controlled", "quality", "stamina"],
)

STEADY_SESSION_FAMILY = SessionFamily(
    id="session_family_steady",
    slug="steady",
    title="Steady",
    summary="Sustained aerobic running a little stronger than easy effort but still below threshold.",
    description="Steady sessions help build aerobic stamina while remaining below the cost of threshold work.",
    tags=["steady", "aerobic", "stamina"],
)

THRESHOLD_SESSION_FAMILY = SessionFamily(
    id="session_family_threshold",
    slug="threshold",
    title="Threshold",
    summary="Controlled hard running near threshold that develops sustainable effort and pacing discipline.",
    description="Threshold sessions build the ability to hold hard but repeatable effort without tipping into racing.",
    tags=["threshold", "tempo", "controlled_intensity"],
)

AEROBIC_POWER_SESSION_FAMILY = SessionFamily(
    id="session_family_aerobic_power",
    slug="aerobic_power",
    title="Aerobic Power",
    summary="Higher-intensity aerobic work that develops upper-aerobic capacity and hard-effort tolerance.",
    description="Aerobic power sessions are potent and costly, so they should stay purposeful and well controlled.",
    tags=["aerobic_power", "vo2max", "high_intensity"],
)

HILL_POWER_SESSION_FAMILY = SessionFamily(
    id="session_family_hill_power",
    slug="hill_power",
    title="Hill Power",
    summary="Short uphill work that develops power, mechanics, and neuromuscular snap.",
    description="Hill power sessions are short, crisp, and mechanically focused rather than long grinding climbs.",
    tags=["hills", "power", "neuromuscular"],
)

STRENGTH_ENDURANCE_SESSION_FAMILY = SessionFamily(
    id="session_family_strength_endurance",
    slug="strength_endurance",
    title="Strength Endurance",
    summary="Sustained hill work that builds the ability to hold force under fatigue.",
    description="Strength endurance work sits between pure endurance and higher-intensity hill power.",
    tags=["strength_endurance", "hills", "muscular_endurance"],
)

NEUROMUSCULAR_SESSION_FAMILY = SessionFamily(
    id="session_family_neuromuscular",
    slug="neuromuscular",
    title="Neuromuscular",
    summary="Very short relaxed speed touches used to maintain rhythm, coordination, and leg speed.",
    description="Neuromuscular sessions should feel smooth and crisp rather than maximal.",
    tags=["speed", "coordination", "rhythm"],
)

RACE_PRACTICE_SESSION_FAMILY = SessionFamily(
    id="session_family_race_practice",
    slug="race_practice",
    title="Race Practice",
    summary="Specific but controlled rehearsal of race demands, pacing, fueling, and execution.",
    description="Race practice sessions are about learning and refining execution without turning every rehearsal into a race.",
    tags=["specificity", "execution", "race"],
)

TRAIL_SPECIFIC_SESSION_FAMILY = SessionFamily(
    id="session_family_trail_specific",
    slug="trail_specific",
    title="Trail Specific Skills",
    summary="Trail-specific skill sessions that focus on climbing, hiking, descending, and terrain handling.",
    description="These sessions build mountain- and trail-specific skills that do not fit neatly into a single pure intensity family.",
    tags=["trail", "mountain", "skills"],
)

STRENGTH_MOBILITY_SUPPORT_SESSION_FAMILY = SessionFamily(
    id="session_family_strength_mobility_support",
    slug="strength_mobility_support",
    title="Strength / Mobility Support",
    summary="Strength, mobility, and activation work used to support durable running.",
    description="Strength and mobility support sessions should improve readiness and durability without accidentally overwhelming the running plan.",
    tags=["strength", "mobility", "activation", "support"],
)

LOW_IMPACT_AEROBIC_SUPPORT_SESSION_FAMILY = SessionFamily(
    id="session_family_low_impact_aerobic_support",
    slug="low_impact_aerobic_support",
    title="Low-Impact Aerobic Support",
    summary="Low-impact aerobic movement that supports endurance while reducing running load.",
    description="Low-impact aerobic support includes cross-training and gentle movement choices that preserve aerobic rhythm with less impact cost.",
    tags=["cross_training", "low_impact", "aerobic", "support"],
)

ALL_SESSION_FAMILIES = [
    EASY_SESSION_FAMILY,
    RECOVERY_SESSION_FAMILY,
    ENDURANCE_SESSION_FAMILY,
    CONTROLLED_QUALITY_SESSION_FAMILY,
    STEADY_SESSION_FAMILY,
    THRESHOLD_SESSION_FAMILY,
    AEROBIC_POWER_SESSION_FAMILY,
    HILL_POWER_SESSION_FAMILY,
    STRENGTH_ENDURANCE_SESSION_FAMILY,
    NEUROMUSCULAR_SESSION_FAMILY,
    RACE_PRACTICE_SESSION_FAMILY,
    TRAIL_SPECIFIC_SESSION_FAMILY,
    STRENGTH_MOBILITY_SUPPORT_SESSION_FAMILY,
    LOW_IMPACT_AEROBIC_SUPPORT_SESSION_FAMILY,
]

SESSION_FAMILY_BY_ID = {family.id: family for family in ALL_SESSION_FAMILIES}
SESSION_FAMILY_BY_SLUG = {family.slug: family for family in ALL_SESSION_FAMILIES}


def get_session_family(family_id_or_slug: str) -> SessionFamily:
    family = SESSION_FAMILY_BY_ID.get(family_id_or_slug) or SESSION_FAMILY_BY_SLUG.get(family_id_or_slug)
    if family is None:
        raise KeyError(f"Unknown session family: {family_id_or_slug}")
    return family
