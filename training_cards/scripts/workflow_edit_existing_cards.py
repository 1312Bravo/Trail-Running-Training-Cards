def main() -> None:
    print(
        "\n".join(
            [
                "Existing-card workflow:",
                "1. py -m training_cards.scripts.download_cloud_library",
                "2. Edit JSON in training_cards/local_cache/cloud_library/",
                "3. py -m training_cards.scripts.validate_cache",
                "4. py -m training_cards.scripts.build_bundle",
                "5. py -m training_cards.scripts.upload_cache",
                "",
                "Use this when changing cards that already exist in Google Drive.",
                "Google Drive JSON remains the source of truth; the local cache is the working copy.",
            ]
        )
    )


if __name__ == "__main__":
    main()
