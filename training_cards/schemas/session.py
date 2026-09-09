from __future__ import annotations
from dataclasses import dataclass, field
from enum import StrEnum
from .base import BaseTrainingCard
from .enums import CardType
from .session_family import SessionFamily

# ----------------------------------------------------------
# Session Workout Structure
# ----------------------------------------------------------
# Session cards are structured as workout blocks. Each block contains one or
# more options, and each option contains the concrete parts the athlete follows.

class WorkoutBlockType(StrEnum):
    WARMUP = "warmup"
    MAIN = "main"
    RECOVERY = "recovery"
    COOLDOWN = "cooldown"
    OPTIONAL_ADDON = "optional_addon"
    NOTES = "notes"


class WorkoutBlockExecutionMode(StrEnum):
    DO_ALL = "do_all"
    CHOOSE_ONE = "choose_one"
    OPTIONAL = "optional"


@dataclass(slots=True)
class SessionPart:
    title: str
    prescription: str = ""
    duration: str = ""
    rpe: str = ""
    selection_notes: str = ""
    coaching_notes: str = ""
    terrain_notes: str = ""
    adjustment_notes: str = ""

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("Session part title cannot be empty.")


@dataclass(slots=True)
class WorkoutOption:
    title: str
    repeat: str = ""
    selection_notes: str = ""
    load_notes: str = ""
    parts: list[SessionPart] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("Workout option title cannot be empty.")
        if not self.parts:
            raise ValueError("Workout option parts cannot be empty.")


@dataclass(slots=True)
class WorkoutBlock:
    block_type: WorkoutBlockType
    execution_mode: WorkoutBlockExecutionMode = WorkoutBlockExecutionMode.DO_ALL
    options: list[WorkoutOption] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.block_type = WorkoutBlockType(self.block_type)
        self.execution_mode = WorkoutBlockExecutionMode(self.execution_mode)
        if not self.options:
            raise ValueError("Workout block options cannot be empty.")

# ----------------------------------------------------------
# Session Card
# ----------------------------------------------------------
# Session cards are individual workout patterns that can be reused across
# many different micro weeks.

@dataclass(slots=True, kw_only=True)
class SessionCard(BaseTrainingCard):
    session_family: SessionFamily
    typical_duration: str = ""
    workout_blocks: list[WorkoutBlock] = field(default_factory=list)

    def __post_init__(self) -> None:
        BaseTrainingCard.__post_init__(self)
        if self.card_type != CardType.SESSION:
            raise ValueError("SessionCard card_type must be CardType.SESSION.")
