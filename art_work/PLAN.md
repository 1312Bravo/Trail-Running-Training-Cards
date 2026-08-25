# Art Work Plan

## Goal

Create an original trading-card-inspired visual system for the training-card app. It should make cards recognisable and connected at a glance while keeping the coaching content primary.

## Current Decisions

- `art_work/` is a root-level area for visual work that belongs to the Streamlit app but stays separate from app code and the core training-card library.
- Google Drive JSON remains the source of truth for coaching content. Artwork metadata and image files will not be added to the card JSON during the first version.
- Each card will have one stable avatar. The avatar will not change when the card appears in different pathways.
- A card's visual identity comes from the shared visual system, its planning-level visual class, and its card-specific avatar brief.
- Coaching relationships are a graph, not a strict family tree. They will be shown by app links and contextual cues, never by avatar inheritance.
- The visual direction will be original and mature, inspired by collectible-card information hierarchy rather than Pokemon, Yu-Gi-Oh!, or any existing characters or artwork.
- The approved working visual is a transparent, mature guardian-animal line avatar for white cards: slate primary lines, pale-slate detail, a muted-gold mark, and no visual background.
- Macro, Mezzo, Micro, and Session are distinct visual classes. Their pose, framing, and restrained accent colour create same-level resemblance without literal parent-child families.
- The first pilot pathway is `Base Development` -> `Endurance Development Block` -> `Long Run Focus Week` -> `Long Run`. It is a coherent endurance lineage and already exists as a complete app pathway.
- The pilot will introduce artwork only in the app presentation layer. It will use a separate art catalog and local image files, never new fields in the Google Drive card JSON.

## Tasks

- [x] Create the root-level `art_work/` workspace and its working documents.
- [x] Agree the working visual world, mood, and guardian-avatar direction.
- [x] Define the first visual role of Macro, Mezzo, Micro, and Session cards.
- [x] Create the shared and planning-level prompt system in `prompts/`.
- [x] Select one complete Macro -> Mezzo -> Micro -> Session pathway as a four-card pilot.
- [x] Add one temporary shared ibex line-avatar to every browse-card header to evaluate artwork placement before assigning individual avatars.
- [x] Create one transparent SVG Macro line-avatar example under `assets/prototype/macro/`.
- [x] Test and retire the literal Macro -> Mezzo visual-inheritance idea; use planning-level prompts instead.
- [x] Create one independent prompt-system prototype at each planning level: Macro, Mezzo, Micro, and Session.
- [x] Define visible coloured planning-level symbols: mountain, trail marker, compass, and stopwatch.
- [ ] Apply the unique-silhouette and planning-level colour review to the four-level prototype before generating more avatars.
- [ ] Review the four active planning-level examples together before connecting any individual card art to the app.
- [ ] Define 4-6 controlled visual affinities and assign them to the pilot cards. Deferred until after the first four-image pilot is reviewed.
- [ ] Review and refine the Macro master avatars for species readability and mature linework.
- [ ] Write one card-specific brief for the first card at each planning level.
- [ ] Generate or draw candidate art using the common prompt, one planning-level prompt, and one card brief.
- [ ] Approve one production image per pilot card after a side-by-side consistency review.
- [ ] Create an art catalog with card id, image path, and alt text.
- [ ] Define image dimensions, file format, file naming, and repository location for approved assets.
- [ ] Define a no-art fallback: retain the existing planning-level icon and layout when the catalog entry or asset is absent.
- [ ] Add a read-only art-catalog loader that cannot block card-library loading.
- [ ] Add the pilot art to the card detail header first, then decide whether browse-grid thumbnails improve scanning.
- [ ] Test missing-art, narrow-screen, and normal-pathway behavior in the running Streamlit app.
- [ ] Expand one visual family or one pathway at a time only after the pilot is accepted.

## Guardrails

- Do not change coaching content, card schemas, or Google Drive JSON only to support artwork.
- Do not generate all card art before one complete pathway has been reviewed in the app.
- Do not use copyrighted characters, logos, card layouts, or artwork from existing games.
- Every future card must have a graceful fallback when its individual artwork has not yet been approved.

## Proposed Art Storage

Keep artwork separate from Google Drive card JSON, but inside this repository so the app can load approved assets locally.

```text
art_work/
  assets/
    prototype/             # Short-lived layout tests, grouped by planning level.
  prompts/                 # Common, planning-level, and card-specific prompt files.
  catalog.json             # The app-facing mapping from card id to image path and alt text.
```

Use stable, card-id-based names for final assets, for example `macro_002.svg` or `macro_002.webp`.

The catalog should contain only the decision the app needs: card id, image path, and alt text. Prototype assets never need to be loaded by the app.

## Open Questions

- Should the first production family remain purely alpine guardian animals, or should later families include terrain guardians or abstract spirits?
- Which exact affinities should form the first controlled vocabulary? The likely pilot set is aerobic development, endurance, fueling, durability, and trail terrain.
- Should browse cards show a small cropped portrait immediately, or should imagery stay detail-view-only until readability has been tested?

## Recommended Build Order

1. Complete and approve the four pilot images outside the app.
2. Add the catalog, image directory, and no-art fallback.
3. Add art to the detail header, where its value is clearest and space is available.
4. Review the full pathway and mobile layout in Streamlit.
5. Add restrained browse-grid artwork only if it improves recognition without crowding the coaching summary.
6. Expand from the pilot deliberately, keeping one approved avatar per card.
