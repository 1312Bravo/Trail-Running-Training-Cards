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
    cards_folder_id = "1l2GNAN348_Q3kXnCVOUZHoHxpEbpPeKv",
    macro_folder_id = "18IABJtzFkQdzaZFcAa1ulVriSgCv0Zr0",
    mezzo_folder_id = "1gQbOltntSbLD4Geapz8VIifJ63QHZg_w",
    micro_folder_id = "14uD_WS3RosZeQ8HRP6xOvBDA41lVi16N",
    session_folder_id = "1NuzKGJSHSis0jNQkPUhsLenfp00fjlV2",
)

CARD_TYPE_FOLDER_IDS = GOOGLE_DRIVE_LIBRARY.card_type_folder_ids
