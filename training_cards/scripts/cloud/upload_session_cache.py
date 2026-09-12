from training_cards.cloud_store import upload_cached_session_library
from training_cards.google_drive_client import GoogleDriveClient


if __name__ == "__main__":
    upload_cached_session_library(GoogleDriveClient())
    print("Uploaded root metadata and session card files to Google Drive.")
