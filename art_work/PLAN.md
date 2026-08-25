# Art Work Plan

## Goal

Create an original trading-card-inspired visual system for the training-card app. It should make cards recognisable and connected at a glance while keeping the coaching content primary.

## Current Decisions

- `art_work/` is a root-level area for visual work that belongs to the Streamlit app but stays separate from app code and the core training-card library.
- Google Drive JSON remains the source of truth for coaching content. Artwork metadata and image files will not be added to the card JSON during the first version.
- Each card will have one stable avatar. The avatar will not change when the card appears in different pathways.
- A card's planning level, primary visual family, and visual affinities will create its visual identity.
- Coaching relationships are a graph, not a strict family tree. A card with multiple parent links will use shared motifs and contextual cues rather than multiple competing avatars.
- The visual direction will be original and mature, inspired by collectible-card information hierarchy rather than Pokemon, Yu-Gi-Oh!, or any existing characters or artwork.
- The approved working visual is polished slate-and-silver guardian concept art in a misty navy alpine world, with thin mountain lines, a subtle trail, cool rim light, and a muted-gold lineage mark.
- A curated four-card visual lineage can progress from a mature Macro guardian to progressively younger Mezzo, Micro, and Session descendants. Age, pose, and a restrained neon accent distinguish the planning level.

## Tasks

- [x] Create the root-level `art_work/` workspace and its working documents.
- [x] Agree the working visual world, mood, and guardian-avatar direction.
- [x] Define the first visual role of Macro, Mezzo, Micro, and Session cards.
- [x] Record the reusable prompt contract in `PROMPT_GUIDE.md`.
- [ ] Define a small controlled set of shared visual affinities.
- [ ] Define the first primary visual families and their reusable reference artwork.
- [ ] Agree the artwork catalog format, naming rules, and missing-art fallback.
- [ ] Select one complete Macro -> Mezzo -> Micro -> Session pathway as a four-card pilot.
- [ ] Write and review the four card-art briefs.
- [ ] Generate and approve pilot artwork before changing the Streamlit UI.
- [ ] Add the artwork loader and preview-card placement in the app.
- [ ] Review the pilot in the running app before expanding to more cards.

## Guardrails

- Do not change coaching content, card schemas, or Google Drive JSON only to support artwork.
- Do not generate all card art before one complete pathway has been reviewed in the app.
- Do not use copyrighted characters, logos, card layouts, or artwork from existing games.
- Every future card must have a graceful fallback when its individual artwork has not yet been approved.

## Open Questions

- Should avatars be animals, terrain guardians, human-like explorers, abstract spirits, or a combination?
- Which visual affinities should be shared across cards, and which should remain card-specific?
- How prominent should artwork be in the preview card compared with the coaching text?
