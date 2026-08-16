# Card Authoring Guidance

This note explains how to write and review training cards once the coach perspective, hierarchy, and source history are understood.

Use this file with:

- `coaching/coaching_philosophy.md`
- `coaching/card_hierarchy.md`
- `coaching/source_history.md`

Treat the current schema as the working container for card content. Do not redesign the schema during normal card writing; only flag a schema limitation when the coaching content truly cannot be expressed with the current fields.

## Card Quality Standard

Each card should answer these questions clearly:

- What is this card for?
- Who is it appropriate for?
- When should it be used?
- When should it not be used?
- What adaptations should it create?
- What should the training feel like?
- What are the main risks or mistakes?
- What cards could logically come before or after it?

## Card Structure Standard

When using the card fields, write them because they support real coaching decisions, not because they look tidy in code.

A good card should make it easy to understand:

- What training problem the card solves.
- What athlete profile or readiness state it fits.
- What type of stress the card introduces.
- How trail-specific demands are represented.
- How progression, regression, and sequencing are handled.
- What warning signs or contraindications matter.
- How the card can later be filtered, compared, recommended, or displayed in the Training Platform app.

## Writing Style

- Be specific, but not overly academic.
- Use concise coaching language.
- Write only as much as the card needs; do not inflate fields with repeated or decorative text.
- Prefer concrete training characteristics over generic motivation.
- Separate primary goals from secondary benefits.
- Mention caution flags when a card may be too aggressive.
- Avoid pretending the card is personalized unless athlete data is explicitly provided.
- Favor practical, research-aware coaching guidance over long explanations. Include detail when it changes the training decision.
- When current best practice or evidence is likely to matter, check reliable sources before finalizing detailed card content.

## Creation Workflow

Create cards step by step.

1. Propose card titles and rough placement first, using the hierarchy macro phase, mezzo block, micro week, and session workout.
2. Wait for approval before filling complete card content.
3. When filling a card, keep the preview fields concise and put deeper coaching detail in the appropriate detailed fields.
4. Review each card for repetition before accepting it.
5. Check the source history and hierarchy notes when the card needs evidence, trail-specific reasoning, or placement logic.

## App Display Assumption

Cards will later be shown in the Training Platform app with two levels of detail:

- Preview: the most important information needed to compare cards quickly.
- Detail view: the full coaching context, including when to use the card, when not to use it, terrain demands, risks, progression, regression, and sequencing.

The schema and card content should support this preview/detail structure without duplicating the same text across many fields.

Use `summary` as the preview-safe card sentence. It should be one concise sentence, usually 12-22 words, written for quick comparison. Do not use `summary` for long context, coaching rationale, or repeated detail.

The detail view may include a longer `additional_information` field. This should be used for readable in-depth coaching context, not a longer version of the preview.

Session cards should include a structured workout guide when enough information is available. Use practical parts such as warm-up, main set, recovery, cooldown, and optional notes. Give duration and RPE guidance on a 1-10 scale, but keep ranges adaptable rather than falsely precise.

## Card Relationships

Cards should be connected with structured references rather than loose string lists or deep nested folders. Keep card files grouped by planning level, and use references to describe hierarchy, sequencing, alternatives, and support relationships.

Use short tags on references when useful. Do not turn references into long explanations; longer reasoning belongs in the card content.

## Output Expectations

When creating or reviewing a card, produce content that can be mapped into the training-card classes. Use stable labels, consistent terminology, and clear lists.

Until the final card schema is defined, include enough information to understand:

- The identity, planning level, and purpose of the card.
- The athlete level, readiness, or context it fits.
- The recommended training stress, duration, and terrain demands.
- The expected adaptations and coaching rationale.
- The situations where the card should or should not be used.
- The progression logic and relationship to other cards.
