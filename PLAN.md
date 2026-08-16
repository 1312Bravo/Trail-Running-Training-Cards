# Training Cards Coaching Plan

This file is the working plan for improving the coaching folder, technical notes, prompt system, and card content in the Training Cards library.

Keep this file updated whenever the work plan, ordering, decisions, or completed phases change.

The current focus is content and coaching quality, not schema changes.

## Guiding Direction

The card library should feel like it was built by a thoughtful endurance coach with trail-running and mountain-running expertise.

Before rebuilding or expanding the cards, we first need to clarify:

- what notes already exist and what each note is responsible for
- where the coach takes knowledge from
- how coaching judgment is translated into cards
- how coaching notes and prompts support consistent card creation
- how card content should balance general running usefulness with trail-specific adaptation
- how future cards should be reviewed before they become part of the library

## Phase 1: Notes Audit

Review everything in `notes/` and decide what each file is for.

Current files to inspect:

- `coaching/coach_card_creation_prompt.md`
- `coaching/coach_knowledge_sources.md`
- `coaching/coaching_card_hierarchy.md`
- `cloud_library_storage_workflow.md`
- `product_backlog.md`
- `schema_design_and_validation.md`
- `schema_onboarding_notes.md`

Audit goals:

- identify overlap between files
- identify vague or misleading file names
- decide which files should be renamed
- decide which files should be merged
- decide which files should stay separate
- identify missing notes needed for coaching and card creation

No content should be rewritten until the intended notes structure is clear.

Status: first read-only audit completed.

Audit findings:

- `cloud_library_storage_workflow.md`: operational note for Google Drive, local cache, manifest, bundle, validation, and upload/download workflow. Keep separate from coaching notes.
- `coaching/coaching_card_hierarchy.md`: strong coach-facing explanation of the macro, mezzo, micro, and session hierarchy. It overlaps with schema explanation and should become a cleaner coaching hierarchy note.
- `coaching/coach_knowledge_sources.md`: source-tracking note that records research and practical sources behind current card ideas. Keep, but later expand into a fuller coach knowledge source note.
- `schema_design_and_validation.md`: technical design note for schema structure, display assumptions, references, pathway validation, registry, and session families. Keep as technical documentation, but avoid mixing it with coaching philosophy.
- `product_backlog.md`: future work list for tag taxonomy, Today session helper, and automated checks. Keep as product/backlog notes so it is not confused with the coaching plan.
- `schema_onboarding_notes.md`: beginner-friendly explanation of dataclass fields, required/optional fields, and controlled values. It overlaps with `schema_design_and_validation.md`, but is useful as an onboarding note for now.

Main structure issue:

- Coaching hierarchy, schema explanation, and beginner object explanation currently repeat parts of the same card-level story from different angles.
- Coaching knowledge sources exist, but they are not yet framed as the full "coach brain" behind card creation.
- Prompt guidance exists, but supporting notes do not yet provide a complete foundation for rebuilding cards.

Initial recommendation:

- Keep implementation/cloud documentation separate.
- Keep technical schema documentation separate.
- Create a stronger coaching notes group before rebuilding cards.
- Preserve useful current explanations, but move them into clearer homes.

## Phase 2: Notes Structure

Create a cleaner notes structure from the audit.

Status: initial rename pass completed. The `/prompts` folder was renamed to `/coaching`, and coach-facing notes were moved there. New outline notes are intentionally postponed.

Possible future notes:

- `coaching/coaching_principles.md`
- `coaching/coach_knowledge_sources.md`
- `coaching/card_creation_workflow.md`
- `coaching/card_quality_review.md`
- `coaching/training_stress_model.md`
- `coaching/trail_mountain_adaptations.md`
- `coaching/progression_regression_framework.md`

Proposed structure from the audit:

- `notes/cloud_library_storage_workflow.md`: renamed from `cloud_storage_notes.md`; owns Drive, cache, manifest, bundle, validation, upload/download.
- `notes/schema_design_and_validation.md`: renamed from `schema_notes.md`; owns schema design, references, pathway indexing, registry, display assumptions, and validation behavior.
- `notes/schema_onboarding_notes.md`: renamed from `training_cards_object_definitions.md`; owns beginner-friendly explanation of dataclasses and required/optional fields.
- `coaching/coach_card_creation_prompt.md`: moved from the old prompt-only folder; owns the reusable instruction prompt for card creation and review.
- `coaching/coaching_card_hierarchy.md`: moved from `notes/`; owns how coaches think across macro, mezzo, micro, and session layers.
- `coaching/coach_knowledge_sources.md`: moved from `notes/`; owns where coaching knowledge comes from and how evidence/practice are translated into cards.
- `coaching/coaching_principles.md`: new; owns enduring principles that should guide all cards.
- `coaching/training_stress_model.md`: new; owns intensity, volume, vertical gain, downhill load, terrain, time-on-feet, recovery cost, and fatigue.
- `coaching/trail_mountain_adaptations.md`: new; owns how general running cards adapt to trail and mountain contexts.
- `coaching/card_creation_workflow.md`: new; owns step-by-step process for creating and reviewing cards.
- `coaching/card_quality_review.md`: new; owns card review checklist and quality standards.
- `notes/product_backlog.md`: renamed from `TODO.md`; owns future app/workflow/product ideas.

Structure goals:

- give each note one clear job
- avoid duplicate explanations across files
- make note names obvious from the filename
- keep technical implementation notes separate from coaching notes
- keep coach-facing prompts and coach notes together in `coaching/`
- preserve useful existing content while moving it into better homes

## Phase 3: Coaching Knowledge Foundation

Define the source of the coach's knowledge.

Key questions:

- What coaching principles should guide every card?
- What evidence sources and best practices should inform the library?
- How should practical coaching experience be represented?
- How should athlete readiness, fatigue, injury history, and recovery influence card choice?
- How should trail and mountain demands change otherwise general running guidance?
- How should the library handle uncertainty, adaptation, and individual differences?

Likely outputs:

- clearer coaching principles
- explicit evidence and practice standards
- a trail-running adaptation model
- a fatigue and readiness decision framework
- a progression and regression framework

## Phase 4: Coaching Prompt Structure

Update the prompts after the note structure and coaching foundation are clearer.

Possible prompt work:

- improve `coaching/coach_card_creation_prompt.md`
- separate card creation guidance from card review guidance if useful
- make the prompt clearer about field purpose and coaching voice
- define how much evidence, specificity, and trail adaptation each card needs

## Phase 5: Card Rebuild Plan

After the coaching foundation and notes structure are clearer, plan the card rebuild.

Goals:

- improve existing card content
- add missing cards
- make cards more specific and useful without becoming too narrow
- improve consistency across macro, mezzo, micro, and session levels
- strengthen references between cards
- keep preview fields concise and detail fields genuinely useful

Likely rebuild order:

1. Macro cards
2. Mezzo block cards
3. Micro week cards
4. Session workout cards
5. Session family support content

## Phase 6: Card Expansion

Once the rebuilt style is established, expand the library with new cards.

Potential expansion areas:

- recovery and return-to-training patterns
- climb-focused development
- downhill conditioning
- hiking and power-hiking progression
- fueling practice
- heat, altitude, and environmental preparation
- race-specific simulation
- strength and mobility support
- technical terrain skill sessions

## Working Rules

- Keep `PLAN.md` current as decisions are made and phases are completed.
- Discuss direction before editing broad coaching content.
- Keep schema changes out of scope unless content work exposes a real need.
- Treat Google Drive JSON as the source of truth for card content.
- Use local card files as implementation artifacts, not the final authority.
- Keep card titles broad and reusable.
- Put trail-specific detail inside card content rather than making every card trail-only.
- Review coaching notes and prompts before rebuilding cards.
- Run validation after card JSON or synced content changes.

## Immediate Next Step

Review the renamed `coaching/` and `notes/` folders and decide whether to create the postponed coaching foundation outlines.

The next useful output should be a decision on whether to add:

- `coaching/coaching_principles.md`
- `coaching/training_stress_model.md`
- `coaching/trail_mountain_adaptations.md`
- `coaching/card_creation_workflow.md`
- `coaching/card_quality_review.md`
- `coaching/progression_regression_framework.md`

After that, write the coaching foundation before rebuilding cards.
