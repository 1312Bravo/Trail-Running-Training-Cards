# Coach Perspective Notes For Training Cards

This note explains the card types from a coach's point of view. The goal is to make each class feel like a real coaching tool, not just a data structure.

The basic idea is simple: a training plan is made of layers, and each layer has a different job. The card system mirrors that coaching reality so the library stays practical instead of abstract.

## How To Think About The Library

The card system moves from broad to specific:

- `MacroCard` answers: what phase are we in?
- `MezzoCard` answers: what block are we building inside that phase?
- `MicroCard` answers: what does this week need to do?
- `SessionCard` answers: what workout should we run today?

`BaseTrainingCard` is the shared coaching contract underneath all of them. It holds the fields that let a card be identified, compared, displayed, and linked to other cards.

This hierarchy matters because coaches rarely make decisions at only one level. A phase makes sense only when it supports the block, the block makes sense only when it supports the week, and the week makes sense only when it produces the right session stress. The card levels keep that chain of reasoning intact.

It also means each card can stay focused on its own job. The macro card should not have to explain every workout detail, and the session card should not have to carry the whole seasonal story. That separation makes the library easier to read, easier to maintain, and easier to coach from.

That design is useful because a coach usually thinks in layers:

- long-term direction first
- then training block
- then week structure
- then the workout itself

The schema follows that same coaching logic.

Another way to say it is this: each level answers a different coaching question.

- Macro cards set the season direction.
- Mezzo cards narrow that direction into a meaningful training block.
- Micro cards decide how the week supports that block.
- Session cards turn the week into actual training stress.

The shared base class keeps those layers connected so the library feels coherent instead of fragmented. A coach should be able to move from broad planning to session detail without changing the way the cards are understood.

The practical benefit is that the cards can stay reusable. A coach can use the same language to think about a phase, a block, a week, or a workout, while still getting the right amount of detail for each level.

## `BaseTrainingCard`

`BaseTrainingCard` is the minimum shape of a usable training card. From a coach's perspective, this is the part that tells you what the card is, who it is for, why it exists, and how it connects to the rest of the system.

It is not the full workout prescription and it is not the full training plan. Instead, it is the foundation that makes a card usable in practice. If a coach opens a card and cannot quickly tell what it represents, what level it belongs to, or why it matters, then the card is not yet doing its job.

The shared fields give the coach enough structure to make a decision:

- identify the card
- understand its coaching intent
- judge whether it fits the athlete
- see how it relates to other cards

That is why the base class matters so much. It creates the stable frame that every specialized card can build on.

### Core identity fields

- `id`: the stable internal identity of the card
- `slug`: a readable identifier for URLs, filenames, or search
- `title`: the coach-facing name of the card
- `card_type`: tells you whether the card is macro, mezzo, micro, or session

These fields matter because a coach needs to be able to refer to a card quickly and unambiguously. In a real planning workflow, this is what keeps the card from becoming just another text note.

`id` is the most technical identifier. `slug` is the most human-friendly reference. `title` is the outward-facing name that should feel coach-readable. `card_type` tells the system and the coach what kind of object they are dealing with.

### Coaching fit fields

- `suitable_levels`: who this card fits
- `summary`: the short preview sentence
- `purpose`: the coaching reason for the card

These are the fields that answer the first coaching question: is this the right card for this athlete and this phase?

`suitable_levels` helps the coach avoid mismatch. A card can be technically valid but still inappropriate for the athlete's current stage. `summary` should give the quick decision sentence. `purpose` should explain the coaching intent in a little more depth so the card is not just descriptive, but meaningful.

In practice, these fields help the coach move from "what is it?" to "why would I use it?" very quickly.

### Support fields

- `tags`: quick labels for search or grouping
- `goal_race_context`: the race or preparation situations where the card makes sense
- `training_profile`: the kind of training stress the card creates
- `expected_adaptations`: what the athlete should gain from it
- `watchouts`: the main risks, limits, or caution flags
- `progression_rules`: what should come after it or how it should build
- `regression_rules`: when to scale it back or simplify it
- `additional_information`: extra coaching detail that does not fit elsewhere
- `references`: links to related cards

From a coaching view, these fields separate the useful detail from the minimum identity. They help a coach decide not just what the card is, but whether it belongs in the plan.

`tags` are for fast retrieval and grouping. `goal_race_context` says where the card belongs in the bigger preparation picture. `training_profile` describes the stress the athlete will actually feel. `expected_adaptations` says what the card is trying to build. `watchouts` says when the card is likely to be too much, too soon, or too blunt.

`progression_rules` and `regression_rules` are especially helpful from a coaching perspective because they keep the card connected to decision-making. A good card should not only say how to use it in ideal conditions. It should also help the coach know what to do when the athlete is not quite ready or when the training load needs to be softened.

`additional_information` is the space for extra coaching context that does not belong in a more structured field. `references` keep the card connected to the rest of the library so the training system can behave like a real plan instead of isolated notes.

## `MacroCard`

`MacroCard` is the broad phase card. It represents the big training picture over several weeks or more.

This card is for decisions like:

- what the athlete is trying to build right now
- whether the current phase is about base, development, build, peak, taper, recovery, or return
- what the longer-term emphasis should be
- what kind of weeks or blocks should probably follow

The macro card is the coach's altitude view. It should not get lost in the details of a single session. Instead, it should explain the purpose of the larger training period and make the season feel intentional.

### Macro-specific fields

- `recommended_duration_weeks`: how long the phase usually lasts
- `timing_guidance`: how to place the phase in the larger season or race calendar

From a coach's perspective, the macro card is less about workouts and more about direction. It should help answer: what are we trying to accomplish over the next few weeks, and why is this the right time for it?

`recommended_duration_weeks` matters because phases should be long enough to create adaptation but not so long that the emphasis loses focus. `timing_guidance` helps the coach judge when the phase should sit relative to race dates, recovery periods, or more specific blocks.

Macro cards are useful when the coach needs to protect the big picture. They prevent the plan from becoming a collection of disconnected weeks.

## `MezzoCard`

`MezzoCard` is the focused block inside the larger phase. It usually sits between the big seasonal direction and the week-to-week execution.

This card is useful when a coach wants to describe a block that has a more specific emphasis, such as:

- threshold development
- endurance development
- long-endurance emphasis
- recovery emphasis
- race practice emphasis

The mezzo card gives the plan shape. It is where the season direction becomes a practical training emphasis that can actually guide weekly work.

### Mezzo-specific fields

- `recommended_duration_weeks`: how long the block should usually last
- `placement_guidance`: where this block belongs inside the broader phase

From a coaching view, the mezzo card answers: what are we sharpening inside this phase, and how should this block sit between the macro plan and the weekly load?

`recommended_duration_weeks` gives the coach a sense of the block's natural size. `placement_guidance` is the strategic piece: should this block come early, late, after a recovery period, before a race-specific block, or as a bridge between two different emphases?

The mezzo level is especially valuable because it is specific enough to matter, but still broad enough to support several weeks of planning without over-prescribing every day.

## `MicroCard`

`MicroCard` is the week-level planning card. It describes how a coach shapes one training week to support the larger block.

This card is where the plan starts to feel operational. It should tell a coach:

- what the week is trying to emphasize
- how hard the week should feel overall
- how the key sessions fit together
- how recovery is being protected
- what kind of rhythm the athlete should expect across the week

The micro card is the bridge between the block-level intention and the day-by-day reality of training. It is where the plan becomes something the athlete can actually live through.

### Micro-specific fields

- `recommended_duration_days`: the typical length of the week structure
- `week_structure`: the shape of the week at a glance
- `key_sessions`: the main sessions that matter most in the week
- `load_pattern`: the way stress is distributed across the week
- `placement_guidance`: where this week fits inside the block
- `recovery_requirements`: what recovery support the week needs

From a coach's perspective, the micro card is the bridge between intent and execution. It should help answer: how do we organize the week so the athlete gets the right stress without losing freshness or consistency?

`recommended_duration_days` tells the coach what kind of week the card is designed for. `week_structure` gives the overall shape, such as whether the week is more conservative, more stacked, more recovery-oriented, or more progressive.

`key_sessions` helps the coach see which days matter most. `load_pattern` explains how the stress is distributed across the week, which is important because week design is not only about totals. It is also about how the athlete absorbs those totals.

`placement_guidance` keeps the micro card connected to the larger block. `recovery_requirements` makes sure the week is not written as if the athlete has unlimited freshness. That is important because week design should always respect accumulated fatigue.

## `SessionCard`

`SessionCard` is the most detailed card. It describes one workout or session pattern.

This is the card a coach reaches for when they want to define:

- the intent of the workout
- the workout family it belongs to
- what the athlete actually does in the session
- how hard each part should feel
- what terrain or execution detail matters
- how the session should be coached in practice

The session card should be specific without becoming overcomplicated. It needs enough structure to guide execution, but it should still feel like a reusable workout concept rather than a one-off prescription.

### Session-specific fields

- `session_family`: the workout family or pattern
- `typical_duration`: the normal time window for the workout
- `workout_parts`: the structured parts of the session

From a coaching perspective, the session card is where specificity matters most. It should say not just what the workout is, but how to coach it well and what to watch for while it is happening.

`session_family` gives the workout its identity within the larger training vocabulary. `typical_duration` gives a practical expectation for how long the session usually takes. `workout_parts` breaks the workout into usable chunks so the coach can see how the session flows from start to finish.

That structure is especially useful when the session includes different intensities, terrain changes, or recovery periods that matter for execution.

### `SessionPart`

`SessionPart` is the internal building block inside a session card.

Its fields should read like a workout prescription:

- `name`: the part of the workout
- `duration`: how long that part lasts
- `rpe`: the intended effort level
- `instructions`: how to do the part
- `terrain_notes`: any terrain or surface guidance

This is useful because a coach can break a workout into the same language used in daily practice: warm-up, main set, recovery, cooldown, and any special notes.

`name` makes the structure readable. `duration` keeps the session anchored in time. `rpe` gives the athlete a simple sense of effort. `instructions` explains how to perform the part, and `terrain_notes` makes sure the workout is shaped by the surface or course demands rather than by effort alone.

For trail and mountain running, that last part matters a lot. Terrain can change the load even when the effort target stays the same.

## How Coaches Should Read The Fields

The fields are not just categories. They each answer a coaching question.

- `summary` gives the fast preview
- `purpose` gives the coaching reason
- `training_profile` gives the stress type
- `expected_adaptations` gives the likely outcome
- `watchouts` gives the risks
- `progression_rules` gives the next step
- `regression_rules` gives the fallback
- `additional_information` gives the deeper context

That means the card should read like a coaching decision aid, not like a database record.

If a coach can skim the card and understand what it is for, who it suits, what stress it creates, and what usually comes next, then the card is doing its job well.

## Practical Rule Of Thumb

If a field helps a coach decide whether, when, or how to use the card, it belongs in the schema.

If a field only repeats information already clear from the card's level or title, it probably does not need its own slot.

That keeps the library usable for real coaching work while still leaving enough structure for search, display, and future app features.

## Coach-Level Reading Of The Whole Stack

The best way to use the library is to read it from top to bottom:

1. Start with the `MacroCard` to understand the season goal.
2. Read the `MezzoCard` to see how that goal is sharpened into a block.
3. Use the `MicroCard` to understand the weekly rhythm and load.
4. Use the `SessionCard` to coach the actual workout details.

That flow helps the coach stay consistent. It prevents overreacting to the workout level when the bigger phase is the real issue, and it prevents building a phase so abstractly that the week-level work becomes unclear.

In other words, each level has its own job, but the real value comes from how they work together.
