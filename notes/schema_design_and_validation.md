# Schema Design And Validation

These notes explain the current card-class structure, reference model, validation behavior, and reasoning behind them. Keep cloud upload/download workflow in `cloud_library_storage_workflow.md`, full Drive replacement safeguards in `card_library_rebuild_workflow.md`, and card taxonomy decisions in `training_cards/cards/card_matrix.md`.

## Coaching Guidance

Before changing schemas or creating cards, consult:

```text
coaching/coaching_foundation.md
coaching/card_authoring_guidance.md
coaching/philosophies/<profile>/philosophy.md
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
- coaching-philosophy provenance: `philosophy_profile_ids`
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

## Coaching Philosophy Profile IDs

`philosophy_profile_ids` records which coaching philosophy profiles materially shaped a card. It is a list because a card can draw from more than one profile.

- Use only real training-method profile IDs.
- The shared coaching foundation applies to every card, but it is not card-level provenance.
- Do not use `common`; it is not a valid philosophy profile.
- Use the philosophy directory name under `coaching/philosophies/` exactly.
- The allowed IDs and their display names are defined once in `training_cards/philosophy_profiles.py` and enforced when cards are created or loaded.
- The field is visible in the card preview and detail view, searchable, and available as a Browse-mode filter.

`SessionFamily` is a separate object used by `SessionCard` to define the reusable workout-family taxonomy. This keeps family labels searchable and consistent without turning them into a full training card.

## Card Levels

The current planning levels are:

- Macro card: a training phase, usually several weeks.
- Mezzo card: a focused block inside a macro phase, usually several weeks.
- Micro card: a week structure inside a mezzo block, usually one week.
- Session card: a specific workout or session pattern inside a micro week.

This structure may change later if real card creation shows that another layer is needed.

## Card Library Index

`card_library_index.json` is app-facing browse metadata generated from the validated card cache plus the reuse maps. It is not a separate content source.

The index groups cards by planning level and philosophy profile:

- `source = "direct"` means the card is owned by that philosophy profile through `philosophy_profile_ids`.
- `source = "reused"` means the card is shown under that philosophy profile through an explicit reuse map.
- `source_profile` is included only for reused entries and tells the app which profile owns the reused card, usually `mainstream_endurance`.

The app can use this file for a compact card-library page: title, short description, and whether an item is direct or reused from another profile. The full card JSON remains the detail source.

## How To Read The Schema Classes

The classes in `training_cards.schemas` are not mainly about behavior. They are definitions.

Each class says:

- what a valid card looks like
- what fields it can have
- which fields belong to all cards
- which fields only belong to one card level

In that sense, each class is more like a schema or contract than a traditional object with many methods.

## How To Read Field Definitions

A line like this:

```python
title: str
```

is a type-annotated field definition. In a dataclass, that is the normal way to define data.

It means:

- this field exists
- its intended type is `str`
- it will be part of the object when the dataclass is created

The annotation alone does not enforce everything. The dataclass and validation code make the shape useful in practice.

## Required And Optional Fields

In a dataclass, a field is usually required if it has no default value.

Example:

```python
id: str
summary: str
tags: list[str] = field(default_factory=list)
```

Here:

- `id` is required
- `summary` is required
- `tags` is optional, because it gets an automatic empty list if nothing is provided

So the rule is simple:

- no default means the caller must supply a value
- a default means the object can be created without supplying that value

`field(default_factory=list)` is used for list fields so each object gets its own fresh list. Without it, multiple objects could accidentally share the same mutable list.

## Current Required Fields

For the current design, the important required fields in `BaseTrainingCard` are:

- `id`
- `slug`
- `title`
- `card_type`
- `suitable_levels`
- `summary`
- `purpose`

Those fields make a card identifiable and meaningful.

The other base fields are optional because they add useful coaching detail but are not needed to recognize the card:

- `tags`
- `goal_race_context`
- `training_profile`
- `expected_adaptations`
- `watchouts`
- `progression_rules`
- `regression_rules`
- `additional_information`
- `references`

For level-specific classes:

- `MacroCard` requires the base fields and `card_type = macro`; `recommended_duration_weeks` and `timing_guidance` can stay optional.
- `MezzoCard` requires the base fields and `card_type = mezzo`; `recommended_duration_weeks` and `placement_guidance` can stay optional.
- `MicroCard` requires the base fields and `card_type = micro`; week structure, key sessions, load pattern, placement guidance, and recovery requirements can stay optional.
- `SessionCard` requires the base fields, `card_type = session`, and `session_family`; `typical_duration` and `workout_blocks` can stay optional.
- `SessionFamily` requires `id`, `slug`, `title`, and `summary`; `description` and `tags` can stay optional.
- `WorkoutBlock` requires a controlled `block_type`, a controlled `execution_mode`, and at least one `WorkoutOption`.
- `WorkoutOption` requires a `title` and at least one `SessionPart`; `repeat`, `selection_notes`, and `load_notes` can stay optional.
- `SessionPart` requires `title`; `prescription`, `duration`, `rpe`, `selection_notes`, `coaching_notes`, `terrain_notes`, and `adjustment_notes` can stay optional.

## Validation Hooks

`__post_init__()` runs right after a dataclass object is created. It is the place where the class checks that the data is actually valid, not just typed correctly.

In this project, `__post_init__()` rejects cards that are missing the minimum fields needed to identify, display, or understand them. The pattern is:

- the dataclass defines the shape
- `__post_init__()` checks that the shape is usable

## Controlled Values

Predetermined values are useful when a field should have a controlled meaning rather than arbitrary wording.

Good places for controlled values:

- `card_type`
- `suitable_levels`
- `relationship` in `CardReference`
- `block_type` in `WorkoutBlock`
- `execution_mode` in `WorkoutBlock`

Good candidates for future controlled values:

- `session_family` values through the family object
- `load_pattern`
- repeated sub-fields if the library starts using the same phrases too often

Do not turn descriptive coaching fields into fixed vocabularies too early. Fields like `summary`, `purpose`, and `additional_information` should stay flexible because they are coach-language fields, not code labels.

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

## Relationship Contract

The `relationship` value has strict structural meaning:

- `parent` and `child` must connect exactly adjacent planning levels.
- `previous`, `next`, and `alternative` must connect cards at the same planning level.
- `support` may connect any levels, but it must not be interpreted as a pathway parent or child.

For `support`, read `source -> target` as: the target materially supports or contextualises the source. Tags explain the reason for a link but do not change the controlled relationship value.

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

Use `training_cards/scripts/cache/validate_cache.py` for the normal quick cache validation. It should fail only when the cached library has real errors.

Use `training_cards/scripts/reports/report_reachability.py` when we want to inspect pathway coverage. It reports card counts, reference warnings, macro reachability, and orphan cards without treating incomplete coverage as a failure.

Publish/export flows also run pathway validation automatically:

- cache export and upload tooling validates before writing or publishing card JSON
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

`SessionCard` includes `workout_blocks` for structured workout guidance.

The workout guide has three nested concepts:

- `WorkoutBlock`: the section of the workout, such as warm-up, main set, recovery, cooldown, optional add-on, or notes.
- `WorkoutOption`: one complete required, optional, or selectable prescription inside that block.
- `SessionPart`: the concrete work inside an option.

Each `SessionPart` can describe:

- `title`
- `prescription`
- `duration`
- `rpe`
- `selection_notes`
- `coaching_notes`
- `terrain_notes`
- `adjustment_notes`

RPE uses a 1-10 scale. Durations should usually be adaptable ranges, not overly precise prescriptions.

`WorkoutBlock.execution_mode` tells the app how to interpret the options: `DO_ALL` means the options are performed together, `CHOOSE_ONE` means the coach or athlete selects one option, and `OPTIONAL` means the option is an add-on. `WorkoutOption.repeat` is mechanical and should be used only when the option's parts repeat as rounds or sets.

## Session Family Objects

`SessionFamily` should be treated as its own definition object, not as a plain text label.

It is useful when we want:

- stable family identities
- easier search and filtering
- clearer definitions for repeated workout families
- a place for family-level summary and description text

The session card should point to the family object directly, so the family can be reused across many sessions without copying the meaning into every card.
