# Card Philosophy Inventory

This inventory records the current card-level philosophy provenance model and the active Drive/cache library status.

## Current Rule

- Every card must include `philosophy_profile_ids`.
- `common` is not a valid philosophy profile.
- The shared coaching foundation applies to every card, but it is not stored as card provenance.
- `mainstream_endurance` is a real training-method profile, not a fallback for unclear cards.
- Python-authored temporary cards should use profile ID constants from `training_cards/philosophy_profiles.py` before being converted to JSON.
- Philosophy-specific implementation filenames, object names, and slugs should be prefixed when the same visible card concept could exist under multiple philosophies.
- A named-philosophy card should exist only when the philosophy meaningfully changes the app choice, explanation, structure, filtering, or sequencing.

## Current Drive/Cache Library

The configured cloud source of truth currently contains the verified 365-card macro, mezzo, micro, and session library.

| Level | Status |
| --- | --- |
| Macro | Accepted and uploaded |
| Mezzo | Accepted and uploaded |
| Micro | Accepted and uploaded |
| Session | Accepted and uploaded |

## Card Counts

| Level | Accepted cards |
| --- | ---: |
| Macro | 33 |
| Mezzo | 78 |
| Micro | 177 |
| Session | 77 |

Total accepted cards: 365.

## Review Standard

When we build or revise macro, mezzo, micro, and session cards, review each proposed card against the matching mainstream concept first.

Create a named-philosophy version only when the profile changes a meaningful coaching decision. Small wording, tone, or emphasis differences should stay in the philosophy notes or in card explanation, not create duplicate cards.
