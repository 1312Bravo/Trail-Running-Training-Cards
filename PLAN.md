# Training Cards Plan

This is the current working plan for the Training Cards library. Keep durable documentation in `notes/`, coaching knowledge in `coaching/`, and card taxonomy decisions in `training_cards/cards/card_matrix.md`.

## Current State

- Google Drive JSON is the source of truth for accepted card content.
- The local cache at `training_cards/local_cache/cloud_library/` is the temporary working copy.
- The Drive-backed library has been verified at 365 cards: 33 macro, 78 mezzo, 177 micro, and 77 session cards.
- Reuse metadata is active for macro-to-mezzo, mezzo-to-micro, and micro-to-session inheritance.
- The old full Python seed-card library has been retired.
- Four Python examples remain under `training_cards/cards/examples/` for macro, mezzo, micro, and session authoring.
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

## Working Rules

- Treat Google Drive JSON as the accepted card-content source of truth.
- Use the local cache as a temporary working copy, not as permanent storage.
- Use Python card classes only as examples or temporary authoring scaffolding.
- Validate after editing JSON, syncing with Drive, changing schema behavior, or changing reuse metadata.
- Consult `coaching/coaching_foundation.md`, `coaching/card_authoring_guidance.md`, and the relevant philosophy profile before changing coaching content.
- Apply the philosophy-specificity standard strictly: create named-philosophy cards only when they change app choice, explanation, structure, filtering, or sequencing meaningfully.
- After each substantial work block, review for overlap, missing pieces, level fit, naming, local/cloud/doc alignment, and app impact.

## Next Step

Review the final cleanup state and decide whether empty old card folders should remain as structural placeholders or be removed now that real card content lives in Drive JSON.

## Documentation Map

- `README.md`: short repository orientation and common commands.
- `AGENTS.md`: rules Codex should follow in this repository.
- `notes/README.md`: documentation map.
- `notes/cloud_library_storage_workflow.md`: cloud/cache workflow, Drive structure, and authoring helper workflow.
- `notes/schema_design_and_validation.md`: schema fields, validation, registry, pathway, and session workout structure.
- `notes/card_library_rebuild_workflow.md`: full-library replacement safeguards.
- `training_cards/cards/card_matrix.md`: card taxonomy, coach reasoning, philosophy review, and build decisions.
