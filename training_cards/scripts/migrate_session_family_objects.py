from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SESSION_DIR = REPO_ROOT / "training_cards" / "cards" / "session"

FAMILY_IMPORTS = {
    "aerobic_power_intervals.py": "AEROBIC_POWER_SESSION_FAMILY",
    "downhill_conditioning_run.py": "TRAIL_SPECIFIC_SESSION_FAMILY",
    "easy_run.py": "EASY_SESSION_FAMILY",
    "hiking_or_power_hiking_practice.py": "TRAIL_SPECIFIC_SESSION_FAMILY",
    "long_run.py": "ENDURANCE_SESSION_FAMILY",
    "progression_run.py": "CONTROLLED_QUALITY_SESSION_FAMILY",
    "race_simulation_run.py": "RACE_PRACTICE_SESSION_FAMILY",
    "recovery_run.py": "RECOVERY_SESSION_FAMILY",
    "short_hill_repeats.py": "HILL_POWER_SESSION_FAMILY",
    "steady_run.py": "STEADY_SESSION_FAMILY",
    "strength_endurance_hills.py": "STRENGTH_ENDURANCE_SESSION_FAMILY",
    "strides.py": "NEUROMUSCULAR_SESSION_FAMILY",
    "tempo_run.py": "THRESHOLD_SESSION_FAMILY",
    "threshold_intervals.py": "THRESHOLD_SESSION_FAMILY",
}

FAMILY_VALUES = {
    "aerobic_power_intervals.py": "aerobic_power",
    "downhill_conditioning_run.py": "trail_specific",
    "easy_run.py": "easy",
    "hiking_or_power_hiking_practice.py": "trail_specific",
    "long_run.py": "endurance",
    "progression_run.py": "controlled_quality",
    "race_simulation_run.py": "race_practice",
    "recovery_run.py": "recovery",
    "short_hill_repeats.py": "hill_power",
    "steady_run.py": "steady",
    "strength_endurance_hills.py": "strength_endurance",
    "strides.py": "neuromuscular",
    "tempo_run.py": "threshold",
    "threshold_intervals.py": "threshold",
}


def transform_file(path: Path, family_import: str, family_value: str) -> bool:
    source = path.read_text(encoding="utf-8")
    updated = source

    import_line = f"from training_cards.session_families import {family_import}"
    if import_line not in updated:
        marker = "from training_cards.schemas import CardRelationship, CardReference, CardType, SessionCard, SessionPart, TrainingLevel\n"
        replacement = marker + import_line + "\n"
        if marker not in updated:
            raise ValueError(f"Expected schema import line in {path.name}")
        updated = updated.replace(marker, replacement, 1)

    updated = updated.replace(f"session_family = '{family_value}'", f"session_family = {family_import}")

    if updated != source:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = []
    for filename, family_import in FAMILY_IMPORTS.items():
        path = SESSION_DIR / filename
        if transform_file(path, family_import, FAMILY_VALUES[filename]):
            changed.append(filename)

    print(f"Updated {len(changed)} session card files.")
    for filename in changed:
        print(f"training_cards/cards/session/{filename}")


if __name__ == "__main__":
    main()
