from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

# ----------------------------------------------------------
# Cloud Library Location
# ----------------------------------------------------------
# These IDs point to the verified replacement Google Drive JSON library.

PACKAGE_ROOT = Path(__file__).resolve().parent
DEFAULT_LOCAL_CACHE_DIR = PACKAGE_ROOT / "local_cache" / "cloud_library"


@dataclass(frozen=True, slots=True)
class GoogleDriveLibraryConfig:
    library_name: str
    root_folder_id: str
    root_folder_url: str
    cards_folder_id: str
    macro_folder_id: str
    mezzo_folder_id: str
    micro_folder_id: str
    session_folder_id: str
    local_cache_dir: Path = DEFAULT_LOCAL_CACHE_DIR

    @property
    def card_type_folder_ids(self) -> dict[str, str]:
        return {
            "macro": self.macro_folder_id,
            "mezzo": self.mezzo_folder_id,
            "micro": self.micro_folder_id,
            "session": self.session_folder_id,
        }


GOOGLE_DRIVE_LIBRARY = GoogleDriveLibraryConfig(
    library_name = "training_cards_library",
    root_folder_id = "1Y7lXD-wr3kQH9QVbsi_nrkK9ihDrKKPV",
    root_folder_url = "https://drive.google.com/drive/folders/1Y7lXD-wr3kQH9QVbsi_nrkK9ihDrKKPV",
    cards_folder_id = "1QrIiVVeC8JjH-tKNGcYu3WoaY8kxI5aQ",
    macro_folder_id = "1vH4gK24aPDoVtcHo4OCfLHfs3Pe2xcCb",
    mezzo_folder_id = "1WUyxrzpaPR8DBQaRMPiTEFoWgyRIAbV8",
    micro_folder_id = "1QK7BJ6Ss31qLv-1i17iavl9HpXFILlyx",
    session_folder_id = "11GMo7Dzo1_MzkkA32tV9iqQcnNJKSYl-",
)

CARD_TYPE_FOLDER_IDS = GOOGLE_DRIVE_LIBRARY.card_type_folder_ids
