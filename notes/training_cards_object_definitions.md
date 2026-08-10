# Training Card Object Definitions

This note explains the basic meaning of the training-card classes and how to think about their fields.

## What These Classes Are

The classes in `training_cards.schemas` are not mainly about behavior. They are about definition.

Each class says:

- what a valid card looks like
- what fields it can have
- which fields belong to all cards
- which fields only belong to one card level

In that sense, the class is more like a schema or contract than a traditional object with lots of methods.

## Why `name: type` Is Normal

A line like this:

```python
title: str
```

is a type-annotated field definition. In a dataclass, that is a very normal way to define data.

It means:

- this field exists
- its intended type is `str`
- it will be part of the object when the dataclass is created

By itself, the annotation does not enforce much. The dataclass and validation code are what make it real.

## Required Fields Versus Optional Fields

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
- `tags` is optional, because it gets an automatic empty list if nothing is passed in

So the rule is simple:

- no default means the caller must supply a value
- a default means the object can be created without supplying that value

## `str` Versus `field(default_factory=list)`

These two ideas do different jobs.

### `str`

`str` is the type of a text field.

It means the value should be a string such as:

- `"Base Development"`
- `"Easy Run"`
- `"15-45 minutes"`

If a field is defined only as `name: str`, then it is required unless a default is added.

### `field(default_factory=list)`

This is used for list fields.

It means:

- if no value is provided, create a fresh empty list
- do not share the same list between objects

That matters because lists are mutable. Without `default_factory=list`, multiple objects could accidentally end up sharing the same list instance.

So this:

```python
tags: list[str] = field(default_factory=list)
```

means:

- the field is a list of strings
- the default value is a new empty list for each object

## What `__post_init__()` Does

`__post_init__()` runs right after a dataclass object is created. It is the place where the class can check that the data is actually valid, not just typed correctly.

In this project, that matters because we do not want broken cards to quietly exist. The `__post_init__()` method checks the important minimums, such as:

- the card has an `id`
- the card has a `slug`
- the card has a `title`
- the card has at least one training level
- the card has a `summary`
- the card has a `purpose`

So the pattern is:

- the dataclass defines the shape
- `__post_init__()` checks the shape is usable

That is why `__post_init__()` is a good fit for schema objects like these.

## What Should Feel Required In `BaseTrainingCard`

For the current design, the important required fields in `BaseTrainingCard` make sense as:

- `id`
- `slug`
- `title`
- `card_type`
- `suitable_levels`
- `summary`
- `purpose`

Those are the fields that make a card identifiable and meaningful.

The other fields are better as optional, because they add detail but are not needed to recognize the card at the start.

## What Should Feel Optional In `BaseTrainingCard`

These are reasonable as optional fields for now:

- `tags`
- `goal_race_context`
- `training_profile`
- `expected_adaptations`
- `watchouts`
- `progression_rules`
- `regression_rules`
- `additional_information`
- `references`

That gives the schema a clear minimum while still letting a card stay lean if it does not need every extra section.

## What Should Feel Required In The Other Classes

For the level-specific classes, the same idea applies.

### `MacroCard`

The class itself should require:

- the base card fields
- `card_type = macro`

The extra macro fields can stay optional for now:

- `recommended_duration_weeks`
- `timing_guidance`

### `MezzoCard`

The class itself should require:

- the base card fields
- `card_type = mezzo`

The extra mezzo fields can stay optional for now:

- `recommended_duration_weeks`
- `placement_guidance`

### `MicroCard`

The class itself should require:

- the base card fields
- `card_type = micro`

The extra micro fields can stay optional for now:

- `recommended_duration_days`
- `week_structure`
- `key_sessions`
- `load_pattern`
- `placement_guidance`
- `recovery_requirements`

### `SessionCard`

The class itself should require:

- the base card fields
- `card_type = session`
- `session_family`

The extra session fields can stay optional for now:

- `typical_duration`
- `workout_parts`

### `SessionFamily`

The family object itself should require:

- `id`
- `slug`
- `title`
- `summary`

The extra family fields can stay optional for now:

- `description`
- `tags`

`SessionPart` is a little different because it is a smaller object inside a workout. Its current required fields make sense as:

- `name`
- `duration`
- `rpe`

The detailed instructions can stay optional:

- `instructions`
- `terrain_notes`

## Should There Be Predetermined Values

Yes, but only where they help clarity.

Predetermined values are useful when the field should have a controlled meaning, not arbitrary wording.

### Good Places For Controlled Values

- `card_type`
- `suitable_levels`
- `relationship` in `CardReference`

These should stay controlled because the app and the code need to understand them consistently.

### Good Candidates For Future Controlled Values

- `session_family` values through the family object
- `load_pattern`
- maybe some future sub-fields if the library starts repeating the same phrases too often

### When To Avoid Too Much Control

Do not make every descriptive field into a fixed vocabulary if it would make the cards harder to write.

For example, fields like:

- `summary`
- `purpose`
- `additional_information`

should stay flexible, because those are coach language fields, not code labels.

## The Practical Rule

Use required fields for the minimum shape of a card.

Use optional fields for useful coaching detail.

Use predetermined values only where consistency matters more than free wording.
