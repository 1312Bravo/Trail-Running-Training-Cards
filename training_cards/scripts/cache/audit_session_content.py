from __future__ import annotations

import math
import re

from training_cards.cloud_store import load_cached_cloud_library
from training_cards.schemas import CardType


# Calculate the envelope of the actual written parts, including repeated recovery.
def duration_range(text: str) -> tuple[float, float]:
    if not text:
        return 0, 0
    match = re.match(r"^(\d+(?:\.\d+)?)(?:-(\d+(?:\.\d+)?))?\s*(seconds?|minutes?|hours?)", text)
    if not match:
        raise ValueError(f"Duration needs manual review: {text}")
    scale = 1 / 60 if match[3].startswith("second") else 60 if match[3].startswith("hour") else 1
    return float(match[1]) * scale, float(match[2] or match[1]) * scale


def workout_duration(card) -> tuple[int, int]:
    total_low = total_high = 0
    for block in card.workout_blocks:
        if block.block_type == "notes":
            continue
        ranges = []
        for option in block.options:
            low = high = 0
            for part in option.parts:
                part_low, part_high = duration_range(part.duration)
                low += part_low
                high += part_high
            if option.repeat:
                repeat = re.fullmatch(r"(\d+)(?:-(\d+))? rounds", option.repeat)
                if not repeat:
                    raise ValueError(f"Repeat needs manual review: {option.repeat}")
                low *= int(repeat[1])
                high *= int(repeat[2] or repeat[1])
            ranges.append((low, high))
        if block.execution_mode == "choose_one":
            total_low += min(value[0] for value in ranges)
            total_high += max(value[1] for value in ranges)
        else:
            total_high += sum(value[1] for value in ranges)
            if block.execution_mode != "optional":
                total_low += sum(value[0] for value in ranges)
    return math.floor(total_low), math.ceil(total_high)


# Audit standalone selection and execution details beyond the schema's basic checks.
def main() -> None:
    sessions = [card for card in load_cached_cloud_library() if card.card_type == CardType.SESSION]
    errors = []
    for card in sessions:
        if len(card.goal_race_context) < 2 or any("matches the selected" in value for value in card.goal_race_context):
            errors.append(f"{card.id}: needs actual placement and entry requirements")
        if not card.workout_blocks or not any(block.block_type == "main" for block in card.workout_blocks):
            errors.append(f"{card.id}: needs a main workout block")
        for block in card.workout_blocks:
            for option in block.options:
                if block.block_type == "main" and not option.selection_notes.strip():
                    errors.append(f"{card.id}/{option.title}: needs option selection guidance")
                if any(part.title == "Preparatory Pickups" for part in option.parts) and block.execution_mode != "optional":
                    errors.append(f"{card.id}: conditional pickups must be optional")
        try:
            low, high = workout_duration(card)
            expected = f"{low}-{high} minutes" if high else "No structured exercise"
            if card.typical_duration != expected:
                errors.append(f"{card.id}: duration is {card.typical_duration}, written blocks total {expected}")
        except ValueError as error:
            errors.append(f"{card.id}: {error}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Audited {len(sessions)} sessions: placement, entry requirements, main option selection, optional preparation, and duration envelopes agree.")


if __name__ == "__main__":
    main()
