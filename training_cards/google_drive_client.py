from __future__ import annotations
import os
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

from training_cards.cloud_store import DriveItem


GOOGLE_DRIVE_SCOPES = ["https://www.googleapis.com/auth/drive"]
REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SERVICE_ACCOUNT_FILE = REPO_ROOT / "googleDrive_secrets.json"


# Load service-account credentials using the same pattern as the existing Google jobs.
def get_google_drive_credentials():
    credentials_file = os.getenv("TRAINING_CARDS_GOOGLE_SERVICE_ACCOUNT_FILE") or os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    credentials_path = Path(credentials_file).expanduser() if credentials_file else DEFAULT_SERVICE_ACCOUNT_FILE

    if not credentials_path.exists():
        raise FileNotFoundError(f"Google Drive service-account file not found: {credentials_path}")

    return service_account.Credentials.from_service_account_file(credentials_path, scopes = GOOGLE_DRIVE_SCOPES)


# Build the Google Drive API service used by the training-card cloud client.
def build_drive_service():
    return build("drive", "v3", credentials = get_google_drive_credentials(), cache_discovery = False)


class GoogleDriveClient:
    def __init__(self):
        self.service = build_drive_service()

    # List direct children of one Google Drive folder.
    def list_folder(self, folder_id: str) -> list[DriveItem]:
        response = self.service.files().list(
            q = f"'{folder_id}' in parents and trashed = false",
            fields = "files(id,name,mimeType)",
            pageSize = 1000,
        ).execute()

        return [
            DriveItem(
                id = item["id"],
                title = item["name"],
                file_or_folder = "folder" if item["mimeType"] == "application/vnd.google-apps.folder" else "file",
            )
            for item in response.get("files", [])
        ]

    # Download one Drive file to a local path.
    def download_file(self, file_id: str, output_path: Path) -> None:
        output_path.parent.mkdir(parents = True, exist_ok = True)
        request = self.service.files().get_media(fileId = file_id)

        with output_path.open("wb") as output_file:
            downloader = MediaIoBaseDownload(output_file, request)
            done = False

            while not done:
                _, done = downloader.next_chunk()

    # Upload one local file as a new Drive file.
    def upload_file(self, local_path: Path, folder_id: str, file_name: str, mime_type: str) -> str:
        media = MediaFileUpload(str(local_path), mimetype = mime_type, resumable = False)
        metadata = {"name": file_name, "parents": [folder_id]}
        response = self.service.files().create(
            body = metadata,
            media_body = media,
            fields = "id",
        ).execute()

        return response["id"]

    # Replace the bytes of an existing Drive file while keeping the same Drive file ID.
    def update_file(self, file_id: str, local_path: Path, mime_type: str) -> None:
        media = MediaFileUpload(str(local_path), mimetype = mime_type, resumable = False)
        self.service.files().update(
            fileId = file_id,
            media_body = media,
            fields = "id",
        ).execute()

    # Create a folder under an explicit Drive parent.
    def create_folder(self, folder_name: str, parent_folder_id: str) -> str:
        response = self.service.files().create(
            body={
                "name": folder_name,
                "mimeType": "application/vnd.google-apps.folder",
                "parents": [parent_folder_id],
            },
            fields="id",
        ).execute()
        return response["id"]

    # Return the first parent so a replacement library can be created beside it.
    def get_parent_folder_id(self, file_id: str) -> str | None:
        response = self.service.files().get(fileId=file_id, fields="parents").execute()
        parents = response.get("parents", [])
        if not parents:
            return None
        return parents[0]

    # Permanently remove a Drive file or folder. Folder contents are removed too.
    def delete_file(self, file_id: str) -> None:
        self.service.files().delete(fileId=file_id).execute()

    # Rename a Drive item without changing its ID or parent location.
    def rename_file(self, file_id: str, file_name: str) -> None:
        self.service.files().update(
            fileId=file_id,
            body={"name": file_name},
            fields="id,name",
        ).execute()
