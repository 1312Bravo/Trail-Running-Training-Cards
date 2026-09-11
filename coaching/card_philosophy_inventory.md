# Card Philosophy Inventory

This inventory records the current card-level philosophy provenance model and the active seed-library status.

## Current Rule

- Every card must include `philosophy_profile_ids`.
- `common` is not a valid philosophy profile.
- The shared coaching foundation applies to every card, but it is not stored as card provenance.
- `mainstream_endurance` is a real training-method profile, not a fallback for unclear cards.
- Python-authored cards should use profile ID constants from `training_cards/philosophy_profiles.py`.
- Philosophy-specific implementation filenames, object names, and slugs should be prefixed when the same visible card concept could exist under multiple philosophies.
- A named-philosophy card should exist only when the philosophy meaningfully changes the app choice, explanation, structure, filtering, or sequencing.

## Current Seed Library

The configured cloud source of truth currently contains the verified macro seed set. The local working seed/cache also includes the mainstream mezzo baseline for review before the next cloud replacement.

| Level | Status |
| --- | --- |
| Macro | Active seed cards authored and uploaded |
| Mezzo | Mainstream baseline authored locally; named-philosophy review not started |
| Micro | Folder structure reserved; cards not built yet |
| Session | Folder structure reserved; cards not built yet |

## Macro Card Counts

| Profile folder | Active macro cards |
| --- | ---: |
| `mainstream_endurance` | 9 |
| `80_20_endurance` | 5 |
| `cts` | 4 |
| `evoke_endurance` | 3 |
| `lydiard` | 4 |
| `sharman_ultra` | 2 |
| `swap` | 6 |
| `multi_profile` | 0 |

Total active macro seed cards: 33.

## Mainstream Mezzo Card Counts

| Profile folder | Local working mezzo cards |
| --- | ---: |
| `mainstream_endurance` | 28 |

Total local working mainstream mezzo cards: 28.

## Review Standard

When we build mezzo, micro, and session cards, review each proposed card against the matching mainstream concept first.

Create a named-philosophy version only when the profile changes a meaningful coaching decision. Small wording, tone, or emphasis differences should stay in the philosophy notes or in card explanation, not create duplicate cards.
