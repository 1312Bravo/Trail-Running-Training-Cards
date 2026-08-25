# Art Work Ideas

This is our evolving design thinking for card artwork. It is not a final system specification. We will revise it as we make concrete visual decisions and test the first cards in the app.

## Why Artwork Is Separate

The artwork belongs to the Streamlit app experience, but it should not become part of the core training-card library or change the coaching content. Google Drive JSON remains the source of truth for cards. `art_work/` can hold the visual work that sits alongside it: ideas, briefs, references, metadata, and approved artwork.

## Initial Direction

We want original cards with some of the recognition and collectibility of Pokemon or Yu-Gi-Oh!, without copying their characters, layouts, or artwork. The direction should still feel mature, calm, trail-running focused, and secondary to useful coaching information.

## Avatar Idea

Every card could have one original avatar. The avatar would be stable: the same card always has the same character or visual identity wherever it appears in the app.

The current preferred direction is original alpine guardian animals. The first reference family is a slate-and-silver ibex in a misty blue mountain world. Other Macro cards may later use different guardian species.

## Shared Visual Identity

The current working model has three related layers:

- **Planning level:** Macro, Mezzo, Micro, and Session establish a shared visual role and framing.
- **Primary visual family:** one curated family gives an avatar its main species, silhouette, terrain, palette, markings, or emblem.
- **Affinities:** small shared themes, such as aerobic development, recovery, strength, intensity, race practice, or technical terrain, can appear as symbols, accents, or subtle UI highlights.

This could make related cards feel connected without making every card look identical.

## The Relationship Problem

The coaching hierarchy is a graph, not a strict family tree. A Micro card can validly sit beneath several Mezzo cards, and a Session can be relevant to more than one Micro card.

Because of that, a coaching `parent` or `child` reference should not automatically make an avatar a literal visual child of another avatar. One card should not need several competing versions of its art.

The current idea is:

- Give every card one stable avatar and one primary visual family.
- Let multiple relationships show through shared affinities, small emblems, accent colors, or highlights when a pathway is selected.
- Keep pathway-specific relationship cues in the app UI where possible, rather than permanently baking every relationship into an image.

This means the same Micro avatar can make sense beneath several valid Mezzo pathways.

## First Visual Lineage

For a deliberately chosen four-card pilot, artwork can tell a generational story: the Macro is a mature master guardian; Mezzo is its adult child; Micro is a younger descendant; Session is the youngest and most action-focused form. They share anatomy, markings, materials, background world, and a muted-gold lineage mark.

Planning level should be obvious through the combination of age, pose, and a restrained neon rim-light accent:

- Macro: glacier blue, mature and still.
- Mezzo: neon emerald, deliberate forward walk.
- Micro: electric violet, compact and agile.
- Session: neon amber, focused precise stride.

This is a curated visual-storytelling pattern, not an automatic interpretation of every coaching relationship. The prompt details live in `PROMPT_GUIDE.md`.

## Possible Future Storage

When the design is ready, artwork metadata could live in a separate catalog under `art_work/`, not in card JSON. A future entry might connect a card id to an artwork file, avatar id, visual family, affinities, alt text, and approval status.

We should create that catalog only after agreeing its fields and testing one complete four-card pathway.

## Fallback Principle

New cards must still display well before their individual artwork is approved. The app should use its existing planning-level icon or a later family-level fallback until artwork is ready.

## First Experiment

The first pilot should be one connected Macro -> Mezzo -> Micro -> Session pathway. We should first agree the visual world and choose the pathway, then prepare four focused briefs and review the resulting cards in the app.
