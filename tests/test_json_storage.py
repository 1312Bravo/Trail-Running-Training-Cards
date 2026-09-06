from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from training_cards.json_store import (
    LIBRARY_BUNDLE_FILE_NAME,
    MACRO_MEZZO_REUSE_FILE_NAME,
    MULTI_PROFILE_CARD_FOLDER,
    card_storage_path,
    export_card_library_to_json,
    load_card_library_from_json,
    load_macro_mezzo_reuse_config,
    read_json,
)
from training_cards.philosophy_profiles import CTS, LYDIARD, MAINSTREAM_ENDURANCE
from training_cards.schemas import CardType, MacroCard, TrainingLevel


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
            self.assertEqual(
                0,
                load_macro_mezzo_reuse_config(output_dir)["entry_count"],
            )
            self.assertIn(
                "macro_mezzo_reuse",
                read_json(output_dir / LIBRARY_BUNDLE_FILE_NAME),
            )

            loaded_cards = load_card_library_from_json(output_dir)

        self.assertEqual(["macro_001", "macro_002"], [card.id for card in loaded_cards])


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


if __name__ == "__main__":
    unittest.main()
