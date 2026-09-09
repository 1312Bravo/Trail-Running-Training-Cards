from __future__ import annotations

from training_cards.schemas import CardType


# ----------------------------------------------------------
# App Copy
# ----------------------------------------------------------
# Keep the top-level UI labels in one place so the page shell stays easy to
# change without touching the rendering code.

APP_TITLE = "Run & Train with Deck of Cards"

# ----------------------------------------------------------
# Card Ordering and Detail
# ----------------------------------------------------------
# These lists define the default navigation order and full-card presentation.

TYPE_ORDER = [
    CardType.MACRO,
    CardType.MEZZO,
    CardType.MICRO,
    CardType.SESSION,
]

# Full-card detail follows coaching use rather than raw JSON key order. Fields
# missing on a card type are skipped, while future schema fields still append.
DETAIL_SECTION_ORDER = [
    "summary",
    "purpose",
    "suitable_levels",
    "recommended_duration_weeks",
    "recommended_duration_days",
    "typical_duration",
    "timing_guidance",
    "placement_guidance",
    "goal_race_context",
    "training_profile",
    "session_family",
    "week_structure",
    "key_sessions",
    "load_pattern",
    "workout_blocks",
    "expected_adaptations",
    "recovery_requirements",
    "watchouts",
    "progression_rules",
    "regression_rules",
    "philosophy_profile_ids",
    "tags",
    "additional_information",
    "references",
]

# These are presentation labels only; the source schema field names remain
# unchanged in JSON and in the core library.
DETAIL_FIELD_LABEL_OVERRIDES = {
    "additional_information": "Coaching note",
}

SEARCH_PLACEHOLDER = "Search cards"
