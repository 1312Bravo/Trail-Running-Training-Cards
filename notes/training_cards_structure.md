bou# Training Cards Structure

This note explains the thinking behind the current training-card architecture, especially for use in a blog post or project overview.

## Big Idea

The card library is organized like a coaching hierarchy:

- `macro` = the big phase
- `mezzo` = the focused block
- `micro` = the week
- `session` = the workout

That mirrors how coaches usually think about training. We do not start with workouts in isolation. We start with the athlete's bigger goal, then move down into blocks, weeks, and finally sessions.

The code follows that same structure so the library can answer two questions at once:

1. What is this card?
2. Where does it fit in the wider training plan?

## Why Use Classes

Classes are a good fit here because the cards share a common shape, but each planning level also needs a few fields of its own.

The shared fields live in `BaseTrainingCard`:

- identity fields like `id`, `slug`, and `title`
- display fields like `summary` and `purpose`
- coaching fields like `when_to_choose`, `when_not_to_choose`, `expected_adaptations`, and `warning_signs`
- navigation fields like `references`

Then each card type adds only what it needs:

- `MacroCard`
- `MezzoCard`
- `MicroCard`
- `SessionCard`

This keeps the model consistent without forcing every card to carry every possible field.

## The Class Logic

### `BaseTrainingCard`

`BaseTrainingCard` is the shared foundation.

It captures the fields that every card should have regardless of level:

```python
@dataclass(slots=True)
class BaseTrainingCard:
    id: str
    slug: str
    title: str
    card_type: CardType
    suitable_levels: list[TrainingLevel]
    summary: str
    purpose: str
```

It also includes the detailed coaching and comparison fields used by the app and by future filtering/recommendation logic.

The `__post_init__` validation is intentionally light:

- a card must be identifiable
- it must have a title
- it must have a summary and purpose
- it must be usable at at least one training level

That is enough to prevent broken cards without making the schema rigid.

### `MacroCard`

`MacroCard` is for the biggest planning layer.

It adds:

- `recommended_duration_weeks`
- `timing_guidance`

That makes sense because a macro phase needs broad timing context, not session-level detail.

### `MezzoCard`

`MezzoCard` represents a focused block inside a macro phase.

It adds:

- `recommended_duration_weeks`
- `placement_guidance`

This is the place for guidance like "best after a stable base phase" or "avoid if fatigue is already high."

### `MicroCard`

`MicroCard` is the week-level structure.

It adds:

- `recommended_duration_days`
- `week_structure`
- `key_sessions`
- `load_pattern`
- `placement_guidance`
- `recovery_requirements`

This is where the plan becomes operational. The card can describe how the week is arranged, how hard it feels, and what kind of recovery it needs.

### `SessionCard`

`SessionCard` is the most detailed workout level.

It adds:

- `session_family`
- `typical_duration`
- `workout_parts`
- `intensity_guidance`
- `execution_notes`
- `recovery_requirements`

This is the best place for precise workout structure because the card is now describing one repeatable training session rather than a whole phase.

### `SessionPart`

`SessionPart` breaks a workout into readable components:

- warm-up
- main set
- recoveries
- cooldown

Each part has:

- `name`
- `duration`
- `rpe`
- `instructions`
- `terrain_notes`

This is helpful because a session is easier to understand and export when it is split into named parts instead of being one long block of text.

## Why This Is A Good Design

This structure works well because it balances flexibility and consistency.

### Benefits

- Shared fields stay consistent across all card types.
- Each planning level only gets the fields it really needs.
- Cards are easier to validate because they have a known shape.
- The app can filter, display, and compare cards more reliably.
- References between cards stay structured instead of becoming loose text links.

### Why The Flat File Layout Matters

Cards are stored in folders by type, but they are not deeply nested by training hierarchy.

That means:

- files are easy to find
- cards can be reused in multiple places
- one session can support many weeks
- one micro week can support many blocks

The hierarchy lives in the data, not in the folder tree.

## Is This The Most Common Way

Yes, this is a very common Python pattern.

The combination of:

- dataclasses
- inheritance
- enums
- lightweight validation

is a standard way to model structured domain data when different object types share a common core.

It is especially common when:

- the objects are read from JSON
- the data needs validation
- the objects will later be filtered or serialized
- there is a shared base shape plus a few type-specific extensions

## How The Code Actually Works

If you want to understand the repository as code, not just as concept, think about it as a pipeline:

1. JSON files store the card content.
2. `card_from_dict()` turns JSON into the right dataclass.
3. The dataclass validates the data in `__post_init__()`.
4. `registry.py` loads the full library into memory.
5. The app and export tools read from those validated Python objects.

That flow is what makes the whole design useful.

### 1. JSON Is The Storage Format

The cards are saved as JSON because JSON is portable, easy to diff, and easy to sync with Google Drive.

That means the source data stays simple:

- it can be edited outside Python
- it can be exported and reloaded
- it can be checked for consistency
- it does not depend on Python object state

### 2. `card_from_dict()` Chooses The Right Class

The loader does not guess. It reads `card_type`, converts it into the `CardType` enum, and then picks the matching class:

```python
card_class = CARD_CLASS_BY_TYPE[card_type]
return card_class(**card_data)
```

This is important because the JSON file does not need to know Python internals. It only needs to say:

- I am a `macro`
- I am a `micro`
- I am a `session`

Then the code selects the right model for that card.

### 3. Enums Protect Meaning

Enums are used because they keep important values from drifting into random strings.

For example:

- `CardType.MACRO`
- `CardType.MEZZO`
- `CardType.MICRO`
- `CardType.SESSION`

and:

- `TrainingLevel.BEGINNER`
- `TrainingLevel.INTERMEDIATE`
- `TrainingLevel.ADVANCED`
- `TrainingLevel.ELITE`

This matters because the code is not just storing words. It is storing meaning. Enums make the meaning explicit and reduce the chance of typos or inconsistent labels.

### 4. `__post_init__()` Is The Guardrail

The dataclasses use `__post_init__()` for a simple but useful reason: the object is only allowed to exist if it is valid enough to use.

For example, `BaseTrainingCard` refuses to accept:

- an empty `id`
- an empty `slug`
- an empty `title`
- no training levels
- an empty `summary`
- an empty `purpose`

Then each subclass checks that it was created with the correct `card_type`.

That gives us a clean rule:

> The object should fail early if it cannot be trusted.

This is much better than letting broken data travel deeper into the system.

### 5. `slots=True` Keeps The Objects Tight

The dataclasses use `slots=True`.

That means the object layout is more explicit and avoids accidental dynamic attributes. In practice, that helps keep the model disciplined:

- you can only use defined fields
- the objects stay predictable
- the class is less likely to become a dumping ground for random data

### 6. `asdict()` Makes Serialization Easy

When writing cards back to JSON, `card_to_dict()` starts with `asdict(card)`.

That is useful because the dataclass already knows its fields. The serializer does not need to manually copy every attribute from every card type.

Then the code fixes the few places that need special handling:

- `CardType` becomes a plain string
- `TrainingLevel` values become strings
- `CardReference` objects become JSON-safe dictionaries
- `SessionPart` objects become JSON-safe dictionaries

So the pattern is:

> dataclass for structure, serializer for format, JSON for storage.

## How To Think About Writing A New Card

When you create a new card, the main question is not "what fields can I add?" The main question is:

> What decision does this card help a coach make?

Then work outward from that.

### A Good Mental Checklist

- What level is this card?
- What problem does it solve?
- What athlete or context is it for?
- What does success look like?
- What are the risks?
- What would make it too aggressive?
- What should come before or after it?

If the card is a `SessionCard`, add the workout parts. If it is a `MicroCard`, describe the week structure. If it is a `MacroCard`, stay at the phase level and do not force week-level detail into it.

That is the main design rule of the code: each layer should carry the detail that belongs to its own planning scale.

## Why This Feels Clean In Practice

The code is readable because it separates concerns:

- schema files define what a card is
- serialization handles conversion
- the registry loads the active library
- JSON holds the source content

So when you are working in the repo, you do not have to mentally juggle everything at once.

If a card is wrong, you look at the schema.
If JSON loading is wrong, you look at serialization or the store.
If library selection is wrong, you look at the registry.

That separation is one of the biggest reasons this structure scales well.

## Short Teaching Version

If I were explaining it very simply, I would say:

> We used classes because the cards all share a common backbone, but each planning level needs different detail. The base class gives every card the same core identity and coaching fields. The subclasses add only the fields that belong at that scale. Enums keep the values controlled, `__post_init__()` blocks bad data early, and the serializer converts the objects cleanly back to JSON. That gives us a model that is strict enough to trust but flexible enough to write with.

## Could We Add More Structure Inside The Classes

Yes, absolutely.

That would make sense if the library starts needing tighter control over repeated sub-shapes.

### Good Candidates For More Structure

- `SessionPart` already does this well for workouts.
- A future `TrainingStress` object could hold volume, intensity, vertical gain, and terrain load together.
- A future `PlacementRule` object could separate "when to use" from "what to avoid."
- A future `ProgressionStep` object could represent week-to-week progression more explicitly.
- A future `CardLink` object could separate relationship type, rationale, and priority.

### When More Structure Helps

More structure is useful when:

- the same kind of information repeats across many cards
- you want stronger validation
- you want better filtering or comparison logic
- you want a cleaner UI mapping later

### When More Structure Hurts

Too much structure becomes a burden when:

- the content is still evolving
- the fields are mostly descriptive rather than computational
- the extra objects make card authoring slower
- the schema becomes harder to read than the cards themselves

So the current design is intentionally lean. It has enough structure to be reliable, but not so much that it starts fighting the writing process.

## Why The Fields Are Mostly Lists Of Short Text

Many coaching ideas are still best expressed as short list items.

That is because they are:

- easy to write
- easy to read
- easy to compare
- easy to translate into UI sections later

Examples include:

- `when_to_choose`
- `when_not_to_choose`
- `expected_adaptations`
- `common_mistakes`
- `warning_signs`

If these were turned into deeply nested objects too early, the cards would become harder to create and review without improving them much.

## How The Relationships Work

The library uses `CardReference` instead of string-based links.

```python
CardReference(
    card_id="session_007",
    relationship=CardRelationship.PARENT,
    tags=["key_session"],
)
```

That gives us:

- a stable target card id
- a clear relationship type
- optional tags for extra context

This is better than free-text references because it is easier to validate and much easier to reuse later in an app.

## The Practical Rule

The design rule for this repository is simple:

> Add structure when it improves a coaching decision, a comparison, or a future UI display.

If a field does not help with one of those things, it probably does not belong yet.

## Short Blog-Friendly Summary

If you want a concise explanation for a blog post, you can say:

> We organized the cards with a shared base class and level-specific subclasses because training itself is hierarchical. The base class keeps every card comparable and easy to validate, while the specialized classes add only the fields that matter at each planning level. This gives us consistency, flexibility, and a clean path for future filtering, display, and recommendation features.
