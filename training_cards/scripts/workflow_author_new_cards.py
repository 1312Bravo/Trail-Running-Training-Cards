def main() -> None:
    print(
        "\n".join(
            [
                "New-card authoring workflow:",
                "1. Use training_cards/cards/examples/ as the class-based authoring reference.",
                "2. Create temporary Python authoring code only when it helps build or validate new cards.",
                "3. Convert the authored cards to JSON in training_cards/local_cache/cloud_library/.",
                "4. py -m training_cards.scripts.validate_cache",
                "5. py -m training_cards.scripts.build_bundle",
                "6. Upload the relevant cache files with the normal upload scripts.",
                "",
                "For existing cloud cards that need Python editing:",
                "1. py -m training_cards.scripts.download_cloud_library",
                "2. py -m training_cards.scripts.template_cloud_json_to_python_card --card-id <card_id>",
                "3. Edit the generated temporary Python file.",
                "4. Import AUTHORED_CARD from that file in a targeted helper.",
                "",
                "After upload and Drive readback validation, keep only reusable examples or deliberate tooling.",
                "Do not keep a full duplicate Python seed library beside the Drive JSON library.",
            ]
        )
    )


if __name__ == "__main__":
    main()
