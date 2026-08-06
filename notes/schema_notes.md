# Training Card Schema Notes

These notes explain the current card-class structure and the reasoning behind it.

## Coach Prompt

Before changing schemas or creating cards, consult:

```text
prompts/coach_card_creation_prompt.md
```

The prompt is the coaching standard for this folder. It should guide both the card content and the schema design.

## Class Structure

The schemas use inheritance:

```text
BaseTrainingCard
  MacroCard
  MezzoCard
  MicroCard
  SessionCard
```

`BaseTrainingCard` contains the fields that every card should have:

- identity: `id`, `slug`, `title`, `card_type`
- audience: `suitable_levels`
- preview: `summary`
- coaching purpose: `purpose`
- race/context fit: `goal_race_context`
- load description: `training_profile`
- likely outcomes: `expected_adaptations`
- caution flags: `watchouts`
- progression: `progression_rules`
- regression: `regression_rules`
- overflow context: `additional_information`
- graph links: `references`

`MacroCard`, `MezzoCard`, `MicroCard`, and `SessionCard` inherit the shared base fields and add only the fields that belong at their own planning level.

## Card Levels

The current planning levels are:

- Macro card: a training phase, usually several weeks.
- Mezzo card: a focused block inside a macro phase, usually several weeks.
- Micro card: a week structure inside a mezzo block, usually one week.
- Session card: a specific workout or session pattern inside a micro week.

This structure may change later if real card creation shows that another layer is needed.

## Why These Shared Fields Exist

The shared fields are designed to answer the main coaching questions without overlapping too much:

- `goal_race_context` tells us where the card belongs in the bigger race or preparation picture.
- `training_profile` tells us what kind of stress the card creates.
- `expected_adaptations` tells us what the athlete should gain from it.
- `watchouts` tells us what can go wrong or when it is not a good fit.
- `additional_information` gives us a home for useful extra context that does not fit cleanly anywhere else.

That keeps the cards tight without forcing important coaching detail to disappear.

## Why The Schema Is Kept Lean

Fields should not force repeated writing. The schema deliberately avoids separate fields for ideas that can already be expressed clearly through the shared structure above.

For example:

- `goal_race_context` replaces the old need for a separate `when_to_choose` field.
- `training_profile` replaces separate load, terrain, and stress fields.
- `watchouts` replaces separate `when_not_to_choose`, `common_mistakes`, and `warning_signs` fields.
- `additional_information` replaces the old catch-all detailed description field while keeping the same coaching purpose.

The schema also avoids separate goal/focus fields such as `primary_focus`, `phase_goal`, and `block_goal` because those ideas should usually be clear from `summary`, `purpose`, `training_profile`, and `expected_adaptations`.

## Current Design Rule

Add fields only when they support a real coaching decision, comparison, recommendation, or future Training Platform display.

## App Display Assumption

Cards are expected to support two app views later:

- Preview: quick comparison using concise fields such as title, summary, purpose, suitable levels, and key context.
- Detail view: deeper coaching information such as additional information, race context, training profile, expected adaptations, watchouts, progression, regression, and sequencing.

Card content should be written so the preview is useful without making the detail view repetitive.

## Card References

Cards are stored flat by planning level, but connected through structured references.

```text
cards/
  macro/
  mezzo/
  micro/
  session/
```

Relationships should use `CardReference` instead of loose string lists. This keeps card navigation checkable and reusable when one card fits many places.

```python
CardReference(
    card_id = "mezzo_001",
    relationship = CardRelationship.CHILD,
    tags = ["natural_fit", "low_intensity"],
)
```

Use reference tags for structured context. Put longer explanations in the card content itself.

## Registry

Use `training_cards/registry.py` as the central access point for cards.

It exposes:

- `ALL_CARDS`
- `CARD_BY_ID`
- `get_card`
- `get_cards_by_type`
- `get_cards_by_tag`
- `get_referenced_cards`

## Session Workout Guides

`SessionCard` includes `workout_parts` for TrainingPeaks-style workout guidance.

Each `SessionPart` should describe:

- `name`
- `duration`
- `rpe`
- `instructions`
- `terrain_notes`

RPE uses a 1-10 scale. Durations should usually be adaptable ranges, not overly precise prescriptions.

