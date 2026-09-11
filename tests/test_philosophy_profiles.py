from __future__ import annotations

import unittest

from training_cards.philosophy_profiles import ENDURANCE_80_20, MAINSTREAM_ENDURANCE
from training_cards.schemas import (
    CardType,
    MacroCard,
    PHILOSOPHY_PROFILES,
    TrainingLevel,
    philosophy_profile_display_name,
)


class PhilosophyProfileTests(unittest.TestCase):
    def test_cards_require_a_training_method_profile(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            _macro()

        with self.assertRaisesRegex(ValueError, "cannot be empty"):
            _macro(philosophy_profile_ids=[])

    def test_cards_can_reference_multiple_specific_profiles(self) -> None:
        card = _macro(philosophy_profile_ids=["cts", "evoke_endurance"])

        self.assertEqual(
            ["cts", "evoke_endurance"],
            card.philosophy_profile_ids,
        )

    def test_cards_reject_duplicate_or_unknown_profile_ids(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot contain duplicates"):
            _macro(philosophy_profile_ids=["cts", "cts"])

        with self.assertRaisesRegex(ValueError, "unknown profile IDs"):
            _macro(philosophy_profile_ids=["mountain-endurance"])

    def test_common_is_not_a_philosophy_profile(self) -> None:
        self.assertNotIn("common", PHILOSOPHY_PROFILES)

        with self.assertRaisesRegex(ValueError, "unknown profile IDs"):
            _macro(philosophy_profile_ids=["common"])

    def test_profile_ids_have_display_names(self) -> None:
        self.assertEqual("80/20 Endurance", philosophy_profile_display_name(ENDURANCE_80_20))
        self.assertEqual("Mainstream Endurance", philosophy_profile_display_name(MAINSTREAM_ENDURANCE))

    def test_mainstream_endurance_is_a_regular_profile(self) -> None:
        self.assertIn(MAINSTREAM_ENDURANCE, PHILOSOPHY_PROFILES)


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
