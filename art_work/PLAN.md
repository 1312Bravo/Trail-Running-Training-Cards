# Art Work Plan

## Goal

Create an original trading-card-inspired visual system for the training-card app. It should make cards recognisable and connected at a glance while keeping the coaching content primary.

## Current Decisions

- `art_work/` is a root-level area for visual work that belongs to the Streamlit app but stays separate from app code and the core training-card library.
- Google Drive JSON remains the source of truth for coaching content. Artwork metadata and image files will not be added to the card JSON during the first version.
- Artwork connects to cards by card id through a separate catalog. The card schema does not need to change for the local pilot.
- Each card will have one stable avatar. The avatar will not change when the card appears in different pathways.
- A card's visual identity comes from the shared visual system, its planning-level visual class, and its card-specific avatar brief.
- Coaching relationships are a graph, not a strict family tree. They will be shown by app links and contextual cues, never by avatar inheritance.
- The visual direction will be original and mature, inspired by collectible-card information hierarchy rather than Pokemon, Yu-Gi-Oh!, or any existing characters or artwork.
- The working visual is a transparent, mature guardian-animal line avatar for white cards: slate primary lines, pale-slate detail, a quiet soft-gray personal mark, and no visual background.
- Macro, Mezzo, Micro, and Session are distinct visual classes. Their coloured mountain, trail-marker, compass, and stopwatch symbols create same-level resemblance without literal parent-child families.
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
- [x] Create a local preview catalog for the four pilot card ids with `level`, `asset_path`, `alt_text`, and optional filtering `tags`.
- [ ] Define stable final file names and choose SVG or WebP per approved asset.
- [x] Add a safe local catalog loader that returns artwork by card id without changing card schemas or rendering yet.
- [x] Add a neutral fallback avatar for cards without approved artwork, while keeping missing catalog entries detectable.
- [x] Replace the obsolete global shared-image renderer hook with a safe per-card catalog lookup.
- [x] Define an artwork fallback: show the neutral fallback avatar when an approved card-specific asset is absent.
- [x] Add local catalog artwork to browse cards only, then review the running app.
- [x] Adjust browse-card layout so the planning-level badge sits near the top, the title leads the card, and the larger avatar appears before the coaching fields.
- [x] Refine browse-card level separation with visible card tinting, a stronger level-colored avatar panel, and neutral uppercase level labels.
- [x] Render preview avatars as plain HTML images so Streamlit does not show a fullscreen hover control.
- [x] Tune the browse-card collectible style with lighter card color, stronger black borders, translucent buttons, and glowier avatar panels.
- [x] Move browse-card title above the level/action row and strengthen the collectible-card border/gloss treatment.
- [x] Replace star-like avatar highlights with a subtler holo-style wash over the smoother level-colored art panel.
- [x] Increase browse-card border weight, avatar-panel border weight, and holo texture visibility.
- [x] Make the browse-card border visually heavier with an outer black outline and replace line-only holo with an embedded sparkle texture.
- [x] Remove the experimental sparkle/holo overlays and return the browse-card border to a restrained black collectible-card frame.
- [x] Remove the rejected sparkle texture asset, switch browse-card borders to gray, and make the lower card area more deliberately framed.
- [x] Refine lower preview metadata rows with soft stat bands and stronger label hierarchy without adding more borders.
- [x] Restore lower metadata divider lines, use title-case labels, vertically center row labels, polish buttons, and strengthen avatar-panel color.
- [ ] Test the four art cards, cards without art, narrow screens, and ordinary pathway browsing.
- [ ] Add art to the detail header only after browse-card placement is accepted.
- [ ] Promote locally accepted assets to the web catalog only when they are approved.
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
  catalog.json             # The app-facing mapping from card id to level, image path, alt text, and tags.
```

Use stable, card-id-based names for final assets, for example `macro_002.svg` or `macro_002.webp`.

The catalog should stay flat by card id for fast rendering. Each entry should include `level`, `asset_path`, and `alt_text`; optional tags can support future filtering, duplicate checks, and progress tracking without changing the training-card schema.

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
