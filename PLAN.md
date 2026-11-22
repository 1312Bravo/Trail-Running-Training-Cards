# Training Cards Plan

This is the current working plan for the Training Cards library. Keep durable documentation in `notes/`, coaching knowledge in `coaching/`, and card taxonomy decisions in `training_cards/cards/card_matrix.md`.

## Current State

- Google Drive JSON is the source of truth for accepted card content.
- The local cache at `training_cards/local_cache/cloud_library/` is the temporary working copy.
- The Drive-backed library has been verified at 375 cards: 34 macro, 80 mezzo, 182 micro, and 79 session cards (library 0.10.0).
- Reuse metadata is active for macro-to-mezzo, mezzo-to-micro, and micro-to-session inheritance.
- The old full Python seed-card library has been retired.
- Four Python examples remain under `training_cards/cards/examples/` for macro, mezzo, micro, and session authoring.
- Empty hierarchy/profile folders remain under `training_cards/cards/<level>/<profile>/` with `.gitkeep` placeholders so the intended structure is visible in Git.
- Workflow templates exist for one-card cloud JSON to Python authoring and Python-authored card upload through the local cache.

## Active Goals

- Keep the library source-of-truth structure clean: Drive JSON first, local cache second, Python examples only for authoring.
- Keep card taxonomy and philosophy-review reasoning clear in `training_cards/cards/card_matrix.md`.
- Keep cloud/cache workflow instructions centralized in `notes/cloud_library_storage_workflow.md`.
- Keep schema and validation behavior centralized in `notes/schema_design_and_validation.md`.
- Continue future card changes through validated cache JSON and targeted cloud upload scripts.

## Recently Completed

- Added `mainstream_endurance` as a normal coaching philosophy profile.
- Removed `common` as card-level provenance.
- Built accepted macro, mezzo, micro, and session card layers.
- Added app-facing reuse metadata files: `macro_mezzo_reuse.json`, `mezzo_micro_reuse.json`, and `micro_session_reuse.json`.
- Redefined session cards as `SessionCard -> WorkoutBlock -> WorkoutOption -> SessionPart`.
- Uploaded and verified the 365-card Drive library.
- Removed generated Python card modules and old seed-export scripts.
- Added four card-authoring examples and guarded workflow templates.
- Refactored documentation ownership so README, notes, card matrix, AGENTS, and PLAN have clearer roles.
- Kept local card hierarchy folders with `.gitkeep` placeholders while keeping accepted card content in Drive/cache JSON.

## Working Rules

- Treat Google Drive JSON as the accepted card-content source of truth.
- Use the local cache as a temporary working copy, not as permanent storage.
- Use Python card classes only as examples or temporary authoring scaffolding.
- Validate after editing JSON, syncing with Drive, changing schema behavior, or changing reuse metadata.
- Consult `coaching/coaching_foundation.md`, `coaching/card_authoring_guidance.md`, and the relevant philosophy profile before changing coaching content.
- Apply the philosophy-specificity standard strictly: create named-philosophy cards only when they change app choice, explanation, structure, filtering, or sequencing meaningfully.
- After each substantial work block, review for overlap, missing pieces, level fit, naming, local/cloud/doc alignment, and app impact.

## Next Step

Use the app and continue card/content work from the Drive/cache JSON workflow. The local card hierarchy folders are structural placeholders only.

## Documentation Map

- `README.md`: short repository orientation and common commands.
- `AGENTS.md`: rules Codex should follow in this repository.
- `notes/README.md`: documentation map.
- `notes/cloud_library_storage_workflow.md`: cloud/cache workflow, Drive structure, and authoring helper workflow.
- `notes/schema_design_and_validation.md`: schema fields, validation, registry, pathway, and session workout structure.
- `notes/card_library_rebuild_workflow.md`: full-library replacement safeguards.
- `training_cards/cards/card_matrix.md`: card taxonomy, coach reasoning, philosophy review, and build decisions.

## Session library fixes 2026-11-22

### Goal

Make base sessions discoverable across philosophies and make session cards usable when selected directly from Browse.

### Tasks

- [x] Restore a validated working cache from the current Drive library.
- [x] Include explicit philosophy reuse and phase context in search without crossing philosophy boundaries.
- [x] Revise all session placement, readiness, option selection, and progression guidance.
- [x] Correct duration, repetition, warm-up, strength, calibration, and environmental instructions.
- [x] Add the mainstream Repeatable Aerobic Benchmark and connect appropriate weeks and philosophy reuse.
- [x] Validate content and app behavior, update documentation, sync Drive, and verify readback.

### Decisions

- Preserve stable card identities and existing schemas.
- Keep reusable mainstream content shared through explicit reuse metadata.
- Expand environmental exposure options within existing cards.
- Keep the benchmark submaximal and observational, with no inferred physiological thresholds.
- The user approved implementing the review findings and proposed benchmark on 2026-11-22.

### Progress

- Reviewed 77 existing sessions, philosophy guidance, and the app search implementation.
- Revised those sessions and added one shared benchmark. All 78 session files and seven root JSON files match Drive readback.
- Cache validation and the 78-session content audit pass. All 20 Python tests and six discovery checks pass. Browser checks verified Mainstream and CTS base search and revised session details.
- The production build and deployment ZIP are prepared for the existing manual Netlify publishing workflow.

## Full pipeline review 2026-11-22

- [x] Review current Drive library 0.9.0 across all four levels and seven philosophies.
- [x] Check effective hierarchy coverage including reuse, weekly structure, and session roles.
- [x] Record findings and proposed titles/placement in `training_cards/cards/card_matrix.md`.
- Structural validation passes, and all effective cards are reachable with no dead ends. Semantic review finds inappropriate recovery-session edges, missing key-session connections, generic week structures, and absent block/week transition links.
- Proposed first batch: four cards for the missing Lydiard anaerobic-development stage, one Evoke aerobic-threshold assessment session, and one optional accumulated-endurance micro week.
- The user approved implementing all review findings on 2026-11-22.

### Implementation

- [x] Rewrite all micro week rhythms, entry conditions, progression, and recovery choices.
- [x] Repair missing session roles, incompatible recovery edges, and base/capacity connections.
- [x] Add meaningful block and week transitions and easier alternatives.
- [x] Author the six accepted additions and complete environmental, downhill, low-light, and pole follow-ups.
- [x] Add focused heat preparation at block/week level where repeated exposures change the load pattern.
- [x] Audit all effective philosophy pathways, build the app, sync changed JSON, and verify Drive readback.

Completed release: nine additions and 282 revised cards. All 375 individual card files and seven root files agree with Drive readback. The verified bundle passes the pipeline audit across all seven philosophies. All 23 Python tests, eight app discovery checks, TypeScript checking, content audits, and the production build pass. The deployment ZIP contains the matching card library and seven philosophy profiles. Publishing that ZIP to the existing Netlify project remains the established manual deployment step.
