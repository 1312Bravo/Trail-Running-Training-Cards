# Training Cards Coaching Plan

This file is the working plan for improving the coaching folder, technical notes, prompt system, and card content in the Training Cards library.

Keep this file updated whenever the work plan, ordering, decisions, or completed phases change.

The current focus is content and coaching quality, not schema changes.

## Guiding Direction

The card library should feel like it was built by a thoughtful endurance coach with trail-running and mountain-running expertise.

Before building or expanding the cards, we first need to clarify:

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
- `coaching/philosophies/<profile>/sources.md`: reviewed sources, interpretation boundaries, and outstanding evidence work for that specific philosophy.
- `coaching/philosophies/_template/philosophy.md`: provisional topic structure for future philosophy profiles.
- `coaching/philosophies/_template/sources.md`: source-record scaffold for creating future profile histories.
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
- [ ] Review and refine the CTS profile against the user's source material before using exact protocol details that need direct primary-source confirmation.
- [x] Build matching `summary.md`, `philosophy.md`, and `sources.md` files for `evoke_endurance`; it is available for card authoring, with direct-source review still required for exact protocols.
- [x] Build matching `summary.md`, `philosophy.md`, and `sources.md` files for `swap`; it is available for card authoring, with a deeper primary-source base still needed for exact workout structures.
- [x] Build matching `summary.md`, `philosophy.md`, and `sources.md` files for `sharman_ultra`; it is available for card authoring, with a deeper primary-source base still needed for exact workout structures.
- [x] Build matching `summary.md`, `philosophy.md`, and `sources.md` files for `80_20_endurance`; it is available for card authoring, with primary-book review still required for exact protocols.
- [x] Build matching `summary.md`, `philosophy.md`, and `sources.md` files for `lydiard`; it is available for card authoring, with primary-source review still required for exact historical prescriptions.
- [x] Expand all current system profiles into long-form interpretations with comparable structure: coaching principles, training load and adaptation, trail and mountain application, knowledge and decision-making, card implications, and current limits. All current profiles are available for card authoring; their source boundaries remain explicit.
- [x] Expand each current profile's `summary.md` and `sources.md` alongside the long-form philosophy, separating reviewed material from direct-source work still required.
- [x] Create and maintain a `sources.md` record inside each philosophy profile.
- [x] Define philosophy profiles as documented, source-grounded interpretations of named coaching systems or teams; add `coaching/philosophies/README.md` to set folder structure, source standards, profile-ID rules, and the shared-foundation boundary.
- [x] Catalogue the planned coaching systems in `coaching/philosophies/coaching_systems.md`, with primary official resource links: `cts`, `evoke_endurance` (including the Uphill Athlete lineage), `swap`, `sharman_ultra`, `80_20_endurance`, and `lydiard`.
- [x] Align the `_template/` filenames and contents with the documented `summary.md`, `philosophy.md`, and `sources.md` structure.
- [ ] Update related files if needed: `card_authoring_guidance.md` and `card_hierarchy.md`.
- [x] Add card-level philosophy provenance: `philosophy_profile_ids` is a structured list, uses exact philosophy-directory names, supports multiple profiles, and is shown in card preview/detail and Browse-mode filtering.
- [x] Create `training_cards/philosophy_profiles.py` as the single local registry of valid profile IDs and display names. Use it in card validation and Streamlit rendering/filtering; cards store only stable IDs.
- [x] Define and enforce the card-relationship contract: adjacent-level `parent`/`child`, same-level `previous`/`next`/`alternative`, and cross-level non-structural `support`.
- [x] Convert the existing skipped-level structural links to `support`, preserving their coaching meaning without changing the pathway hierarchy.
- [x] Remove `common` as card-level provenance. The shared coaching foundation is always-on and not stored on cards.
- [x] Publish the validated schema-1.2 replacement library to Google Drive and configure it as the source of truth.
- [x] Remove the obsolete one-off migration scripts after the verified replacement cutover.

Active files:

- `coaching/coaching_foundation.md`
- `coaching/philosophies/_template/sources.md`

## Phase 3: Coaching Prompt Structure

Update the prompts after the note structure and coaching foundation are clearer.

Possible prompt work:

- improve `coaching/coaching_foundation.md`
- improve `coaching/card_authoring_guidance.md`
- separate card creation guidance from card review guidance if useful
- make the prompt clearer about field purpose and coaching voice
- define how much evidence, specificity, and trail adaptation each card needs

## Phase 4: Card Build Plan

Status: active. The 33-card macro seed library is the configured and validated source of truth. Mezzo, micro, and session cards still need to be built from the same card-matrix and philosophy-specific review process.

Goals:

- improve existing card content
- add missing cards
- make cards more specific and useful without becoming too narrow
- improve consistency across macro, mezzo, micro, and session levels
- strengthen references between cards
- keep preview fields concise and detail fields genuinely useful

Likely build order:

1. Macro cards
2. Mezzo block cards
3. Micro week cards
4. Session workout cards
5. Session family support content

Replacement workflow:

- [x] Define the explicit validated replacement workflow in `notes/card_library_rebuild_workflow.md`.
- [x] Add direct active-library replacement tooling. Do not change ordinary `upload_cache` into a deletion command.
- [x] Export, validate, upload, download, and verify the 33-card macro seed library.
- [x] Replace the active Drive library contents in place and update `training_cards/cloud_config.py` with the recreated folder IDs.
- [x] Refresh the active local cache from Drive and validate it.
- [x] Remove obsolete local staging, archive, and migration artifacts after verification.

Current seed-library scope:

- [x] Define macro phase types with coach reasoning in `training_cards/cards/card_matrix.md`.
- [x] Author mainstream macro cards for all accepted baseline macro types.
- [x] Review each named philosophy against the accepted macro types.
- [x] Apply the specificity standard strictly and keep only meaningfully distinct named-philosophy macro cards.
- [x] Upload the verified 33-card macro seed library to Google Drive.
- [x] Review each named philosophy for additional macro-specific phase types that are not covered by the accepted mainstream macro taxonomy.
- [x] Refactor the accepted special macro types into existing stable macro IDs: `macro_type_lydiard_hill_resistance_transition` as `macro_017` and `macro_type_evoke_muscular_endurance_development` as `macro_025`.
- [ ] Build mezzo cards from the accepted macro structure.
- [ ] Build micro cards after mezzo structure is accepted.
- [ ] Build session cards after micro structure is accepted.

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
- Write substantial coaching-philosophy points under clear mini-section headings with explanatory paragraphs, so individual ideas are easy to find and revise without becoming fragmented bullets.
- Discuss direction before editing broad coaching content.
- Keep schema changes out of scope unless content work exposes a real need.
- Treat Google Drive JSON as the source of truth for card content.
- Use local card files as implementation artifacts, not the final authority.
- Keep card titles broad and reusable.
- Put trail-specific detail inside card content rather than making every card trail-only.
- Review coaching notes and prompts before building cards.
- Run validation after card JSON or synced content changes.

## Immediate Next Step

Build mezzo cards from the accepted macro structure. New cards may use any registered philosophy profile when its distinctive reasoning materially shapes the card. Do not use `common` as card-level provenance.

Each profile now uses three files:

- `summary.md`
- `philosophy.md`
- `sources.md`

Keep related topics inside that profile's `philosophy.md` first. Split them out later only if the profile becomes too large or hard to navigate.
