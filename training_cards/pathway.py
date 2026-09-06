from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from training_cards.schemas import (
    BaseTrainingCard,
    CardRelationship,
)


PATHWAY_CARD_TYPES = ("macro", "mezzo", "micro", "session")


@dataclass(frozen=True, slots=True)
class GraphIssue:
    severity: str
    card_id: str
    message: str


@dataclass(frozen=True, slots=True)
class ReachabilitySummary:
    macro_id: str
    macro_title: str
    mezzo_count: int
    micro_count: int
    session_count: int
    dead_end_mezzo_ids: tuple[str, ...] = field(default_factory=tuple)
    dead_end_micro_ids: tuple[str, ...] = field(default_factory=tuple)


class PathwayIndex:
    """Index card references for pathway browsing and lightweight reporting."""

    def __init__(
        self,
        cards: Iterable[BaseTrainingCard],
        macro_mezzo_reuse_config: dict[str, object] | None = None,
    ) -> None:
        self.cards = sorted(cards, key=lambda card: (PATHWAY_CARD_TYPES.index(str(card.card_type)), card.title))
        self.by_id = {card.id: card for card in self.cards}
        self.macro_mezzo_reuse_config = macro_mezzo_reuse_config or {"entries": []}

    def cards_of_type(self, card_type: str) -> list[BaseTrainingCard]:
        return [
            card
            for card in self.cards
            if str(card.card_type) == card_type
        ]

    def children(self, parent_id: str, child_type: str | None = None) -> list[BaseTrainingCard]:
        parent = self.by_id.get(parent_id)
        if parent is None:
            return []

        child_ids = set()
        for reference in parent.references:
            child = self.by_id.get(reference.card_id)
            if reference.relationship == CardRelationship.CHILD and child:
                child_ids.add(child.id)

        for card in self.cards:
            for reference in card.references:
                if reference.relationship == CardRelationship.PARENT and reference.card_id == parent_id:
                    child_ids.add(card.id)

        if child_type in {None, "mezzo"}:
            for entry in self.macro_mezzo_reuse_config.get("entries", []):
                if not isinstance(entry, dict):
                    continue
                if entry.get("macro_card_id") == parent_id:
                    reused_mezzo_id = entry.get("reused_mezzo_card_id")
                    if isinstance(reused_mezzo_id, str):
                        child_ids.add(reused_mezzo_id)

        children = [self.by_id[card_id] for card_id in child_ids if card_id in self.by_id]
        if child_type is not None:
            children = [card for card in children if str(card.card_type) == child_type]
        return self._sort_cards(children)

    def parents(self, child_id: str, parent_type: str | None = None) -> list[BaseTrainingCard]:
        child = self.by_id.get(child_id)
        if child is None:
            return []

        parent_ids = set()
        for reference in child.references:
            parent = self.by_id.get(reference.card_id)
            if reference.relationship == CardRelationship.PARENT and parent:
                parent_ids.add(parent.id)

        for card in self.cards:
            for reference in card.references:
                if reference.relationship == CardRelationship.CHILD and reference.card_id == child_id:
                    parent_ids.add(card.id)

        parents = [self.by_id[card_id] for card_id in parent_ids if card_id in self.by_id]
        if parent_type is not None:
            parents = [card for card in parents if str(card.card_type) == parent_type]
        return self._sort_cards(parents)

    def validate_relaxed(self) -> list[GraphIssue]:
        issues = []
        seen_reference_keys = set()

        for card in self.cards:
            for reference in card.references:
                key = (card.id, str(reference.relationship), reference.card_id)
                if key in seen_reference_keys:
                    issues.append(
                        GraphIssue(
                            "warning",
                            card.id,
                            f"Duplicate {reference.relationship} reference to {reference.card_id}.",
                        )
                    )
                seen_reference_keys.add(key)

                target = self.by_id.get(reference.card_id)
                if target is None:
                    issues.append(
                        GraphIssue(
                            "error",
                            card.id,
                            f"Reference points to missing card {reference.card_id}.",
                        )
                    )
                    continue

                if reference.card_id == card.id:
                    issues.append(
                        GraphIssue(
                            "warning",
                            card.id,
                            f"Self-reference through {reference.relationship}.",
                        )
                    )

                if reference.relationship in {CardRelationship.PARENT, CardRelationship.CHILD}:
                    issue = self._validate_pathway_direction(card, target, reference.relationship)
                    if issue:
                        issues.append(issue)
                elif reference.relationship in {
                    CardRelationship.PREVIOUS,
                    CardRelationship.NEXT,
                    CardRelationship.ALTERNATIVE,
                }:
                    issue = self._validate_same_level_relationship(
                        card,
                        target,
                        reference.relationship,
                    )
                    if issue:
                        issues.append(issue)

        return issues

    def reachability_from_macros(self) -> list[ReachabilitySummary]:
        summaries = []
        for macro in self.cards_of_type("macro"):
            mezzos = self.children(macro.id, "mezzo")
            micros = self._unique_cards(
                micro
                for mezzo in mezzos
                for micro in self.children(mezzo.id, "micro")
            )
            sessions = self._unique_cards(
                session
                for micro in micros
                for session in self.children(micro.id, "session")
            )
            dead_end_mezzos = tuple(
                mezzo.id
                for mezzo in mezzos
                if not self.children(mezzo.id, "micro")
            )
            dead_end_micros = tuple(
                micro.id
                for micro in micros
                if not self.children(micro.id, "session")
            )
            summaries.append(
                ReachabilitySummary(
                    macro_id=macro.id,
                    macro_title=macro.title,
                    mezzo_count=len(mezzos),
                    micro_count=len(micros),
                    session_count=len(sessions),
                    dead_end_mezzo_ids=dead_end_mezzos,
                    dead_end_micro_ids=dead_end_micros,
                )
            )
        return summaries

    def orphan_cards(self) -> list[BaseTrainingCard]:
        return [
            card
            for card in self.cards
            if not card.references and not self.parents(card.id) and not self.children(card.id)
        ]

    def _validate_pathway_direction(
        self,
        source: BaseTrainingCard,
        target: BaseTrainingCard,
        relationship: CardRelationship,
    ) -> GraphIssue | None:
        source_index = PATHWAY_CARD_TYPES.index(str(source.card_type))
        target_index = PATHWAY_CARD_TYPES.index(str(target.card_type))
        expected_delta = 1 if relationship == CardRelationship.CHILD else -1
        actual_delta = target_index - source_index

        if actual_delta == expected_delta:
            return None

        return GraphIssue(
            "error",
            source.id,
            (
                f"{relationship} reference to {target.id} jumps from "
                f"{source.card_type} to {target.card_type}."
            ),
        )

    def _validate_same_level_relationship(
        self,
        source: BaseTrainingCard,
        target: BaseTrainingCard,
        relationship: CardRelationship,
    ) -> GraphIssue | None:
        if source.card_type == target.card_type:
            return None

        return GraphIssue(
            "error",
            source.id,
            (
                f"{relationship} reference to {target.id} must stay within the same "
                f"planning level, not {source.card_type} to {target.card_type}."
            ),
        )

    def _sort_cards(self, cards: Iterable[BaseTrainingCard]) -> list[BaseTrainingCard]:
        return sorted(cards, key=lambda card: (PATHWAY_CARD_TYPES.index(str(card.card_type)), card.title))

    def _unique_cards(self, cards: Iterable[BaseTrainingCard]) -> list[BaseTrainingCard]:
        unique = {}
        for card in cards:
            unique[card.id] = card
        return self._sort_cards(unique.values())


def build_pathway_index(
    cards: Iterable[BaseTrainingCard],
    macro_mezzo_reuse_config: dict[str, object] | None = None,
) -> PathwayIndex:
    return PathwayIndex(cards, macro_mezzo_reuse_config)


def validate_pathway_publish_ready(cards: Iterable[BaseTrainingCard]) -> None:
    """Raise when card relationships violate the publish-ready contract."""
    issues = build_pathway_index(cards).validate_relaxed()
    errors = [issue for issue in issues if issue.severity == "error"]

    if not errors:
        return

    details = "\n".join(
        f"- {issue.card_id}: {issue.message}"
        for issue in errors
    )
    raise ValueError(f"Pathway validation failed:\n{details}")
