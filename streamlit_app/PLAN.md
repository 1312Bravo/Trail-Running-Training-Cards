# Plan

## Goal

Add a Coaching philosophies area to the Streamlit app so the new philosophy profiles are visible, understandable, and connected to the training cards without turning the app into a documentation browser.

## Current Understanding

- The canonical coaching source files live under `coaching/`.
- The Streamlit app uses short app-facing summaries by default and loads a full source note only when the reader requests it.
- App-facing philosophy markdown belongs under `streamlit_app/content/philosophies/`.
- The app-facing content files and Coaching philosophies mode are implemented.

## Critical Review

- Strong: this makes the philosophy work discoverable and useful for browsing cards.
- Strong: keeping app copy separate from source notes avoids mixing content-authoring documentation with UI presentation.
- Risk: if the app-facing summaries drift from the source philosophy notes, the app can become misleading.
- Recommendation: treat `coaching/philosophies/<id>/summary.md` as the source and refresh app summaries whenever profiles change materially.

## Proposed Direction

- Add one markdown file per philosophy profile in `streamlit_app/content/philosophies/`.
- Keep each file short: title, official website link where applicable, overview, main emphases, and a concise interpretation note.
- In the Coaching philosophies mode, show profile overview cards with card counts, a `Show cards` action, and an on-demand full-note dialog.
- Keep philosophy filtering available in `Browse cards`, but make the overview mode the more explanatory entry point.

## Tasks

- [x] Create app-facing philosophy markdown files.
- [x] Add a loader for app-facing philosophy markdown.
- [x] Add a `Coaching philosophies` mode in `streamlit_app/app.py`.
- [x] Render philosophy profile overview cards.
- [x] Show card counts by philosophy profile.
- [x] Add `Show cards` action that switches to Browse mode with that philosophy selected.
- [x] Add a `Read full philosophy` dialog that renders the detailed coaching note.
- [x] Add a `View sources` dialog that shows only reviewed-source bullets and links.
- [ ] Decide whether philosophy filters should also apply to Build pathway and Today session.

## Decisions

- The app-facing files are presentation copy, not the source of truth.
- The source of truth remains the `coaching/` directory plus `training_cards/philosophy_profiles.py`.
- App-facing pages do not show internal source paths or profile IDs.
- Named profiles link to their official website; the shared `Common` foundation has no external counterpart.
- The detailed coaching note opens only on request in a large dialog; it is not mixed into the overview cards.
- Named profiles expose only their reviewed official-source bullets in the app; books-to-review and interpretation boundaries stay in the working source notes.
- We are not implementing ranking or recommendation logic as part of this feature.

## Open Questions

- Should `common` appear as a full philosophy profile card or as a quieter shared-foundation card?
- Should Browse-mode philosophy filters move from multiselect to visible chips?

## Progress

- Created this temporary plan in `streamlit_app/PLAN.md`.
- Created app-facing markdown summaries under `streamlit_app/content/philosophies/`.
- Added a Coaching philosophies app mode with profile summaries, card counts, and direct links into Browse cards.
- Added a large dialog for reading the detailed coaching note behind each profile.
- Added a source dialog for each named profile, limited to reviewed official material and its links.
