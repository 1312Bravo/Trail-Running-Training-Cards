from __future__ import annotations

import unittest

from training_cards.schemas import CardType, MacroCard, TrainingLevel


class PhilosophyProfileTests(unittest.TestCase):
    def test_cards_default_to_the_common_foundation(self) -> None:
        card = _macro()

        self.assertEqual(["common"], card.philosophy_profile_ids)

    def test_cards_can_reference_multiple_specific_profiles(self) -> None:
        card = _macro(philosophy_profile_ids=["mountain-endurance", "readiness-led"])

        self.assertEqual(
            ["mountain-endurance", "readiness-led"],
            card.philosophy_profile_ids,
        )

    def test_cards_reject_empty_or_duplicate_profile_ids(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            _macro(philosophy_profile_ids=[])

        with self.assertRaisesRegex(ValueError, "cannot contain duplicates"):
            _macro(philosophy_profile_ids=["common", "common"])


def _macro(philosophy_profile_ids: list[str] | None = None) -> MacroCard:
    arguments = {}
    if philosophy_profile_ids is not None:
        arguments["philosophy_profile_ids"] = philosophy_profile_ids

    return MacroCard(
        id="macro_001",
        slug="macro-001",
        title="Macro 001",
        card_type=CardType.MACRO,
        suitable_levels=[TrainingLevel.ALL],
        summary="Summary.",
        purpose="Purpose.",
        **arguments,
    )


if __name__ == "__main__":
    unittest.main()
