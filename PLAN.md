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
- Lightly refined the current coaching files before moving into deeper coaching-foundation work.
- Archived `coaching_philosophy.md` and `source_history.md` as `_old` reference files and created fresh working versions.
- Established a shared coaching foundation and a folder-per-philosophy structure; preserved the active foundation and source-history scaffold through file moves rather than content rewrites.

## Phase 1: Notes Structure

Create a cleaner notes and coaching-folder structure from the audit.

Status: completed for now. The `coaching/` folder will stay intentionally small, with a few larger files instead of many narrow files.

Current coaching structure:

- `coaching/coaching_foundation.md`: shared coach identity, trail and mountain context, claim integrity, and safety boundary that apply across every philosophy profile.
- `coaching/philosophies/<profile>/philosophy.md`: a complete, internally consistent coaching approach.
- `coaching/philosophies/<profile>/source_history.md`: sources, rationale, and evidence history for that specific philosophy.
- `coaching/philosophies/_template/philosophy.md`: provisional topic structure for future philosophy profiles.
- `coaching/philosophies/_template/source_history.md`: preserved source-history scaffold for creating future profile histories.
- `coaching/card_authoring_guidance.md`: practical guidance for writing, reviewing, structuring, and displaying cards.
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

Define the shared coaching foundation, then establish philosophy-specific coaching approaches and their source history.

Status: active. Keep the coach identity and responsible-guidance standards shared; define training models, knowledge stance, and source history inside individual philosophy profiles.

Key questions:

- What standards must apply across every coaching philosophy?
- What complete coaching philosophy should be defined first?
- How should each philosophy represent its own sources, evidence, coaching practice, and uncertainty?
- How should athlete readiness, fatigue, injury history, and recovery influence card choice?
- How should trail and mountain demands change otherwise general running guidance?
- How should the library handle uncertainty, adaptation, and individual differences?

Likely outputs:

- a clear shared coaching foundation
- one or more explicit philosophy profiles
- philosophy-specific source histories
- philosophy-specific trail-running adaptation, fatigue/readiness, and progression/regression frameworks

Coaching foundation and philosophy-profile TODO:

- [x] Define the coach identity as broadly reusable coaching guidance: an experienced, practical, athlete-centred and access-aware endurance-running coach with trail and mountain depth; aware of the runner's whole life and varied goals; focused on durable development, purposeful and enjoyable training, education, athlete agency, a calm but firm tone, and clear professional scope.
- [x] Define the shared trail and mountain context as running-first guidance with terrain-specific interpretation, transferable training intent, intentional specificity, skill development, conditions-aware judgement, access-aware substitutions, and variable recovery cost.
- [x] Define the shared claim-integrity and uncertainty standard: use sound knowledge, state what depends on the runner or context, avoid false certainty, and keep philosophy-specific reasoning traceable.
- [x] Define the shared safety boundary for plan authoring: plans are general guidance, should be built conservatively, need cautions only when directly relevant, and do not replace professional care.
- [x] Select `cts` as the first complete coaching philosophy profile.
- [x] Create and expand the long-form `cts` interpretation, using mini-section headings with explanatory paragraphs for each substantive principle, plus section-level framing, practical application, boundaries, training load and adaptation model, trail and mountain approach, knowledge and decision-making stance, limits, and card implications.
- [x] Add `cts/summary.md` as a short, practical entry point derived from the detailed CTS interpretation; make `summary.md` part of the documented profile structure.
- [ ] Review and refine the CTS profile against the user's source material before treating it as active for card authoring.
- [x] Build matching `summary.md`, `philosophy.md`, and `sources.md` files for `evoke_endurance`; keep it in development pending source review.
- [x] Build matching `summary.md`, `philosophy.md`, and `sources.md` files for `swap`; keep it in development pending a deeper primary-source base.
- [x] Build matching `summary.md`, `philosophy.md`, and `sources.md` files for `sharman_ultra`; keep it in development pending a deeper primary-source base.
- [x] Build matching `summary.md`, `philosophy.md`, and `sources.md` files for `80_20_endurance`; keep it in development pending primary-book review.
- [x] Build matching `summary.md`, `philosophy.md`, and `sources.md` files for `lydiard`; keep it in development pending primary-source review.
- [ ] Create and maintain a `sources.md` record inside each philosophy profile.
- [x] Define philosophy profiles as documented, source-grounded interpretations of named coaching systems or teams; add `coaching/philosophies/README.md` to set folder structure, source standards, profile-ID rules, and the `common` boundary.
- [x] Catalogue the planned coaching systems in `coaching/philosophies/coaching_systems.md`, with primary official resource links: `cts`, `evoke_endurance` (including the Uphill Athlete lineage), `swap`, `sharman_ultra`, `80_20_endurance`, and `lydiard`.
- [x] Align the `_template/` filenames and contents with the documented `summary.md`, `philosophy.md`, and `sources.md` structure.
- [ ] Update related files if needed: `card_authoring_guidance.md` and `card_hierarchy.md`.
- [x] Add card-level philosophy provenance: `philosophy_profile_ids` is a structured list, uses `common` for cards shaped only by the shared foundation, uses exact philosophy-directory names for other values, supports multiple profiles, and is shown in card preview/detail and Browse-mode filtering.
- [x] Define and enforce the card-relationship contract: adjacent-level `parent`/`child`, same-level `previous`/`next`/`alternative`, and cross-level non-structural `support`.
- [x] Convert the existing skipped-level structural links to `support`, preserving their coaching meaning without changing the pathway hierarchy.
- [x] Re-export and validate the 38-card local cache with schema 1.2 and `philosophy_profile_ids` set to `common`.
- [ ] Upload the validated schema-1.2 cache to the configured Google Drive source-of-truth library. This is pending a final explicit confirmation because it replaces JSON files in that external folder.
- [ ] Remove `training_cards/scripts/migrate_philosophy_profile_ids.py` only after the Drive upload succeeds; it remains as the rollback-safe migration path until then.

Reference files:

- `coaching/coaching_philosophy_old.md`
- `coaching/source_history_old.md`

Active files:

- `coaching/coaching_foundation.md`
- `coaching/philosophies/_template/source_history.md`

## Phase 3: Coaching Prompt Structure

Update the prompts after the note structure and coaching foundation are clearer.

Possible prompt work:

- improve `coaching/coaching_foundation.md`
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
- Write substantial coaching-philosophy points as labelled bullets, so individual ideas are easy to find and revise.
- Discuss direction before editing broad coaching content.
- Keep schema changes out of scope unless content work exposes a real need.
- Treat Google Drive JSON as the source of truth for card content.
- Use local card files as implementation artifacts, not the final authority.
- Keep card titles broad and reusable.
- Put trail-specific detail inside card content rather than making every card trail-only.
- Review coaching notes and prompts before rebuilding cards.
- Run validation after card JSON or synced content changes.

## Immediate Next Step

Complete the shared standards in `coaching/coaching_foundation.md`, then decide and define the first philosophy profile.

For now, keep each philosophy profile focused on these two files:

- `philosophy.md`
- `source_history.md`

Keep related topics inside that profile's `philosophy.md` first. Split them out later only if the profile becomes too large or hard to navigate.
