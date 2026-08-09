from __future__ import annotations
from dataclasses import dataclass, field
from .base import BaseTrainingCard
from .enums import CardType

# ----------------------------------------------------------
# Session Family Definition
# ----------------------------------------------------------
# Session families group related workouts into searchable coaching labels.

@dataclass(slots=True)
class SessionFamily:
    id: str
    slug: str
    title: str
    summary: str
    description: str = ""
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValueError("Session family id cannot be empty.")
        if not self.slug.strip():
            raise ValueError("Session family slug cannot be empty.")
        if not self.title.strip():
            raise ValueError("Session family title cannot be empty.")
        if not self.summary.strip():
            raise ValueError("Session family summary cannot be empty.")

# ----------------------------------------------------------
# Session Workout Structure
# ----------------------------------------------------------
# Session parts make workouts exportable/readable as warm-up, main set,
# recovery, cooldown, or execution blocks with duration and RPE guidance.

@dataclass(slots=True)
class SessionPart:
    name: str
    duration: str
    rpe: str
    instructions: str = ""
    terrain_notes: str = ""

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Session part name cannot be empty.")
        if not self.duration.strip():
            raise ValueError("Session part duration cannot be empty.")
        if not self.rpe.strip():
            raise ValueError("Session part rpe cannot be empty.")

# ----------------------------------------------------------
# Session Card
# ----------------------------------------------------------
# Session cards are individual workout patterns that can be reused across
# many different micro weeks.

@dataclass(slots=True, kw_only=True)
class SessionCard(BaseTrainingCard):
    session_family: SessionFamily
    typical_duration: str = ""
    workout_parts: list[SessionPart] = field(default_factory=list)

    def __post_init__(self) -> None:
        BaseTrainingCard.__post_init__(self)
        if self.card_type != CardType.SESSION:
            raise ValueError("SessionCard card_type must be CardType.SESSION.")
