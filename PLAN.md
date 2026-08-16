# Training Cards Coaching Plan

This file is the working plan for improving the coaching folder, technical notes, prompt system, and card content in the Training Cards library.

Keep this file updated whenever the work plan, ordering, decisions, or completed phases change.

The current focus is content and coaching quality, not schema changes.

## Guiding Direction

The card library should feel like it was built by a thoughtful endurance coach with trail-running and mountain-running expertise.

Before rebuilding or expanding the cards, we first need to clarify:

- where the coach takes knowledge from
- how coaching judgment is translated into cards
- how coaching notes and prompts support consistent card creation
- how card content should balance general running usefulness with trail-specific adaptation
- how future cards should be reviewed before they become part of the library

## Completed Work

- Completed the initial read-only audit of existing notes and prompts.
- Renamed unclear notes.
- Replaced the old prompt-only folder with `coaching/`.
- Moved coach-facing prompt and coaching notes into `coaching/`.
- Kept technical and project notes in `notes/`.
- Merged `schema_onboarding_notes.md` into `notes/schema_design_and_validation.md`.
- Split `coach_guidance.md` into `coaching_philosophy.md` and `card_authoring_guidance.md`.

## Phase 1: Notes Structure

Create a cleaner notes and coaching-folder structure from the audit.

Status: completed for now. The `coaching/` folder will stay intentionally small, with a few larger files instead of many narrow files.

Current coaching files:

- `coaching/coaching_philosophy.md`: coach identity, principles, source posture, specificity rules, and safety boundary.
- `coaching/card_authoring_guidance.md`: practical guidance for writing, reviewing, structuring, and displaying cards.
- `coaching/source_history.md`: where the coach's knowledge came from, including evidence, practice, trail demands, readiness, fatigue, and lessons learned while rebuilding cards.
- `coaching/card_hierarchy.md`: coach-facing explanation of macro, mezzo, micro, and session layers.

Proposed structure from the audit:

- `notes/cloud_library_storage_workflow.md`: renamed from `cloud_storage_notes.md`; owns Drive, cache, manifest, bundle, validation, upload/download.
- `notes/schema_design_and_validation.md`: merged from `schema_notes.md` and `training_cards_object_definitions.md`; owns schema design, onboarding explanation, references, pathway indexing, registry, display assumptions, and validation behavior.
- `notes/product_backlog.md`: renamed from `TODO.md`; owns future app/workflow/product ideas.

Structure goals:

- give each note one clear job
- avoid duplicate explanations across files
- make note names obvious from the filename
- keep technical implementation notes separate from coaching notes
- keep coach-facing prompts and coach notes together in `coaching/`
- prefer a few larger coaching files until the content becomes too large to navigate
- preserve useful existing content while moving it into better homes

## Phase 2: Coaching Knowledge Foundation

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

## Phase 3: Coaching Prompt Structure

Update the prompts after the note structure and coaching foundation are clearer.

Possible prompt work:

- improve `coaching/coaching_philosophy.md`
- improve `coaching/card_authoring_guidance.md`
- separate card creation guidance from card review guidance if useful
- make the prompt clearer about field purpose and coaching voice
- define how much evidence, specificity, and trail adaptation each card needs

## Phase 4: Card Rebuild Plan

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

## Phase 5: Card Expansion

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

Start Phase 2 by expanding `coaching/source_history.md` into the coaching foundation.

For now, do not create separate files for:

- coaching principles
- training stress model
- trail and mountain adaptations
- progression and regression framework
- card quality review
- card creation workflow

Fold those topics into the larger coaching files first. Split them out later only if the files become too large or hard to navigate.
