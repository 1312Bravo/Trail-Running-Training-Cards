from training_cards.cloud_store import upload_cached_mezzo_library
from training_cards.google_drive_client import GoogleDriveClient


if __name__ == "__main__":
    upload_cached_mezzo_library(GoogleDriveClient())
    print("Uploaded root metadata and mezzo card files to Google Drive.")
