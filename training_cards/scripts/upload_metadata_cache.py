from training_cards.cloud_store import upload_cached_root_metadata
from training_cards.google_drive_client import GoogleDriveClient


if __name__ == "__main__":
    upload_cached_root_metadata(GoogleDriveClient())
    print("Uploaded root metadata files to Google Drive.")
