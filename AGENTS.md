# AGENTS.md

## Purpose
This repository contains the standalone Training Cards library.

## Working Principles
- Treat Google Drive JSON as the source of truth for card content.
- Use training_cards/local_cache/ only as a temporary downloaded working copy.
- Use training_cards/cards/examples/ as Python authoring references only; do not maintain a full duplicate Python seed-card library beside the Drive JSON library.
- Run validation after editing JSON or syncing with Drive.
- Keep routine checks proportional to the change:
  - Avatar-only SVG changes usually need visual preview, not automated tests.
  - CSS or card-layout styling changes usually need app preview; run focused checks only when Python rendering logic changes.
  - Python renderer, catalog, or cloud-sync changes should get a focused compile or targeted test.
  - Full test runs are for larger checkpoints, schema/content changes, or deployment prep.
- Consult coaching/coaching_foundation.md, coaching/card_authoring_guidance.md, and the relevant coaching philosophy profile before changing card content, schemas, or coaching logic.
- Keep code readable and avoid unnecessary abstraction.
- Preserve secrets and local cache files out of git.

## Reusable Skills
- Use data-science-project-workflow for analysis, evidence notes, or data-backed card review.
- Reusable skill source files live in C:\Users\Urh\Desktop\Urh\Github Repositories\Codex-Instructions\skills\ and installed copies live under C:\Users\Urh\.codex\skills\.
