from training_cards.cloud_store import load_cached_cloud_library
from training_cards.pathway import build_pathway_index


def main() -> None:
    cards = load_cached_cloud_library()
    issues = build_pathway_index(cards).validate_relaxed()
    errors = [issue for issue in issues if issue.severity == "error"]
    warnings = [issue for issue in issues if issue.severity == "warning"]

    if errors:
        print("Pathway reference errors:")
        for issue in errors:
            print(f"- {issue.card_id}: {issue.message}")
        raise SystemExit(1)

    warning_note = ""
    if warnings:
        warning_note = f" ({len(warnings)} non-blocking pathway warnings)"

    print(f"Validated cached training-card library: {len(cards)} cards{warning_note}")


if __name__ == "__main__":
    main()
