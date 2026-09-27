from __future__ import annotations

from training_cards.philosophy_profiles import PHILOSOPHY_PROFILES
from training_cards.schemas import CardType


# ----------------------------------------------------------
# App Copy
# ----------------------------------------------------------
# Keep the top-level UI labels in one place so the page shell stays easy to
# change without touching the rendering code.

APP_TITLE = "Run & Train with Deck of Cards"

APP_MODES = [
    "Browse cards",
    "Today session",
    "Card library",
    "Build pathway",
    "Coaching philosophies",
]

APP_MODE_INFO = {
    "Browse cards": [
        "Browse the full card deck or narrow it by level.",
        "Use search, tags, and coaching philosophy filters to find useful cards.",
        "Open a card to inspect the full coaching details.",
    ],
    "Today session": [
        "Focus on session cards you can use for a single workout.",
        "Add search terms to narrow sessions by goal, terrain, intensity, or theme.",
        "Open a card when you want the full session structure.",
    ],
    "Card library": [
        "See the library organized by coaching philosophy.",
        "Use level filters for macro, mezzo, micro, or session cards.",
        "Expand a philosophy group to scan cards and preview details.",
    ],
    "Build pathway": [
        "Build a training pathway from macro to session.",
        "Choose one card at each level; the next step shows related options.",
        "Use filters if you want the pathway to follow a specific coaching lens.",
    ],
    "Coaching philosophies": [
        "Read short summaries of the coaching systems behind the library.",
        "Use Show cards to browse cards connected to a philosophy.",
        "Open sources when you want the reviewed references.",
    ],
}

PHILOSOPHY_SUMMARY_HEIGHT = 330
DEFAULT_CARDS_PER_PAGE = 8
LIBRARY_DEFAULT_CARDS_PER_PAGE = 10
PATHWAY_STEPS = [
    ("macro", "Macro"),
    ("mezzo", "Mezzo"),
    ("micro", "Micro"),
    ("session", "Session"),
]

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

# Keep the philosophy order consistent across every card view.
PHILOSOPHY_ORDER = tuple(PHILOSOPHY_PROFILES)

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
