# Art Work Plan

Status: archived locally. The Streamlit app does not use artwork today; preview
cards currently render without avatars, artwork backgrounds, or block-logo
overlays. Keep this plan as history and possible future reference, not as active
implementation scope.

## Goal

Create an original trading-card-inspired visual system for the training-card app. It should make cards recognisable and connected at a glance while keeping the coaching content primary.

## Archived Decisions

- `archive/artwork/` is a local archive for visual work that used to sit beside the Streamlit app.
- Google Drive JSON remains the source of truth for coaching content. Artwork metadata and image files will not be added to the card JSON during the first version.
- The archived artwork catalog connects artwork experiments to cards by card id. The active app no longer reads this catalog.
- Each card will have one stable avatar. The avatar will not change when the card appears in different pathways.
- A card's visual identity comes from the shared visual system, its planning-level visual class, and its card-specific avatar brief.
- Coaching relationships are a graph, not a strict family tree. They will be shown by app links and contextual cues, never by avatar inheritance.
- The visual direction will be original and mature, inspired by collectible-card information hierarchy rather than Pokemon, Yu-Gi-Oh!, or any existing characters or artwork.
- The working visual is a transparent, mature guardian-animal line avatar for white cards: slate primary lines, pale-slate detail, a quiet soft-gray personal mark, and no visual background.
- Macro, Mezzo, Micro, and Session are distinct visual classes. Their coloured mountain, trail-marker, compass, and stopwatch symbols create same-level resemblance without literal parent-child families.
- Planning-level colour moods use the `Mystic Training Elements` palette: `Frost` for Macro, `Verdant` for Mezzo, `Ember` for Micro, and `Radiance` for Session. The mostly white card body should stay calm while these colours live primarily in the avatar window.
- Avatar-window backgrounds use project-local stylized SVG scenery over the block colour panels: big mountains for Macro, smaller hills for Mezzo, meadow for Micro, and macadam singletrack for Session.
- The first pilot pathway is `Base Development` -> `Endurance Development Block` -> `Long Run Focus Week` -> `Long Run`. It is a coherent endurance lineage and already exists as a complete app pathway.
- The former pilot introduced artwork only in the app presentation layer. That integration has been retired; the files remain here only for reference.

## Tasks

- [x] Create the original artwork workspace and its working documents.
- [x] Agree the working visual world, mood, and guardian-avatar direction.
- [x] Define the first visual role of Macro, Mezzo, Micro, and Session cards.
- [x] Create the shared and planning-level prompt system in `prompts/`.
- [x] Select one complete Macro -> Mezzo -> Micro -> Session pathway as a four-card pilot.
- [x] Add one temporary shared ibex line-avatar to every browse-card header to evaluate artwork placement before assigning individual avatars.
- [x] Create one transparent SVG Macro line-avatar example under `assets/avatars/macro/`.
- [x] Test and retire the literal Macro -> Mezzo visual-inheritance idea; use planning-level prompts instead.
- [x] Create one independent prompt-system draft at each planning level: Macro, Mezzo, Micro, and Session.
- [x] Define visible coloured planning-level symbols: mountain, trail marker, compass, and stopwatch.
- [ ] Apply the unique-silhouette and planning-level colour review to the four-level draft before generating more avatars.
- [ ] Review the four active planning-level examples together before connecting any individual card art to the app.
- [ ] Define 4-6 controlled visual affinities and assign them to the pilot cards. Deferred until after the first four-image pilot is reviewed.
- [ ] Review and refine the Macro master avatars for species readability and mature linework.
- [ ] Write one card-specific brief for the first card at each planning level.
- [ ] Generate or draw improved art using the common prompt, one planning-level prompt, and one card brief.
- [ ] Approve one production image per pilot card after a side-by-side consistency review.
- [x] Create a local preview catalog for the four pilot card ids with `level`, `asset_path`, `alt_text`, and optional filtering `tags`.
- [ ] Keep stable card-id-based file names and choose SVG or WebP per approved asset.
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
- [x] Capitalize preview suitable-level values, render preview tags as clickable underlined labels, and remap planning-level card colors.
- [x] Bring opened-card detail view closer to preview styling with a tinted card shell, avatar panel, title-first header, and clickable label tags.
- [x] Refine opened-card detail into a calmer card-back view with no large avatar, a coloured title band, compact key facts, quieter coaching note, and single-item lists without bullets.
- [x] Tighten opened-card spacing, remove coaching-note borders, move summary below the title, style key facts more strongly, and replace raw session/reference markdown bullets.
- [x] Remove the remaining opened-card inner frame, strengthen summary/key-fact hierarchy, add support-section dividers, promote session workout structure, and align preview type-symbol colors.
- [x] Rework opened-card title into a thin level strip, improve summary as description text, make references clickable card links, remove session-family internal tags, and drop last-section dividers.
- [x] Replace the opened-card title strip with a top-left diagonal level accent, naturalise summary text, and restore duration/RPE as the primary workout-part line.
- [x] Add level-specific fallback avatars, force reference-card links to rerun into the parent card, and replace the detail accent with thicker four-corner patches.
- [x] Fix opened-card reference navigation without callback rerun warnings, narrow modal positioning CSS, and prevent duplicated duration units.
- [x] Add opened-card back navigation after reference jumps and switch avatar block symbols from level color to quiet charcoal.
- [x] Move avatar block symbols into a consistent top-right emblem position across pilot and fallback assets.
- [x] Push avatar block symbols further into the top-right corner while keeping them inside the SVG canvas.
- [x] Move block symbols out of the avatar SVGs and render them as top-right avatar-panel overlays.
- [x] Test a more collectible preview-card treatment with lighter card tint, framed art window, emblem badge, subtype strip, effect-style summary, subtle level rail, and collector footer.
- [x] Refine preview-card collectible layout with shared meta/action row, full inner level frame, stronger emblem badge, clickable footer tags, and more playful summary typography.
- [x] Soften preview-card title, summary, footer tags, and emblem badge shape after visual review.
- [x] Further reduce preview title, summary, subtype strip, and footer-tag visual weight.
- [x] Rebalance preview subtype strip, summary, and footer-tag text after the first reduction became too small.
- [x] Pale down full-card level tint, quiet the avatar block badge, and vary pilot avatar gender marks 50/50 off the animal body.
- [x] Move avatar gender marks from SVG files into the renderer so fallback and future cards alternate per card id, and unify preview card borders with a warm brown frame.
- [x] Restore avatar gender marks inside SVG assets, move fallback marks off-center, strengthen mark visibility, and make preview card frames uniformly warm brown.
- [x] Add a richer collectible color pass with paler card bodies, jewel-toned avatar windows, metallic art frames, and distinct level-specific fallback avatars.
- [x] Tighten preview-card internal spacing while preserving card dimensions, and reduce the block badge size.
- [x] Add preview-card nameplates, level pips, a quieter effect-text summary box, and switch the shared frame from brown to muted gold.
- [x] Replace round level pips with small stars and tone the shared gold treatment down to champagne.
- [x] Enlarge preview stars slightly and rebalance gold so borders stay collectible while title and summary fills stay mostly neutral.
- [x] Restore warmer title and summary panels while making the outer preview-card frame a thicker gold edge.
- [x] Test the four art cards, cards without art, narrow screens, and ordinary pathway browsing.
- [x] Bring opened-card detail styling closer to the preview cards with a gold frame, nameplate header, star pips, and preview-style summary/key facts.
- [x] Split the Streamlit renderer mega-file into a `renderers/` package with focused style, shared, preview, detail, and grid modules.
- [x] Restore mostly white preview-card bodies and keep block color identity concentrated in richer avatar-window gradients.
- [x] Choose and apply the `Mystic Training Elements` avatar-window palette: Frost, Verdant, Ember, and Radiance.
- [x] Add block-specific landscape backgrounds inside avatar windows: mountains, hills, meadow, and macadam singletrack.
- [x] Prototype realistic painterly raster backgrounds for all four block types, then delete them after visual review in favour of the earlier stylized card backgrounds.
- [x] Test removing level-colour gradient panels, then restore the earlier gradient-plus-stylized-scenery treatment.
- [x] Test alternate Micro raster backgrounds, then revert the active Micro preview back to the earlier stylized meadow layer.
- [x] Move the active stylized block backgrounds into `assets/backgrounds/` as one SVG asset per block.
- [x] Strengthen the opened-card meta line while keeping the opened-card header free of extra block symbols.
- [x] Generate a first full-coverage avatar set so every active card has a specific local SVG asset and catalog entry.
- [x] Add an ignored artwork cloud cache, Google Drive upload/download scripts, and make the app prefer the synced artwork cache.
- [x] Upload the current artwork cache to Google Drive and verify it by downloading the cloud copy back into the local cache.
- [ ] Add art to the detail header only after browse-card placement is accepted.
- [ ] Review and refine the full-coverage avatars for species clarity, silhouette variety, and block-level consistency.
- [ ] Promote locally accepted assets to the web catalog only when they are approved.
- [ ] Expand one visual family or one pathway at a time only after the pilot is accepted.

## Guardrails

- Do not change coaching content, card schemas, or Google Drive JSON only to support artwork.
- Do not generate all card art before one complete pathway has been reviewed in the app.
- Do not use copyrighted characters, logos, card layouts, or artwork from existing games.
- Every future card must have a graceful fallback when its individual artwork has not yet been approved.

## Archived Art Storage

Artwork remains separate from Google Drive card JSON and active app code.

```text
archive/artwork/
  assets/
    avatars/               # Card-id-based avatar SVGs, grouped by planning level.
    backgrounds/           # Shared block background SVG experiments.
    fallback/              # Fallback avatar SVG experiments.
  prompts/                 # Archived common, planning-level, and card-specific prompt files.
  catalog.json             # Archived mapping from card id to level, image path, alt text, and tags.
```

Use stable, card-id-based names for assets, for example `macro_002.svg` or `macro_002.webp`.

If artwork is revived, keep the catalog flat by card id for fast rendering. Each entry should include `level`, `asset_path`, and `alt_text`; optional tags can support future filtering, duplicate checks, and progress tracking without changing the training-card schema.

## Former Cloud Artwork Storage

The Google Drive artwork folder was removed when artwork was retired from the active app. Do not recreate cloud artwork storage unless the app starts using artwork again.

Former structure:

```text
training_cards_library/
  cards/
  artwork/
    catalog.json
    artwork_manifest.json
    assets/
      avatars/
      backgrounds/
      fallback/
  display_config.json
  manifest.json
  training_cards_library.json
```

If cloud artwork storage is ever revived, keep `artwork_manifest.json` simple. Its job should only be to show which catalog and assets were uploaded so incomplete artwork syncs are easier to detect.

## Open Questions

- Should the first production family remain purely alpine guardian animals, or should later families include terrain guardians or abstract spirits?
- Which exact affinities should form the first controlled vocabulary? The likely pilot set is aerobic development, endurance, fueling, durability, and trail terrain.
- Should browse cards show a small cropped portrait immediately, or should imagery stay detail-view-only until readability has been tested?

## Recommended Build Order If Revived

1. Complete and approve the four pilot images outside the app.
2. Add the catalog, image directory, and no-art fallback.
3. Add art to the detail header, where its value is clearest and space is available.
4. Review the full pathway and mobile layout in Streamlit.
5. Add restrained browse-grid artwork only if it improves recognition without crowding the coaching summary.
6. Expand from the pilot deliberately, keeping one approved avatar per card.
