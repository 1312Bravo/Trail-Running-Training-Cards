# Card Hierarchy

This note explains the card hierarchy from a coach's point of view. The goal is to make each card level feel like a real planning tool, not just a data structure.

For technical schema details, use `notes/schema_design_and_validation.md`. This note stays focused on coaching decisions and how the layers work together.

## How This File Is Used

Use this file when deciding where a card belongs and how it should connect to other cards.

It should help answer:

- Is this idea a phase, block, week, or session?
- Is the card trying to do too many levels at once?
- What should sit above or below this card?
- Does the card need a parent, child, previous, next, alternative, or support relationship?

## The Basic Idea

A training plan is made of layers, and each layer has a different job.

The card system mirrors that coaching reality:

- `MacroCard` answers: what phase are we in?
- `MezzoCard` answers: what block are we building inside that phase?
- `MicroCard` answers: what does this week need to do?
- `SessionCard` answers: what workout should we run today?

The coach should be able to move from broad planning to session detail without changing the logic of the plan. A phase makes sense only when it supports the block, the block makes sense only when it supports the week, and the week makes sense only when it creates the right session stress.

## How Coaches Should Read The Stack

Read the library from broad to specific:

1. Start with the `MacroCard` to understand the season direction.
2. Read the `MezzoCard` to see how that direction becomes a focused block.
3. Use the `MicroCard` to understand the weekly rhythm and load.
4. Use the `SessionCard` to coach the actual workout.

This prevents two common mistakes:

- overreacting to a single workout when the bigger phase is the real issue
- writing broad phases that never translate into useful weekly or daily training

## Shared Card Role

Every card should help a coach decide:

- what the card is
- who it is for
- why it exists
- what stress it creates
- what adaptation it should support
- when it should not be used
- how it connects to other cards

The shared fields are there to support coaching judgment, comparison, display, and linking. They should not become filler. If a field does not help the coach choose, adapt, sequence, or explain the card, it probably needs less text.

## Relationship Contract

Every relationship describes the target card in relation to the source card. Use the most specific relationship that is true; tags add context, but do not change the relationship's meaning.

- **Parent:** The target is exactly one planning level above the source and directly contains its planning role. For example, a micro week can have a mezzo block parent.
- **Child:** The target is exactly one planning level below the source and directly implements its planning role. For example, a mezzo block can have a micro week child.
- **Previous:** The target is a usual preceding option at the same planning level.
- **Next:** The target is a usual following option at the same planning level.
- **Alternative:** The target is an interchangeable option at the same planning level and for a similar coaching decision.
- **Support:** The target materially supports or contextualises the source card, but is not its direct structural parent, child, or sequence step. Support can cross planning levels.

Read `source --support--> target` as: the target usefully supports or contextualises the source. Add reciprocal support references only when both card detail views need the connection. A support relationship must not be used to create or imply a pathway hierarchy.

## Macro Cards

Macro cards describe the broad training phase.

They are useful for decisions like:

- what the athlete is trying to build over several weeks
- whether the current period is base, build, race-specific preparation, taper, recovery, or return-to-consistency
- what kind of block should probably come next
- what should be protected at the big-picture level

A macro card should not explain every workout detail. Its job is to set direction and protect the plan from becoming a disconnected list of sessions.

Good macro cards answer:

- Why is this phase appropriate now?
- What does this phase emphasize?
- What should be avoided during this phase?
- What kind of blocks naturally belong inside it?

## Mezzo Cards

Mezzo cards describe focused blocks inside a larger phase.

They are useful for decisions like:

- what specific training quality is being developed
- how long the block should usually last
- where the block fits inside the larger phase
- what weekly structures and key sessions should support it

Examples include endurance development, threshold development, strength endurance, race practice, and recovery emphasis.

A mezzo card should be specific enough to guide several weeks of training, but broad enough that it does not prescribe every day.

Good mezzo cards answer:

- What training problem does this block solve?
- What kind of athlete readiness does it require?
- What should progression look like across the block?
- What week types and sessions naturally belong inside it?

## Micro Cards

Micro cards describe a week-level structure.

They are useful for decisions like:

- what the week is trying to emphasize
- how stress is distributed across the week
- which sessions matter most
- how recovery is protected
- where the week belongs inside the block

The micro card is where the plan starts to feel livable. It should describe the rhythm of the week, not just list workouts.

Good micro cards answer:

- What is the main job of this week?
- What are the key sessions?
- What should the rest of the week do?
- What fatigue or recovery signals would make the coach adjust it?

## Session Cards

Session cards describe individual workout patterns.

They are useful for decisions like:

- why this workout belongs today
- what the athlete actually does
- what the effort should feel like
- what terrain or execution detail matters
- how to scale the workout up or down

Session cards should be practical and coachable. They need enough structure to guide execution, but they should still be reusable workout concepts rather than one-off prescriptions. A session card uses workout blocks, options, and parts: the block gives the workout section, the option gives a complete selectable or required prescription, and the part gives the concrete work the athlete performs.

Good session cards answer:

- What stimulus is this session trying to create?
- What should the athlete feel during the key work?
- What terrain or pacing guidance matters?
- What are the common mistakes?
- What should the coach change if the athlete is not ready?

Use mechanical repeats only when the parts repeat. For example, a hill circuit option can repeat several rounds, while a simple continuous easy run usually has no repeat value.

## Trail And Mountain Context

Trail and mountain running do not require every card to become trail-only. Instead, broad cards should include trail-specific adaptation where it changes the coaching decision.

Important trail and mountain demands include:

- vertical gain
- downhill load
- hiking and power-hiking
- technical terrain
- variable pacing
- muscular endurance
- fueling under longer or rougher conditions
- terrain confidence and coordination

For example, an endurance card can stay generally useful while noting that trail runners may measure the work by time-on-feet, vertical gain, hiking, and descent load rather than distance alone.

## Sequencing Logic

Cards should connect like coaching decisions, not like static folders.

Useful relationship questions:

- What usually comes before this?
- What usually comes after this?
- What blocks or weeks support this phase?
- What sessions support this week?
- What is an easier alternative?
- What is a more specific or more demanding next step?

The coach should be able to follow relationships from macro to session, but the system should also allow flexible alternatives when athlete readiness, terrain, race goals, or fatigue make a different choice better.

Good sequencing should also allow feedback upward. If a session idea keeps requiring a week structure that does not exist, that may reveal a missing micro card. If several weeks point toward the same training emphasis, that may reveal a missing mezzo block.

## Rule Of Thumb

Each card level should do its own job:

- macro sets direction
- mezzo gives the block emphasis
- micro organizes the week
- session creates the actual training stress

If a card tries to do too many levels at once, simplify it. If a card cannot explain its coaching decision, rewrite it before adding more detail.
