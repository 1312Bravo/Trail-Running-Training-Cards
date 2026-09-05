# Card Authoring Guidance

This note explains how to write and review training cards once the shared coaching foundation, selected training-method philosophy profile, hierarchy, and relevant source history are understood.

Use this file with:

- `coaching/coaching_foundation.md`
- `coaching/card_hierarchy.md`
- `coaching/card_storage_architecture.md`
- `coaching/philosophies/<profile>/philosophy.md`
- `coaching/philosophies/<profile>/sources.md`

Treat the current schema as the working container for card content. Do not redesign the schema during normal card writing; only flag a schema limitation when the coaching content truly cannot be expressed with the current fields.

## Before Writing

Before writing or rebuilding a card, check:

- the intended card level in `coaching/card_hierarchy.md`
- the shared coach identity and standards in `coaching/coaching_foundation.md`
- the selected coaching approach in `coaching/philosophies/<profile>/philosophy.md`
- any relevant source record in `coaching/philosophies/<profile>/sources.md`
- the `philosophy_profile_ids` value: use the exact directory names of every actual training-method profile that materially shaped the card
- in Python-authored seed cards, use the profile ID constants from `training_cards/philosophy_profiles.py` rather than raw profile strings
- choose the profile ID from its documented method, source record, and actual influence on the card
- do not use `common`; the shared coaching foundation is always-on and is not a card-level philosophy profile
- whether the card should be broad and reusable or more specific inside the details only

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

## Philosophy Specificity Standard

Use `mainstream_endurance` for the baseline evidence-informed version of a card type. Create a named-philosophy version only when that philosophy creates a meaningful distinction from the matching `mainstream_endurance` card.

The distinction must be large enough that it would affect how the app chooses, explains, structures, filters, or sequences the card. This applies at every level: macro, mezzo, micro, and session.

Use coaching common sense rather than a mechanical checklist. A separate named-philosophy card is justified when a coach using that philosophy would make a noticeably different coaching decision from a mainstream evidence-informed coach for the same athlete and situation.

Small emphasis differences should stay in the relevant philosophy notes, card explanation, or lower-level cards. If the philosophy would only produce the same card with different language, tone, or minor watchouts, do not create a duplicate.

When unsure, default to no separate named-philosophy card until the distinction becomes clear during coaching review or card drafting.

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

## Field Discipline

- `summary`: one preview-safe sentence for quick comparison.
- `philosophy_profile_ids`: structured training-method provenance. Use only IDs defined in `training_cards/philosophy_profiles.py`. Profile IDs match directories under `coaching/philosophies/` exactly. In Python cards, use constants such as `MAINSTREAM_ENDURANCE`, `CTS`, `EVOKE_ENDURANCE`, `SWAP`, `SHARMAN_ULTRA`, `ENDURANCE_80_20`, and `LYDIARD`. Exported JSON stores the literal string values. `common` is not valid card provenance.
- `purpose`: the coaching job of the card.
- `goal_race_context`: when this card fits the athlete, goal, phase, or terrain context.
- `training_profile`: the actual stress pattern, feel, terrain, and loading demand.
- `expected_adaptations`: what the athlete should gain from the card.
- `watchouts`: when not to use the card and common mistakes.
- `progression_rules`: how to build when the card is working.
- `regression_rules`: how to simplify when readiness or recovery is not there.
- `additional_information`: deeper coaching context that does not repeat the preview.

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

Use `parent` and `child` only for directly adjacent planning levels. Use `previous`, `next`, and `alternative` only between cards at the same planning level. Use `support` for a meaningful cross-level connection that is not part of the direct Macro -> Mezzo -> Micro -> Session pathway.

Use short tags on references when useful. Do not turn references into long explanations; longer reasoning belongs in the card content.

## Naming And Storage

Visible card titles should be readable coaching names. They do not need to include the philosophy name unless that is genuinely part of the card identity.

Implementation identifiers need stronger uniqueness:

- Python filenames for philosophy-specific variants should use a profile prefix when the card concept could exist in more than one philosophy, such as `mainstream_easy_aerobic_run.py`.
- Python object names should follow the same uniqueness pattern when they are exported through a package-level registry.
- Card `slug` values should also stay unique because cloud JSON files are written as `<slug>.json` inside the card-type folder.
- Card `id` values remain the primary stable identity for references and app behavior.
- Cloud JSON stores `philosophy_profile_ids` as literal strings, not Python constants, so it stays portable outside the Python authoring environment.

Example: a mainstream and a Lydiard version may both display as `Easy Aerobic Run`, but their Python filenames, object names, slugs, IDs, and `philosophy_profile_ids` should make the distinction unambiguous.

## Output Expectations

When creating or reviewing a card, produce content that can be mapped into the training-card classes. Use stable labels, consistent terminology, and clear lists.

Until the final card schema is defined, include enough information to understand:

- The identity, planning level, and purpose of the card.
- The athlete level, readiness, or context it fits.
- The recommended training stress, duration, and terrain demands.
- The expected adaptations and coaching rationale.
- The situations where the card should or should not be used.
- The progression logic and relationship to other cards.
