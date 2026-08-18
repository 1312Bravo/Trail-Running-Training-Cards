from __future__ import annotations

import unittest

from training_cards.schemas import (
    CardType,
    MacroCard,
    TrainingLevel,
    philosophy_profile_display_name,
)


class PhilosophyProfileTests(unittest.TestCase):
    def test_cards_default_to_the_common_foundation(self) -> None:
        card = _macro()

        self.assertEqual(["common"], card.philosophy_profile_ids)

    def test_cards_can_reference_multiple_specific_profiles(self) -> None:
        card = _macro(philosophy_profile_ids=["cts", "evoke_endurance"])

        self.assertEqual(
            ["cts", "evoke_endurance"],
            card.philosophy_profile_ids,
        )

    def test_cards_reject_empty_duplicate_or_unknown_profile_ids(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            _macro(philosophy_profile_ids=[])

        with self.assertRaisesRegex(ValueError, "cannot contain duplicates"):
            _macro(philosophy_profile_ids=["common", "common"])

        with self.assertRaisesRegex(ValueError, "unknown profile IDs"):
            _macro(philosophy_profile_ids=["mountain-endurance"])

    def test_common_cannot_be_combined_with_a_named_profile(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot combine common"):
            _macro(philosophy_profile_ids=["common", "cts"])

    def test_profile_ids_have_display_names(self) -> None:
        self.assertEqual("80/20 Endurance", philosophy_profile_display_name("80_20_endurance"))


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
