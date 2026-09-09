from __future__ import annotations

import unittest

from training_cards.philosophy_profiles import ENDURANCE_80_20, MAINSTREAM_ENDURANCE
from training_cards.pathway import (
    build_pathway_index,
    validate_pathway_publish_ready,
)
from training_cards.schemas import (
    CardReference,
    CardRelationship,
    CardType,
    MacroCard,
    MezzoCard,
    MicroCard,
    SessionCard,
    SessionFamily,
    TrainingLevel,
)


class PathwayIndexTests(unittest.TestCase):
    def test_children_follow_direct_child_references(self) -> None:
        cards = [
            _macro("macro_001", references=[_child("mezzo_001")]),
            _mezzo("mezzo_001"),
        ]

        children = build_pathway_index(cards).children("macro_001", "mezzo")

        self.assertEqual(["mezzo_001"], [card.id for card in children])

    def test_children_can_be_inferred_from_child_parent_reference(self) -> None:
        cards = [
            _macro("macro_001"),
            _mezzo("mezzo_001", references=[_parent("macro_001")]),
        ]

        children = build_pathway_index(cards).children("macro_001", "mezzo")

        self.assertEqual(["mezzo_001"], [card.id for card in children])

    def test_children_include_reused_macro_mezzo_mapping(self) -> None:
        cards = [
            _macro("macro_010", philosophy_profile_ids=[ENDURANCE_80_20]),
            _mezzo("mezzo_001"),
            _mezzo(
                "mezzo_029",
                philosophy_profile_ids=[ENDURANCE_80_20],
                references=[_parent("macro_010")],
            ),
        ]
        reuse_config = {
            "entries": [
                {
                    "philosophy_profile_id": ENDURANCE_80_20,
                    "macro_card_id": "macro_010",
                    "macro_card_name": "80/20 Base Development",
                    "reused_mezzo_card_id": "mezzo_001",
                    "reused_mezzo_card_name": "Re-Entry Rhythm Block",
                    "reuse_type": "reuse_mainstream",
                }
            ]
        }

        children = build_pathway_index(cards, reuse_config).children("macro_010", "mezzo")

        self.assertEqual(["mezzo_001", "mezzo_029"], [card.id for card in children])

    def test_children_include_reused_mezzo_micro_mapping(self) -> None:
        cards = [
            _mezzo("mezzo_001"),
            _micro("micro_001", references=[_parent("mezzo_001")]),
            _micro("micro_065", philosophy_profile_ids=[ENDURANCE_80_20], references=[_parent("mezzo_029")]),
        ]
        reuse_config = {
            "entries": [
                {
                    "philosophy_profile_id": ENDURANCE_80_20,
                    "mezzo_card_id": "mezzo_001",
                    "mezzo_card_name": "Re-Entry Rhythm Block",
                    "reused_micro_card_id": "micro_001",
                    "reused_micro_card_name": "Routine Anchor Week",
                    "reuse_type": "inherit_mainstream",
                }
            ]
        }

        children = build_pathway_index(
            cards,
            mezzo_micro_reuse_config=reuse_config,
        ).children("mezzo_001", "micro")

        self.assertEqual(["micro_001"], [card.id for card in children])

    def test_shortcut_parent_child_references_are_publish_errors(self) -> None:
        cards = [
            _macro("macro_001", references=[_child("micro_001")]),
            _micro("micro_001"),
        ]

        issues = build_pathway_index(cards).validate_relaxed()

        self.assertEqual(["error"], [issue.severity for issue in issues])
        self.assertIn("jumps from macro to micro", issues[0].message)

        with self.assertRaisesRegex(ValueError, "Pathway validation failed"):
            validate_pathway_publish_ready(cards)

    def test_orphan_cards_are_publish_ready(self) -> None:
        cards = [
            _macro("macro_001"),
            _mezzo("mezzo_001"),
        ]

        validate_pathway_publish_ready(cards)

    def test_sequence_and_alternative_references_must_stay_at_the_same_level(self) -> None:
        cards = [
            _macro(
                "macro_001",
                references=[
                    CardReference(
                        card_id="mezzo_001",
                        relationship=CardRelationship.NEXT,
                    ),
                    CardReference(
                        card_id="mezzo_002",
                        relationship=CardRelationship.ALTERNATIVE,
                    ),
                ],
            ),
            _mezzo("mezzo_001"),
            _mezzo("mezzo_002"),
        ]

        issues = build_pathway_index(cards).validate_relaxed()

        self.assertEqual(["error", "error"], [issue.severity for issue in issues])
        self.assertIn("same planning level", issues[0].message)

    def test_support_references_can_cross_planning_levels(self) -> None:
        cards = [
            _macro(
                "macro_001",
                references=[
                    CardReference(
                        card_id="session_001",
                        relationship=CardRelationship.SUPPORT,
                    )
                ],
            ),
            _session("session_001"),
        ]

        validate_pathway_publish_ready(cards)

    def test_reachability_counts_full_pathway(self) -> None:
        cards = [
            _macro("macro_001", references=[_child("mezzo_001")]),
            _mezzo("mezzo_001", references=[_child("micro_001")]),
            _micro("micro_001", references=[_child("session_001")]),
            _session("session_001"),
        ]

        summaries = build_pathway_index(cards).reachability_from_macros()

        self.assertEqual(1, len(summaries))
        self.assertEqual(1, summaries[0].mezzo_count)
        self.assertEqual(1, summaries[0].micro_count)
        self.assertEqual(1, summaries[0].session_count)
        self.assertEqual((), summaries[0].dead_end_mezzo_ids)
        self.assertEqual((), summaries[0].dead_end_micro_ids)


def _child(card_id: str) -> CardReference:
    return CardReference(card_id=card_id, relationship=CardRelationship.CHILD)


def _parent(card_id: str) -> CardReference:
    return CardReference(card_id=card_id, relationship=CardRelationship.PARENT)


def _macro(
    card_id: str,
    references: list[CardReference] | None = None,
    philosophy_profile_ids: list[str] | None = None,
) -> MacroCard:
    return MacroCard(
        id=card_id,
        slug=card_id,
        title=card_id,
        card_type=CardType.MACRO,
        suitable_levels=[TrainingLevel.ALL],
        philosophy_profile_ids=philosophy_profile_ids or [MAINSTREAM_ENDURANCE],
        summary="Summary.",
        purpose="Purpose.",
        references=references or [],
    )


def _mezzo(
    card_id: str,
    references: list[CardReference] | None = None,
    philosophy_profile_ids: list[str] | None = None,
) -> MezzoCard:
    return MezzoCard(
        id=card_id,
        slug=card_id,
        title=card_id,
        card_type=CardType.MEZZO,
        suitable_levels=[TrainingLevel.ALL],
        philosophy_profile_ids=philosophy_profile_ids or [MAINSTREAM_ENDURANCE],
        summary="Summary.",
        purpose="Purpose.",
        references=references or [],
    )


def _micro(
    card_id: str,
    references: list[CardReference] | None = None,
    philosophy_profile_ids: list[str] | None = None,
) -> MicroCard:
    return MicroCard(
        id=card_id,
        slug=card_id,
        title=card_id,
        card_type=CardType.MICRO,
        suitable_levels=[TrainingLevel.ALL],
        philosophy_profile_ids=philosophy_profile_ids or [MAINSTREAM_ENDURANCE],
        summary="Summary.",
        purpose="Purpose.",
        references=references or [],
    )


def _session(card_id: str, references: list[CardReference] | None = None) -> SessionCard:
    return SessionCard(
        id=card_id,
        slug=card_id,
        title=card_id,
        card_type=CardType.SESSION,
        suitable_levels=[TrainingLevel.ALL],
        philosophy_profile_ids=[MAINSTREAM_ENDURANCE],
        summary="Summary.",
        purpose="Purpose.",
        references=references or [],
        session_family=SessionFamily(
            id="family_001",
            slug="family",
            title="Family",
            summary="Family summary.",
        ),
    )


if __name__ == "__main__":
    unittest.main()
