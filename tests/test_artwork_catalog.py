from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from streamlit_app.artwork import (
    artwork_for_card,
    clear_artwork_catalog_cache,
    fallback_artwork,
    load_artwork_catalog,
)


class ArtworkCatalogTests(unittest.TestCase):
    def tearDown(self) -> None:
        clear_artwork_catalog_cache()

    def test_loads_valid_catalog_entry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            art_root = Path(directory)
            asset_path = art_root / "assets" / "macro_001.svg"
            asset_path.parent.mkdir()
            asset_path.write_text("<svg />", encoding="utf-8")
            catalog_path = art_root / "catalog.json"
            catalog_path.write_text(
                json.dumps(
                    {
                        "macro_001": {
                            "level": "macro",
                            "asset_path": "assets/macro_001.svg",
                            "alt_text": "Macro avatar",
                            "tags": ["pilot", "ibex"],
                        }
                    }
                ),
                encoding="utf-8",
            )

            catalog = load_artwork_catalog(catalog_path)

            self.assertEqual(["macro_001"], list(catalog))
            self.assertEqual("macro", catalog["macro_001"].level)
            self.assertEqual(asset_path.resolve(), catalog["macro_001"].asset_path)
            self.assertEqual("Macro avatar", catalog["macro_001"].alt_text)
            self.assertEqual(("pilot", "ibex"), catalog["macro_001"].tags)

    def test_missing_or_invalid_catalog_returns_empty_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            missing_catalog = Path(directory) / "missing.json"

            self.assertEqual({}, load_artwork_catalog(missing_catalog))

    def test_skips_entries_with_paths_outside_art_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            art_root = Path(directory) / "art_work"
            outside = Path(directory) / "outside.svg"
            art_root.mkdir()
            outside.write_text("<svg />", encoding="utf-8")
            catalog_path = art_root / "catalog.json"
            catalog_path.write_text(
                json.dumps(
                    {
                        "macro_001": {
                            "level": "macro",
                            "asset_path": "../outside.svg",
                            "alt_text": "Outside avatar",
                            "tags": [],
                        }
                    }
                ),
                encoding="utf-8",
            )

            self.assertEqual({}, load_artwork_catalog(catalog_path))

    def test_skips_entries_with_missing_assets(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            art_root = Path(directory)
            catalog_path = art_root / "catalog.json"
            catalog_path.write_text(
                json.dumps(
                    {
                        "macro_001": {
                            "level": "macro",
                            "asset_path": "assets/missing.svg",
                            "alt_text": "Missing avatar",
                            "tags": ["pilot"],
                        }
                    }
                ),
                encoding="utf-8",
            )

            self.assertEqual({}, load_artwork_catalog(catalog_path))

    def test_artwork_lookup_can_distinguish_missing_entry_from_fallback(self) -> None:
        catalog_entry = artwork_for_card("not_in_catalog", use_fallback=False)
        fallback_entry = artwork_for_card("not_in_catalog")

        self.assertIsNone(catalog_entry)
        self.assertIsNotNone(fallback_entry)
        self.assertTrue(fallback_entry.is_fallback)
        self.assertEqual("fallback", fallback_entry.level)

    def test_artwork_lookup_can_use_level_specific_fallback(self) -> None:
        fallback_entry = artwork_for_card("not_in_catalog", fallback_level="session")

        self.assertIsNotNone(fallback_entry)
        self.assertTrue(fallback_entry.is_fallback)
        self.assertEqual("session", fallback_entry.level)
        self.assertEqual("fallback_session.svg", fallback_entry.asset_path.name)
        self.assertIn("session", fallback_entry.tags)

    def test_fallback_asset_must_stay_inside_art_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            outside = Path(directory) / "outside.svg"
            outside.write_text("<svg />", encoding="utf-8")

            self.assertIsNone(fallback_artwork(outside))


if __name__ == "__main__":
    unittest.main()
