def main() -> None:
    print(
        "\n".join(
            [
                "Existing-card workflow:",
                "1. py -m training_cards.scripts.cloud.download_cloud_library",
                "2. Edit JSON in training_cards/local_cache/cloud_library/",
                "3. py -m training_cards.scripts.cache.validate_cache",
                "4. py -m training_cards.scripts.cache.build_bundle",
                "5. py -m training_cards.scripts.cloud.upload_cache",
                "",
                "Optional helpers:",
                "- py -m training_cards.scripts.cache.add_cards_to_cache path/to/card.json",
                "- py -m training_cards.scripts.cache.remove_cards_from_cache card_id_001",
                "- py -m training_cards.scripts.cache.build_card_library_index",
                "",
                "Use this when changing cards that already exist in Google Drive.",
                "Google Drive JSON remains the source of truth; the local cache is the working copy.",
            ]
        )
    )


if __name__ == "__main__":
    main()
