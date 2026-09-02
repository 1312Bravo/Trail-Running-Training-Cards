# Art Work Ideas

Status: archived reference. The active Streamlit app currently does not render
artwork, avatars, or artwork backgrounds.

This is our evolving design thinking for card artwork. It is not a final system specification. We will revise it as we make concrete visual decisions and test the first cards in the app.

## Why Artwork Is Separate

The artwork belongs to the Streamlit app experience, but it should not become part of the core training-card library or change the coaching content. Google Drive JSON remains the source of truth for cards. `archive/artwork/` now holds the retired visual work that sits alongside it: ideas, briefs, references, metadata, and artwork experiments.

## Initial Direction

We want original cards with some of the recognition and collectibility of Pokemon or Yu-Gi-Oh!, without copying their characters, layouts, or artwork. The direction should still feel mature, calm, trail-running focused, and secondary to useful coaching information.

## Avatar Idea

Every card could have one original avatar. The avatar would be stable: the same card always has the same character or visual identity wherever it appears in the app.

The current preferred direction is original guardian animals as transparent, mature, sparse line avatars on the white cards. Each card will choose its own clearly recognisable species; Macro cards establish the strongest, most grounded visual class.

## Shared Visual Identity

The current working model has three related layers:

- **Shared visual system:** transparent canvas, slate linework, pale-slate detail, muted-gold mark, mature animal anatomy, and no scenery.
- **Planning level:** Macro, Mezzo, Micro, and Session establish a shared visual role, pose, framing, and restrained accent colour.
- **Card-specific brief:** each card chooses one stable animal avatar, its species-defining features, and its pose.

This could make related cards feel connected without making every card look identical.

## The Relationship Problem

The coaching hierarchy is a graph, not a strict family tree. A Micro card can validly sit beneath several Mezzo cards, and a Session can be relevant to more than one Micro card.

Because of that, a coaching `parent` or `child` reference should not automatically make an avatar a literal visual child of another avatar. One card should not need several competing versions of its art.

The current idea is:

- Give every card one stable avatar.
- Let multiple relationships show through normal app links, ordering, and highlights when a pathway is selected.
- Keep pathway-specific relationship cues in the app UI where possible, rather than permanently baking every relationship into an image.

This means the same Micro avatar can make sense beneath several valid Mezzo pathways.

## Prompt Architecture

Every avatar prompt was assembled from three files in `archive/artwork/prompts/`:

1. `COMMON.md` defines the visual system shared by every card.
2. One planning-level file defines the Macro, Mezzo, Micro, or Session visual class.
3. `CARD_BRIEF_TEMPLATE.md` captures the card's own species, recognisable features, pose, and alt text.

The planning level creates resemblance across cards of the same level. It does not imply that a card inherits species or anatomy from coaching parents.

## Possible Future Storage

If the design is revived, artwork metadata can live in a separate catalog under `archive/artwork/` while it is being tested, not in card JSON. A future active implementation should only connect a card id to an artwork file and alt text after the visual direction is accepted.

We should create that catalog only after agreeing its fields and testing one complete four-card pathway.

## Fallback Principle

New cards must still display well before their individual artwork is approved. The app should use its existing planning-level icon or a later family-level fallback until artwork is ready.

## First Experiment

The first pilot should be one connected Macro -> Mezzo -> Micro -> Session pathway. We should first agree the visual world and choose the pathway, then prepare four focused briefs and review the resulting cards in the app.
