from __future__ import annotations
from dataclasses import dataclass, field

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
