from __future__ import annotations

from training_cards.schemas import CardType


# ----------------------------------------------------------
# App Copy
# ----------------------------------------------------------
# Keep the top-level UI labels in one place so the page shell stays easy to
# change without touching the rendering code.

APP_TITLE = "Trail Running Training Cards"
APP_SUBTITLE = "A clean browser for macro, mezzo, micro, and session cards."

# ----------------------------------------------------------
# Card Ordering and Preview
# ----------------------------------------------------------
# These lists define the default navigation order and the fields shown in the
# preview-first layout.

TYPE_ORDER = [
    CardType.MACRO,
    CardType.MEZZO,
    CardType.MICRO,
    CardType.SESSION,
]

PREVIEW_FIELDS = ["title", "card_type", "summary", "purpose", "suitable_levels", "tags"]

DETAIL_SKIP_FIELDS = {"title", "card_type", "summary", "purpose", "suitable_levels", "tags"}

SEARCH_PLACEHOLDER = "Try: aerobic, taper, long run, recovery..."
