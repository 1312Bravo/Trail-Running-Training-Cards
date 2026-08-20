# Plan

## Goal

Evolve the app's preview cards into a restrained training-card deck: recognisable at a glance, compact to browse, and always grounded in the schema-defined card content.

## Design Direction

- Borrow the information grammar of a trading card, not Pokemon's visual assets or exact design.
- Keep the fixed light theme, readable typography, and minimal interface.
- Treat Macro, Mezzo, Micro, and Session as distinct card families through subtle frame and identity cues.
- Keep the preview as a scan-friendly introduction; the full schema remains available through `Open card`.

## Preview Card Structure

1. Framed card with a subtle type-specific top edge.
2. Title, type marker, and actions form the identity area.
3. Summary is the card's primary effect: readable and visually distinct.
4. Purpose, suitable levels, race context, training profile, and philosophy are compact attributes.
5. Clickable tags form the footer and continue to filter the library.

## Tasks

- [x] Replace the previous temporary philosophy plan with this card-design plan.
- [x] Establish the first restrained training-card frame and preview hierarchy.
- [x] Present preview attributes as a compact label-and-value stat block.
- [x] Use each card family's icon as a subdued identity watermark beside the type marker.
- [x] Give the full-card dialog the same type-aware header and clean section language.
- [x] Use a Streamlit-only coaching sequence for full-card fields, while retaining future schema fields as a fallback.
- [ ] Review the updated preview cards in the running app and adjust density from screenshots.
- [x] Add a small, semantic line icon to each card-family type marker.
- [ ] Consider optional card art only after the information hierarchy is proven useful.

## Guardrails

- Preview content remains driven by `display_config` and the card schema; no invented coaching content.
- Card type colors stay muted and functional, not decorative noise.
- Full-card dialogs retain the complete schema-defined detail view.
