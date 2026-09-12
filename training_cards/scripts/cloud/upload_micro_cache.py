from training_cards.cloud_store import upload_cached_micro_library
from training_cards.google_drive_client import GoogleDriveClient


if __name__ == "__main__":
    upload_cached_micro_library(GoogleDriveClient())
    print("Uploaded root metadata and micro card files to Google Drive.")
