# Card Philosophy Inventory

This inventory records the current transition away from the old shared-foundation/default model toward explicit card-level philosophy provenance.

## Current Rule

- Every card must include `philosophy_profile_ids`.
- `common` is not a valid philosophy profile.
- The shared coaching foundation applies to every card, but it is not stored as card provenance.
- `mainstream_endurance` is a real training-method profile, not a fallback for unclear cards.
- Python-authored cards should use profile ID constants from `training_cards/philosophy_profiles.py`.
- Philosophy-specific implementation filenames, object names, and slugs should be prefixed when the same visible card concept could exist under multiple philosophies.

## Inventory Status

The existing active card modules have been given explicit `mainstream_endurance` provenance so the library can construct cards again after the removal of the old default. This is a structural checkpoint, not the final content judgement for every card.

Each existing card still needs a later content review to decide whether it should:

- remain mainstream after refinement
- move to a named profile because its logic is actually CTS, Evoke, SWAP, Sharman Ultra, 80/20, or Lydiard
- become a multi-profile card
- be rewritten or removed because the concept is too generic

## Existing Active Cards

| Level | Card ID | Title | Current profile | Review note |
| --- | --- | --- | --- | --- |
| Macro | `macro_001` | Return To Consistency | `mainstream_endurance` | General return-to-training logic; review for health/scope wording. |
| Macro | `macro_002` | Base Development | `mainstream_endurance` | Strong mainstream fit; could overlap with Lydiard if rewritten around sequential base-first doctrine. |
| Macro | `macro_003` | Build Phase | `mainstream_endurance` | Broad development logic; review strength-endurance language for possible Evoke overlap. |
| Macro | `macro_004` | Race-Specific Preparation | `mainstream_endurance` | General specificity logic; could overlap with CTS/Sharman if rewritten around event-demand analysis. |
| Macro | `macro_005` | Peak And Taper | `mainstream_endurance` | Good mainstream fit through tapering and fatigue reduction. |
| Macro | `macro_006` | Recovery And Reset | `mainstream_endurance` | General adaptation/recovery logic; keep broad unless a named recovery model is added. |
| Mezzo | `mezzo_001` | Easy Volume Block | `mainstream_endurance` | Mainstream progression/recovery fit. |
| Mezzo | `mezzo_002` | Endurance Development Block | `mainstream_endurance` | Mainstream aerobic/long-run progression fit. |
| Mezzo | `mezzo_003` | Strength Endurance Block | `mainstream_endurance` | Review for Evoke if rewritten around mountain muscular-endurance layering. |
| Mezzo | `mezzo_004` | Threshold Development Block | `mainstream_endurance` | Mainstream intensity-domain fit. |
| Mezzo | `mezzo_005` | Aerobic Power Block | `mainstream_endurance` | Mainstream aerobic-power/VO2-style fit. |
| Mezzo | `mezzo_006` | Long Endurance Block | `mainstream_endurance` | Mainstream long-duration progression; review for ultra-specific profile if execution dominates. |
| Mezzo | `mezzo_007` | Race Practice Block | `mainstream_endurance` | General specificity fit; review for CTS/Sharman if event-demand coaching becomes central. |
| Mezzo | `mezzo_008` | Fueling Practice Block | `mainstream_endurance` | Mainstream execution-support fit; keep inside professional-scope boundaries. |
| Mezzo | `mezzo_009` | Recovery Block | `mainstream_endurance` | General load-management fit. |
| Micro | `micro_001` | Recovery Week | `mainstream_endurance` | General recovery/consolidation week. |
| Micro | `micro_002` | Aerobic Maintenance Week | `mainstream_endurance` | General maintenance week. |
| Micro | `micro_003` | Volume Progression Week | `mainstream_endurance` | General progressive-overload week. |
| Micro | `micro_004` | Strength Support Week | `mainstream_endurance` | Review for named strength/mountain emphasis if expanded. |
| Micro | `micro_005` | Intensity Support Week | `mainstream_endurance` | General quality-placement week. |
| Micro | `micro_006` | Long Run Focus Week | `mainstream_endurance` | General endurance week; review if ultra-execution dominates. |
| Micro | `micro_007` | Back-To-Back Focus Week | `mainstream_endurance` | Review carefully; likely ultra-specific if retained in this form. |
| Micro | `micro_008` | Race Practice Week | `mainstream_endurance` | Review for CTS/Sharman if practical race execution becomes distinctive. |
| Micro | `micro_009` | Taper Week | `mainstream_endurance` | Mainstream taper fit. |
| Session | `session_001` | Easy Run | `mainstream_endurance` | General aerobic/recovery stimulus. |
| Session | `session_002` | Recovery Run | `mainstream_endurance` | General recovery stimulus. |
| Session | `session_003` | Long Run | `mainstream_endurance` | General long-run stimulus; review ultra specificity. |
| Session | `session_004` | Progression Run | `mainstream_endurance` | General controlled progression stimulus. |
| Session | `session_005` | Steady Run | `mainstream_endurance` | General moderate aerobic stimulus. |
| Session | `session_006` | Tempo Run | `mainstream_endurance` | General threshold-support stimulus. |
| Session | `session_007` | Threshold Intervals | `mainstream_endurance` | General threshold interval stimulus. |
| Session | `session_008` | Aerobic Power Intervals | `mainstream_endurance` | General aerobic-power stimulus. |
| Session | `session_009` | Short Hill Repeats | `mainstream_endurance` | General hill power/mechanics; review Lydiard/SWAP if rewritten. |
| Session | `session_010` | Strength Endurance Hills | `mainstream_endurance` | Review for Evoke if rewritten around muscular-endurance progression. |
| Session | `session_011` | Strides | `mainstream_endurance` | General neuromuscular/economy stimulus; review SWAP if rewritten around speed-and-joy logic. |
| Session | `session_012` | Race Simulation Run | `mainstream_endurance` | Review for CTS/Sharman if event-demand decision rehearsal dominates. |
| Session | `session_013` | Hiking Or Power-Hiking Practice | `mainstream_endurance` | Review for Sharman/Evoke depending on final coaching logic. |
| Session | `session_014` | Downhill Conditioning Run | `mainstream_endurance` | General trail load-management fit; review named trail profiles if expanded. |

## New Mainstream Pathway

These cards were created directly for `mainstream_endurance` rather than migrated from the old shared-foundation idea.

| Level | Card ID | Title | Role |
| --- | --- | --- | --- |
| Macro | `macro_007` | Mainstream Evidence-Informed Development | A broad phase organised around adaptation targets, progressive overload, specificity, and recovery. |
| Mezzo | `mezzo_010` | Progressive Aerobic Development Block | A block for increasing aerobic load while controlling dose variables. |
| Mezzo | `mezzo_011` | Controlled Quality Development Block | A block for adding purposeful intensity after aerobic consistency is stable. |
| Mezzo | `mezzo_012` | Recovery And Adaptation Block | A block for lowering fatigue and consolidating adaptation. |
| Micro | `micro_010` | Aerobic Progression Week | A week that increases one aerobic load variable while keeping intensity controlled. |
| Micro | `micro_011` | Quality And Recovery Week | A week that places one key quality session inside enough easy running and recovery. |
| Micro | `micro_012` | Consolidation Week | A reduced-load week for absorbing training and checking readiness. |
| Session | `session_015` | Submaximal Aerobic Benchmark Run | A controlled assessment session for repeatable aerobic-response information. |
| Session | `session_016` | Mainstream Easy Aerobic Run | A deliberately simple aerobic run governed by effort, recovery, and repeatability. |
| Session | `session_017` | Progressive Endurance Long Run | A long run that progresses duration or terrain while holding intensity boundaries. |
| Session | `session_018` | Controlled Quality Intervals | A structured moderate-to-hard session with clear recovery and execution limits. |
