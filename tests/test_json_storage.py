from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from training_cards.json_store import (
    LIBRARY_BUNDLE_FILE_NAME,
    MACRO_MEZZO_REUSE_FILE_NAME,
    MEZZO_MICRO_REUSE_FILE_NAME,
    MULTI_PROFILE_CARD_FOLDER,
    card_storage_path,
    export_card_library_to_json,
    load_card_library_from_json,
    load_macro_mezzo_reuse_config,
    load_mezzo_micro_reuse_config,
    read_json,
)
from training_cards.philosophy_profiles import CTS, LYDIARD, MAINSTREAM_ENDURANCE
from training_cards.schemas import CardType, MacroCard, TrainingLevel
from training_cards.schemas import (
    SessionCard,
    SessionFamily,
    SessionPart,
    WorkoutBlock,
    WorkoutBlockExecutionMode,
    WorkoutBlockType,
    WorkoutOption,
)


class JsonStorageTests(unittest.TestCase):
    def test_single_profile_card_uses_profile_folder(self) -> None:
        card = _macro("macro_001", [MAINSTREAM_ENDURANCE])

        self.assertEqual(
            Path("macro") / MAINSTREAM_ENDURANCE / "macro-001.json",
            card_storage_path(card),
        )

    def test_multi_profile_card_uses_multi_profile_folder(self) -> None:
        card = _macro("macro_001", [CTS, LYDIARD])

        self.assertEqual(
            Path("macro") / MULTI_PROFILE_CARD_FOLDER / "macro-001.json",
            card_storage_path(card),
        )

    def test_export_and_load_nested_profile_folders(self) -> None:
        cards = [
            _macro("macro_001", [MAINSTREAM_ENDURANCE]),
            _macro("macro_002", [CTS, LYDIARD]),
        ]

        with tempfile.TemporaryDirectory(prefix="training_cards_json_storage_") as temp_dir:
            output_dir = Path(temp_dir)
            export_card_library_to_json(cards, output_dir)

            self.assertTrue(
                (output_dir / "cards" / "macro" / MAINSTREAM_ENDURANCE / "macro-001.json").exists()
            )
            self.assertTrue(
                (output_dir / "cards" / "macro" / MULTI_PROFILE_CARD_FOLDER / "macro-002.json").exists()
            )
            self.assertTrue((output_dir / MACRO_MEZZO_REUSE_FILE_NAME).exists())
            self.assertTrue((output_dir / MEZZO_MICRO_REUSE_FILE_NAME).exists())
            self.assertEqual(
                0,
                load_macro_mezzo_reuse_config(output_dir)["entry_count"],
            )
            self.assertEqual(
                0,
                load_mezzo_micro_reuse_config(output_dir)["entry_count"],
            )
            self.assertIn(
                "macro_mezzo_reuse",
                read_json(output_dir / LIBRARY_BUNDLE_FILE_NAME),
            )
            self.assertIn(
                "mezzo_micro_reuse",
                read_json(output_dir / LIBRARY_BUNDLE_FILE_NAME),
            )

            loaded_cards = load_card_library_from_json(output_dir)

        self.assertEqual(["macro_001", "macro_002"], [card.id for card in loaded_cards])

    def test_session_workout_blocks_round_trip(self) -> None:
        cards = [_session("session_001")]

        with tempfile.TemporaryDirectory(prefix="training_cards_session_storage_") as temp_dir:
            output_dir = Path(temp_dir)
            export_card_library_to_json(cards, output_dir)

            session_json = read_json(
                output_dir
                / "cards"
                / "session"
                / MAINSTREAM_ENDURANCE
                / "session-001.json"
            )
            self.assertIn("workout_blocks", session_json)
            self.assertNotIn("workout_parts", session_json)

            loaded_card = load_card_library_from_json(output_dir)[0]

        self.assertIsInstance(loaded_card, SessionCard)
        self.assertEqual(WorkoutBlockType.MAIN, loaded_card.workout_blocks[0].block_type)
        self.assertEqual(
            WorkoutBlockExecutionMode.CHOOSE_ONE,
            loaded_card.workout_blocks[0].execution_mode,
        )
        self.assertEqual("4 rounds", loaded_card.workout_blocks[0].options[0].repeat)
        self.assertEqual(
            "Hard Repetition",
            loaded_card.workout_blocks[0].options[0].parts[0].title,
        )


def _macro(card_id: str, philosophy_profile_ids: list[str]) -> MacroCard:
    return MacroCard(
        id=card_id,
        slug=card_id.replace("_", "-"),
        title=card_id,
        card_type=CardType.MACRO,
        suitable_levels=[TrainingLevel.ALL],
        philosophy_profile_ids=philosophy_profile_ids,
        summary="Summary.",
        purpose="Purpose.",
    )


def _session(card_id: str) -> SessionCard:
    return SessionCard(
        id=card_id,
        slug=card_id.replace("_", "-"),
        title=card_id,
        card_type=CardType.SESSION,
        suitable_levels=[TrainingLevel.INTERMEDIATE],
        philosophy_profile_ids=[MAINSTREAM_ENDURANCE],
        summary="Summary.",
        purpose="Purpose.",
        session_family=SessionFamily(
            id="session_family_test",
            slug="test",
            title="Test",
            summary="Test family.",
        ),
        workout_blocks=[
            WorkoutBlock(
                block_type=WorkoutBlockType.MAIN,
                execution_mode=WorkoutBlockExecutionMode.CHOOSE_ONE,
                options=[
                    WorkoutOption(
                        title="4 x 4 Min Hard / 3 Min Easy",
                        repeat="4 rounds",
                        parts=[
                            SessionPart(
                                title="Hard Repetition",
                                prescription="Run hard at controlled aerobic-power effort.",
                                duration="4 minutes",
                                rpe="8-9",
                            ),
                            SessionPart(
                                title="Easy Recovery",
                                prescription="Jog easily.",
                                duration="3 minutes",
                                rpe="1-3",
                            ),
                        ],
                    )
                ],
            )
        ],
    )


if __name__ == "__main__":
    unittest.main()
