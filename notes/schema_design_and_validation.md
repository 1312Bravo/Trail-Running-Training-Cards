# Schema Design And Validation

These notes explain the current card-class structure, reference model, validation behavior, and reasoning behind them.

## Coach Prompt

Before changing schemas or creating cards, consult:

```text
coaching/coach_card_creation_prompt.md
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

`SessionFamily` is a separate object used by `SessionCard` to define the reusable workout-family taxonomy. This keeps family labels searchable and consistent without turning them into a full training card.

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

## Pathway Index And Relaxed Validation

`training_cards/pathway.py` turns the flat card list into a reusable pathway index for macro -> mezzo -> micro -> session browsing.

The index is intentionally not a separate source of truth. It only reads the existing `references` fields from the JSON-backed card objects.

Current pathway behavior:

- child links can be found from explicit `child` references on a parent card
- child links can also be inferred from matching `parent` references on the child card
- parent lookup works in the opposite direction for the same reason
- cards are sorted by planning level and title for stable app display

Validation is deliberately relaxed about coverage, but strict about hierarchy meaning:

- broken references are errors
- hierarchy jumps are errors for `parent` and `child` references
- duplicate references and self-references are warnings
- orphan cards are allowed because the library is still growing
- cards do not need to be connected both above and below to be valid

Use `training_cards/scripts/validate_cache.py` for the normal quick cache validation. It should fail only when the cached library has real errors.

Use `training_cards/scripts/report_reachability.py` when we want to inspect pathway coverage. It reports card counts, reference warnings, macro reachability, and orphan cards without treating incomplete coverage as a failure.

Publish/export flows also run pathway validation automatically:

- seed-card export validates before writing the local cache
- cache upload validates before rebuilding the bundle and uploading to Google Drive
- the Streamlit app can still read the current cache while we are cleaning pathway issues

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

## Session Family Objects

`SessionFamily` should be treated as its own definition object, not as a plain text label.

It is useful when we want:

- stable family identities
- easier search and filtering
- clearer definitions for repeated workout families
- a place for family-level summary and description text

The session card should point to the family object directly, so the family can be reused across many sessions without copying the meaning into every card.
