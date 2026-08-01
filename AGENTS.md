# AGENTS.md

## Purpose
This repository contains the standalone Training Cards library.

## Working Principles
- Treat Google Drive JSON as the source of truth for card content.
- Use training_cards/local_cache/ only as a temporary downloaded working copy.
- Run validation after editing JSON or syncing with Drive.
- Consult prompts/coach_card_creation_prompt.md before changing card content, schemas, or coaching logic.
- Keep code readable and avoid unnecessary abstraction.
- Preserve secrets and local cache files out of git.

## Reusable Skills
- Use data-science-project-workflow for analysis, evidence notes, or data-backed card review.
- Use vibecode-app-builder only when changing workflows, docs, future app integration, or project structure.
- Use developing-with-streamlit only when working on the separate Training Platform Streamlit app.
- Reusable skill source files live in C:\Users\Urh\Desktop\Urh\Github Repositories\Codex-Instructions\skills\ and installed copies live under C:\Users\Urh\.codex\skills\.
