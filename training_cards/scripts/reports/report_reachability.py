from __future__ import annotations

from collections import Counter
from typing import Any

from training_cards.cloud_store import load_cached_cloud_library
from training_cards.pathway import build_pathway_index


def main() -> None:
    cards = load_cached_cloud_library()
    index = build_pathway_index(cards)
    issues = index.validate_relaxed()
    orphan_cards = index.orphan_cards()

    print("Training card reachability report")
    print("")
    _print_counts(cards)
    _print_issues(issues)
    _print_macro_reachability(index.reachability_from_macros())
    _print_orphans(orphan_cards)


def _print_counts(cards: list[Any]) -> None:
    counts = Counter(str(card.card_type) for card in cards)

    print("Card counts")
    print(f"- all: {len(cards)}")
    for card_type in ("macro", "mezzo", "micro", "session"):
        print(f"- {card_type}: {counts[card_type]}")
    print("")


def _print_issues(issues: list[Any]) -> None:
    if not issues:
        print("Pathway reference validation")
        print("- no relaxed reference issues found")
        print("")
        return

    errors = [issue for issue in issues if issue.severity == "error"]
    warnings = [issue for issue in issues if issue.severity == "warning"]

    print("Pathway reference validation")
    print(f"- errors: {len(errors)}")
    print(f"- warnings: {len(warnings)}")

    for issue in errors + warnings:
        print(f"- {issue.severity}: {issue.card_id}: {issue.message}")
    print("")


def _print_macro_reachability(summaries: list[Any]) -> None:
    print("Macro reachability")

    if not summaries:
        print("- no macro cards found")
        print("")
        return

    for summary in summaries:
        print(
            f"- {summary.macro_title} ({summary.macro_id}): "
            f"{summary.mezzo_count} mezzo, "
            f"{summary.micro_count} micro, "
            f"{summary.session_count} session"
        )
        if summary.dead_end_mezzo_ids:
            print(f"  dead-end mezzo: {', '.join(summary.dead_end_mezzo_ids)}")
        if summary.dead_end_micro_ids:
            print(f"  dead-end micro: {', '.join(summary.dead_end_micro_ids)}")
    print("")


def _print_orphans(orphan_cards: list[Any]) -> None:
    print("Orphan cards")
    print(f"- count: {len(orphan_cards)}")

    for card in orphan_cards:
        print(f"- {card.id}: {card.title}")


if __name__ == "__main__":
    main()
