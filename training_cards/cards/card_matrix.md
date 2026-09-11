# Card Matrix

This file is the working build map for the training card library. It owns card taxonomy, coach review decisions, philosophy-specific card justification, and build-status notes. It does not own cloud upload/download workflow or schema rules; those live in `notes/cloud_library_storage_workflow.md` and `notes/schema_design_and_validation.md`.

It has four connected roles:

- a knowledge/design file for the card system
- a notes file for deciding which card types should exist
- a prompt/context file for future card-building work
- a possible active source for app-facing card-type explanations

It is not a list of finished cards. It should guide the conversation before cards are written, so each card has a clear type, level, philosophy reason, and coaching purpose.

Parts of this file may later become active app-consumed knowledge, especially card type names, phase descriptions, and philosophy review explanations. If that happens, the relevant sections should be kept structured enough for reliable use in the app. Finished card objects still need their own card files or JSON records unless the app is deliberately changed to read card definitions directly from this matrix.

The coach has the primary voice for all coaching-related decisions in this file. Type selection, type naming, phase purpose, sequencing, philosophy differences, watchouts, progression logic, and final card content should be accepted only when they make coaching sense.

When building cards from this file, use the existing coaching foundation, card hierarchy, card authoring guidance, and relevant philosophy profile as the coach authority before writing implementation files. The goal is to let the coaching logic shape the card, not simply fill a template.

## Coach Review Gate

Before a type or card is accepted, ask the coach-facing questions:

- Is this a real coaching concept, or only a convenient label?
- Does it belong at this planning level?
- Is it meaningfully different from nearby types?
- Would an experienced endurance running coach recognize the purpose?
- Does the type help a coach make better sequencing, progression, or safety decisions?
- Does trail or mountain context change the logic?
- Does any named philosophy treat this differently enough to justify its own card?

If the coach answer is weak, unclear, or duplicative, revise, merge, or reject the type before writing cards.

## Completion Review Rule

After any substantial work block is finished, complete a coach-led review before moving to the next block. A work block can be a type taxonomy, philosophy review pass, card batch, storage restructuring step, cloud sync checkpoint, or other meaningful set of decisions. It is not limited to the macro, mezzo, micro, or session hierarchy labels.

The review should check:

- whether the block includes too much or reaches beyond its level
- whether an important type, philosophy distinction, card, relationship, or app-facing note is missing
- whether any items overlap enough that they should be merged, renamed, split, or deleted
- whether the coaching logic still matches the hierarchy level
- whether the local structure, cloud structure, card matrix, plan notes, and app assumptions still agree

Make small and obvious adjustments as part of the review. Pause for user realignment only when the adjustment changes the direction, deletes meaningful work, or has non-obvious consequences.

## Build Rule

For each card level:

- First define the baseline endurance type taxonomy.
- Then build the `mainstream_endurance` version for the baseline types.
- Then review each baseline type through each named philosophy.
- Create a philosophy-specific card only when the philosophy creates a meaningful distinction from the `mainstream_endurance` version.
- After baseline types are reviewed, add philosophy-specific special types that are not part of the mainstream taxonomy.

For macro cards, build the accepted `mainstream_endurance` baseline cards first. Philosophy review should compare each named philosophy against those concrete baseline cards, not against vague type names alone.

## Philosophy Specificity Standard

A named-philosophy card should exist only when the philosophy creates a meaningful distinction from the matching `mainstream_endurance` card. The distinction must be large enough that it would affect how the app chooses, explains, structures, filters, or sequences the card.

This standard applies to every card level: macro, mezzo, micro, and session.

Use coaching common sense rather than a mechanical checklist. A separate named-philosophy card is justified when a coach using that philosophy would make a noticeably different coaching decision from a mainstream evidence-informed coach for the same athlete and situation.

Small emphasis differences should stay in the relevant philosophy notes, card explanation, or lower-level cards. If the philosophy would only produce the same card with different language, tone, or minor watchouts, do not create a duplicate.

When unsure, default to no separate named-philosophy card until the distinction becomes clear during coaching review or card drafting.

## Macro Level

Macro cards define the broad training phase. They answer: what phase are we in, why is this phase appropriate now, and what kind of blocks should sit inside it?

Macro cards should not prescribe detailed workouts. They should set direction, protect sequencing, and make later block/week/session choices coherent.

### Coach-Led Macro Type Work

Macro types are not preselected. The macro type set must be generated by coach reasoning first.

Use the coaching foundation, card hierarchy, card authoring guidance, and relevant philosophy context to decide which broad training phases are genuinely useful for endurance running planning. The coach decision comes before the table. The table records the outcome; it does not create the taxonomy by itself.

When defining the macro type set, the coach should decide:

- which broad training phases should exist
- which labels are real coaching concepts rather than convenient names
- which concepts should be merged because they are not meaningfully different
- which concepts are too specific and belong at mezzo, micro, or session level
- which concepts are outside the intended card library scope
- how trail or mountain running changes the macro-level phase decisions
- which baseline types should receive `mainstream_endurance` cards
- which named philosophies may later need distinct macro versions

### Coach-Derived Macro Types

These macro types are accepted as useful broad training phases. They are generated from coaching reasoning, not from old card inventory.

| Type ID | Type name | Coach decision | About this phase | Mainstream status |
| --- | --- | --- | --- | --- |
| `macro_type_return_to_consistency` | Return To Consistency | Keep | This phase is used when the athlete first needs to restore dependable training rhythm, frequency, and basic load tolerance. The coaching priority is not to chase fitness quickly, but to make running feel repeatable again and to rebuild confidence in the routine. Training should be simple, mostly easy, and conservative with intensity, terrain, and downhill cost. Useful supporting blocks may include consistency, easy aerobic running, recovery, low-risk strength support, and gradual reintroduction of trail exposure. | Built as `mainstream_return_to_consistency` |
| `macro_type_base_development` | Base Development | Keep | This phase builds the durable foundation that later training depends on: broad aerobic capacity, consistent routine, basic strength support, movement competence, and the ability to absorb progressive load. It absorbs the old separate ideas of general preparation and aerobic development at macro level because, for broad planning, these belong to one foundation-building phase. Training should avoid premature race specificity, excessive intensity, and chronic moderate-hard work. Trail and mountain context can be introduced gradually through varied terrain, climbing, hiking, and controlled descents without making every run race-specific. | Built as `mainstream_base_development` |
| `macro_type_capacity_development` | Capacity Development | Keep | This phase follows a sufficient base and develops stronger performance capacities through purposeful block emphases. The macro decision is that the athlete is ready for more directed training, while the exact emphasis, such as threshold, aerobic power, strength endurance, long-endurance tolerance, or climbing durability, is selected at mezzo level. The phase should create meaningful adaptation without trying to develop every quality at once. Good coaching protects aerobic support and recovery while increasing the specificity or intensity of selected stressors. | Built as `mainstream_capacity_development` |
| `macro_type_race_specific_preparation` | Race-Specific Preparation | Keep | This phase converts developed fitness into the capabilities and decisions required by the goal event or objective. It should emphasize terrain demands, pacing, fueling, equipment, environmental conditions, technical confidence, and race-execution rehearsal in proportion to the actual goal. The phase should not abandon general capacity or recovery, and it should not confuse copying race terrain with preparing the athlete well. In trail and mountain running, this phase often changes substantially because gradient, descent load, technicality, duration, weather, and remoteness can matter more than pace. | Built as `mainstream_race_specific_preparation` |
| `macro_type_peak_and_taper` | Peak And Taper | Merge | This phase protects readiness while reducing unnecessary fatigue before an important race or objective. Peak, sharpening, and taper are kept together at macro level because they share one broad coaching job: maintain useful fitness, preserve rhythm, improve freshness, and help the athlete arrive confident rather than overloaded. The finer distinction between sharpening sessions, reduced-load weeks, and final taper details belongs mostly at mezzo, micro, or session level. Trail and ultra goals may require special attention to residual muscle damage, travel, equipment checks, and confidence on goal-relevant terrain. | Built as `mainstream_peak_and_taper` |
| `macro_type_competition_management` | Competition Management | Keep | This phase is for athletes navigating a race season, race series, or multiple meaningful events close enough together that the plan cannot be treated as one simple build-and-taper cycle. The main coaching job is balancing recovery, freshness, small fitness touchpoints, learning from races, and readiness for the next event. It is distinct from maintenance because competition stress itself becomes a major training and recovery input. In trail and mountain running, races may create high muscular, technical, environmental, and travel cost, so the space between events must be coached deliberately rather than filled automatically. | Built as `mainstream_competition_management` |
| `macro_type_recovery_and_transition` | Recovery And Transition | Keep | This phase restores readiness after a race, demanding block, disrupted period, or accumulated fatigue. It gives the athlete time to absorb previous work, reduce physical and mental load, and create a clean bridge into the next training cycle. Recovery should not be treated as either total inactivity or hidden training; the right dose depends on fatigue, motivation, soreness, and upcoming goals. Trail and mountain athletes may need extra respect for descent damage, long-duration fatigue, technical stress, and travel load even when general fitness feels intact. | Built as `mainstream_recovery_and_transition` |
| `macro_type_off_season` | Off-Season | Keep | This phase is an intentional step away from race preparation and structured performance pressure. It is different from recovery because it is not only about absorbing a recent stress, and different from maintenance because the goal is not primarily to preserve peak-specific fitness. The coach uses it to restore freshness, widen movement options, address basic strength or mobility, keep enough aerobic rhythm, and let motivation return without drifting into either total inactivity or hidden training. For trail and mountain runners, off-season may reduce technical and downhill cost while keeping outdoor movement, hiking, easy running, and general durability alive. | Built as `mainstream_off_season` |
| `macro_type_maintenance` | Maintenance | Keep | This phase holds useful fitness with controlled training cost when full development is not the right objective. It fits between goals, during busy life periods, travel, uncertain schedules, or times when preserving consistency and key qualities matters more than pushing adaptation. The phase should keep rhythm, aerobic support, and small touches of strength or intensity where appropriate, but it should not pretend to be a full build phase. For trail runners, maintenance may also preserve terrain familiarity, climbing rhythm, and descent tolerance at a sustainable dose. | Built as `mainstream_maintenance` |

### Macro Philosophy Review Matrix

Use this to decide, later, whether an accepted baseline macro type needs a distinct philosophy-specific version. `Build` means the baseline mainstream card should be created. `Review` means the philosophy may alter the logic enough to justify a separate card, but that decision is not made yet.

| Type ID | `mainstream_endurance` | `80_20_endurance` | `lydiard` | `cts` | `evoke_endurance` | `swap` | `sharman_ultra` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `macro_type_return_to_consistency` | Build | No separate macro card | No separate macro card | No separate macro card | No separate macro card | Distinct version justified | No separate macro card |
| `macro_type_base_development` | Build | Distinct version justified | Distinct version justified | Distinct version justified | Distinct version justified | Distinct version justified | No separate macro card |
| `macro_type_capacity_development` | Build | Distinct version justified | Special macro type instead | Distinct version justified | Special macro type instead | Distinct version justified | No separate macro card |
| `macro_type_race_specific_preparation` | Build | Distinct version justified | Distinct version justified | Distinct version justified | Distinct version justified | Distinct version justified | Distinct version justified |
| `macro_type_peak_and_taper` | Build | No separate macro card | Distinct version justified | No separate macro card | No separate macro card | No separate macro card | No separate macro card |
| `macro_type_competition_management` | Build | Distinct version justified | No separate macro card | Distinct version justified | No separate macro card | Distinct version justified | Distinct version justified |
| `macro_type_recovery_and_transition` | Build | No separate macro card | No separate macro card | No separate macro card | No separate macro card | No separate macro card | No separate macro card |
| `macro_type_off_season` | Build | No separate macro card | No separate macro card | No separate macro card | No separate macro card | Distinct version justified | No separate macro card |
| `macro_type_maintenance` | Build | Distinct version justified | No separate macro card | No separate macro card | No separate macro card | No separate macro card | No separate macro card |

### Built Macro Card Set

The justified macro cards have been created and published as Drive/cache JSON cards. This section records build status without duplicating the full card content.

| Philosophy profile | Built macro cards |
| --- | --- |
| `mainstream_endurance` | `mainstream_return_to_consistency`, `mainstream_base_development`, `mainstream_capacity_development`, `mainstream_race_specific_preparation`, `mainstream_peak_and_taper`, `mainstream_competition_management`, `mainstream_recovery_and_transition`, `mainstream_off_season`, `mainstream_maintenance` |
| `80_20_endurance` | `endurance_80_20_base_development`, `endurance_80_20_capacity_development`, `endurance_80_20_race_specific_preparation`, `endurance_80_20_competition_management`, `endurance_80_20_maintenance` |
| `lydiard` | `lydiard_base_development`, `lydiard_hill_resistance_transition`, `lydiard_race_specific_preparation`, `lydiard_peak_and_taper` |
| `cts` | `cts_base_development`, `cts_capacity_development`, `cts_race_specific_preparation`, `cts_competition_management` |
| `evoke_endurance` | `evoke_base_development`, `evoke_muscular_endurance_development`, `evoke_race_specific_preparation` |
| `swap` | `swap_return_to_consistency`, `swap_base_development`, `swap_capacity_development`, `swap_race_specific_preparation`, `swap_competition_management`, `swap_off_season` |
| `sharman_ultra` | `sharman_race_specific_preparation`, `sharman_competition_management` |

### 80/20 Endurance Macro Review

Coach decision: create 80/20-specific macro cards only where deliberate intensity distribution, hard/easy contrast, zone discipline, and recovery spacing change the macro-phase logic. Do not create a separate 80/20 card when the phase is mostly a shared coaching state with the same macro purpose as mainstream.

| Type ID | 80/20 decision | Coach rationale |
| --- | --- | --- |
| `macro_type_return_to_consistency` | No separate macro card | The 80/20 philosophy reinforces easy discipline and conservative re-entry, but the macro job is still restoring routine and tolerance. This can be handled inside mainstream return-to-consistency guidance unless later lower-level cards need 80/20-specific execution. |
| `macro_type_base_development` | Distinct version justified | Base development is strongly affected by 80/20 because the phase must protect a deliberately low-intensity majority, prevent moderate-effort drift, and build volume through manageable cycles rather than harder ordinary running. |
| `macro_type_capacity_development` | Distinct version justified | The phase changes meaningfully because 80/20 capacity work should place moderate and high intensity as a bounded minority inside enough easy training and recovery spacing. The macro card should define how selected quality is added without eroding the distribution. |
| `macro_type_race_specific_preparation` | Distinct version justified | Race-specific work may temporarily change the intensity pattern, but 80/20 requires that specificity be deliberate rather than accidental. The card should explain how terrain, race pace, long duration, and moderate work fit without turning the whole phase into grey-zone training. |
| `macro_type_peak_and_taper` | No separate macro card | 80/20 can influence taper execution, but the macro job remains the mainstream taper job: reduce fatigue, preserve rhythm, and arrive ready. Distribution details can be handled later in taper weeks and sessions. |
| `macro_type_competition_management` | Distinct version justified | Racing disrupts clean intensity accounting, so 80/20 needs a distinct macro logic for treating competitions as high-cost inputs, restoring hard/easy contrast, and avoiding too much moderate work between events. |
| `macro_type_recovery_and_transition` | No separate macro card | Recovery is central to 80/20, but the macro-phase purpose is not distinct enough from mainstream recovery and transition. The 80/20 influence can be expressed later through recovery weeks, easy sessions, and density rules. |
| `macro_type_off_season` | No separate macro card | Off-season is mainly about decompression, movement variety, and stepping away from performance pressure. 80/20 may inform how much easy rhythm remains, but it should not turn off-season into ratio management. |
| `macro_type_maintenance` | Distinct version justified | Maintenance changes under 80/20 because the phase should preserve useful fitness through a low-cost distribution, small purposeful intensity touchpoints, and easy-work discipline rather than unplanned moderate running. |

### Lydiard Macro Review

Coach decision: create Lydiard-specific macro cards where base-first development, sequential phase order, response-regulated recovery, inner-coach effort judgement, or backward timing changes the macro logic. Do not label a card Lydiard only because it includes aerobic running, hills, or a taper.

| Type ID | Lydiard decision | Coach rationale |
| --- | --- | --- |
| `macro_type_return_to_consistency` | No separate macro card | Lydiard effort judgement and conservative progression can support re-entry, but the macro job is still restoring basic rhythm and tolerance. A distinct Lydiard card is not justified unless the return phase is explicitly rebuilding toward the Lydiard sequence. |
| `macro_type_base_development` | Distinct version justified | The base is central to Lydiard. A Lydiard version should treat aerobic conditioning as the durable resource that makes later hill, anaerobic, integration, and taper work productive, with progression limited by the slowest adapting system. |
| `macro_type_capacity_development` | Special macro type instead | Lydiard changes this phase enough that a generic capacity-development label is too vague. The useful macro concept is the hill-resistance transition: a bridge from base toward later faster, anaerobic, coordination, or race-relevant work. |
| `macro_type_race_specific_preparation` | Distinct version justified | Lydiard race preparation is shaped by backward timing and integration of capacities before the target race. A distinct version should explain what previous phases built and how race-relevant work connects them. |
| `macro_type_peak_and_taper` | Distinct version justified | Peaking is central to Lydiard's timed sequence. A distinct version should protect the idea that the final phase expresses accumulated preparation rather than forcing missing fitness at the end. |
| `macro_type_competition_management` | No separate macro card | Lydiard is most clearly organised around timing a target race rather than managing dense race seasons. Use mainstream competition management unless a later source review supports a distinct Lydiard race-season approach. |
| `macro_type_recovery_and_transition` | No separate macro card | Response-regulated recovery is important in Lydiard, but recovery and transition do not become a distinct macro card unless they are tied to a specific phase-sequence decision. |
| `macro_type_off_season` | No separate macro card | Off-season is not a distinctive Lydiard macro phase in the current source interpretation. Lydiard logic may inform easy aerobic rhythm, but the phase purpose remains mainstream. |
| `macro_type_maintenance` | No separate macro card | Lydiard values preserving the aerobic base, but maintenance as a constrained life or between-goal phase is not distinct enough from mainstream to justify its own macro card. |

### CTS Macro Review

Coach decision: create CTS-specific macro cards where event-demand analysis, long-range ultra planning, focused limiter development, workload cost, and race-execution rehearsal change the macro logic. Do not use CTS for generic ultrarunning language or generic hard sessions.

| Type ID | CTS decision | Coach rationale |
| --- | --- | --- |
| `macro_type_return_to_consistency` | No separate macro card | CTS would still ask whether the athlete is ready for work, but the macro purpose is not distinct from mainstream re-entry. Demand-led ultra specificity should wait until basic consistency exists. |
| `macro_type_base_development` | Distinct version justified | CTS base work is shaped by patient workload development, event relevance, and the fundamentals that make later ultra-specific preparation possible. A distinct version should frame base as earned, repeatable workload rather than generic mileage. |
| `macro_type_capacity_development` | Distinct version justified | CTS often uses focused blocks when they solve a meaningful limiter. A distinct version should name the performance problem, prerequisite workload, trade-off, and recovery cost of the chosen capacity emphasis. |
| `macro_type_race_specific_preparation` | Distinct version justified | This is one of the strongest CTS fits. The card should start from the event's consequential demands and rehearse only what matters: terrain, duration, descending, fueling, heat, altitude, equipment, pacing, or hiking. |
| `macro_type_peak_and_taper` | No separate macro card | CTS can inform taper decisions, but the current documented distinction is not strong enough to require a separate macro card before source-specific taper material is reviewed. |
| `macro_type_competition_management` | Distinct version justified | Closely spaced ultras and tune-up races require demand-led cost accounting. A CTS version should treat each race as both stress and information, then choose only the work that improves readiness for the next event. |
| `macro_type_recovery_and_transition` | No separate macro card | CTS is highly cost-aware, but recovery and transition can stay mainstream at macro level until a specific CTS post-race or transition method is documented. |
| `macro_type_off_season` | No separate macro card | Off-season is not a distinctive CTS macro concept in the current source interpretation. Use mainstream off-season unless an event-demand goal already turns the phase into preparation. |
| `macro_type_maintenance` | No separate macro card | CTS can help choose efficient training during constraints, but the current macro purpose remains mainstream maintenance unless a specific ultra-event demand or race season changes it. |

### Evoke Endurance Macro Review

Coach decision: create Evoke-specific macro cards where the layered mountain-endurance model changes the phase: aerobic capacity, strength reserve, muscular endurance, and later utilisation of those capacities. Do not use Evoke merely because a card includes trails, hills, or hard climbing.

| Type ID | Evoke decision | Coach rationale |
| --- | --- | --- |
| `macro_type_return_to_consistency` | No separate macro card | Evoke would support conservative re-entry and aerobic control, but the phase purpose is still restoring rhythm and tolerance. Distinct Evoke layering is premature until the athlete can train consistently. |
| `macro_type_base_development` | Distinct version justified | Evoke base development is strongly distinct because it prioritises a substantial aerobic base, often with threshold-informed intensity control and attention to aerobic imbalance before visible mountain-specific work. |
| `macro_type_capacity_development` | Special macro type instead | Evoke changes this phase enough that a generic capacity-development label is too vague. The useful macro concept is muscular endurance development layered onto aerobic capacity and strength reserve before objective-like utilisation. |
| `macro_type_race_specific_preparation` | Distinct version justified | Evoke changes race-specific preparation through the capacity-versus-utilisation distinction. Event-like mountain work should appear only when the athlete has enough underlying capacity to use it productively. |
| `macro_type_peak_and_taper` | No separate macro card | Evoke tapering should respect prior layer costs, but the documented philosophy does not yet justify a separate macro taper card beyond mainstream principles. |
| `macro_type_competition_management` | No separate macro card | The current Evoke interpretation is strongest for objective preparation layers, not race-season management across multiple competitions. Use mainstream unless a later source review supports more. |
| `macro_type_recovery_and_transition` | No separate macro card | Recovery response is central to Evoke dosing, especially after muscular-endurance or descent stress, but this influence can be handled inside recovery blocks and sessions rather than a separate macro phase. |
| `macro_type_off_season` | No separate macro card | Off-season may include strength and general movement, but Evoke's distinctive layered model is not the main organising principle of the phase. |
| `macro_type_maintenance` | No separate macro card | Maintaining aerobic rhythm or strength reserve can be Evoke-informed at lower levels, but the broad macro phase does not need a separate Evoke card yet. |

### SWAP Macro Review

Coach decision: create SWAP-specific macro cards where whole-person sustainability, long-term engagement, economy and speed as skills, fatigue-resistance curiosity, positive response, and athlete agency change the phase purpose. Do not use SWAP only for friendly tone.

| Type ID | SWAP decision | Coach rationale |
| --- | --- | --- |
| `macro_type_return_to_consistency` | Distinct version justified | SWAP can meaningfully change this phase by rebuilding consistency without shame, restoring confidence, and using enjoyment and agency to make training feel safe and repeatable again. |
| `macro_type_base_development` | Distinct version justified | A SWAP base is not only aerobic foundation; it should protect long-term consistency, health, enjoyment, and early economy or speed touches when appropriate. That changes the macro emphasis enough for a distinct card. |
| `macro_type_capacity_development` | Distinct version justified | SWAP capacity work can be distinct through speed and economy development, fatigue-resistance questions, curiosity about individual response, and restraint that keeps demanding work compatible with long-term engagement. |
| `macro_type_race_specific_preparation` | Distinct version justified | SWAP race-specific preparation should integrate performance with confidence, adventure, fueling, terrain response, and a healthy relationship with the goal. This is more than generic specificity. |
| `macro_type_peak_and_taper` | No separate macro card | SWAP can strongly influence taper tone, confidence, and fear-management, but the macro structure is not distinct enough from mainstream peak and taper. Keep those influences in lower-level taper cards or explanatory notes. |
| `macro_type_competition_management` | Distinct version justified | SWAP's long-term lens matters when races are close together. A distinct version should balance ambition, health, joy, learning, and fatigue resistance instead of letting race excitement become unmanaged load. |
| `macro_type_recovery_and_transition` | No separate macro card | SWAP can make recovery feel more positive and humane, but this is mostly framing unless it changes the macro decision itself. Use mainstream recovery and express SWAP-specific tone or reflection later where needed. |
| `macro_type_off_season` | Distinct version justified | Off-season strongly fits SWAP because it can emphasise play, movement variety, identity outside performance pressure, and renewed motivation without losing purposeful rhythm. |
| `macro_type_maintenance` | No separate macro card | SWAP values can improve maintenance language and lower-level choices, but the macro purpose remains holding useful fitness with low cost. This does not need a duplicate macro card. |

### Sharman Ultra Macro Review

Coach decision: create Sharman Ultra-specific macro cards where athlete-specific adaptation, education, practical ultra-execution reasoning, lifestyle fit, and success definition change the macro logic. Stay careful because the public source base supports coaching stance more than exact proprietary workouts.

| Type ID | Sharman Ultra decision | Coach rationale |
| --- | --- | --- |
| `macro_type_return_to_consistency` | No separate macro card | Sharman Ultra coaching can individualise re-entry, but the macro purpose is still restoring rhythm and basic tolerance. The distinction is not strong enough for a separate macro card. |
| `macro_type_base_development` | No separate macro card | Sharman Ultra uses established endurance principles, but the current source base does not justify a distinct base macro beyond mainstream unless ultra execution or athlete-specific adaptation substantially changes it. |
| `macro_type_capacity_development` | No separate macro card | Capacity development can be adapted by a Sharman-style coach, but the documented public method does not yet provide a distinct enough macro structure for generic capacity work. |
| `macro_type_race_specific_preparation` | Distinct version justified | This is a strong Sharman Ultra fit. A distinct version should connect fitness to practical ultra execution: terrain, pacing, fueling, hiking, gear, logistics, problem-solving, and athlete-specific success. |
| `macro_type_peak_and_taper` | No separate macro card | Sharman Ultra can individualise taper choices, but current sources do not justify a distinct macro taper card before more direct material is reviewed. |
| `macro_type_competition_management` | Distinct version justified | Race-season management can be distinct because Sharman Ultra emphasises athlete-specific adaptation, practical experience, and learning from races rather than applying a fixed between-race template. |
| `macro_type_recovery_and_transition` | No separate macro card | Sharman Ultra can individualise post-ultra recovery, but the macro phase remains close to mainstream recovery and transition unless a more specific source-supported recovery method is identified. |
| `macro_type_off_season` | No separate macro card | Off-season may be adapted to the athlete, but the current Sharman Ultra source base does not make it a distinctive macro phase beyond mainstream. |
| `macro_type_maintenance` | No separate macro card | Lifestyle fit and athlete-specific adaptation are important, but they are not enough by themselves to create a distinct Sharman Ultra maintenance macro card. Keep maintenance mainstream unless ultra race demands change the phase into race-specific preparation or competition management. |

### Philosophy-Specific Macro Types

This is a separate review from deciding whether a named philosophy needs its own version of an accepted baseline macro type.

The baseline review asks:

- Does this philosophy change an existing mainstream macro type enough to justify its own card?

The special-type review asks:

- Does this philosophy contain a real macro-phase concept that is not covered by the accepted mainstream macro taxonomy at all?

Do not add speculative philosophy-specific macro types. A special macro type must describe a true phase-level planning concept, not only a favorite workout, a block emphasis, a coaching tone, or a lower-level detail.

For each philosophy, the coach must explicitly decide whether its distinct training model creates any additional macro types beyond the accepted baseline set.

| Philosophy | Review status | Possible special macro-type question | Coach verdict | Notes |
| --- | --- | --- | --- | --- |
| `80_20_endurance` | Complete | Does 80/20 need a separate macro phase for distribution reset, intensity-ratio correction, or race-season redistribution beyond baseline base/capacity/race-specific/maintenance/competition phases? | Reject additional macro type | 80/20 changes the operating rules across phases: low-intensity majority, hard/easy contrast, intensity accounting, and recovery spacing. Those are strong enough for distinct versions of several baseline macro types, but not a new phase category. Distribution reset is usually a mezzo, micro, or review problem rather than a macro phase. |
| `lydiard` | Complete | Does Lydiard need a separate hill-strength or coordination/integration macro phase beyond baseline capacity development and race-specific preparation? | Keep one additional macro type | Lydiard hill-resistance transition is a true phase-level concept when used in the classic sequence. It bridges the aerobic base toward later faster and race-relevant work, changes sequencing, and changes the blocks that should sit inside it. Coordination, sharpening, and final race integration are already covered by Lydiard race-specific preparation and peak/taper at this library level. |
| `cts` | Complete | Does CTS need a separate long-range event-demand planning phase, limiter-identification phase, or ultra-specific preparation phase beyond baseline race-specific preparation? | Reject additional macro type | CTS strongly changes how base, capacity, race-specific preparation, and competition management are designed. But event-demand analysis and limiter identification are coaching processes, not separate training phases. Ultra-specific preparation is covered by the CTS version of race-specific preparation. |
| `evoke_endurance` | Complete | Does Evoke need separate macro phases for aerobic capacity, strength reserve, muscular endurance, or utilisation rather than treating these as capacity/race-specific variants? | Keep one additional macro type | Evoke's layered model can create a real muscular-endurance macro phase for mountain objectives: after sufficient aerobic capacity and strength reserve, before full objective utilisation. Strength reserve alone is usually support or mezzo-level unless it becomes the primary block sequence. Utilisation is covered by Evoke race-specific preparation. |
| `swap` | Complete | Does SWAP need a separate speed/economy development phase, joy/reconnection phase, or fatigue-resistance phase beyond baseline return, base, capacity, and off-season? | Reject additional macro type | SWAP meaningfully changes return to consistency, base, capacity, race-specific preparation, competition management, and off-season. Speed, economy, joy, and fatigue resistance are central emphases, but they fit inside those phase types rather than creating a separate macro taxonomy. |
| `sharman_ultra` | Complete | Does Sharman Ultra need a separate athlete-specific ultra planning, education, or execution-preparation phase beyond baseline race-specific preparation and competition management? | Reject additional macro type | Sharman Ultra changes race-specific preparation and competition management through athlete-specific adaptation, education, and practical ultra execution. Planning and education are coaching methods rather than macro phases, and the public source base does not justify inventing additional Sharman-specific phase categories. |

### Accepted Special Macro Types

These are philosophy-specific macro types that are not fully covered by the accepted mainstream macro taxonomy. They require a follow-up decision before more cards are authored: create a new macro card, rename/refactor an existing philosophy-specific macro card, or hold the type as future work.

| Type ID | Type name | Philosophy | Coach verdict | About this phase | Card status |
| --- | --- | --- | --- | --- | --- |
| `macro_type_lydiard_hill_resistance_transition` | Hill Resistance Transition | `lydiard` | Keep | This phase sits after a substantial aerobic base and before later faster, anaerobic, coordination, or race-relevant work. Its job is to convert general aerobic durability into stronger, more resilient running mechanics and leg power while preserving the base that makes the later sequence useful. At macro level it matters because it changes the order of the plan: the athlete should not jump straight from base into hard race-like work when the hill-resistance bridge is still needed. For trail and mountain running, this phase must be adapted carefully; hills can support strength and coordination, but technical descent, long climbing specificity, and mountain execution still need their own later justification. | Built by refactoring `lydiard_capacity_development` into `lydiard_hill_resistance_transition` while keeping stable ID `macro_017`. |
| `macro_type_evoke_muscular_endurance_development` | Muscular Endurance Development | `evoke_endurance` | Keep | This phase is used when a mountain or uphill objective requires repeated local force production that ordinary aerobic volume and general strength do not fully prepare. It belongs after the athlete has enough aerobic capacity and strength reserve to absorb the work, and before full objective utilisation or race simulation dominates the plan. The phase should emphasize targeted uphill or climbing-specific muscular endurance, continued aerobic support, careful recovery, and clear prerequisites. It should avoid using visible fatigue as proof of value, adding muscular-endurance work too early, or replacing the aerobic base with repeated hard hill suffering. | Built by refactoring `evoke_capacity_development` into `evoke_muscular_endurance_development` while keeping stable ID `macro_025`. |

## Open Questions

- No open macro-type questions remain after the current special-type review and refactor.

## Mezzo Level

Mezzo cards define focused blocks inside a macro phase. They answer: what specific training quality or planning problem is being developed for several weeks, where does it sit inside the macro phase, and what kinds of weeks and sessions should usually support it?

Mezzo cards should not prescribe exact weekly calendars or individual workouts. They should be concrete enough to guide several weeks of training, but broad enough that micro weeks and session cards still have real work to do.

### Coach-Led Mainstream Mezzo Type Work

For the first mezzo pass, only `mainstream_endurance` baseline block types are defined and built. Named-philosophy mezzo reviews come later.

The coach accepted three mainstream block types under most accepted mainstream macro types, with a fourth under Base Development because trail skill and terrain familiarity are important enough to need their own pre-specificity block. This is intentionally lean: enough to make every macro phase actionable, but not so many that mezzo becomes a session catalog.

For each proposed mainstream mezzo type, the coach asked:

- Is this a real block-level coaching concept?
- Does it belong under this macro phase?
- Is it different enough from nearby blocks?
- Is it too broad for mezzo or too detailed for micro/session?
- What should the block emphasize?
- What should it avoid?
- What micro weeks and sessions should usually sit inside it later?
- How does trail or mountain context change the block decision?

### Coach-Derived Mainstream Mezzo Types

| Parent macro type | Type ID | Type name | Coach decision | About this block | Mainstream status |
| --- | --- | --- | --- | --- | --- |
| Return To Consistency | `mezzo_type_reentry_rhythm_block` | Re-Entry Rhythm Block | Keep | Restores dependable training frequency and routine before meaningful load progression. It belongs at mezzo level because it organises several weeks around rhythm, not a single easy session. It should emphasize short repeatable outings, confidence, and low-risk terrain, while avoiding former-fitness tests or premature intensity. | Built as `mainstream_reentry_rhythm_block` |
| Return To Consistency | `mezzo_type_easy_aerobic_reconditioning_block` | Easy Aerobic Reconditioning Block | Keep | Rebuilds basic easy aerobic tolerance after interruption. It is more developed than simple re-entry rhythm but still below full base development. It should emphasize conservative duration progression, run-walk or low-impact options when useful, and recovery response. | Built as `mainstream_easy_aerobic_reconditioning_block` |
| Return To Consistency | `mezzo_type_movement_strength_reintroduction_block` | Movement Strength Reintroduction Block | Keep | Reintroduces supportive strength, mobility, and movement control without competing with the return to running. It belongs at mezzo level when movement support needs several weeks of careful exposure before hills, strength endurance, or technical terrain. | Built as `mainstream_movement_strength_reintroduction_block` |
| Base Development | `mezzo_type_aerobic_volume_block` | Aerobic Volume Block | Keep | Builds repeatable aerobic workload through controlled frequency, duration, or total-time progression. It should emphasize easy intensity, recoverability, and one-variable progression, while avoiding simultaneous increases in volume, intensity, and terrain cost. | Built as `mainstream_aerobic_volume_block` |
| Base Development | `mezzo_type_long_endurance_development_block` | Long Endurance Development Block | Keep | Extends long-run and time-on-feet tolerance while keeping the work mostly aerobic. It belongs under base when the athlete needs longer endurance before race-specific demands. Trail context changes the dose through vertical gain, surface, technicality, and descent load. | Built as `mainstream_long_endurance_development_block` |
| Base Development | `mezzo_type_strength_and_movement_support_block` | Strength And Movement Support Block | Keep | Builds general strength and movement quality around aerobic running. It is a support block, not a gym-focused phase. It should improve durability and readiness for later work while avoiding strength fatigue that displaces the base. | Built as `mainstream_strength_and_movement_support_block` |
| Base Development | `mezzo_type_trail_skill_and_terrain_familiarity_block` | Trail Skill And Terrain Familiarity Block | Keep | Builds low-to-moderate trail movement skill, hiking transitions, descending control, and confidence before race-specific preparation. It belongs under base because some terrain ability should be introduced gradually before course-specific work, while still avoiding premature race simulation. | Built as `mainstream_trail_skill_and_terrain_familiarity_block` |
| Capacity Development | `mezzo_type_threshold_control_block` | Threshold Control Block | Keep | Develops sustainable moderate-hard control, pacing discipline, and threshold-adjacent capacity after the base can support quality. It should emphasize controlled pressure and easy support days, while avoiding repeated race efforts. | Built as `mainstream_threshold_control_block` |
| Capacity Development | `mezzo_type_aerobic_power_block` | Aerobic Power Block | Keep | Targets high-end aerobic capacity through demanding but recoverable quality work. It belongs at mezzo level because the main coaching decision is several weeks of hard-work placement and recovery, not one interval session. | Built as `mainstream_aerobic_power_block` |
| Capacity Development | `mezzo_type_strength_endurance_block` | Strength Endurance Block | Keep | Develops force endurance for hills, fatigue, and durable mechanics. It should emphasize targeted muscular demand with aerobic support and clear recovery cost, while avoiding soreness chasing or treating all hills as the same stimulus. | Built as `mainstream_strength_endurance_block` |
| Race-Specific Preparation | `mezzo_type_course_demands_block` | Course Demands Block | Keep | Prepares the consequential demands of the target route or event: terrain, duration, gradient, technicality, environment, and descent cost. It belongs at mezzo level because it selects a several-week emphasis from the macro race-specific phase. | Built as `mainstream_course_demands_block` |
| Race-Specific Preparation | `mezzo_type_race_execution_practice_block` | Race Execution Practice Block | Keep | Rehearses pacing, gear, hiking transitions, route decisions, and composure under goal-relevant conditions. It should create useful race-day decision skill without turning every practice into a full race simulation. | Built as `mainstream_race_execution_practice_block` |
| Race-Specific Preparation | `mezzo_type_fueling_and_hydration_practice_block` | Fueling And Hydration Practice Block | Keep | Makes fueling and hydration trainable execution skills for longer or higher-cost events. It stays within coaching scope and belongs at mezzo level when intake practice needs repeated sessions and review. | Built as `mainstream_fueling_and_hydration_practice_block` |
| Peak And Taper | `mezzo_type_taper_freshness_block` | Taper Freshness Block | Keep | Reduces accumulated fatigue while preserving rhythm and confidence. It should emphasize freshness, familiarity, and reduced cost, while avoiding panic workouts or late fitness chasing. | Built as `mainstream_taper_freshness_block` |
| Peak And Taper | `mezzo_type_sharpening_touchpoint_block` | Sharpening Touchpoint Block | Keep | Keeps small reminders of race rhythm, coordination, or controlled intensity without adding meaningful fatigue. It belongs at mezzo level only when several final sessions are organised around touchpoints rather than development. | Built as `mainstream_sharpening_touchpoint_block` |
| Peak And Taper | `mezzo_type_race_readiness_check_block` | Race Readiness Check Block | Keep, watch scope | Organises the final one-to-two week readiness process around familiar movement, logistics, gear, pacing, and support routines. It stays at mezzo level only because it shapes the final taper window; if it becomes only a checklist, it should move to micro or app guidance. | Built as `mainstream_race_readiness_check_block` |
| Competition Management | `mezzo_type_between_race_recovery_block` | Between-Race Recovery Block | Keep | Restores function after one race before deciding what can fit before the next. It belongs under competition management because race stress itself is the main input and the next event limits ambition. | Built as `mainstream_between_race_recovery_block` |
| Competition Management | `mezzo_type_race_season_maintenance_block` | Race Season Maintenance Block | Keep | Preserves useful fitness between competitions with controlled cost. It should emphasize aerobic rhythm and small touchpoints, while avoiding a hidden build between close races. | Built as `mainstream_race_season_maintenance_block` |
| Competition Management | `mezzo_type_competition_learning_block` | Competition Learning Block | Keep, watch scope | Uses tune-up races and repeated race-season feedback to shape targeted practice before the next event. It remains a mezzo block only when the review changes the next several weeks of training; if it is only a debrief, it belongs in notes or app guidance. | Built as `mainstream_competition_learning_block` |
| Recovery And Transition | `mezzo_type_post_race_recovery_block` | Post-Race Recovery Block | Keep | Restores physical and mental readiness after a race or major objective. Trail and mountain context can increase recovery need through descent damage, duration, travel, heat, and technical load. | Built as `mainstream_post_race_recovery_block` |
| Recovery And Transition | `mezzo_type_reduced_load_adaptation_block` | Reduced-Load Adaptation Block | Keep | Lowers training load so previous work can be absorbed and reviewed. It belongs at mezzo level because recovery and consolidation may need several weeks, not merely one easy week. | Built as `mainstream_reduced_load_adaptation_block` |
| Recovery And Transition | `mezzo_type_transition_bridge_block` | Transition Bridge Block | Keep | Moves the athlete from recovery toward the next appropriate training direction. It should emphasize flexible structure and readiness observation, while avoiding an accidental build. | Built as `mainstream_transition_bridge_block` |
| Off-Season | `mezzo_type_low_pressure_aerobic_rhythm_block` | Low-Pressure Aerobic Rhythm Block | Keep | Preserves easy running continuity without race-preparation pressure. It belongs under off-season because the aim is decompression with enough rhythm to prevent a hard restart later. | Built as `mainstream_low_pressure_aerobic_rhythm_block` |
| Off-Season | `mezzo_type_general_strength_and_mobility_block` | General Strength And Mobility Block | Keep | Uses lower race pressure to rebuild supportive strength, mobility, balance, and movement options. It should build future capacity without creating a gym peak that compromises running. | Built as `mainstream_general_strength_and_mobility_block` |
| Off-Season | `mezzo_type_movement_variety_block` | Movement Variety Block | Keep | Restores freshness through varied, low-stakes movement. It should maintain general capacity and reduce monotony, while avoiding novelty overload or risky adventures during decompression. | Built as `mainstream_movement_variety_block` |
| Maintenance | `mezzo_type_aerobic_maintenance_block` | Aerobic Maintenance Block | Keep | Preserves aerobic fitness and training rhythm with controlled cost when full development is not appropriate. It should hold a repeatable dose rather than escalate. | Built as `mainstream_aerobic_maintenance_block` |
| Maintenance | `mezzo_type_quality_touchpoint_block` | Quality Touchpoint Block | Keep | Keeps a small amount of quality, coordination, or controlled intensity without starting a full build. It is useful for experienced runners who benefit from reminders but need low overall cost. | Built as `mainstream_quality_touchpoint_block` |
| Maintenance | `mezzo_type_constraint_friendly_consistency_block` | Constraint-Friendly Consistency Block | Keep | Preserves training through busy, uncertain, or limited life periods. It should protect a small repeatable dose and avoid guilt-driven sessions or pretending constraints are a hidden build. | Built as `mainstream_constraint_friendly_consistency_block` |

### Built Mainstream Mezzo Card Set

The accepted mainstream mezzo cards have been created and published as Drive/cache JSON cards. This section records build status without duplicating the full card content.

| Parent macro card | Built mainstream mezzo cards |
| --- | --- |
| `mainstream_return_to_consistency` | `mainstream_reentry_rhythm_block`, `mainstream_easy_aerobic_reconditioning_block`, `mainstream_movement_strength_reintroduction_block` |
| `mainstream_base_development` | `mainstream_aerobic_volume_block`, `mainstream_long_endurance_development_block`, `mainstream_strength_and_movement_support_block`, `mainstream_trail_skill_and_terrain_familiarity_block` |
| `mainstream_capacity_development` | `mainstream_threshold_control_block`, `mainstream_aerobic_power_block`, `mainstream_strength_endurance_block` |
| `mainstream_race_specific_preparation` | `mainstream_course_demands_block`, `mainstream_race_execution_practice_block`, `mainstream_fueling_and_hydration_practice_block` |
| `mainstream_peak_and_taper` | `mainstream_taper_freshness_block`, `mainstream_sharpening_touchpoint_block`, `mainstream_race_readiness_check_block` |
| `mainstream_competition_management` | `mainstream_between_race_recovery_block`, `mainstream_race_season_maintenance_block`, `mainstream_competition_learning_block` |
| `mainstream_recovery_and_transition` | `mainstream_post_race_recovery_block`, `mainstream_reduced_load_adaptation_block`, `mainstream_transition_bridge_block` |
| `mainstream_off_season` | `mainstream_low_pressure_aerobic_rhythm_block`, `mainstream_general_strength_and_mobility_block`, `mainstream_movement_variety_block` |
| `mainstream_maintenance` | `mainstream_aerobic_maintenance_block`, `mainstream_quality_touchpoint_block`, `mainstream_constraint_friendly_consistency_block` |

### Mezzo Philosophy Review

Named-philosophy mezzo review is in progress. The 80/20 pilot is drafted below and should be accepted or adjusted before building cards or repeating the workflow for the remaining philosophies.

This section defines only the macro-to-mezzo workflow. It explains how to decide which mezzo cards belong under named-philosophy macro cards. Mezzo-to-micro and micro-to-session workflows should be defined separately later.

For named philosophies, do not force the full mainstream macro structure onto the philosophy. Use three macro categories:

- `inherited_macro`: the philosophy has no separate macro card for this phase and uses the mainstream macro card.
- `philosophy_specific_equivalent_macro`: the philosophy has its own macro card for the same broad phase as mainstream.
- `philosophy_specific_new_macro`: the philosophy has a macro card that does not directly exist in the mainstream macro taxonomy.

Use this order:

1. Inherited macro pass: for each macro type marked `No separate macro card` in the macro review matrix, check whether the mainstream mezzo cards can also be inherited or whether the philosophy creates a mezzo-level distinction despite sharing the macro card.
2. Philosophy-specific equivalent macro pass: for each named-philosophy macro card that is an equivalent version of a mainstream macro type, compare the mainstream mezzo cards one by one and decide whether each should be reused, rewritten as a philosophy-specific version, renamed or restructured, or removed from that philosophy's mezzo set.
3. Shared macro addition pass: inside each inherited or equivalent macro context, ask whether the philosophy needs additional mezzo types that mainstream does not include.
4. Philosophy-specific new macro pass: define mezzo types for macro cards that are specific to the named philosophy and do not have a direct mainstream equivalent.
5. Completion review: after each philosophy, check for overbuilding, missing concepts, overlap, wrong level, bad parent mapping, and cards that should be merged or removed before building.

Use these verdicts during the shared macro mezzo comparison:

| Verdict | Meaning |
| --- | --- |
| `inherit_mainstream` | In an inherited macro context, the mainstream mezzo card is also inherited; no separate named-philosophy card is built. |
| `reuse_mainstream` | The mainstream mezzo card is sufficient; no separate named-philosophy card is built. |
| `specific_version` | The same broad mezzo type belongs, but the philosophy changes it enough to need its own card. |
| `remove_from_philosophy` | This mezzo type does not belong inside the philosophy's version of the macro. |
| `rename_or_restructure` | The concept belongs, but the name, boundaries, or grouping should change before a card is built. |
| `special_addition` | The philosophy needs an additional mezzo type not covered by the mainstream mezzo set. |

Parenting rule: if a named philosophy has an equivalent macro card, any accepted philosophy-specific mezzo card should parent to that named-philosophy macro card, not to the mainstream macro card. If the verdict is `reuse_mainstream`, do not create a duplicate card.

If a philosophy-specific mezzo card is justified inside an inherited macro context, it should parent to the inherited mainstream macro card, because that mainstream macro card is the actual macro parent for that philosophy in that phase.

#### Macro-To-Mezzo Coach Prompt

Use this prompt for each named philosophy before building mezzo cards:

```text
Hi team,

We are preparing macro-to-mezzo card decisions for {philosophy_profile_id}.
Please use the shared coaching foundation, the accepted macro matrix, the mainstream mezzo taxonomy, and the named philosophy profile as context.

First, classify the macro phases for this philosophy into three groups:
- inherited_macro: the philosophy uses the mainstream macro card without a separate macro card.
- philosophy_specific_equivalent_macro: the philosophy has its own macro card for the same broad phase as a mainstream macro.
- philosophy_specific_new_macro: the philosophy has a macro card that does not directly correspond to a mainstream macro phase.

For each inherited macro phase, check every mainstream mezzo under that macro. Decide whether each mezzo is inherited as-is, needs a philosophy-specific card despite the inherited macro, should be removed for that philosophy, or should be renamed/restructured.

Still inside each inherited macro phase, check whether the philosophy needs an added mezzo type that mainstream does not include.

For each philosophy-specific equivalent macro phase, compare every mainstream mezzo under the matching mainstream macro. Decide whether each should be reused, rewritten, removed, renamed, or restructured.

Still inside each philosophy-specific equivalent macro phase, check whether the philosophy needs an added mezzo type that mainstream does not include.

For each philosophy-specific new macro phase, define mezzo types directly from that philosophy's logic instead of starting from the mainstream mezzo taxonomy.

Before building cards, run a completion review. Remove duplicates, merge small distinctions, check parent mapping, and confirm that each candidate would affect app choice, explanation, sequencing, or structure.
```

### 80/20 Endurance Macro-To-Mezzo Pilot Review

This pilot applies the macro-to-mezzo workflow to `80_20_endurance` before repeating it for other philosophies. The purpose is to test the decision style and strictness before building named-philosophy mezzo cards.

Coach framing: 80/20 should not receive a duplicate mezzo card just because every block can mention easy/hard contrast. A separate 80/20 mezzo card is justified only where intensity distribution, protected easy work, selected quality density, metric choice, or trail mechanical-cost accounting changes the block structure enough that the app would choose, explain, or sequence it differently.

80/20 inherited macro phases are reviewed first. These are mainstream macro phases where 80/20 has no separate macro card:

| Inherited mainstream macro | Mainstream mezzo type reviewed | Coach verdict | Candidate card, if built | Coach reasoning |
| --- | --- | --- | --- | --- |
| `macro_001` `Mainstream Return To Consistency` | Re-Entry Rhythm Block | `inherit_mainstream` | None | The coaching problem is restoring rhythm and confidence. 80/20 does not change the block structure enough at this level. |
| `macro_001` `Mainstream Return To Consistency` | Easy Aerobic Reconditioning Block | `inherit_mainstream` | None | Easy discipline matters, but mainstream reconditioning already protects conservative aerobic rebuilding. A separate 80/20 card would mostly repeat the same block with different language. |
| `macro_001` `Mainstream Return To Consistency` | Movement Strength Reintroduction Block | `inherit_mainstream` | None | This block is about safe reintroduction of support work, not 80/20 distribution logic. |
| `macro_001` `Mainstream Return To Consistency` | Additional 80/20-specific return types | No `special_addition` | None | A distribution-reset idea is better handled later in base, maintenance, or micro/session guidance rather than creating a new return-to-consistency mezzo. |
| `macro_005` `Mainstream Peak And Taper` | Taper Freshness Block | `inherit_mainstream` | None | 80/20 can inform reduced-load and intensity-preservation details, but freshness remains the same mezzo-level objective. |
| `macro_005` `Mainstream Peak And Taper` | Sharpening Touchpoint Block | `inherit_mainstream` | None | Small race-rhythm or intensity reminders belong, but 80/20-specific dosing is more likely a micro/session prescription than a separate mezzo block. |
| `macro_005` `Mainstream Peak And Taper` | Race Readiness Check Block | `inherit_mainstream` | None | Readiness, logistics, and confidence checks are not structurally changed by 80/20. |
| `macro_005` `Mainstream Peak And Taper` | Additional 80/20-specific taper types | No `special_addition` | None | Exact 80/20 taper structures would require primary-plan review and likely belong below mezzo unless they change the whole taper block. |
| `macro_007` `Mainstream Recovery And Transition` | Post-Race Recovery Block | `inherit_mainstream` | None | Recovery is governed by race cost, soreness, readiness, and motivation. 80/20 does not change the post-race recovery block enough here. |
| `macro_007` `Mainstream Recovery And Transition` | Reduced-Load Adaptation Block | `inherit_mainstream` | None | Reduced-load weeks fit 80/20, but the inherited mainstream card is sufficient until exact 80/20 recovery-cycle prescriptions are reviewed. |
| `macro_007` `Mainstream Recovery And Transition` | Transition Bridge Block | `inherit_mainstream` | None | The bridge decision is about readiness for the next phase, not a unique 80/20 block structure. |
| `macro_007` `Mainstream Recovery And Transition` | Additional 80/20-specific recovery or transition types | No `special_addition` | None | If distribution correction is needed after a stressful period, it should usually appear in the next base or maintenance block rather than as a recovery-specific mezzo. |
| `macro_008` `Mainstream Off-Season` | Low-Pressure Aerobic Rhythm Block | `inherit_mainstream` | None | 80/20 can keep easy running easy, but off-season rhythm is mainly about decompression and continuity. |
| `macro_008` `Mainstream Off-Season` | General Strength And Mobility Block | `inherit_mainstream` | None | 80/20 strength material may matter later, but without deeper source review this remains mainstream support work. |
| `macro_008` `Mainstream Off-Season` | Movement Variety Block | `inherit_mainstream` | None | Movement variety is not primarily an 80/20 intensity-distribution concept. |
| `macro_008` `Mainstream Off-Season` | Additional 80/20-specific off-season types | No `special_addition` | None | No extra 80/20 off-season mezzo is justified because the phase goal is lower-pressure general readiness, not ratio enforcement. |

80/20 philosophy-specific equivalent macro cards are reviewed after the inherited macro pass. These are 80/20 macro cards that exist as distinct versions of mainstream macro phases:

| 80/20 macro card | Mainstream equivalent | Review status |
| --- | --- | --- |
| `macro_010` `80/20 Base Development` | `macro_002` `Mainstream Base Development` | Reviewed in pilot |
| `macro_011` `80/20 Capacity Development` | `macro_003` `Mainstream Capacity Development` | Reviewed in pilot |
| `macro_012` `80/20 Race-Specific Preparation` | `macro_004` `Mainstream Race-Specific Preparation` | Reviewed in pilot |
| `macro_014` `80/20 Competition Management` | `macro_006` `Mainstream Competition Management` | Reviewed in pilot |
| `macro_015` `80/20 Maintenance` | `macro_009` `Mainstream Maintenance` | Reviewed in pilot |

The inherited macro pass above is not a blanket skip. Each inherited mainstream mezzo type is checked, and each inherited macro also gets an addition check for possible 80/20-specific mezzo types.

| 80/20 macro | Mainstream mezzo type reviewed | Coach verdict | Candidate card, if built | Coach reasoning |
| --- | --- | --- | --- | --- |
| `80/20 Base Development` | Aerobic Volume Block | `specific_version` | `endurance_80_20_low_intensity_volume_block` | This is central enough to 80/20 to deserve its own block: volume progression must preserve a low-intensity majority and avoid accidental steady running. |
| `80/20 Base Development` | Long Endurance Development Block | `specific_version` | `endurance_80_20_long_endurance_distribution_block` | Long runs can quietly become moderate-hard through duration, climbing, descents, or terrain. 80/20 changes the block by requiring intensity and mechanical-cost accounting. |
| `80/20 Base Development` | Strength And Movement Support Block | `reuse_mainstream` | None | Strength support belongs, but without page-level 80/20 strength-plan review the distinction is not large enough for a separate mezzo card. |
| `80/20 Base Development` | Trail Skill And Terrain Familiarity Block | `reuse_mainstream` | None | Trail skill belongs, but 80/20 mostly changes the watchouts around hidden cost rather than the skill-development block itself. |
| `80/20 Base Development` | Additional 80/20-specific base types | No `special_addition` | None | Zone calibration and easy-discipline education should shape the specific aerobic-volume and long-endurance cards rather than become an extra block. |
| `80/20 Capacity Development` | Threshold Control Block | `specific_version` | `endurance_80_20_planned_moderate_work_block` | 80/20 treats moderate work as useful only when it has a job, dose, and recovery plan. That meaningfully changes threshold-adjacent block boundaries. |
| `80/20 Capacity Development` | Aerobic Power Block | `specific_version` | `endurance_80_20_high_intensity_quality_block` | High-intensity work needs protected easy support and enough spacing. The app would explain and sequence this differently from a generic aerobic-power block. |
| `80/20 Capacity Development` | Strength Endurance Block | `specific_version` | `endurance_80_20_hill_strength_quality_block` | Hill or strength-endurance work can count as hard even when pace or heart rate misleads. 80/20 changes placement and recovery accounting enough for a distinct card. |
| `80/20 Capacity Development` | Additional 80/20-specific capacity types | No `special_addition` | None | Quality density and hard/easy contrast are governing rules for the accepted capacity cards, not a separate block type. |
| `80/20 Race-Specific Preparation` | Course Demands Block | `specific_version` | `endurance_80_20_distribution_safe_course_demands_block` | 80/20 changes how course specificity is added: terrain, race pace, and environmental exposure must not dissolve into constant grey-zone stress. |
| `80/20 Race-Specific Preparation` | Race Execution Practice Block | `reuse_mainstream` | None | Execution practice belongs, but most distinctive 80/20 logic can be handled by the course-demands card plus later micro/session choices. |
| `80/20 Race-Specific Preparation` | Fueling And Hydration Practice Block | `reuse_mainstream` | None | Fueling practice is important, but 80/20 does not materially change the block enough to justify a duplicate. |
| `80/20 Race-Specific Preparation` | Additional 80/20-specific race-specific types | No `special_addition` | None | The specific distinction is distribution-safe specificity; that is covered by the accepted course-demands rewrite. |
| `80/20 Competition Management` | Between-Race Recovery Block | `specific_version` | `endurance_80_20_race_counted_recovery_block` | 80/20 treats races as hard inputs inside the distribution window, so recovery and next-stress timing are meaningfully different. |
| `80/20 Competition Management` | Race Season Maintenance Block | `specific_version` | `endurance_80_20_race_season_distribution_maintenance_block` | Between-race maintenance must protect low-intensity dominance and use small touchpoints only when race recovery allows. |
| `80/20 Competition Management` | Competition Learning Block | `reuse_mainstream` | None | Race feedback matters, but the learning process itself is not distinct enough from mainstream unless it changes the next block's distribution or recovery spacing. |
| `80/20 Competition Management` | Additional 80/20-specific competition types | No `special_addition` | None | The race-counted recovery and race-season maintenance cards cover the distinctive competition-season logic. |
| `80/20 Maintenance` | Aerobic Maintenance Block | `specific_version` | `endurance_80_20_easy_discipline_maintenance_block` | Maintenance is a common place for limited-time running to become moderate by default. 80/20 changes the block by protecting easy discipline. |
| `80/20 Maintenance` | Quality Touchpoint Block | `specific_version` | `endurance_80_20_quality_touchpoint_maintenance_block` | The quality touchpoint must be small, purposeful, and surrounded by low-cost work, which is distinct enough for app explanation and sequencing. |
| `80/20 Maintenance` | Constraint-Friendly Consistency Block | `reuse_mainstream` | None | The constraint context belongs, but it should be handled inside the two 80/20 maintenance cards rather than becoming a third duplicate. |
| `80/20 Maintenance` | Additional 80/20-specific maintenance types | No `special_addition` | None | No extra maintenance category is needed beyond easy-discipline maintenance and quality touchpoints. |

80/20 candidate review set: 10 cards.

- `endurance_80_20_low_intensity_volume_block`, parent `macro_010`
- `endurance_80_20_long_endurance_distribution_block`, parent `macro_010`
- `endurance_80_20_planned_moderate_work_block`, parent `macro_011`
- `endurance_80_20_high_intensity_quality_block`, parent `macro_011`
- `endurance_80_20_hill_strength_quality_block`, parent `macro_011`
- `endurance_80_20_distribution_safe_course_demands_block`, parent `macro_012`
- `endurance_80_20_race_counted_recovery_block`, parent `macro_014`
- `endurance_80_20_race_season_distribution_maintenance_block`, parent `macro_014`
- `endurance_80_20_easy_discipline_maintenance_block`, parent `macro_015`
- `endurance_80_20_quality_touchpoint_maintenance_block`, parent `macro_015`

Completion review: the pilot is intentionally stricter than "make an 80/20 version of every mainstream mezzo." Inherited and reused mainstream types stay mainstream because the 80/20 difference is either already handled at macro level, better handled in later micro/session cards, or not distinctive enough to change app behavior. The inherited macro pass now checks each mainstream mezzo and possible special additions explicitly rather than assuming inheritance automatically continues below macro level. The main cleanup question is whether the two 80/20 maintenance candidates should remain separate or merge into one low-cost maintenance card before building.

### Lydiard Macro-To-Mezzo Prepared Review

Coach framing: Lydiard mezzo cards should be built only where base-first sequencing, response-regulated recovery, feeling-based effort control, hill-resistance transition, or backward timing changes the block. Do not label general trail skills, generic hills, or generic long runs as Lydiard unless the sequence and recovery logic are doing real work.

| Macro category | Macro context | Coach result |
| --- | --- | --- |
| `inherited_macro` | Return To Consistency, Competition Management, Recovery And Transition, Off-Season, Maintenance | Mostly inherit mainstream mezzos. One recovery candidate is justified because response-regulated recovery is central to Lydiard readiness decisions. |
| `philosophy_specific_equivalent_macro` | `macro_016` Lydiard Base Development, `macro_018` Lydiard Race-Specific Preparation, `macro_019` Lydiard Peak And Taper | Review mainstream mezzos, then rewrite only where sequence, absorption, and integration materially change the block. |
| `philosophy_specific_new_macro` | `macro_017` Lydiard Hill Resistance Transition | Define mezzo types from Lydiard sequence logic rather than from mainstream capacity blocks. |

| Lydiard macro context | Mainstream or new mezzo concept reviewed | Coach verdict | Candidate card, if built | Coach reasoning |
| --- | --- | --- | --- | --- |
| Inherited `macro_001` Return To Consistency | All return-to-consistency mainstream mezzos and possible additions | `inherit_mainstream` | None | Lydiard principles can support patience, but the return structure is not distinct enough for separate mezzo cards. |
| Inherited `macro_006` Competition Management | All competition mainstream mezzos and possible additions | `inherit_mainstream` | None | Lydiard's classic sequence is goal-peak oriented, not primarily a multi-race management system. |
| Inherited `macro_007` Recovery And Transition | Reduced-Load Adaptation Block | `specific_version` | `lydiard_response_regulated_reduced_load_block` | Recovery response is a central Lydiard decision rule and can change when the next layer is allowed. |
| Inherited `macro_007` Recovery And Transition | Post-Race Recovery Block, Transition Bridge Block, and additions | `inherit_mainstream` | None | These remain mainstream unless the card is specifically about readiness for the next Lydiard layer. |
| Inherited `macro_008` Off-Season | All off-season mainstream mezzos and possible additions | `inherit_mainstream` | None | Off-season is not distinctive enough in the current Lydiard source record. |
| Inherited `macro_009` Maintenance | All maintenance mainstream mezzos and possible additions | `inherit_mainstream` | None | Lydiard aerobic support matters, but maintenance itself is not distinct enough at mezzo level. |
| `macro_016` Lydiard Base Development | Aerobic Volume Block | `specific_version` | `lydiard_sustainable_aerobic_conditioning_block` | Lydiard base asks for the greatest sustainable aerobic capacity the athlete can absorb, not merely more volume. |
| `macro_016` Lydiard Base Development | Long Endurance Development Block | `specific_version` | `lydiard_long_aerobic_conditioning_block` | Long aerobic work is important enough when tied to base-first sequencing and whole-runner absorption. |
| `macro_016` Lydiard Base Development | Strength And Movement Support Block, Trail Skill And Terrain Familiarity Block, and additions | `reuse_mainstream` | None | These can support the base but are not Lydiard-specific unless hill-resistance sequence logic appears. |
| `macro_017` Lydiard Hill Resistance Transition | Hill-resistance entry, coordination, and stronger running mechanics on hills | `special_addition` | `lydiard_hill_resistance_development_block` | The entry and hill-strength concepts overlap enough to become one block: introduce hill resistance, develop resilient mechanics, and prepare the next layer without chasing maximal climbing fatigue. |
| `macro_017` Lydiard Hill Resistance Transition | Absorption before later layers | `special_addition` | `lydiard_hill_transition_absorption_block` | The block should confirm the athlete can absorb the hill-resistance layer before moving on. |
| `macro_018` Lydiard Race-Specific Preparation | Course Demands Block and Race Execution Practice Block | `rename_or_restructure` | `lydiard_capacity_integration_block` | Lydiard race-specific work should integrate already built capacities rather than simply copy course demands. |
| `macro_018` Lydiard Race-Specific Preparation | Fueling And Hydration Practice Block and additions | `reuse_mainstream` | None | Fueling practice matters, but it is not Lydiard-specific with current source support. |
| `macro_019` Lydiard Peak And Taper | Taper Freshness Block and Sharpening Touchpoint Block | `rename_or_restructure` | `lydiard_sequence_expression_taper_block` | The taper expresses the completed sequence; it cannot manufacture missing base or hill preparation. |
| `macro_019` Lydiard Peak And Taper | Race Readiness Check Block and additions | `reuse_mainstream` | None | Readiness checks are useful but not distinct enough outside sequence-expression framing. |

Lydiard candidate review set after coverage sanity review: 7 cards.

- `lydiard_response_regulated_reduced_load_block`, parent `macro_007`
- `lydiard_sustainable_aerobic_conditioning_block`, parent `macro_016`
- `lydiard_long_aerobic_conditioning_block`, parent `macro_016`
- `lydiard_hill_resistance_development_block`, parent `macro_017`
- `lydiard_hill_transition_absorption_block`, parent `macro_017`
- `lydiard_capacity_integration_block`, parent `macro_018`
- `lydiard_sequence_expression_taper_block`, parent `macro_019`

Completion review: the hill-resistance transition was reduced from three candidates to two. This keeps the distinctive Lydiard sequence visible without splitting entry, coordination, and hill strength into cards that would mostly repeat each other.

### CTS Macro-To-Mezzo Prepared Review

Coach framing: CTS mezzo cards should exist where event demands, limiter selection, long-range trade-offs, ultra-specific workload, or practical race execution change the block. Avoid making every useful trail block a CTS card; the CTS label needs a clear demand-led decision.

| Macro category | Macro context | Coach result |
| --- | --- | --- |
| `inherited_macro` | Return To Consistency, Peak And Taper, Recovery And Transition, Off-Season, Maintenance | Inherit mainstream mezzos. No additional CTS-specific mezzo is justified without a CTS macro phase or a clear event-demand change. |
| `philosophy_specific_equivalent_macro` | `macro_020` CTS Base Development, `macro_021` CTS Capacity Development, `macro_022` CTS Race-Specific Preparation, `macro_023` CTS Competition Management | Rewrite only the blocks where demand-led limiter logic changes the planning decision. |
| `philosophy_specific_new_macro` | None currently | No new-macro mezzo pass. |

| CTS macro context | Mainstream or new mezzo concept reviewed | Coach verdict | Candidate card, if built | Coach reasoning |
| --- | --- | --- | --- | --- |
| Inherited macro phases | All mainstream mezzos and possible additions | `inherit_mainstream` | None | CTS can inform many coaching decisions, but inherited phases do not justify extra CTS mezzo cards without event-demand-specific structure. |
| `macro_020` CTS Base Development | Aerobic Volume Block | `specific_version` | `cts_repeatable_workload_foundation_block` | CTS base is about earned, repeatable workload that supports later ultra-specific demands. |
| `macro_020` CTS Base Development | Long Endurance Development Block | `specific_version` | `cts_long_run_durability_block` | Long-run development changes when duration, terrain cost, and ultra durability are explicit limiters. |
| `macro_020` CTS Base Development | Strength And Movement Support Block, Trail Skill And Terrain Familiarity Block, and additions | `reuse_mainstream` | None | These matter, but the distinct CTS work appears later when they map to a specific event demand or limiter. |
| `macro_021` CTS Capacity Development | Threshold Control Block and Aerobic Power Block | `rename_or_restructure` | `cts_limiter_focused_quality_block` | CTS should select quality because it solves a meaningful limiter, not because the plan needs a generic quality phase. |
| `macro_021` CTS Capacity Development | Strength Endurance Block | `specific_version` | `cts_ultra_strength_endurance_limiter_block` | Strength endurance is distinct when it addresses climbing, fatigue resistance, or terrain cost for a real event. |
| `macro_021` CTS Capacity Development | Additional CTS-specific capacity types | No `special_addition` | None | Limiter focus is the organising rule for the accepted quality and strength-endurance blocks. |
| `macro_022` CTS Race-Specific Preparation | Course Demands Block | `specific_version` | `cts_event_demands_block` | This is central CTS logic: the block starts from what the event will actually require. |
| `macro_022` CTS Race-Specific Preparation | Race Execution Practice Block | `specific_version` | `cts_race_execution_rehearsal_block` | Execution rehearsal is distinct when tied to the event's likely failure points and trade-offs. |
| `macro_022` CTS Race-Specific Preparation | Fueling And Hydration Practice Block | `specific_version` | `cts_fueling_and_hydration_strategy_block` | Fueling and hydration are major ultra execution demands and can deserve their own CTS block. |
| `macro_022` CTS Race-Specific Preparation | Additional CTS-specific race-specific types | No `special_addition` | None | The three accepted race-specific cards cover the main demand-led areas. |
| `macro_023` CTS Competition Management | Between-Race Recovery Block | `specific_version` | `cts_race_stress_recovery_block` | The race itself becomes a demand-specific stress that changes what can fit before the next event. |
| `macro_023` CTS Competition Management | Race Season Maintenance Block and Competition Learning Block | `rename_or_restructure` | `cts_between_event_adjustment_block` | Between-event work and race feedback overlap in CTS because both are used to decide the next demand-led adjustment. One card should cover readiness, learning, limiter review, and next-event trade-offs. |
| `macro_023` CTS Competition Management | Additional CTS-specific competition types | No `special_addition` | None | Recovery, readiness, and feedback adjustment cover the race-season logic. |

CTS candidate review set after coverage sanity review: 9 cards.

- `cts_repeatable_workload_foundation_block`, parent `macro_020`
- `cts_long_run_durability_block`, parent `macro_020`
- `cts_limiter_focused_quality_block`, parent `macro_021`
- `cts_ultra_strength_endurance_limiter_block`, parent `macro_021`
- `cts_event_demands_block`, parent `macro_022`
- `cts_race_execution_rehearsal_block`, parent `macro_022`
- `cts_fueling_and_hydration_strategy_block`, parent `macro_022`
- `cts_race_stress_recovery_block`, parent `macro_023`
- `cts_between_event_adjustment_block`, parent `macro_023`

Completion review: the race-season set was reduced from three competition-management candidates to two. `cts_between_event_adjustment_block` should carry the readiness and race-feedback logic together, because splitting them would create two cards that answer the same planning question.

### Evoke Endurance Macro-To-Mezzo Prepared Review

Coach framing: Evoke cards should exist where the layered model changes the block: aerobic capacity, strength reserve, muscular endurance, utilisation, threshold-informed intensity control, or local muscular cost. Do not make every mountain card Evoke-specific unless the layer and prerequisite logic are visible.

| Macro category | Macro context | Coach result |
| --- | --- | --- |
| `inherited_macro` | Return To Consistency, Peak And Taper, Competition Management, Recovery And Transition, Off-Season, Maintenance | Mostly inherit mainstream mezzos. One recovery candidate may be justified because local muscular-endurance work has distinctive absorption costs. |
| `philosophy_specific_equivalent_macro` | `macro_024` Evoke Base Development, `macro_026` Evoke Race-Specific Preparation | Rewrite where aerobic-capacity and utilisation logic change the block. |
| `philosophy_specific_new_macro` | `macro_025` Evoke Muscular Endurance Development | Define muscular-endurance mezzo types directly from the Evoke layer model. |

| Evoke macro context | Mainstream or new mezzo concept reviewed | Coach verdict | Candidate card, if built | Coach reasoning |
| --- | --- | --- | --- | --- |
| Inherited macro phases | Return, peak/taper, competition, off-season, maintenance mainstream mezzos and additions | `inherit_mainstream` | None | Evoke does not need separate cards in these inherited phases unless a layer-specific cost changes the block. |
| Inherited `macro_007` Recovery And Transition | Reduced-Load Adaptation Block | `specific_version` | `evoke_layer_absorption_recovery_block` | Recovery after muscular-endurance or high-cost mountain work can be structurally different because local damage may exceed cardiovascular stress. |
| Inherited `macro_007` Recovery And Transition | Post-Race Recovery Block, Transition Bridge Block, and additions | `inherit_mainstream` | None | These remain mainstream unless they are specifically absorbing an Evoke layer. |
| `macro_024` Evoke Base Development | Aerobic Volume Block and Long Endurance Development Block | `rename_or_restructure` | `evoke_aerobic_capacity_development_block` | Evoke base is less about generic volume and more about substantial aerobic capacity below/around the right threshold. |
| `macro_024` Evoke Base Development | Strength And Movement Support Block | `specific_version` | `evoke_strength_reserve_support_block` | Strength reserve is a named layer supporting later muscular endurance and utilisation. |
| `macro_024` Evoke Base Development | Trail Skill And Terrain Familiarity Block | `reuse_mainstream` | None | Trail familiarity matters, but the Evoke distinction is not the generic skill block itself. |
| `macro_024` Evoke Base Development | Additional Evoke-specific base types | `special_addition` | `evoke_aerobic_threshold_control_block` | Threshold-informed control is central enough to shape how the base is monitored and progressed. |
| `macro_025` Evoke Muscular Endurance Development | Readiness for muscular-endurance work | Entry criteria | None | Readiness is important, but it should be built into the uphill muscular-endurance card as prerequisites and progression checks rather than becoming a standalone mezzo block. |
| `macro_025` Evoke Muscular Endurance Development | Main repeated-force development | `special_addition` | `evoke_uphill_muscular_endurance_block` | This is the defining block: repeated uphill force with clear local muscular demand and recovery cost, entered only after adequate aerobic capacity and strength reserve. |
| `macro_025` Evoke Muscular Endurance Development | Absorption and progression control | `special_addition` | `evoke_muscular_endurance_absorption_block` | The block should prevent soreness chasing and confirm whether the layer is being absorbed. |
| `macro_026` Evoke Race-Specific Preparation | Course Demands Block and Race Execution Practice Block | `rename_or_restructure` | `evoke_objective_utilisation_block` | Race-specific work should integrate developed capacities rather than simulate too early. |
| `macro_026` Evoke Race-Specific Preparation | Fueling And Hydration Practice Block and additions | `reuse_mainstream` | None | Fueling practice matters, but the Evoke-specific distinction is utilisation of capacity, not fueling itself. |

Evoke candidate review set after coverage sanity review: 7 cards.

- `evoke_layer_absorption_recovery_block`, parent `macro_007`
- `evoke_aerobic_capacity_development_block`, parent `macro_024`
- `evoke_strength_reserve_support_block`, parent `macro_024`
- `evoke_aerobic_threshold_control_block`, parent `macro_024`
- `evoke_uphill_muscular_endurance_block`, parent `macro_025`
- `evoke_muscular_endurance_absorption_block`, parent `macro_025`
- `evoke_objective_utilisation_block`, parent `macro_026`

Completion review: the readiness candidate was removed as a standalone card. It should become entry criteria and progression guidance inside `evoke_uphill_muscular_endurance_block`, which keeps the muscular-endurance macro focused on actual block work and absorption.

### SWAP Macro-To-Mezzo Prepared Review

Coach framing: SWAP cards should exist where long-term fulfilment, athlete agency, health protection, economy/speed development, fatigue-resistance curiosity, or joyful adventure changes the block. Do not make separate SWAP cards for tone alone; the training decision must change.

| Macro category | Macro context | Coach result |
| --- | --- | --- |
| `inherited_macro` | Peak And Taper, Recovery And Transition, Maintenance | Mostly inherit mainstream mezzos, with one recovery/reset candidate because SWAP whole-athlete support can change the block. |
| `philosophy_specific_equivalent_macro` | `macro_027` SWAP Return To Consistency, `macro_028` SWAP Base Development, `macro_029` SWAP Capacity Development, `macro_030` SWAP Race-Specific Preparation, `macro_032` SWAP Competition Management, `macro_034` SWAP Off-Season | Review mainstream mezzos and keep only cards where the decision changes beyond supportive language. |
| `philosophy_specific_new_macro` | None currently | No new-macro mezzo pass. |

| SWAP macro context | Mainstream or new mezzo concept reviewed | Coach verdict | Candidate card, if built | Coach reasoning |
| --- | --- | --- | --- | --- |
| Inherited `macro_005` Peak And Taper | All peak/taper mainstream mezzos and additions | `inherit_mainstream` | None | SWAP confidence and support can shape language, but taper block structure remains mainstream unless a distinct athlete-agency decision appears later. |
| Inherited `macro_007` Recovery And Transition | Post-Race Recovery Block and Transition Bridge Block | `specific_version` | `swap_supported_recovery_reset_block` | SWAP can change recovery by explicitly protecting health, emotional reset, and athlete agency after stress. |
| Inherited `macro_007` Recovery And Transition | Reduced-Load Adaptation Block and additions | `inherit_mainstream` | None | Reduced load remains mainstream unless it is part of the supported reset card. |
| Inherited `macro_009` Maintenance | All maintenance mainstream mezzos and additions | `inherit_mainstream` | None | SWAP has no separate maintenance macro; the distinct maintenance logic is better handled in base, recovery, or competition contexts. |
| `macro_027` SWAP Return To Consistency | Re-Entry Rhythm Block and Easy Aerobic Reconditioning Block | `rename_or_restructure` | `swap_confidence_reentry_block` | The no-shame rhythm and confidence-aerobic return concepts answer one planning question: rebuild consistency while protecting agency, confidence, and health. |
| `macro_027` SWAP Return To Consistency | Movement Strength Reintroduction Block and additions | `reuse_mainstream` | None | Movement support is useful but not distinct enough without a health-specific limiter. |
| `macro_028` SWAP Base Development | Aerobic Volume Block | `specific_version` | `swap_sustainable_aerobic_rhythm_block` | SWAP base should build aerobic durability without sacrificing health, joy, or long-term consistency. |
| `macro_028` SWAP Base Development | Long Endurance Development Block | `specific_version` | `swap_adventure_endurance_block` | Long endurance can be shaped by purposeful adventure while still keeping boundaries. |
| `macro_028` SWAP Base Development | Strength And Movement Support Block and Trail Skill And Terrain Familiarity Block | `reuse_mainstream` | None | These belong but should not become SWAP cards unless economy, play, or health logic changes the structure. |
| `macro_028` SWAP Base Development | Additional SWAP-specific base types | `special_addition` | `swap_economy_speed_skill_support_block` | SWAP often keeps economy and speed as transferable skills even while building the base. |
| `macro_029` SWAP Capacity Development | Threshold Control Block and Aerobic Power Block | `rename_or_restructure` | `swap_speed_economy_development_block` | SWAP capacity work is often framed around speed, economy, and sustainable performance skill, not generic hard workouts. |
| `macro_029` SWAP Capacity Development | Strength Endurance Block | `specific_version` | `swap_fatigue_resistance_development_block` | Fatigue resistance is distinct enough when treated as a question to develop without chasing exhaustion. |
| `macro_029` SWAP Capacity Development | Additional SWAP-specific capacity types | No `special_addition` | None | The two accepted cards cover the main capacity distinction. |
| `macro_030` SWAP Race-Specific Preparation | Course Demands Block | `specific_version` | `swap_confidence_building_course_demands_block` | Specificity changes when confidence, agency, and health are protected alongside performance demands. |
| `macro_030` SWAP Race-Specific Preparation | Race Execution Practice Block | `specific_version` | `swap_agency_race_execution_practice_block` | Race execution should help the athlete make good decisions rather than only rehearse logistics. |
| `macro_030` SWAP Race-Specific Preparation | Fueling And Hydration Practice Block and additions | `reuse_mainstream` | None | Fueling is important but not distinct enough unless it becomes a health or confidence limiter. |
| `macro_032` SWAP Competition Management | Between-Race Recovery Block | `specific_version` | `swap_whole_athlete_between_race_recovery_block` | Between races, SWAP changes the decision by weighing excitement, health, identity, and long-term consistency. |
| `macro_032` SWAP Competition Management | Race Season Maintenance Block and Competition Learning Block | `rename_or_restructure` | `swap_race_season_health_and_joy_block` | Race-season work should preserve health, joy, and learning rather than turning every race into pressure. |
| `macro_032` SWAP Competition Management | Additional SWAP-specific competition types | No `special_addition` | None | The accepted race-season card should include learning without needing a separate debrief card. |
| `macro_034` SWAP Off-Season | Low-Pressure Aerobic Rhythm Block and Movement Variety Block | `rename_or_restructure` | `swap_off_season_identity_and_play_block` | Off-season identity reset and playful movement variety belong together as one lower-pressure reset block rather than two cards that would mostly share purpose and watchouts. |
| `macro_034` SWAP Off-Season | General Strength And Mobility Block and additions | `reuse_mainstream` | None | Support work remains mainstream unless it is part of playful reset or health restoration. |

SWAP candidate review set after coverage sanity review: 12 cards.

- `swap_supported_recovery_reset_block`, parent `macro_007`
- `swap_confidence_reentry_block`, parent `macro_027`
- `swap_sustainable_aerobic_rhythm_block`, parent `macro_028`
- `swap_adventure_endurance_block`, parent `macro_028`
- `swap_economy_speed_skill_support_block`, parent `macro_028`
- `swap_speed_economy_development_block`, parent `macro_029`
- `swap_fatigue_resistance_development_block`, parent `macro_029`
- `swap_confidence_building_course_demands_block`, parent `macro_030`
- `swap_agency_race_execution_practice_block`, parent `macro_030`
- `swap_whole_athlete_between_race_recovery_block`, parent `macro_032`
- `swap_race_season_health_and_joy_block`, parent `macro_032`
- `swap_off_season_identity_and_play_block`, parent `macro_034`

Completion review: this draft was reduced from 14 to 12 candidates because SWAP is the most at risk of overbuilding through tone alone. The return pair became one confidence re-entry block, and the off-season pair became one identity-and-play reset block.

### Sharman Ultra Macro-To-Mezzo Prepared Review

Coach framing: Sharman Ultra cards should exist where athlete-context adaptation, practical ultra execution, accessible substitutions, race feedback, or course reality changes the block. Because public source detail is less prescriptive, avoid creating Sharman cards that merely say "individualise this."

| Macro category | Macro context | Coach result |
| --- | --- | --- |
| `inherited_macro` | Return To Consistency, Base Development, Capacity Development, Peak And Taper, Recovery And Transition, Off-Season, Maintenance | Inherit mainstream mezzos. No inherited-macro additions are justified from the current source record. |
| `philosophy_specific_equivalent_macro` | `macro_037` Sharman Ultra Race-Specific Preparation, `macro_038` Sharman Ultra Competition Management | Rewrite only the practical ultra-execution and context-adaptation blocks. |
| `philosophy_specific_new_macro` | None currently | No new-macro mezzo pass. |

| Sharman macro context | Mainstream or new mezzo concept reviewed | Coach verdict | Candidate card, if built | Coach reasoning |
| --- | --- | --- | --- | --- |
| Inherited macro phases | All mainstream mezzos and possible additions | `inherit_mainstream` | None | Sharman principles can inform coaching judgement, but inherited phases do not have enough public method specificity for separate mezzo cards. |
| `macro_037` Sharman Ultra Race-Specific Preparation | Course Demands Block | `specific_version` | `sharman_course_reality_preparation_block` | Sharman-specific value is practical ultra course reality fitted to the athlete's life and access. |
| `macro_037` Sharman Ultra Race-Specific Preparation | Race Execution Practice Block | `specific_version` | `sharman_practical_ultra_execution_block` | Pacing, logistics, substitutions, and execution skills can materially change the block. |
| `macro_037` Sharman Ultra Race-Specific Preparation | Fueling And Hydration Practice Block | `specific_version` | `sharman_fueling_gear_logistics_block` | Fueling, gear, and logistics are practical ultra limiters that can deserve a distinct card. |
| `macro_037` Sharman Ultra Race-Specific Preparation | Additional Sharman-specific race-specific types | No `special_addition` | None | The three accepted cards cover practical ultra preparation without inventing proprietary structure. |
| `macro_038` Sharman Ultra Competition Management | Between-Race Recovery Block | `specific_version` | `sharman_context_aware_between_race_recovery_block` | Recovery between events is shaped by athlete life, goals, experience, and ultra-specific cost. |
| `macro_038` Sharman Ultra Competition Management | Competition Learning Block | `specific_version` | `sharman_adaptive_race_feedback_block` | Race feedback matters when it teaches the athlete and changes the next decision. |
| `macro_038` Sharman Ultra Competition Management | Race Season Maintenance Block and additions | `reuse_mainstream` | None | Maintenance is not distinct enough without clearer Sharman-specific structure. |

Sharman candidate review set: 5 cards.

- `sharman_course_reality_preparation_block`, parent `macro_037`
- `sharman_practical_ultra_execution_block`, parent `macro_037`
- `sharman_fueling_gear_logistics_block`, parent `macro_037`
- `sharman_context_aware_between_race_recovery_block`, parent `macro_038`
- `sharman_adaptive_race_feedback_block`, parent `macro_038`

Completion review: this is intentionally conservative. The current source record supports practical ultra coaching judgement, but not enough named block structure to justify many additional Sharman-specific mezzos.

## Named-Philosophy Mezzo Coverage Sanity Review

This review checks whether the candidate lists are too small, too large, or appropriately strict before building card files. The specific card count is not the whole philosophy coverage; inherited and reused mainstream mezzos still remain available through `macro_mezzo_reuse.json`.

| Philosophy | Specific mezzo candidates after sanity review | Inherited mainstream mezzos | Reused mainstream mezzos | Planned usable mezzo relationships after build | Coach verdict |
| --- | ---: | ---: | ---: | ---: | --- |
| `80_20_endurance` | 10 | 12 | 6 | 28 | Acceptable strict set. The specific cards cover distribution-protected volume, quality, race specificity, competition stress, and maintenance. Calibration, distribution audits, and easy-discipline reminders should mostly appear inside those cards or later micro/session/app guidance unless they become multi-week blocks. |
| `lydiard` | 7 | 14 | 4 | 25 | Acceptable after reduction. Hill-resistance was reduced from three cards to two because entry, coordination, and hill strength belong together; absorption remains separate because it governs movement to the next Lydiard layer. |
| `cts` | 9 | 15 | 2 | 26 | Acceptable after reduction. CTS has enough specific mezzo coverage where demand-led limiter logic changes the block, while between-event readiness and race feedback were merged because they answer the same next-adjustment question. |
| `evoke_endurance` | 7 | 17 | 2 | 26 | Acceptable after reduction. The set protects the Evoke layer model without creating a standalone readiness card; readiness belongs as entry criteria inside muscular-endurance development. |
| `swap` | 12 | 7 | 5 | 24 | Acceptable but intentionally watched for tone-based overbuilding. Return and off-season cards were each merged into one stronger card so SWAP-specific content changes planning decisions rather than only emotional language. |
| `sharman_ultra` | 5 | 22 | 1 | 28 | Acceptable conservative set. Sharman-specific cards stay focused on practical ultra course reality, execution, fueling/logistics, between-race recovery, and adaptive feedback; generic individualisation remains card guidance, not a separate type. |

Coverage conclusion: the prepared sets are not underbuilt once inherited and reused mainstream coverage is counted. They are strict by design. Build the accepted named-philosophy mezzo card files next, but keep micro/session/app guidance available for concepts that are important yet too narrow or operational to be mezzo cards.

## Open Mezzo Questions

- Review the built named-philosophy mezzo card files for content quality before cloud upload.
- During later micro/session work, keep readiness checks, calibration details, workout distribution, and exact session execution mostly below mezzo unless they truly define a multi-week block.

## Macro-Mezzo Reuse Metadata

When a named philosophy inherits a mainstream macro or reuses a mainstream mezzo under a philosophy-specific equivalent macro, the app should use explicit reuse metadata instead of duplicated card files. The metadata lives in `macro_mezzo_reuse.json` and is also included in the app-facing `training_cards_library.json` bundle.

Each reuse entry records the philosophy profile, macro card ID and name, reused mainstream mezzo card ID and name, and whether the relationship is `inherit_mainstream` or `reuse_mainstream`. This keeps the structure visible for the app while preserving one source of truth for shared card content.

## Micro Level

Micro cards define reusable week-level structures inside a mezzo block. They answer: what does this week need to do, how is stress distributed, which session roles matter most, how is recovery protected, and what signs would make the coach progress, hold, or reduce?

Micro cards should not become single-session prescriptions. They can name likely session roles, but the exact workout belongs at session level. They should also avoid becoming mini-mezzo cards; the block-level purpose is already defined by the parent mezzo card.

For micro work, use the same build system as macro-to-mezzo:

- First define the `mainstream_endurance` week-type taxonomy under accepted mainstream mezzo blocks.
- Then review named philosophies against those mainstream week types.
- Reuse mainstream micro cards when the week structure is still the same.
- Create a philosophy-specific micro card only when the philosophy meaningfully changes the week structure, stress distribution, sequencing, or app-facing decision.
- After mainstream week types are reviewed, add philosophy-specific special week types that do not exist in the mainstream taxonomy.

The specificity standard is stricter at micro level than at macro or mezzo level because weekly variations can multiply quickly. A separate micro type is justified only when it changes the week-level coaching decision. Small differences in language, watchouts, workout flavor, or exact session execution should stay in the parent mezzo card, session cards, or app guidance.

### Coach-Led Mainstream Micro Type Work

Micro types are not copied mechanically from the mezzo card names. For each parent mezzo block, the coach should ask:

- What weekly structures are actually needed to make this block coachable?
- Is this a real week-level pattern, or only a session detail?
- Does the week have a distinct job inside the block?
- Does it change stress distribution, key session placement, recovery demand, or readiness checks?
- Is the concept already covered by another micro type?
- How does trail or mountain context change this week?
- Should `mainstream_endurance` receive a card for this type?

### Coach-Derived Mainstream Micro Types

These are accepted mainstream week types for the micro layer. They are intentionally strict and reusable, but they are not forced into a fixed "two weeks per block" pattern. Each parent mezzo receives as many week types as the coach needs to make the block usable without pushing session-level detail upward into the micro layer.

Common low-complexity blocks often need two week roles: one to create or maintain the main stimulus and one to consolidate, check, or reduce cost. Higher-stress, higher-specificity, or more operational blocks may need three week roles because introduction, development, and absorption are genuinely different coaching decisions.

#### Return To Consistency

| Parent mezzo | Micro type ID | Week type name | Coach decision | About this week | Mainstream status |
| --- | --- | --- | --- | --- | --- |
| Re-Entry Rhythm Block | `micro_type_reentry_routine_anchor_week` | Routine Anchor Week | Keep | Establishes a repeatable weekly rhythm with short, easy, predictable runs and enough space between them that the athlete finishes wanting to continue. It belongs at micro level because the coaching decision is how the week is arranged, not which single session is run. | Planned |
| Re-Entry Rhythm Block | `micro_type_reentry_frequency_extension_week` | Frequency Extension Week | Keep | Adds one small exposure or slightly lengthens an existing easy outing only after the routine is stable. The week emphasizes continuity over load and avoids using motivation spikes to rush back into full training. | Planned |
| Easy Aerobic Reconditioning Block | `micro_type_easy_aerobic_reconditioning_week` | Easy Aerobic Reconditioning Week | Keep | Uses mostly easy running to rebuild aerobic feel, basic durability, and confidence after interruption. The week should feel controlled, familiar, and recoverable rather than like a test of lost fitness. | Planned |
| Easy Aerobic Reconditioning Block | `micro_type_aerobic_reconditioning_hold_week` | Aerobic Reconditioning Hold Week | Keep | Holds volume and terrain cost steady so the athlete can absorb returning frequency. This is a real micro decision because the coach deliberately chooses not to progress despite the block still aiming at reconditioning. | Planned |
| Movement Strength Reintroduction Block | `micro_type_strength_reintroduction_week` | Strength Reintroduction Week | Keep | Reintroduces simple strength, mobility, drills, or strides at a dose that does not compromise easy running. The week protects soreness management and movement quality before heavier or more specific work appears. | Planned |
| Movement Strength Reintroduction Block | `micro_type_movement_tolerance_check_week` | Movement Tolerance Check Week | Keep | Keeps strength and movement work present while checking next-day soreness, stiffness, downhill tolerance, and coordination. It belongs at micro level because the main decision is weekly spacing and response, not exercise selection alone. | Planned |

#### Base Development

| Parent mezzo | Micro type ID | Week type name | Coach decision | About this week | Mainstream status |
| --- | --- | --- | --- | --- | --- |
| Aerobic Volume Block | `micro_type_aerobic_volume_baseline_week` | Aerobic Volume Baseline Week | Keep | Establishes the current repeatable volume and frequency before meaningful progression. It belongs at micro level because the coach is deciding whether the week is stable enough to build from, not prescribing individual runs. | Planned |
| Aerobic Volume Block | `micro_type_aerobic_volume_build_week` | Aerobic Volume Build Week | Keep | Builds weekly aerobic load through easy running frequency, modest duration increases, or both. It avoids turning volume growth into faster ordinary running and keeps the athlete's easy effort genuinely sustainable. | Planned |
| Aerobic Volume Block | `micro_type_aerobic_volume_absorption_week` | Aerobic Volume Absorption Week | Keep | Holds or slightly reduces load so the athlete can consolidate recent volume. This week is needed because durable aerobic development depends on absorbing frequency and duration, not only adding them. | Planned |
| Long Endurance Development Block | `micro_type_long_run_extension_week` | Long Run Extension Week | Keep | Extends the long outing or time-on-feet stimulus while keeping the rest of the week supportive. Trail context may shift the progression from distance to duration, vertical gain, hiking, or descent cost. | Planned |
| Long Endurance Development Block | `micro_type_long_endurance_specificity_week` | Long Endurance Specificity Week | Keep | Keeps the long-endurance emphasis but changes the terrain, duration, hiking, vertical, or fueling context to better match the athlete's goal. It is distinct from simply extending the long run because the week changes what kind of endurance is being practiced. | Planned |
| Long Endurance Development Block | `micro_type_long_run_consolidation_week` | Long Run Consolidation Week | Keep | Keeps the long-endurance stimulus familiar while reducing novelty or total cost elsewhere. It prevents the long run from becoming a weekly exam and protects consistency around it. | Planned |
| Strength And Movement Support Block | `micro_type_strength_support_integration_week` | Strength Support Integration Week | Keep | Places strength or movement support around running so it improves durability without stealing from the main aerobic work. The weekly spacing decision is the key coaching feature. | Planned |
| Strength And Movement Support Block | `micro_type_strength_support_deload_week` | Strength Support Deload Week | Keep | Reduces strength load, novelty, or soreness risk while preserving movement quality. This week is useful when run training needs priority or when connective tissue and muscle response need more time. | Planned |
| Trail Skill And Terrain Familiarity Block | `micro_type_trail_familiarity_exposure_week` | Trail Familiarity Exposure Week | Keep | Adds controlled trail, gradient, surface, or technical exposure without making the whole week race-specific. The week develops confidence and coordination while limiting descent and terrain novelty. | Planned |
| Trail Skill And Terrain Familiarity Block | `micro_type_trail_skill_consolidation_week` | Trail Skill Consolidation Week | Keep | Repeats familiar terrain demands at low enough cost that the athlete becomes more fluent rather than more fatigued. It is distinct from exposure because the main job is stabilizing skill and confidence. | Planned |

#### Capacity Development

| Parent mezzo | Micro type ID | Week type name | Coach decision | About this week | Mainstream status |
| --- | --- | --- | --- | --- | --- |
| Threshold Control Block | `micro_type_threshold_introduction_week` | Threshold Introduction Week | Keep | Introduces controlled threshold or comfortably-hard work while preserving enough easy running and recovery around it. The week teaches restraint before larger doses are considered. | Planned |
| Threshold Control Block | `micro_type_threshold_development_week` | Threshold Development Week | Keep | Builds the amount or specificity of threshold work without letting it drift into uncontrolled race effort. It belongs at micro level because the week must decide where quality sits relative to endurance and recovery. | Planned |
| Threshold Control Block | `micro_type_threshold_absorption_week` | Threshold Absorption Week | Keep | Reduces or simplifies threshold demand while checking whether the athlete is absorbing the work. This is distinct from development because the main coaching decision is restraint, not progression. | Planned |
| Aerobic Power Block | `micro_type_aerobic_power_introduction_week` | Aerobic Power Introduction Week | Keep | Introduces aerobic-power work with conservative dose, familiar terrain, and generous recovery spacing. It is needed because high-end aerobic stress should not jump immediately to full development load. | Planned |
| Aerobic Power Block | `micro_type_aerobic_power_stimulus_week` | Aerobic Power Stimulus Week | Keep | Places a clear aerobic-power stimulus in an otherwise supportive week. The goal is meaningful high-end aerobic stress without stacking too many demanding sessions. | Planned |
| Aerobic Power Block | `micro_type_aerobic_power_recovery_spacing_week` | Aerobic Power Recovery-Spacing Week | Keep | Keeps the aerobic-power signal present while increasing spacing, reducing volume, or simplifying terrain so the athlete can absorb the work. This is not a full deload; it is a controlled quality-support week. | Planned |
| Strength Endurance Block | `micro_type_strength_endurance_introduction_week` | Strength Endurance Introduction Week | Keep | Introduces uphill, resistance, or sustained muscular demand before a full strength-endurance stimulus week is appropriate. It protects connective tissue and downhill recovery cost while the athlete learns the feel of the work. | Planned |
| Strength Endurance Block | `micro_type_strength_endurance_stimulus_week` | Strength Endurance Stimulus Week | Keep | Adds sustained climbing, resistance, uphill work, or muscular-endurance demand at a recoverable dose. Trail and mountain context strongly affect the chosen stress because grade, footing, and descent cost matter. | Planned |
| Strength Endurance Block | `micro_type_strength_endurance_absorption_week` | Strength Endurance Absorption Week | Keep | Protects recovery from muscular damage while keeping easy aerobic rhythm alive. This week is needed because strength-endurance stress can outlast the workout and affect several following days. | Planned |

#### Race-Specific Preparation

| Parent mezzo | Micro type ID | Week type name | Coach decision | About this week | Mainstream status |
| --- | --- | --- | --- | --- | --- |
| Course Demands Block | `micro_type_course_demands_exposure_week` | Course Demands Exposure Week | Keep | Introduces the most consequential terrain, duration, gradient, surface, or environmental demand in controlled form. It avoids copying the race blindly and focuses on the demands that actually change preparation. | Planned |
| Course Demands Block | `micro_type_course_demands_integration_week` | Course Demands Integration Week | Keep | Combines course-relevant demands with normal training rhythm so the athlete learns to absorb specificity without losing the broader plan. It is week-level because the decision is how specificity fits around recovery and support work. | Planned |
| Course Demands Block | `micro_type_course_demands_simulation_week` | Course Demands Simulation Week | Keep | Uses a larger or more complete course-specific exposure when the athlete is ready and the timing justifies it. It is distinct from exposure because the week intentionally tests how multiple demands interact, without becoming a race replacement. | Planned |
| Race Execution Practice Block | `micro_type_race_execution_integration_week` | Race Execution Integration Week | Keep | Introduces execution skills such as pacing discipline, gear use, decision routines, or aid-station flow inside normal training. It prepares the athlete for later rehearsal without requiring a high-cost simulation. | Planned |
| Race Execution Practice Block | `micro_type_race_execution_rehearsal_week` | Race Execution Rehearsal Week | Keep | Practices pacing, gear, terrain decisions, mental routines, or aid-station-like behaviors in a structured week. The goal is better execution, not proving readiness through excessive simulation. | Planned |
| Race Execution Practice Block | `micro_type_execution_feedback_week` | Execution Feedback Week | Keep | Uses a lower-cost week to review what the athlete learned from rehearsal and adjust future race strategy. It belongs at micro level when the week is deliberately organized around learning, not just analysis after a workout. | Planned |
| Fueling And Hydration Practice Block | `micro_type_fueling_integration_week` | Fueling Integration Week | Keep | Introduces fueling and hydration practice into ordinary endurance training before making it a primary rehearsal demand. This week is needed because the athlete often needs habit formation before tolerance testing. | Planned |
| Fueling And Hydration Practice Block | `micro_type_fueling_practice_week` | Fueling Practice Week | Keep | Places fueling and hydration practice into long, steady, or race-relevant sessions while keeping training stress manageable. The week treats nutrition as a trainable skill under realistic conditions. | Planned |
| Fueling And Hydration Practice Block | `micro_type_fueling_tolerance_check_week` | Fueling Tolerance Check Week | Keep | Keeps the physical training simpler while checking gut tolerance, timing, product choice, heat response, and logistics. This week is distinct because the main adaptation target is execution reliability, not bigger fitness. | Planned |

#### Peak And Taper

| Parent mezzo | Micro type ID | Week type name | Coach decision | About this week | Mainstream status |
| --- | --- | --- | --- | --- | --- |
| Taper Freshness Block | `micro_type_taper_load_reduction_week` | Taper Load Reduction Week | Keep | Reduces training cost while preserving rhythm, confidence, and enough movement to avoid feeling flat. The week should not chase new fitness or remove all familiar running. | Planned |
| Taper Freshness Block | `micro_type_final_freshness_week` | Final Freshness Week | Keep | Organizes the final pre-race week around freshness, familiarity, logistics, sleep, and low-risk movement. Trail and ultra goals may require extra attention to travel, equipment, and descent-damage avoidance. | Planned |
| Sharpening Touchpoint Block | `micro_type_sharpening_touchpoint_week` | Sharpening Touchpoint Week | Keep | Includes a small familiar quality touch that preserves coordination and confidence without creating fatigue. The week is distinct from general taper reduction because it intentionally keeps a small performance signal. | Planned |
| Sharpening Touchpoint Block | `micro_type_sharpening_absorption_week` | Sharpening Absorption Week | Keep | Allows a previous sharpening touch to settle while keeping the athlete calm and prepared. It prevents a good touchpoint from inviting extra last-minute work. | Planned |
| Race Readiness Check Block | `micro_type_readiness_confirmation_week` | Readiness Confirmation Week | Keep | Confirms gear, pacing cues, fueling plan, logistics, and body signals with very low added cost. It is a week structure only when these checks are integrated into the final taper rhythm. | Planned |
| Race Readiness Check Block | `micro_type_pre_race_settle_week` | Pre-Race Settle Week | Keep | Prioritizes calm, familiar movement, problem prevention, and confidence when the athlete is close enough to the race that doing less is often the best coaching choice. | Planned |

#### Competition Management

| Parent mezzo | Micro type ID | Week type name | Coach decision | About this week | Mainstream status |
| --- | --- | --- | --- | --- | --- |
| Between-Race Recovery Block | `micro_type_post_competition_reset_week` | Post-Competition Reset Week | Keep | Reduces load and complexity after a race while checking soreness, motivation, sleep, and musculoskeletal response. Trail races may require special respect for descent damage and travel fatigue. | Planned |
| Between-Race Recovery Block | `micro_type_between_race_bridge_week` | Between-Race Bridge Week | Keep | Rebuilds a small amount of rhythm between events without pretending there is time for a full development block. The week keeps the athlete moving toward the next race while protecting recovery. | Planned |
| Race Season Maintenance Block | `micro_type_race_season_rhythm_week` | Race Season Rhythm Week | Keep | Maintains aerobic rhythm and a small touch of quality between competitions. It avoids loading the week as if the athlete were outside race season. | Planned |
| Race Season Maintenance Block | `micro_type_low_cost_quality_touch_week` | Low-Cost Quality Touch Week | Keep | Uses a small controlled stimulus to keep coordination or intensity familiarity without adding meaningful fatigue. It belongs at micro level because placement and restraint across the whole week are the coaching decision. | Planned |
| Competition Learning Block | `micro_type_race_debrief_learning_week` | Race Debrief Learning Week | Keep | Turns a recent race into useful coaching information while keeping physical training cost modest. The week can include easy movement, review, and targeted rehearsal of one lesson. | Planned |
| Competition Learning Block | `micro_type_race_lesson_integration_week` | Race Lesson Integration Week | Keep | Applies one clear race lesson in training without overcorrecting everything at once. The week is justified when learning changes the structure, not merely when the athlete writes notes. | Planned |

#### Recovery And Transition

| Parent mezzo | Micro type ID | Week type name | Coach decision | About this week | Mainstream status |
| --- | --- | --- | --- | --- | --- |
| Post-Race Recovery Block | `micro_type_immediate_post_race_recovery_week` | Immediate Post-Race Recovery Week | Keep | Protects healing, sleep, nutrition, mobility, and very gentle movement after a demanding event. The week should not be judged by fitness maintenance. | Planned |
| Post-Race Recovery Block | `micro_type_post_race_return_to_movement_week` | Post-Race Return-To-Movement Week | Keep | Reintroduces easy running or cross-training only as symptoms and motivation allow. Trail and ultra events may require a slower return because soreness and neuromuscular fatigue can linger. | Planned |
| Reduced-Load Adaptation Block | `micro_type_reduced_load_absorption_week` | Reduced-Load Absorption Week | Keep | Deliberately lowers training cost after a demanding block or fatigue signal while maintaining enough rhythm for the athlete to feel connected to training. | Planned |
| Reduced-Load Adaptation Block | `micro_type_reduced_load_readiness_check_week` | Reduced-Load Readiness Check Week | Keep | Uses simple sessions and response checks to decide whether the athlete is ready to resume building. It is a micro card because the week is organized around the readiness decision. | Planned |
| Transition Bridge Block | `micro_type_transition_reorientation_week` | Transition Reorientation Week | Keep | Shifts attention from one training emphasis to the next with reduced pressure and simple structure. The week helps avoid abrupt jumps between blocks. | Planned |
| Transition Bridge Block | `micro_type_transition_rhythm_week` | Transition Rhythm Week | Keep | Re-establishes enough normal weekly rhythm to enter the next block cleanly. It should feel purposeful but not like a hidden development week. | Planned |

#### Off-Season

| Parent mezzo | Micro type ID | Week type name | Coach decision | About this week | Mainstream status |
| --- | --- | --- | --- | --- | --- |
| Low-Pressure Aerobic Rhythm Block | `micro_type_low_pressure_aerobic_week` | Low-Pressure Aerobic Week | Keep | Preserves easy aerobic rhythm without race-preparation pressure. The week should leave room for life, freshness, and motivation to return. | Planned |
| Low-Pressure Aerobic Rhythm Block | `micro_type_unstructured_aerobic_option_week` | Unstructured Aerobic Option Week | Keep | Allows flexible easy movement while still protecting enough consistency to avoid a complete reset later. It belongs at micro level because the coach sets boundaries for freedom across the week. | Planned |
| General Strength And Mobility Block | `micro_type_general_strength_foundation_week` | General Strength Foundation Week | Keep | Uses general strength, mobility, and tissue-capacity work without needing race-specific transfer immediately. Running remains supportive rather than dominant. | Planned |
| General Strength And Mobility Block | `micro_type_general_mobility_recovery_week` | General Mobility Recovery Week | Keep | Keeps movement quality and range of motion alive while reducing load and soreness. This week is useful when the athlete needs restoration more than progression. | Planned |
| Movement Variety Block | `micro_type_movement_variety_exploration_week` | Movement Variety Exploration Week | Keep | Introduces hiking, cycling, skiing, gym work, games, or other movement options at low pressure. The goal is freshness and general athleticism, not disguised training stress. | Planned |
| Movement Variety Block | `micro_type_movement_variety_rhythm_week` | Movement Variety Rhythm Week | Keep | Keeps varied movement repeatable enough that off-season does not become random overload. It protects recovery while letting the athlete enjoy broader movement choices. | Planned |

#### Maintenance

| Parent mezzo | Micro type ID | Week type name | Coach decision | About this week | Mainstream status |
| --- | --- | --- | --- | --- | --- |
| Aerobic Maintenance Block | `micro_type_aerobic_maintenance_week` | Aerobic Maintenance Week | Keep | Holds useful aerobic rhythm with controlled cost during busy, between-goal, or constrained periods. The week should be easy to repeat and hard to derail. | Planned |
| Aerobic Maintenance Block | `micro_type_aerobic_maintenance_refresh_week` | Aerobic Maintenance Refresh Week | Keep | Adds a small dose of freshness, variety, or slightly longer easy running without turning maintenance into development. It is useful when the athlete is stable but needs the week to feel alive. | Planned |
| Quality Touchpoint Block | `micro_type_quality_touchpoint_week` | Quality Touchpoint Week | Keep | Keeps a small familiar quality stimulus in the week while protecting low overall cost. It should preserve coordination or intensity familiarity, not create a full capacity block. | Planned |
| Quality Touchpoint Block | `micro_type_quality_touchpoint_recovery_week` | Quality Touchpoint Recovery Week | Keep | Places recovery emphasis around a small quality touch so the week remains sustainable. This prevents maintenance from drifting into chronic moderate fatigue. | Planned |
| Constraint-Friendly Consistency Block | `micro_type_constraint_friendly_week` | Constraint-Friendly Week | Keep | Builds a realistic week around limited time, travel, work, family, or energy constraints. The coaching decision is preserving what matters most rather than forcing a normal template. | Planned |
| Constraint-Friendly Consistency Block | `micro_type_minimum_effective_rhythm_week` | Minimum Effective Rhythm Week | Keep | Defines the smallest useful weekly rhythm that keeps the athlete connected to training. It should be honest, repeatable, and protective rather than a guilty compromise. | Planned |

### Built Mainstream Micro Card Set

The 64 accepted mainstream micro types have been created and published as Drive/cache JSON cards.

Build status:

- `mainstream_endurance`: 64 micro cards, `micro_001` through `micro_064`
- Parent coverage: all 28 mainstream mezzo blocks
- Exported cache count after build: 175 total cards, including 64 micro cards

### Mainstream Micro Completion Review

Coach review: the mainstream micro taxonomy is accepted as a planning map and has now been implemented as mainstream micro card files. The set is intentionally conservative but no longer artificially symmetrical. Low-complexity or low-risk blocks usually stay at two week types. Higher-stress and higher-specificity blocks receive three week types where introduction, development, simulation, practice, feedback, or absorption represent genuinely different weekly coaching decisions.

Potential reduction watchouts:

- Some absorption, recovery-spacing, and hold weeks may later be merged if the card content becomes too similar.
- Some learning, readiness, and check weeks must stay week-structured; if they become only checklists, they should move to app guidance or session support notes.
- Some quality touchpoint weeks may later become shared/reused micro cards instead of separate cards under several parent mezzos.
- Some three-week-role blocks should be reduced back to two if card drafting shows that the middle role adds language rather than a different week structure.

Missing-piece watchouts:

- Trail and mountain specificity is represented inside week descriptions, but named-philosophy review may reveal special week structures for downhill tolerance, hiking economy, muscular endurance, heat/altitude, or technical confidence.
- The micro-to-session layer will need clearer session-role taxonomy before session cards are built.
- If the app needs reusable week-type explanations independent of cards, this section may later become active type metadata.

Next micro step: review named philosophies against these mainstream micro types. The review should follow the same pattern as macro-to-mezzo: inherited mainstream mezzo, philosophy-specific equivalent mezzo, philosophy-specific new mezzo, then special philosophy-specific additions.

### Micro Philosophy Review

This section reviews whether named philosophies need their own micro cards. The review uses the same structure as macro-to-mezzo, but with a stricter threshold because micro cards are week-level objects and can multiply quickly.

Default rule:

- If a named philosophy inherits a mainstream mezzo, reuse the mainstream micro cards under that mezzo unless the philosophy changes the week structure itself.
- If a named philosophy reuses a mainstream mezzo under a philosophy-specific macro, reuse the mainstream micro cards under that mezzo unless the philosophy changes the week structure itself.
- If a named philosophy has a philosophy-specific mezzo, review that mezzo directly and create only the micro cards whose weekly structure is meaningfully distinct.
- If a distinction is mostly workout execution, intensity target, exact terrain choice, wording, motivation, or reminder language, defer it to session cards or app guidance.

Expected app/storage implication: if named-philosophy macro-to-mezzo reuse is handled by `macro_mezzo_reuse.json`, then named-philosophy mezzo-to-micro reuse should later be handled by a matching `mezzo_micro_reuse.json` file rather than duplicate micro card content.

#### 80/20 Endurance Micro Review

Coach decision: create 80/20-specific micro cards where weekly intensity distribution, hard/easy contrast, race-counted load, moderate-work containment, or easy-discipline maintenance changes the week structure. Reuse mainstream micro cards where the week structure is ordinary and only the language changes.

| Parent mezzo | Decision | Accepted 80/20 micro types | Coach rationale |
| --- | --- | --- | --- |
| Inherited/reused mainstream mezzos | `inherit_or_reuse_mainstream` | Use mapped mainstream micro children later | If the parent mezzo is already mainstream, its week structures stay mainstream unless intensity accounting changes the week itself. |
| 80/20 Low-Intensity Volume Block | `specific_version` | Low-Intensity Baseline Week; Low-Intensity Volume Build Week; Low-Intensity Absorption Week | Base-volume weeks are distinct because easy discipline and low-intensity majority are not optional details; they shape the whole week. |
| 80/20 Long Endurance Distribution Block | `specific_version` | Long-Endurance Distribution Week; Long-Endurance Absorption Week | Long trail duration, climbing, descents, and hiking can behave like hard work, so the week must count hidden intensity and muscular cost. A separate hidden-cost check week was rejected because those checks belong inside both accepted weeks rather than forming a different weekly structure. |
| 80/20 Planned Moderate Work Block | `specific_version` | Planned Moderate Introduction Week; Planned Moderate Development Week; Moderate Spillover Control Week | Moderate work is allowed only when deliberate and contained; the week structure must prevent grey-zone spread. |
| 80/20 High-Intensity Quality Block | `specific_version` | High-Intensity Quality Week; Hard-Easy Protection Week; High-Intensity Absorption Week | Hard work needs enough low-intensity support and recovery spacing that the weekly distribution still works. |
| 80/20 Hill Strength Quality Block | `specific_version` | Hill-Strength Introduction Week; Hill-Strength Quality Week; Hill-Strength Recovery-Accounting Week | Hill strength is not automatically easy; the week must count muscular load and downhill cost as real stress. |
| 80/20 Distribution-Safe Course Demands Block | `specific_version` | Distribution-Safe Course Exposure Week | Course specificity can easily become chronic moderate work, so the week needs explicit distribution guardrails. A separate audit week was rejected because auditing is app/detail guidance unless it changes the training week. |
| 80/20 Race-Counted Recovery Block | `specific_version` | Race-Counted Reset Week | Races are counted as hard inputs before new training stress is added. A separate accounting week was rejected because the accounting should shape the reset week and the next-build decision. |
| 80/20 Race-Season Distribution Maintenance Block | `specific_version` | Race-Season Easy-Volume Week; Sparse Quality Touch Week | The week maintains fitness by protecting easy volume and limiting quality between races. |
| 80/20 Easy Discipline Maintenance Block | `specific_version` | Easy-Discipline Maintenance Week; Moderate-Drift Correction Week | Maintenance changes when the main risk is letting constrained training become too hard too often. |
| 80/20 Quality Touchpoint Maintenance Block | `specific_version` | Quality-Touchpoint Protection Week | The small quality touch needs enough easy support that it does not become a hidden build week. A separate absorption week was rejected because the recovery logic belongs inside the protection week at maintenance level. |
| Additional 80/20 special micro types | `no_special_addition` | None | The specific mezzo set already covers the week-level 80/20 distinctions. Calibration reminders and exact zone execution mostly belong in session cards or app guidance. |

80/20 candidate count after final reduction: 21 philosophy-specific micro types.

#### Lydiard Micro Review

Coach decision: create Lydiard-specific micro cards where base-first sequencing, response-regulated effort, hill resistance, capacity integration, or final sequence expression changes the week structure. Do not create Lydiard micro cards merely because the week includes aerobic running or hills.

| Parent mezzo | Decision | Accepted Lydiard micro types | Coach rationale |
| --- | --- | --- | --- |
| Inherited/reused mainstream mezzos | `inherit_or_reuse_mainstream` | Use mapped mainstream micro children later | Mainstream weeks remain adequate for shared return, competition, recovery, off-season, maintenance, strength support, trail familiarity, fueling, and readiness roles. |
| Lydiard Response-Regulated Reduced-Load Block | `specific_version` | Response-Regulated Absorption Week | Recovery is governed by athlete response, not a fixed calendar. A separate readiness-check week was rejected because readiness checking belongs inside the absorption week unless training structure changes. |
| Lydiard Sustainable Aerobic Conditioning Block | `specific_version` | Sustainable Aerobic Establishment Week; Aerobic Load Build Week; Aerobic Response Hold Week | The week structure is distinct because the base is built around the greatest aerobic work the athlete can consistently absorb. |
| Lydiard Long Aerobic Conditioning Block | `specific_version` | Long Aerobic Extension Week; Long Aerobic Support Week; Long Aerobic Consolidation Week | The long run belongs inside a base-first sequence and should not become detached heroics. |
| Lydiard Hill Resistance Development Block | `specific_version` | Hill Resistance Introduction Week; Hill Resistance Development Week; Hill Resistance Coordination Week | Hill work bridges base toward later faster work through resistance, mechanics, and coordination. |
| Lydiard Hill Transition Absorption Block | `specific_version` | Hill Transition Absorption Week | The week checks whether the athlete has absorbed hill resistance before moving forward. A separate post-hill readiness week was rejected because it duplicates the absorption-week purpose. |
| Lydiard Capacity Integration Block | `specific_version` | Capacity Integration Week; Race-Preparation Coordination Week | The week coordinates already built capacities rather than inventing fitness late. |
| Lydiard Sequence Expression Taper Block | `specific_version` | Sequence Expression Sharpening Week; Lydiard Freshness Protection Week | The taper expresses completed preparation and protects freshness rather than forcing missing work. |
| Additional Lydiard special micro types | `no_special_addition` | None | The accepted Lydiard mezzo set already contains the meaningful week-level distinctions. |

Lydiard candidate count after final reduction: 15 philosophy-specific micro types.

#### CTS Micro Review

Coach decision: create CTS-specific micro cards where event demands, limiter focus, long-range workload cost, ultra durability, rehearsal strategy, or between-event adjustment changes the week structure. Do not create CTS cards for generic hard weeks or generic ultra language.

| Parent mezzo | Decision | Accepted CTS micro types | Coach rationale |
| --- | --- | --- | --- |
| Inherited/reused mainstream mezzos | `inherit_or_reuse_mainstream` | Use mapped mainstream micro children later | Shared return, taper, recovery, off-season, maintenance, strength support, and trail-familiarity weeks do not need CTS duplicates. |
| CTS Repeatable Workload Foundation Block | `specific_version` | Repeatable Workload Baseline Week; Workload Extension Week; Workload Cost Check Week | CTS changes the week by treating workload as useful only when repeatable and recoverable. |
| CTS Long-Run Durability Block | `specific_version` | Long-Run Durability Build Week; Terrain-Durability Week; Durability Absorption Week | Long-run work is judged by durability for the real event, not by duration alone. |
| CTS Limiter-Focused Quality Block | `specific_version` | Limiter-Focused Quality Week; Limiter Response Week | The week is built around the chosen performance limiter and the trade-off it creates. A separate limiter-selection week was rejected because selecting the limiter is block planning unless it changes the training week. |
| CTS Ultra Strength-Endurance Limiter Block | `specific_version` | Ultra Strength-Endurance Introduction Week; Ultra Strength-Endurance Development Week; Muscular-Cost Absorption Week | Strength endurance is justified only when it solves an actual ultra limiter. |
| CTS Event Demands Block | `specific_version` | Event-Demands Exposure Week; Event-Demands Integration Week | The week starts from what the event will require, then exposes and integrates only meaningful demands. A separate analysis week was rejected because analysis is preparation/app guidance unless paired with a real training structure. |
| CTS Race Execution Rehearsal Block | `specific_version` | Race-Execution Planning Week; Race-Execution Rehearsal Week; Execution Adjustment Week | Rehearsal is tied to pacing, terrain decisions, gear, aid, and problem solving. |
| CTS Fueling And Hydration Strategy Block | `specific_version` | Fueling Strategy Integration Week; Fueling Strategy Rehearsal Week; Fueling Problem-Solving Week | Nutrition work becomes planned strategy, not generic advice. |
| CTS Race Stress Recovery Block | `specific_version` | Race-Stress Recovery Week | Each race is treated as a specific stress with its own recovery profile. A separate assessment week was rejected because assessment should shape the recovery week rather than stand alone. |
| CTS Between-Event Adjustment Block | `specific_version` | Between-Event Decision Week; Between-Event Targeted Adjustment Week | The week is shaped by the next event, athlete readiness, and what the last race revealed. |
| Additional CTS special micro types | `no_special_addition` | None | The accepted CTS mezzo set already covers the week-level distinctions. |

CTS candidate count after final reduction: 22 philosophy-specific micro types.

#### Evoke Endurance Micro Review

Coach decision: create Evoke-specific micro cards where aerobic capacity, aerobic threshold control, strength reserve, muscular endurance, layer absorption, or objective utilisation changes the week structure. Do not create Evoke cards for ordinary hill or trail weeks.

| Parent mezzo | Decision | Accepted Evoke micro types | Coach rationale |
| --- | --- | --- | --- |
| Inherited/reused mainstream mezzos | `inherit_or_reuse_mainstream` | Use mapped mainstream micro children later | Shared return, taper, competition, recovery, off-season, maintenance, trail familiarity, and fueling roles can reuse mainstream weeks. |
| Evoke Layer Absorption Recovery Block | `specific_version` | Layer Absorption Week | Recovery is specific to absorbing prior mountain, strength, or muscular-endurance layers. A separate readiness-check week was rejected because readiness should be assessed inside the absorption week. |
| Evoke Aerobic Capacity Development Block | `specific_version` | Aerobic Capacity Baseline Week; Aerobic Capacity Build Week; Aerobic Capacity Absorption Week | Aerobic capacity is the base layer that supports later mountain work. |
| Evoke Strength Reserve Support Block | `specific_version` | Strength Reserve Development Week; Strength Reserve Integration Week; Strength Reserve Deload Week | Strength reserve supports later muscular endurance and must be placed without disrupting aerobic development. |
| Evoke Aerobic Threshold Control Block | `specific_version` | Aerobic Threshold Calibration Week; Aerobic Threshold Development Week; Aerobic Threshold Drift Check Week | Intensity control changes the week because the goal is preserving the correct aerobic range. |
| Evoke Uphill Muscular Endurance Block | `specific_version` | Uphill Muscular-Endurance Introduction Week; Uphill Muscular-Endurance Development Week; Uphill Muscular-Endurance Recovery Week | This is a defining Evoke week structure and must respect prerequisites and muscular cost. |
| Evoke Muscular Endurance Absorption Block | `specific_version` | Muscular-Endurance Absorption Week | The week lets the prior ME dose become usable capacity rather than stacking stress. A separate transfer-check week was rejected because transfer signs belong inside absorption and later objective-utilisation weeks. |
| Evoke Objective Utilisation Block | `specific_version` | Objective Utilisation Integration Week; Objective Simulation Week; Objective Readiness Week | Race/objective preparation uses developed capacity rather than creating capacity late. |
| Additional Evoke special micro types | `no_special_addition` | None | The accepted Evoke mezzo set already captures the distinct weekly layer logic. |

Evoke candidate count after final reduction: 17 philosophy-specific micro types.

#### SWAP Micro Review

Coach decision: create SWAP-specific micro cards where health, joy, confidence, athlete agency, speed/economy as skill, fatigue-resistance curiosity, or whole-athlete sustainability changes the week structure. Do not create SWAP cards only for warmer language.

| Parent mezzo | Decision | Accepted SWAP micro types | Coach rationale |
| --- | --- | --- | --- |
| Inherited/reused mainstream mezzos | `inherit_or_reuse_mainstream` | Use mapped mainstream micro children later | Shared taper, reduced-load, maintenance, strength support, trail familiarity, and fueling roles can reuse mainstream micro cards unless SWAP changes the week structure. |
| SWAP Supported Recovery Reset Block | `specific_version` | Supported Recovery Reset Week | Recovery includes health, agency, and emotional readiness rather than only physical load reduction. A separate agency-return check week was rejected because it is a coaching checkpoint inside the reset week. |
| SWAP Confidence Re-Entry Block | `specific_version` | Confidence Anchor Week; Confidence Extension Week | Re-entry is distinct when the week is built to remove shame and restore trust. |
| SWAP Sustainable Aerobic Rhythm Block | `specific_version` | Sustainable Aerobic Rhythm Week; Health-Protected Aerobic Build Week | Base rhythm is shaped by health, consistency, and positive response. A separate joy-check week was rejected because joy is a required review lens inside both accepted weeks, not a separate week structure. |
| SWAP Adventure Endurance Block | `specific_version` | Adventure Endurance Exposure Week; Adventure Endurance Confidence Week; Adventure Recovery Week | Adventure is used as purposeful endurance and confidence development, not random overload. |
| SWAP Economy Speed Skill Support Block | `specific_version` | Economy Skill Touch Week; Speed-Skill Support Week | Speed/economy touchpoints can support base without hijacking aerobic work. |
| SWAP Speed Economy Development Block | `specific_version` | Speed Economy Introduction Week; Speed Economy Development Week; Speed Economy Absorption Week | Speed and economy become sustainable skills rather than punishment or maximal strain. |
| SWAP Fatigue Resistance Development Block | `specific_version` | Fatigue-Resistance Development Week; Fatigue-Resistance Response Week | The week tests a coaching question about durability without chasing exhaustion. A separate question week was rejected because the coaching question should be set at block planning level. |
| SWAP Confidence-Building Course Demands Block | `specific_version` | Confidence Course Exposure Week; Confidence Course Integration Week; Confidence Course Simulation Week | Course specificity is shaped by confidence and agency, not only demands. |
| SWAP Agency Race Execution Practice Block | `specific_version` | Agency Execution Choice Week; Agency Rehearsal Week; Agency Feedback Week | Race execution practice helps the athlete make decisions, not just follow logistics. |
| SWAP Whole-Athlete Between-Race Recovery Block | `specific_version` | Whole-Athlete Recovery Week | Between-race recovery weighs health, identity, excitement, and long-term consistency. A separate excitement-check week was rejected because it is a readiness lens inside the recovery week. |
| SWAP Race-Season Health And Joy Block | `specific_version` | Race-Season Health Week; Race-Season Joy Touch Week; Race-Season Sustainability Week | Race-season structure protects health and joy across repeated competitions. |
| SWAP Off-Season Identity And Play Block | `specific_version` | Off-Season Play Week; Playful Rhythm Week | Off-season is distinct when it restores identity and playful movement without hidden pressure. A separate identity-reconnect week was rejected because the identity lens should shape both accepted off-season weeks. |
| Additional SWAP special micro types | `no_special_addition` | None | The accepted SWAP mezzo set already contains the meaningful special week structures. |

SWAP candidate count after final reduction: 27 philosophy-specific micro types.

#### Sharman Ultra Micro Review

Coach decision: create Sharman Ultra-specific micro cards where practical ultra execution, course reality, athlete-specific constraints, fueling/gear/logistics, between-race recovery, or adaptive feedback changes the week structure. Stay conservative because the source base supports coaching stance and practical reasoning more than exact proprietary workout formulas.

| Parent mezzo | Decision | Accepted Sharman Ultra micro types | Coach rationale |
| --- | --- | --- | --- |
| Inherited/reused mainstream mezzos | `inherit_or_reuse_mainstream` | Use mapped mainstream micro children later | Shared return, base, capacity, taper, recovery, off-season, maintenance, and race-season maintenance weeks can reuse mainstream structures. |
| Sharman Course Reality Preparation Block | `specific_version` | Course Reality Exposure Week; Course Reality Integration Week | The week adapts course demands to the athlete's real terrain access, life constraints, and readiness. A separate constraint week was rejected because constraints should modify exposure and integration rather than create a distinct week. |
| Sharman Practical Ultra Execution Block | `specific_version` | Practical Ultra Execution Week; Ultra Problem-Solving Rehearsal Week; Sustainable Pacing Practice Week | Ultra execution is practical and decision-oriented, not only fitness expression. |
| Sharman Fueling Gear Logistics Block | `specific_version` | Fueling-Gear Integration Week; Logistics Rehearsal Week | Fueling, gear, and logistics become weekly practice targets before race day. A separate gear problem-solving week was rejected because troubleshooting belongs inside rehearsal unless it changes the week structure. |
| Sharman Context-Aware Between-Race Recovery Block | `specific_version` | Context-Aware Recovery Week; Next-Race Readiness Week | Between-race recovery is shaped by event cost, athlete life, and the next race. |
| Sharman Adaptive Race Feedback Block | `specific_version` | Adaptive Race Feedback Week; Practical Adjustment Week | Race feedback becomes a specific, practical next-step adjustment. |
| Additional Sharman Ultra special micro types | `no_special_addition` | None | The accepted Sharman Ultra mezzo set already covers the useful public-source distinctions. |

Sharman Ultra candidate count after final reduction: 11 philosophy-specific micro types.

### Micro Philosophy Coverage Sanity Review

| Philosophy profile | Specific micro candidates | Mainstream reuse expected | Coach verdict |
| --- | ---: | ---: | --- |
| `80_20_endurance` | 21 | High | Accept. The count is justified because 80/20 distinctions often operate at weekly distribution and recovery-spacing level. Audit-only candidates were folded into stronger week cards. |
| `lydiard` | 15 | High | Accept. The distinct weeks are concentrated around sequence, aerobic base, hill resistance, integration, and taper expression. Readiness-only candidates were folded into absorption weeks. |
| `cts` | 22 | Medium-high | Accept. CTS has many specific week decisions because limiter focus, event demands, fueling strategy, and between-event adjustment are operational at micro level. Planning-only candidates were removed. |
| `evoke_endurance` | 17 | Medium-high | Accept. The weeks are concentrated around layer order, threshold control, strength reserve, muscular endurance, and objective utilisation. Check-only candidates were folded into absorption/utilisation cards. |
| `swap` | 27 | Medium | Accept with strict drafting review. SWAP legitimately changes many weekly decisions through health, joy, agency, confidence, and speed/economy skill, but values-only candidates were folded into stronger week cards. |
| `sharman_ultra` | 11 | High | Accept. Keep conservative because public source support is strongest for practical ultra execution and athlete-specific adjustment. Constraint/troubleshooting-only candidates were folded into practical weeks. |

Total accepted named-philosophy micro candidates after final reduction: 113.

Reduction review:

- Keep the reduced candidate set because it follows the existing 50 named-philosophy mezzo cards rather than inventing unrelated weekly types.
- Remove or fold candidates that were mostly check, audit, debrief, readiness, constraint, or planning labels without a distinct training-week structure.
- During card drafting, merge or delete any candidate whose final content differs only by tone, reminder language, or exact session execution.
- Watch SWAP and CTS most closely because they still have the highest counts and the greatest risk of values becoming duplicate card language instead of distinct week structure.
- Do not build `mezzo_micro_reuse.json` until philosophy-specific micro cards exist; otherwise the mapping would point into an unstable target set.
- Reused mainstream micro cards should stay mainstream card content and be surfaced by metadata, not copied into philosophy-specific folders.

### Built Named-Philosophy Micro Card Set

The 113 accepted named-philosophy micro candidates have been created and published as Drive/cache JSON cards.

Build status:

- `80_20_endurance`: 21 micro cards, `micro_065` through `micro_085`
- `lydiard`: 15 micro cards, `micro_086` through `micro_100`
- `cts`: 22 micro cards, `micro_101` through `micro_122`
- `evoke_endurance`: 17 micro cards, `micro_123` through `micro_139`
- `swap`: 27 micro cards, `micro_140` through `micro_166`
- `sharman_ultra`: 11 micro cards, `micro_167` through `micro_177`
- Exported cache count after build: 288 total cards, including 177 micro cards

## Session Level

Session cards define reusable workout concepts inside micro weeks. They answer: what workout should the athlete do today, what stimulus should it create, how should the work be executed, what terrain or pacing details matter, and how should the coach scale the session when readiness or context changes?

Session cards should be specific enough to guide a real workout, but not so narrow that every small prescription variant becomes a separate card. At session level, the coach must make one extra decision before creating a card: is this a genuinely different workout concept, or is it a workout option inside an existing session card?

### Session Card Authoring Shape

Use the current session structure:

```text
SessionCard
  workout_blocks[]
    WorkoutBlock
      block_type
      execution_mode
      options[]
        WorkoutOption
          repeat
          parts[]
            SessionPart
```

`WorkoutBlock` describes the section of the workout:

- `block_type`: `warmup`, `main`, `recovery`, `cooldown`, `optional_addon`, or `notes`
- `execution_mode`: `do_all`, `choose_one`, or `optional`

`WorkoutOption` describes one complete required, optional, or selectable prescription inside a block:

- `title`
- `repeat`, used mechanically when the option's parts repeat as rounds or sets
- `selection_notes`, used when a coach needs to know when to choose this option
- `load_notes`, used when the option's stress cost needs clarification

`SessionPart` describes the concrete work inside an option:

- `title`
- `prescription`
- `duration`
- `rpe`
- `selection_notes`
- `coaching_notes`
- `terrain_notes`
- `adjustment_notes`

### Card Versus Option Standard

A separate session card is justified when the workout concept changes enough to affect how the app chooses, explains, structures, filters, or sequences the session. A workout option belongs inside an existing session card when it is a true prescription variant of the same coaching concept.

Use coaching common sense rather than a mechanical rule. Small changes in repetition count, duration, or recovery usually belong as `WorkoutOption`s. Changes in terrain, execution style, risk profile, athlete readiness requirement, or intended adaptation may justify a separate session card.

Examples:

- `Aerobic Power Intervals` can be one session card.
- `4 x 4`, `5 x 3`, and `6 x 2` can be `WorkoutOption`s inside that card when they are all controlled aerobic-power interval prescriptions.
- `Uphill Aerobic Power Intervals` may be a separate session card if terrain, mechanics, pacing control, or recovery cost changes the coaching decision.
- `Aerobic Power Fartlek` may be a separate session card because continuous/variable execution changes how the athlete controls effort compared with structured intervals.
- `Technical Downhill Conditioning` should be a separate session card because the adaptation, terrain demand, mechanical risk, and readiness requirement differ from ordinary aerobic or interval work.

### Mechanical Repeat Example

Use `repeat` only when the option's parts mechanically repeat. A simple continuous easy run usually has no repeat value.

```text
WorkoutBlock: Main
execution_mode: do_all

WorkoutOption: 4 x 4 Min Hard / 3 Min Easy
repeat: 4 rounds

SessionPart:
- Hard Repetition: 4 min, RPE 8-9
- Easy Recovery: 3 min, RPE 1-3
```

Rendered meaning:

```text
Main Set
Do all

4 x 4 Min Hard / 3 Min Easy
Repeat 4 rounds:
- Hard Repetition: 4 min | RPE 8-9
- Easy Recovery: 3 min | RPE 1-3
```

### Coach-Led Mainstream Session Type Work

For each accepted mainstream micro card, the coach should define the session types that usually belong underneath it. The coach should decide:

- whether the proposed session is a real workout concept
- whether it belongs at session level rather than micro, mezzo, or app guidance level
- whether similar prescriptions should become options inside the card
- whether terrain or execution changes are large enough to justify a separate card
- which workout blocks, options, repeats, and parts the card likely needs
- whether `mainstream_endurance` should get a card for this session type
- which named philosophies may need a distinct version later

Do not create session card files until the mainstream session type set and option grouping have been reviewed.

### Coach-Derived Mainstream Session Type Catalog

This is the first accepted mainstream session-type catalog for the `micro -> session` layer. The purpose is not to invent every possible workout, but to define reusable session concepts that can sit under many mainstream micro weeks. Exact prescriptions belong inside a session card as `WorkoutOption`s when they are variants of the same coaching concept.

Coach verdict after reduction: keep the catalog compact and reusable. The session layer should cover the actual daily training choices implied by the mainstream micro cards, while resisting separate cards for every small duration, repetition-count, or route variant.

Before building session cards, review whether the current `SessionFamily` registry needs two support families: one for strength/mobility sessions and one for low-impact aerobic alternatives. The session concepts are accepted here, but the final family labels may need a small registry update before implementation.

| Session type ID | Session type name | Likely family | Coach verdict | Why this is a real session concept | Option grouping guidance |
| --- | --- | --- | --- | --- | --- |
| `session_type_rest_day` | Rest Day | Recovery | Keep | Rest is an intentional daily prescription when recovery, taper, race aftermath, or constraints make non-training the correct training choice. | Options may distinguish full rest, sleep-focused rest, travel-day rest, or logistics-supported rest. |
| `session_type_walk_or_gentle_movement` | Walk Or Gentle Movement | Recovery | Keep | Gentle movement can support recovery, re-entry, or post-race transition without becoming a run. | Options may include walk, gentle hike, or very light spin if the stimulus remains recovery. |
| `session_type_mobility_reset` | Mobility Reset | Strength/mobility support | Keep | Mobility and tissue-care work is a real session when the day's purpose is movement quality or recovery support. | Options may include mobility flow, light activation, or tissue-care routine; do not split by exercise list unless the app later needs exercise-level programming. |
| `session_type_light_activation_strength` | Light Activation Strength | Strength/mobility support | Keep | Low-dose strength can prepare or preserve movement without creating a main strength stress. | Options may include activation circuit, light general strength, or pre-run movement prep. |
| `session_type_general_strength_session` | General Strength Session | Strength/mobility support | Keep | General strength is a distinct workout when it is the day's primary non-running support stress. | Options may cover introductory, standard, and reduced-load versions; exact exercises can stay inside parts. |
| `session_type_strength_support_session` | Strength Support Session | Strength/mobility support | Keep | Running-support strength differs from general gym work because it must be placed around key running and soreness cost. | Options may distinguish durability circuit, single-leg control, or low-eccentric support. |
| `session_type_run_walk_reentry` | Run-Walk Re-Entry | Easy | Keep | Run-walk is distinct from continuous easy running when the athlete is rebuilding tolerance or confidence. | Options may include short run-walk ratios and progression steps; keep them inside one card. |
| `session_type_short_easy_run` | Short Easy Run | Easy | Keep | A short easy run is a useful low-cost session for re-entry, taper, maintenance, and constrained weeks. | Options may vary 15-20, 20-30, or 30-40 minutes. |
| `session_type_easy_aerobic_run` | Easy Aerobic Run | Easy | Keep | This is the core low-intensity running session used across most phases. | Options may vary by duration, terrain simplicity, or route familiarity while preserving easy effort. |
| `session_type_recovery_run` | Recovery Run | Recovery | Keep | Recovery running is intentionally easier and lower-cost than ordinary easy aerobic running. | Options may include very short jog, easy shuffle, or recovery run-walk. |
| `session_type_aerobic_support_run` | Aerobic Support Run | Easy | Keep | Support runs maintain aerobic rhythm around key work without becoming the focal stress. | Options may vary by short, normal, and extended support dose. |
| `session_type_long_easy_run` | Long Easy Run | Endurance | Keep | Long easy running is a major endurance session with its own recovery and fueling implications. | Options may distinguish introductory, standard, and extended versions by duration/time-on-feet. |
| `session_type_time_on_feet_outing` | Time-On-Feet Outing | Endurance | Keep | Time-on-feet is distinct when duration, hiking, terrain, or fatigue tolerance matters more than running pace. | Options may include easy run-hike, hilly time-on-feet, or low-intensity long trail outing. |
| `session_type_goal_terrain_endurance_run` | Goal-Terrain Endurance Run | Endurance | Keep | Goal terrain changes the session when vertical, surface, hiking, descent, or route cost matters. | Options may distinguish climb-focused, rolling trail, technical-surface, or descent-light versions. |
| `session_type_low_impact_aerobic_alternative` | Low-Impact Aerobic Alternative | Low-impact aerobic support | Keep | Cross-training or low-impact aerobic work is a real session when it replaces or supports running load. | Options may include bike, elliptical, swim, ski, or hike if intensity and recovery cost match. |
| `session_type_movement_variety_session` | Movement Variety Session | Low-impact aerobic support | Keep | Off-season or recovery variety is useful when the goal is freshness, general athleticism, or lower emotional pressure. | Options may include hike, cycling, skiing, easy gym circuit, or playful aerobic movement. |
| `session_type_trail_familiarity_run` | Trail Familiarity Run | Trail Specific Skills | Keep | Controlled trail exposure teaches footing, rhythm, and confidence without making the session race-specific. | Options may vary by surface, mild grade, or technicality. |
| `session_type_trail_skill_drills` | Trail Skill Drills | Trail Specific Skills | Keep | Drills, strides, and focused terrain practice are distinct when skill rather than fitness is the main stimulus. | Options may include uphill cadence, foot-placement practice, relaxed trail strides, or balance-focused terrain. |
| `session_type_power_hike_practice` | Power-Hike Practice | Trail Specific Skills | Keep | Power hiking is a distinct mountain-running skill and load pattern, especially for trail and ultra goals. | Options may include short steep hiking repeats, sustained hike intervals, or hike-run transitions. |
| `session_type_downhill_skill_conditioning` | Downhill Skill Conditioning | Trail Specific Skills | Keep | Downhill work has distinct mechanical risk, coordination demand, and recovery cost. | Keep separate from ordinary trail running; options may cover technical skill, controlled descent repeats, or low-cost downhill exposure. |
| `session_type_steady_aerobic_run` | Steady Aerobic Run | Steady | Keep | Steady running is stronger than easy but below threshold, useful when a controlled aerobic stimulus is needed. | Options may include short steady finish, continuous steady run, or steady segments. |
| `session_type_controlled_threshold_session` | Controlled Threshold Session | Threshold | Keep | Threshold work is a distinct sustainable hard session that teaches restraint and pacing discipline. | Options may include continuous tempo, cruise intervals, or progression tempo when they share threshold intent. |
| `session_type_short_threshold_touch` | Short Threshold Touch | Threshold | Keep | A small threshold dose is different from a development threshold workout because the goal is touchpoint, not build. | Options may include short cruise intervals, short tempo insert, or uphill threshold touch. |
| `session_type_aerobic_power_intervals` | Aerobic Power Intervals | Aerobic Power | Keep | Aerobic-power intervals create high-end aerobic stress that needs deliberate spacing and control. | `4 x 4`, `5 x 3`, `6 x 2`, and similar structured intervals can be options inside this card. |
| `session_type_aerobic_power_touch` | Aerobic Power Touch | Aerobic Power | Keep | A small aerobic-power touch maintains or introduces intensity without becoming a full stimulus workout. | Options may include short hard repeats, reduced repetition count, or brief hill equivalent. |
| `session_type_aerobic_power_fartlek` | Aerobic Power Fartlek | Aerobic Power | Keep separate | Fartlek execution changes pacing control, continuity, and athlete perception enough to justify a separate card from structured intervals. | Options may include 10 x 1 min, 8 x 90 sec, or variable short-hard/easy patterns. |
| `session_type_intro_uphill_endurance_repeats` | Intro Uphill Endurance Repeats | Strength Endurance | Keep | Shorter uphill endurance work introduces force and grade without a full muscular-endurance load. | Options may vary duration, grade, and recovery conservatively. |
| `session_type_strength_endurance_climb_session` | Strength-Endurance Climb Session | Strength Endurance | Keep | Sustained uphill or resistance work creates a distinct muscular-endurance stimulus and recovery cost. | Options may include sustained climb intervals, hike-run climbs, or treadmill/stair alternatives when the same stress is preserved. |
| `session_type_hill_strength_circuit` | Hill Strength Circuit | Strength Endurance | Keep | Circuit structure is needed when several hill-force parts repeat as rounds. | Options may include intro and advanced circuits; `repeat` should describe rounds mechanically. |
| `session_type_short_hill_power` | Short Hill Power | Hill Power | Keep | Short hill power is neuromuscular and mechanical, not a long grinding hill session. | Options may include short hill sprints, relaxed uphill strides, or low-volume power touches. |
| `session_type_neuromuscular_strides` | Neuromuscular Strides | Neuromuscular | Keep | Strides preserve rhythm, coordination, and leg speed at low cost when kept relaxed. | Options may vary number, duration, flat/upright terrain, or gentle uphill. |
| `session_type_sharpening_touch` | Sharpening Touch | Controlled Quality | Keep | Sharpening before racing is a small familiar quality signal rather than a development workout. | Options may include short strides, short controlled intervals, or race-pace feel depending on event. |
| `session_type_pre_race_shakeout` | Pre-Race Shakeout | Easy | Keep | A shakeout is a very short, confidence-preserving session close to racing. | Options may include easy shakeout only or easy shakeout plus a few relaxed strides. |
| `session_type_gear_fueling_check` | Gear And Fueling Check | Race Practice | Keep | Gear and fueling checks are trainable execution tasks when paired with movement or low-cost rehearsal. | Options may include shoe/pack check, bottle/gel timing, poles, lights, or weather kit check. |
| `session_type_fueling_habit_run` | Fueling Habit Run | Race Practice | Keep | Fueling practice can be low-key habit formation before it becomes tolerance testing. | Options may include easy run with planned intake or hydration timing. |
| `session_type_long_run_fueling_practice` | Long-Run Fueling Practice | Race Practice | Keep | Fueling under longer duration is a distinct session because gut tolerance, logistics, and effort interact. | Options may vary intake timing, product practice, heat/hydration emphasis, or event-specific format. |
| `session_type_controlled_fueling_test` | Controlled Fueling Test | Race Practice | Keep | A controlled fueling test isolates nutrition tolerance more than fitness progression. | Options may include simple product test, timing test, or hydration/electrolyte check. |
| `session_type_race_execution_cue_run` | Race Execution Cue Run | Race Practice | Keep | Pacing, gear, hiking transitions, and decision cues can be practiced at low cost. | Options may include pacing cue run, hiking-transition practice, aid-flow rehearsal, or mental checkpoint practice. |
| `session_type_race_rehearsal_session` | Race Rehearsal Session | Race Practice | Keep | Rehearsal combines several race demands in a controlled session without becoming a race. | Options may include short rehearsal, long rehearsal, terrain rehearsal, or gear/fueling rehearsal. |
| `session_type_course_demands_exposure_run` | Course-Demands Exposure Run | Race Practice | Keep | Course demand exposure prepares the athlete for a specific requirement without full simulation. | Options may focus on climb, descent, technical surface, heat, altitude, or duration. |
| `session_type_course_demands_simulation_outing` | Course-Demands Simulation Outing | Race Practice | Keep | Simulation combines multiple demands at higher cost and needs different placement than exposure. | Options may vary simulation size and demand combination. |
| `session_type_easy_run_with_response_check` | Easy Run With Response Check | Easy | Keep | Response-check runs use simple movement to assess readiness without adding a hard test. | Options may include easy run with soreness check, stairs/downhill check, or perceived-effort check. |
| `session_type_transition_preview_session` | Transition Preview Session | Controlled Quality | Keep | A small preview of the next emphasis helps bridge blocks without jumping to full demand. | Options depend on the next block: small threshold touch, short hill touch, short terrain exposure, or easy endurance preview. |
| `session_type_targeted_lesson_practice` | Targeted Lesson Practice | Race Practice | Keep | Race lessons become useful when one clear behavior is practiced, not when every lesson becomes a new plan. | Options may include pacing correction, gear fix, fueling timing, hiking transition, or descent-control practice. |
| `session_type_race_debrief_easy_run` | Race Debrief Easy Run | Recovery | Keep | Easy movement after competition can pair recovery with practical reflection. | Options may include easy recovery run, walk-and-reflect, or one low-cost lesson cue. |
| `session_type_constraint_priority_session` | Constraint Priority Session | Easy | Keep | Constraints require choosing the highest-value short session rather than forcing a normal template. | Options may include short easy run, minimum aerobic dose, or short support session. |

### Mainstream Session Type Coverage By Micro Week

This table defines the baseline session concepts that can sit under each mainstream micro card. It is not a fixed weekly schedule. It tells the later card build which session cards should exist and which session types each micro week can point to as children.

| Micro card | Baseline session types under this week | Coach notes on options and grouping |
| --- | --- | --- |
| `micro_001` Routine Anchor Week | `session_type_run_walk_reentry`; `session_type_walk_or_gentle_movement`; `session_type_rest_day` | Keep prescriptions short and confidence-building. Run-walk ratios are options, not separate cards. |
| `micro_002` Frequency Extension Week | `session_type_short_easy_run`; `session_type_run_walk_reentry`; `session_type_rest_day` | The extra exposure is an option inside the short/easy concept, not a new session type. |
| `micro_003` Easy Aerobic Reconditioning Week | `session_type_easy_aerobic_run`; `session_type_low_impact_aerobic_alternative`; `session_type_recovery_run` | Low-impact alternatives may need their own family before building. |
| `micro_004` Aerobic Reconditioning Hold Week | `session_type_easy_aerobic_run`; `session_type_low_impact_aerobic_alternative`; `session_type_rest_day` | The hold decision belongs to the micro card; the session stays ordinary and repeatable. |
| `micro_005` Strength Reintroduction Week | `session_type_light_activation_strength`; `session_type_easy_aerobic_run`; `session_type_mobility_reset` | Exercise details should be parts/options inside the support session, not separate cards. |
| `micro_006` Movement Tolerance Check Week | `session_type_light_activation_strength`; `session_type_easy_run_with_response_check`; `session_type_mobility_reset` | Response checking belongs in notes/options; avoid a separate check-only workout card unless movement changes. |
| `micro_007` Aerobic Volume Baseline Week | `session_type_easy_aerobic_run`; `session_type_long_easy_run`; `session_type_recovery_run` | Long-run duration options stay inside long easy run. |
| `micro_008` Aerobic Volume Build Week | `session_type_easy_aerobic_run`; `session_type_long_easy_run`; `session_type_recovery_run` | Progression is mostly duration/frequency options, not new card types. |
| `micro_009` Aerobic Volume Absorption Week | `session_type_short_easy_run`; `session_type_easy_aerobic_run`; `session_type_low_impact_aerobic_alternative`; `session_type_rest_day` | Reduced dose belongs as option selection inside easy/support cards. |
| `micro_010` Long Run Extension Week | `session_type_long_easy_run`; `session_type_aerobic_support_run`; `session_type_recovery_run` | Extension variants are long-run options unless terrain changes the coaching decision. |
| `micro_011` Long Endurance Specificity Week | `session_type_goal_terrain_endurance_run`; `session_type_power_hike_practice`; `session_type_long_run_fueling_practice`; `session_type_recovery_run` | Goal-terrain and fueling may both appear, but avoid making every long run a simulation card. |
| `micro_012` Long Run Consolidation Week | `session_type_long_easy_run`; `session_type_short_easy_run`; `session_type_rest_day`; `session_type_mobility_reset` | Familiarity and reduced novelty are micro-level instructions; session cards stay reusable. |
| `micro_013` Strength Support Integration Week | `session_type_strength_support_session`; `session_type_easy_aerobic_run`; `session_type_mobility_reset` | Strength support needs options for low/moderate dose and soreness management. |
| `micro_014` Strength Support Deload Week | `session_type_light_activation_strength`; `session_type_easy_aerobic_run`; `session_type_mobility_reset` | Deload versions are options inside light activation and mobility cards. |
| `micro_015` Trail Familiarity Exposure Week | `session_type_trail_familiarity_run`; `session_type_easy_aerobic_run`; `session_type_trail_skill_drills` | Surface and technicality variants stay options until risk/adaptation changes enough for downhill conditioning. |
| `micro_016` Trail Skill Consolidation Week | `session_type_trail_familiarity_run`; `session_type_easy_aerobic_run`; `session_type_mobility_reset` | Repetition of familiar terrain is a micro placement choice, not a separate session card. |
| `micro_017` Threshold Introduction Week | `session_type_controlled_threshold_session`; `session_type_easy_aerobic_run`; `session_type_recovery_run` | Shorter cruise/tempo prescriptions are options inside controlled threshold. |
| `micro_018` Threshold Development Week | `session_type_controlled_threshold_session`; `session_type_aerobic_support_run`; `session_type_long_easy_run` | Continuous tempo, cruise intervals, and progression tempo can be options if the intent remains threshold control. |
| `micro_019` Threshold Absorption Week | `session_type_short_threshold_touch`; `session_type_easy_aerobic_run`; `session_type_recovery_run`; `session_type_rest_day` | No-quality absorption can use easy/rest cards rather than a special threshold card. |
| `micro_020` Aerobic Power Introduction Week | `session_type_aerobic_power_touch`; `session_type_easy_aerobic_run`; `session_type_recovery_run` | Intro prescriptions are options inside aerobic-power touch. |
| `micro_021` Aerobic Power Stimulus Week | `session_type_aerobic_power_intervals`; `session_type_aerobic_support_run`; `session_type_long_easy_run`; `session_type_recovery_run` | `4 x 4`, `5 x 3`, and `6 x 2` belong as options when structured interval intent is the same. |
| `micro_022` Aerobic Power Recovery-Spacing Week | `session_type_aerobic_power_touch`; `session_type_easy_aerobic_run`; `session_type_low_impact_aerobic_alternative`; `session_type_rest_day` | Small touches are options, not separate development sessions. |
| `micro_023` Strength Endurance Introduction Week | `session_type_intro_uphill_endurance_repeats`; `session_type_easy_aerobic_run`; `session_type_light_activation_strength` | Uphill intro variants stay grouped unless they become true hill circuits or ME climb sessions. |
| `micro_024` Strength Endurance Stimulus Week | `session_type_strength_endurance_climb_session`; `session_type_hill_strength_circuit`; `session_type_easy_aerobic_run`; `session_type_recovery_run` | Sustained climb sessions and circuits are separate cards because execution structure differs. |
| `micro_025` Strength Endurance Absorption Week | `session_type_easy_aerobic_run`; `session_type_walk_or_gentle_movement`; `session_type_short_hill_power`; `session_type_mobility_reset` | The hill touch is optional and should use a low-volume option inside short hill power. |
| `micro_026` Course Demands Exposure Week | `session_type_course_demands_exposure_run`; `session_type_easy_aerobic_run`; `session_type_recovery_run` | Climb, descent, heat, altitude, and technicality can be options only when exposure remains controlled. |
| `micro_027` Course Demands Integration Week | `session_type_goal_terrain_endurance_run`; `session_type_course_demands_exposure_run`; `session_type_mobility_reset`; `session_type_recovery_run` | If multiple demands are combined at high cost, use simulation instead of exposure. |
| `micro_028` Course Demands Simulation Week | `session_type_course_demands_simulation_outing`; `session_type_long_run_fueling_practice`; `session_type_recovery_run`; `session_type_rest_day` | Simulation size is an option; do not split every route profile into a card. |
| `micro_029` Race Execution Integration Week | `session_type_race_execution_cue_run`; `session_type_gear_fueling_check`; `session_type_long_easy_run` | Cue categories are options inside the execution cue card. |
| `micro_030` Race Execution Rehearsal Week | `session_type_race_rehearsal_session`; `session_type_easy_aerobic_run`; `session_type_recovery_run` | Rehearsal options can vary by terrain, gear, fueling, pacing, or aid-flow emphasis. |
| `micro_031` Execution Feedback Week | `session_type_race_execution_cue_run`; `session_type_targeted_lesson_practice`; `session_type_recovery_run` | Feedback analysis alone is app/coach note; a session card exists only when there is movement practice. |
| `micro_032` Fueling Integration Week | `session_type_fueling_habit_run`; `session_type_long_run_fueling_practice`; `session_type_gear_fueling_check` | Habit and long-run practice stay separate because the training cost and context differ. |
| `micro_033` Fueling Practice Week | `session_type_long_run_fueling_practice`; `session_type_controlled_fueling_test`; `session_type_recovery_run` | Product/timing variants belong as options inside the fueling cards. |
| `micro_034` Fueling Tolerance Check Week | `session_type_controlled_fueling_test`; `session_type_easy_aerobic_run`; `session_type_recovery_run` | Keep physical load simple so tolerance is interpretable. |
| `micro_035` Taper Load Reduction Week | `session_type_short_easy_run`; `session_type_sharpening_touch`; `session_type_rest_day`; `session_type_mobility_reset` | Taper doses are options; do not create separate taper cards by exact minute count. |
| `micro_036` Final Freshness Week | `session_type_pre_race_shakeout`; `session_type_neuromuscular_strides`; `session_type_rest_day`; `session_type_gear_fueling_check` | Shakeout plus strides can be one option if both are meant to be done together. |
| `micro_037` Sharpening Touchpoint Week | `session_type_sharpening_touch`; `session_type_easy_aerobic_run`; `session_type_recovery_run` | Event-specific sharpening variants stay options if they are low-cost and familiar. |
| `micro_038` Sharpening Absorption Week | `session_type_easy_aerobic_run`; `session_type_neuromuscular_strides`; `session_type_rest_day`; `session_type_mobility_reset` | Strides are optional; no need for a separate absorption-only session. |
| `micro_039` Readiness Confirmation Week | `session_type_short_easy_run`; `session_type_gear_fueling_check`; `session_type_race_execution_cue_run` | Readiness checks belong inside low-cost sessions, not as standalone analysis cards. |
| `micro_040` Pre-Race Settle Week | `session_type_pre_race_shakeout`; `session_type_neuromuscular_strides`; `session_type_rest_day`; `session_type_gear_fueling_check` | Keep all options familiar and low risk. |
| `micro_041` Post-Competition Reset Week | `session_type_rest_day`; `session_type_walk_or_gentle_movement`; `session_type_mobility_reset`; `session_type_recovery_run` | Race cost determines whether recovery run appears at all. |
| `micro_042` Between-Race Bridge Week | `session_type_easy_aerobic_run`; `session_type_transition_preview_session`; `session_type_recovery_run`; `session_type_rest_day` | Race-relevant touches should be small preview options, not development workouts. |
| `micro_043` Race Season Rhythm Week | `session_type_easy_aerobic_run`; `session_type_long_easy_run`; `session_type_recovery_run` | Shorter long-run and endurance-touch versions are long-run options. |
| `micro_044` Low-Cost Quality Touch Week | `session_type_sharpening_touch`; `session_type_short_threshold_touch`; `session_type_easy_aerobic_run`; `session_type_recovery_run` | Choose one quality touch; do not stack touchpoint cards. |
| `micro_045` Race Debrief Learning Week | `session_type_race_debrief_easy_run`; `session_type_targeted_lesson_practice`; `session_type_rest_day`; `session_type_mobility_reset` | Debrief is not a session unless paired with easy movement or one concrete rehearsal. |
| `micro_046` Race Lesson Integration Week | `session_type_targeted_lesson_practice`; `session_type_easy_aerobic_run`; `session_type_recovery_run` | Lesson categories are options, not separate cards unless execution/risk changes strongly. |
| `micro_047` Immediate Post-Race Recovery Week | `session_type_rest_day`; `session_type_walk_or_gentle_movement`; `session_type_mobility_reset` | No running session is required in this week. |
| `micro_048` Post-Race Return-To-Movement Week | `session_type_walk_or_gentle_movement`; `session_type_recovery_run`; `session_type_run_walk_reentry`; `session_type_rest_day` | Return options depend on soreness and motivation, not a fixed calendar. |
| `micro_049` Reduced-Load Absorption Week | `session_type_easy_aerobic_run`; `session_type_rest_day`; `session_type_mobility_reset`; `session_type_low_impact_aerobic_alternative` | Reduced load is expressed by choosing lower-cost options. |
| `micro_050` Reduced-Load Readiness Check Week | `session_type_easy_run_with_response_check`; `session_type_sharpening_touch`; `session_type_rest_day`; `session_type_mobility_reset` | Short familiar touch is optional only if readiness is already plausible. |
| `micro_051` Transition Reorientation Week | `session_type_easy_aerobic_run`; `session_type_transition_preview_session`; `session_type_recovery_run` | Preview options depend on the next block; keep the card generic but option notes specific. |
| `micro_052` Transition Rhythm Week | `session_type_easy_aerobic_run`; `session_type_aerobic_support_run`; `session_type_rest_day`; `session_type_mobility_reset` | Normal rhythm support is an easy/support session, not a new card. |
| `micro_053` Low-Pressure Aerobic Week | `session_type_easy_aerobic_run`; `session_type_low_impact_aerobic_alternative`; `session_type_rest_day` | Emotional pressure is handled in card notes and option selection. |
| `micro_054` Unstructured Aerobic Option Week | `session_type_easy_aerobic_run`; `session_type_walk_or_gentle_movement`; `session_type_low_impact_aerobic_alternative`; `session_type_rest_day` | Flexible choices should still have intensity and cost guardrails. |
| `micro_055` General Strength Foundation Week | `session_type_general_strength_session`; `session_type_mobility_reset`; `session_type_easy_aerobic_run`; `session_type_low_impact_aerobic_alternative` | Strength progression options belong inside the general strength card. |
| `micro_056` General Mobility Recovery Week | `session_type_mobility_reset`; `session_type_walk_or_gentle_movement`; `session_type_light_activation_strength` | Keep very low load; avoid creating too many exercise-list variants. |
| `micro_057` Movement Variety Exploration Week | `session_type_movement_variety_session`; `session_type_easy_aerobic_run`; `session_type_rest_day` | Activity types are options if the training effect stays low-pressure and aerobic. |
| `micro_058` Movement Variety Rhythm Week | `session_type_easy_aerobic_run`; `session_type_movement_variety_session`; `session_type_mobility_reset`; `session_type_rest_day` | Rhythm is a weekly pattern; session cards stay broad. |
| `micro_059` Aerobic Maintenance Week | `session_type_easy_aerobic_run`; `session_type_long_easy_run`; `session_type_recovery_run` | Maintenance uses familiar options and avoids development-style escalation. |
| `micro_060` Aerobic Maintenance Refresh Week | `session_type_easy_aerobic_run`; `session_type_long_easy_run`; `session_type_walk_or_gentle_movement`; `session_type_mobility_reset` | Route variety belongs as an option unless it changes terrain demand substantially. |
| `micro_061` Quality Touchpoint Week | `session_type_short_threshold_touch`; `session_type_aerobic_power_touch`; `session_type_sharpening_touch`; `session_type_easy_aerobic_run`; `session_type_recovery_run` | Choose one quality-touch family according to the goal; exact touch prescriptions are options. |
| `micro_062` Quality Touchpoint Recovery Week | `session_type_sharpening_touch`; `session_type_recovery_run`; `session_type_rest_day`; `session_type_mobility_reset` | Recovery protection is the micro decision; the quality touch remains small. |
| `micro_063` Constraint-Friendly Week | `session_type_constraint_priority_session`; `session_type_short_easy_run`; `session_type_light_activation_strength`; `session_type_low_impact_aerobic_alternative` | Use options that preserve the highest-value work under real constraints. |
| `micro_064` Minimum Effective Rhythm Week | `session_type_short_easy_run`; `session_type_walk_or_gentle_movement`; `session_type_mobility_reset`; `session_type_rest_day` | The minimum should be honest and repeatable; optional second exposure is an option, not another card. |

### Mainstream Session Taxonomy Completion Review

Coach review after defining the first mainstream session catalog:

- Keep 46 mainstream session types. This is enough to cover the 64 mainstream micro weeks without creating a unique session card for every micro card.
- Treat exact duration, repetition count, and recovery choices as `WorkoutOption`s when they preserve the same workout concept.
- Keep separate cards when execution meaning changes: structured intervals versus fartlek, sustained climb work versus hill circuit, trail familiarity versus downhill conditioning, course exposure versus simulation, fueling habit versus controlled fueling test.
- Add session-family support before building if needed for strength/mobility and low-impact aerobic alternatives; forcing those sessions into unrelated families would make the app less clear.
- Before building, review the taxonomy once more for missing concepts, over-splitting, and whether any accepted type should be merged. After that review, build only the accepted mainstream session cards.

### Built Mainstream Session Card Set

The 46 accepted mainstream session types have been created and published as Drive/cache JSON cards.

Build status:

- `mainstream_endurance`: 46 session cards, `session_001` through `session_046`
- Added session-family support for `Strength / Mobility Support` and `Low-Impact Aerobic Support`
- Exported cache count after build: 334 total cards, including 46 session cards
- Session-to-micro parent references: 217 total; every mainstream session card has at least one parent micro card

This mainstream build checkpoint was followed by the named-philosophy session review below. Reuse mainstream session cards where execution stays the same, and create philosophy-specific session cards only when the philosophy changes the workout decision.

### Named-Philosophy Session Specificity Standard

At session level the specificity standard must be stricter than at macro, mezzo, or micro level because workout variants can multiply quickly. A named-philosophy session card should exist only when the philosophy creates a meaningful distinction from the mainstream session card that changes how the app should choose, explain, or structure the workout.

A named-philosophy session card is justified when it changes at least one of these:

- the actual workout execution, not only the language around it
- the option grouping inside the card
- the intended intensity control or load accounting enough to affect selection
- the terrain, technical, or muscular-risk management enough to change prescription
- the recovery placement or readiness gate enough to change whether the session should appear
- the athlete-facing decision process enough that the session would be misleading as a generic mainstream workout

A named-philosophy session card is not justified when the only difference is emphasis, tone, a reminder, a small duration change, or a normal variant that fits cleanly inside an existing mainstream `WorkoutOption`.

Coach verdict: keep this stricter standard for all philosophies. Most named-philosophy micro cards should still be able to reuse many mainstream session cards. Build specific session cards only where the session itself becomes different, not where the week or block already carries the philosophy-specific logic.

### Named-Philosophy Session Review Matrix

This review compares the named-philosophy micro cards against the 46 mainstream session cards. It does not build the cards yet. It decides which specific session concepts are strong enough to become card candidates and which concepts should reuse mainstream sessions through future `micro_session_reuse.json` metadata.

| Philosophy | Specific micro cards reviewed | Mainstream session reuse expectation | Candidate specific session cards after strict review | Coach verdict |
| --- | ---: | --- | --- | --- |
| `80_20_endurance` | 21 | High reuse for easy running, recovery, rest, fueling, race execution, trail familiarity, and ordinary long-run support. | 4 candidates: `80/20 Low-Intensity Discipline Run`, `80/20 Planned Moderate Session`, `80/20 Distribution-Protected High-Intensity Session`, `80/20 Distribution-Protected Hill-Strength Session`. | Keep candidates only where intensity-distribution accounting changes session selection or execution. Do not duplicate every easy, hard, or hill session just because it belongs inside an 80/20 week. |
| `lydiard` | 15 | High reuse for recovery, basic easy running, long easy running, fueling, readiness checks, and ordinary sharpening touches. | 3 candidates: `Lydiard Sustainable Aerobic Conditioning Run`, `Lydiard Hill Resistance Circuit`, `Lydiard Sequence-Expression Sharpening Session`. | Keep hill resistance as the clearest specific session. Keep aerobic conditioning and sharpening only if the final card preserves Lydiard sequence logic rather than becoming generic steady running or generic sharpening. |
| `cts` | 22 | High reuse for recovery, easy support, fueling checks, course exposure, and many race-practice sessions. | 4 candidates: `CTS Repeatable Workload Session`, `CTS Limiter-Focused Quality Session`, `CTS Event-Demands Durability Session`, `CTS Between-Event Adjustment Session`. | Keep candidates where CTS changes the practical limiter decision. Reuse mainstream cards when the workout is simply a normal threshold, aerobic-power, long-run, fueling, or recovery session. |
| `evoke_endurance` | 17 | Moderate reuse for recovery, easy running, long aerobic support, race logistics, and some course-demand exposure. | 4 candidates: `Evoke Aerobic Threshold Calibration Run`, `Evoke Strength Reserve Session`, `Evoke Uphill Muscular-Endurance Session`, `Evoke Objective Utilisation Session`. | Keep candidates where the session expresses Evoke layer logic, uphill muscular endurance, or objective utilisation. Reuse mainstream sessions for ordinary easy, recovery, fueling, and general endurance support. |
| `swap` | 27 | Moderate reuse for rest, recovery, easy running, mobility, fueling, and many race-practice basics. | 5 candidates: `SWAP Confidence Re-Entry Session`, `SWAP Health-Protected Aerobic Session`, `SWAP Speed-Economy Play Session`, `SWAP Adventure Endurance Session`, `SWAP Agency Race-Practice Session`. | Keep candidates where health, joy, confidence, agency, or speed-as-skill changes session execution. Avoid turning every supportive tone difference into a separate card. |
| `sharman_ultra` | 11 | Moderate-to-high reuse for easy running, recovery, maintenance, fueling basics, and standard long-run support. | 4 candidates: `Sharman Course-Reality Exposure Session`, `Sharman Practical Ultra Execution Session`, `Sharman Ultra Problem-Solving Rehearsal`, `Sharman Logistics Rehearsal Session`. | Keep candidates where practical ultra constraints change the workout design. Reuse mainstream race-practice cards when the only difference is race-distance context or wording. |

### Named-Philosophy Session Candidate Review

These candidates are accepted for the next build pass only if the card authoring step can preserve the distinction named here. If a candidate collapses into an existing mainstream session during writing, do not build it; map the named-philosophy micro cards to the mainstream session instead.

| Candidate session | Philosophy | Coach verdict | Why it may need a specific card | Mainstream sessions it must not duplicate |
| --- | --- | --- | --- | --- |
| `80/20 Low-Intensity Discipline Run` | `80_20_endurance` | Provisional keep | The session may need a firm low-intensity ceiling, drift correction, and distribution-aware selection notes that affect whether the workout should appear in 80/20 easy-discipline weeks. | `Easy Aerobic Run`; `Short Easy Run`; `Recovery Run` |
| `80/20 Planned Moderate Session` | `80_20_endurance` | Keep | Deliberate moderate work is distinct from accidental grey-zone drift and should be structured as a controlled exception inside the 80/20 distribution. | `Steady Aerobic Run`; `Controlled Threshold Session`; `Short Threshold Touch` |
| `80/20 Distribution-Protected High-Intensity Session` | `80_20_endurance` | Provisional keep | The hard work may be similar to mainstream intervals, but the session must preserve polarized load accounting, avoid moderate spillover, and protect low-intensity volume around it. | `Aerobic Power Intervals`; `Aerobic Power Touch`; `Aerobic Power Fartlek` |
| `80/20 Distribution-Protected Hill-Strength Session` | `80_20_endurance` | Provisional keep | Uphill muscular load can hide intensity cost. A specific card is justified only if it changes option size, recovery, or accounting compared with mainstream hill strength. | `Intro Uphill Endurance Repeats`; `Strength-Endurance Climb Session`; `Hill Strength Circuit` |
| `Lydiard Sustainable Aerobic Conditioning Run` | `lydiard` | Provisional keep | It may express Lydiard aerobic conditioning as a sustainable system-building run rather than a generic easy or steady session. Build only if the session clearly carries sequence-aware aerobic conditioning. | `Easy Aerobic Run`; `Steady Aerobic Run`; `Long Easy Run` |
| `Lydiard Hill Resistance Circuit` | `lydiard` | Keep | Hill resistance is a distinctive bridge between aerobic conditioning and later faster work, with specific circuit-style mechanics and sequencing. | `Hill Strength Circuit`; `Strength-Endurance Climb Session` |
| `Lydiard Sequence-Expression Sharpening Session` | `lydiard` | Provisional keep | Sharpening should express the completed sequence without chasing missing fitness. Build only if it differs from a generic sharpening touch. | `Sharpening Touch`; `Pre-Race Shakeout`; `Neuromuscular Strides` |
| `CTS Repeatable Workload Session` | `cts` | Provisional keep | CTS often starts from repeatable workload under real-life constraints; this is specific only if the session uses workload repeatability as the primary selection rule. | `Easy Aerobic Run`; `Aerobic Support Run`; `Constraint Priority Session` |
| `CTS Limiter-Focused Quality Session` | `cts` | Keep | The session is chosen by the athlete's limiter and should make trade-offs explicit rather than assuming one generic quality type. | `Controlled Threshold Session`; `Aerobic Power Intervals`; `Strength-Endurance Climb Session` |
| `CTS Event-Demands Durability Session` | `cts` | Keep | CTS event-demand work should target the course or race limiter that matters most, with practical cost control. | `Goal-Terrain Endurance Run`; `Course-Demands Exposure Run`; `Course-Demands Simulation Outing` |
| `CTS Between-Event Adjustment Session` | `cts` | Provisional keep | Between-event sessions are justified only when the session adapts recovery, maintenance, or limiter work based on the next event. | `Transition Preview Session`; `Targeted Lesson Practice`; `Recovery Run` |
| `Evoke Aerobic Threshold Calibration Run` | `evoke_endurance` | Keep | Aerobic threshold calibration can change the effort target and feedback loop enough to differ from generic steady or easy running. | `Steady Aerobic Run`; `Easy Aerobic Run` |
| `Evoke Strength Reserve Session` | `evoke_endurance` | Keep | Strength reserve is not generic strength; it supports later mountain capacity and must avoid replacing aerobic development. | `General Strength Session`; `Strength Support Session` |
| `Evoke Uphill Muscular-Endurance Session` | `evoke_endurance` | Keep | Evoke ME work is a distinctive uphill force-endurance stimulus and should be more specific than mainstream hill strength. | `Strength-Endurance Climb Session`; `Hill Strength Circuit`; `Intro Uphill Endurance Repeats` |
| `Evoke Objective Utilisation Session` | `evoke_endurance` | Keep | The session should use existing capacity for mountain-objective demands instead of proving fitness through more development load. | `Race Rehearsal Session`; `Course-Demands Simulation Outing`; `Goal-Terrain Endurance Run` |
| `SWAP Confidence Re-Entry Session` | `swap` | Keep | The session should rebuild safety, possibility, and ownership, not only prescribe a run-walk return. | `Run-Walk Re-Entry`; `Short Easy Run`; `Walk Or Gentle Movement` |
| `SWAP Health-Protected Aerobic Session` | `swap` | Provisional keep | It is specific only if health protection changes the session gate, option size, or stop rules. | `Easy Aerobic Run`; `Aerobic Support Run`; `Constraint Priority Session` |
| `SWAP Speed-Economy Play Session` | `swap` | Keep | SWAP speed work should feel like relaxed skill and economy practice, not a strain contest or generic interval session. | `Neuromuscular Strides`; `Short Hill Power`; `Sharpening Touch` |
| `SWAP Adventure Endurance Session` | `swap` | Keep | Adventure endurance changes the emotional and practical structure of long aerobic work while still protecting health. | `Long Easy Run`; `Time-On-Feet Outing`; `Goal-Terrain Endurance Run` |
| `SWAP Agency Race-Practice Session` | `swap` | Keep | Agency-centered race practice should train choices and confidence, not just rehearse compliance with a plan. | `Race Execution Cue Run`; `Race Rehearsal Session`; `Targeted Lesson Practice` |
| `Sharman Course-Reality Exposure Session` | `sharman_ultra` | Keep | The session should reflect practical course preparation under real access constraints instead of idealized specificity. | `Course-Demands Exposure Run`; `Goal-Terrain Endurance Run` |
| `Sharman Practical Ultra Execution Session` | `sharman_ultra` | Keep | Ultra execution should be trained through realistic pacing, hiking, fueling, and restraint under practical conditions. | `Race Execution Cue Run`; `Race Rehearsal Session` |
| `Sharman Ultra Problem-Solving Rehearsal` | `sharman_ultra` | Keep | The session should rehearse foreseeable race problems and calm adaptations, not only ordinary execution cues. | `Targeted Lesson Practice`; `Race Execution Cue Run` |
| `Sharman Logistics Rehearsal Session` | `sharman_ultra` | Provisional keep | Logistics are specific only when gear, fueling, aid-flow, weather, or route constraints change the workout design. | `Gear And Fueling Check`; `Long-Run Fueling Practice`; `Race Rehearsal Session` |

Session review conclusion: the first strict pass accepts 24 named-philosophy session candidates for the next authoring pass, with several marked provisional. This is intentionally smaller than the 113 named-philosophy micro cards because most micro cards should reuse mainstream sessions through metadata rather than duplicate daily workouts.

### Second Coach Pass On Named-Philosophy Session Coverage

Concern reviewed: 24 specific session candidates may be too small if broad candidates hide materially different session decisions. The coach review agrees with keeping a strict standard, but also finds that the first pass compressed several concepts too much. Some named philosophies change not only the weekly structure, but the daily workout gate, terrain choice, option grouping, intensity accounting, or athlete decision process.

Second-pass verdict: increase the next authoring candidate set from 24 to 39. This is still intentionally selective because 39 candidates sit underneath 113 named-philosophy micro cards; most specific micro cards should continue to reuse mainstream session cards through metadata.

| Philosophy | First-pass candidates | Second-pass candidates | Coach adjustment |
| --- | ---: | ---: | --- |
| `80_20_endurance` | 4 | 6 | Split easy-discipline work from long low-intensity distribution, and add course exposure where vertical or terrain cost can distort 80/20 accounting. |
| `lydiard` | 3 | 5 | Add long aerobic conditioning and capacity integration because they are more sequence-specific than generic easy, long, or sharpening sessions. |
| `cts` | 4 | 8 | Split practical limiter work into workload, long-run durability, ultra strength-endurance, event demands, race execution, fueling strategy, and between-event adjustment where the workout decision changes. |
| `evoke_endurance` | 4 | 5 | Add aerobic capacity development separately from aerobic-threshold calibration because Evoke's layer model can make those distinct session roles. |
| `swap` | 5 | 9 | Add supported recovery, fatigue-resistance, confidence course practice, and off-season play because SWAP may change gates, emotional load, agency, and stop rules at session level. |
| `sharman_ultra` | 4 | 6 | Add fueling-gear integration and context-aware between-race recovery because Sharman's practical ultra context can change the session design. |

Revised next authoring candidates:

| Philosophy | Candidate specific session cards to author or final-check |
| --- | --- |
| `80_20_endurance` | `80/20 Low-Intensity Discipline Run`; `80/20 Distribution-Protected Long Endurance Run`; `80/20 Planned Moderate Session`; `80/20 Distribution-Protected High-Intensity Session`; `80/20 Distribution-Protected Hill-Strength Session`; `80/20 Distribution-Safe Course Exposure Session` |
| `lydiard` | `Lydiard Sustainable Aerobic Conditioning Run`; `Lydiard Long Aerobic Conditioning Run`; `Lydiard Hill Resistance Circuit`; `Lydiard Capacity Integration Session`; `Lydiard Sequence-Expression Sharpening Session` |
| `cts` | `CTS Repeatable Workload Session`; `CTS Limiter-Focused Quality Session`; `CTS Long-Run Durability Session`; `CTS Ultra Strength-Endurance Limiter Session`; `CTS Event-Demands Session`; `CTS Race-Execution Strategy Rehearsal`; `CTS Fueling Strategy Rehearsal`; `CTS Between-Event Adjustment Session` |
| `evoke_endurance` | `Evoke Aerobic Capacity Development Run`; `Evoke Aerobic Threshold Calibration Run`; `Evoke Strength Reserve Session`; `Evoke Uphill Muscular-Endurance Session`; `Evoke Objective Utilisation Session` |
| `swap` | `SWAP Supported Recovery Session`; `SWAP Confidence Re-Entry Session`; `SWAP Health-Protected Aerobic Session`; `SWAP Speed-Economy Play Session`; `SWAP Adventure Endurance Session`; `SWAP Fatigue-Resistance Session`; `SWAP Confidence Course-Practice Session`; `SWAP Agency Race-Practice Session`; `SWAP Off-Season Play Session` |
| `sharman_ultra` | `Sharman Course-Reality Exposure Session`; `Sharman Practical Ultra Execution Session`; `Sharman Ultra Problem-Solving Rehearsal`; `Sharman Fueling-Gear Integration Session`; `Sharman Logistics Rehearsal Session`; `Sharman Context-Aware Between-Race Recovery Session` |

Second-pass guardrail: this expanded list is not permission to duplicate mainstream sessions. During authoring, each card must still prove that its `WorkoutBlock`s, `WorkoutOption`s, gates, stop rules, terrain notes, or selection logic differ meaningfully from the corresponding mainstream session. If the difference disappears while writing the card, remove that candidate and map the relevant micro card to the mainstream session instead.

### Third Coach Pass On Named-Philosophy Session Reduction

Concern reviewed: the second pass only looked for missing candidates, so it may have over-corrected. The reduction pass challenges each of the 39 candidates against the same strict session-level standard.

Coach verdict: reduce the build candidate set from 39 to 31. This keeps the session layer richer than the first pass while removing candidates whose difference mostly belongs in a micro card, reuse mapping, or `WorkoutOption` inside another card.

| Philosophy | Second-pass candidates | Reduced build candidates | Reduction verdict |
| --- | ---: | ---: | --- |
| `80_20_endurance` | 6 | 5 | Remove separate `80/20 Distribution-Safe Course Exposure Session`; the course-demand idea should usually map to mainstream course exposure or the 80/20 long/hill cards depending on the actual limiter. |
| `lydiard` | 5 | 4 | Remove separate `Lydiard Capacity Integration Session`; integration is mostly a week/block sequencing decision unless the final workout becomes hill resistance, sharpening, or aerobic conditioning. |
| `cts` | 8 | 6 | Remove separate `CTS Repeatable Workload Session` and `CTS Between-Event Adjustment Session`; both are better handled by selecting existing easy, recovery, preview, or limiter sessions unless a sharper workout decision appears. |
| `evoke_endurance` | 5 | 4 | Remove separate `Evoke Aerobic Capacity Development Run`; capacity development can usually reuse mainstream easy, long, or steady sessions while Evoke-specific control is clearer in threshold, strength reserve, ME, and objective-utilisation cards. |
| `swap` | 9 | 8 | Remove separate `SWAP Supported Recovery Session`; recovery support should usually reuse rest, walk, mobility, or recovery run cards with SWAP micro-level framing unless health gates change the workout itself. |
| `sharman_ultra` | 6 | 4 | Merge `Sharman Fueling-Gear Integration Session` and `Sharman Logistics Rehearsal Session` into one logistics-focused candidate; remove separate context-aware recovery because the workout choices are usually mainstream recovery choices selected through Sharman context. |

Final reduced authoring candidates:

| Philosophy | Candidate specific session cards to build next |
| --- | --- |
| `80_20_endurance` | `80/20 Low-Intensity Discipline Run`; `80/20 Distribution-Protected Long Endurance Run`; `80/20 Planned Moderate Session`; `80/20 Distribution-Protected High-Intensity Session`; `80/20 Distribution-Protected Hill-Strength Session` |
| `lydiard` | `Lydiard Sustainable Aerobic Conditioning Run`; `Lydiard Long Aerobic Conditioning Run`; `Lydiard Hill Resistance Circuit`; `Lydiard Sequence-Expression Sharpening Session` |
| `cts` | `CTS Limiter-Focused Quality Session`; `CTS Long-Run Durability Session`; `CTS Ultra Strength-Endurance Limiter Session`; `CTS Event-Demands Session`; `CTS Race-Execution Strategy Rehearsal`; `CTS Fueling Strategy Rehearsal` |
| `evoke_endurance` | `Evoke Aerobic Threshold Calibration Run`; `Evoke Strength Reserve Session`; `Evoke Uphill Muscular-Endurance Session`; `Evoke Objective Utilisation Session` |
| `swap` | `SWAP Confidence Re-Entry Session`; `SWAP Health-Protected Aerobic Session`; `SWAP Speed-Economy Play Session`; `SWAP Adventure Endurance Session`; `SWAP Fatigue-Resistance Session`; `SWAP Confidence Course-Practice Session`; `SWAP Agency Race-Practice Session`; `SWAP Off-Season Play Session` |
| `sharman_ultra` | `Sharman Course-Reality Exposure Session`; `Sharman Practical Ultra Execution Session`; `Sharman Ultra Problem-Solving Rehearsal`; `Sharman Fueling-Gear Logistics Rehearsal Session` |

Reduction guardrail: the removed candidates are intentionally not active card candidates. Their coaching content should be handled by parent micro cards, mainstream session reuse, or options inside the retained specific cards rather than kept as a watchlist.

### Built Named-Philosophy Session Card Set

The 31 reduced named-philosophy session candidates have been created and published as Drive/cache JSON cards.

Build status:

- `80_20_endurance`: 5 session cards, `session_047` through `session_051`
- `lydiard`: 4 session cards, `session_052` through `session_055`
- `cts`: 6 session cards, `session_056` through `session_061`
- `evoke_endurance`: 4 session cards, `session_062` through `session_065`
- `swap`: 8 session cards, `session_066` through `session_073`
- `sharman_ultra`: 4 session cards, `session_074` through `session_077`
- Exported cache count after build: 365 total cards, including 77 session cards

The `micro_session_reuse.json` metadata has been added locally so named-philosophy micro cards can surface reused mainstream session cards without duplicate session content.

### Micro-Session Reuse Metadata

When a named philosophy uses mainstream session cards under either reused mainstream micro cards or philosophy-specific micro cards, the app should use explicit reuse metadata instead of duplicated session files. The metadata lives in `micro_session_reuse.json` and is also included in the app-facing `training_cards_library.json` bundle.

Each reuse entry records the philosophy profile, micro card ID and name, reused mainstream session card ID and name, and whether the relationship is `inherit_mainstream` or `reuse_mainstream`. This keeps shared session content as one source of truth while allowing the pathway UI to show ordinary easy, recovery, support, fueling, skill, and race-practice sessions under named-philosophy micro contexts.

Build status:

- `micro_session_reuse.json`: 1087 entries in the local exported cache
- Source coverage: automatic reuse from `mezzo_micro_reuse.json` plus explicit named-philosophy micro-to-mainstream-session mappings
- Pathway reachability after build: 0 dead-end micro cards
- App wiring: pathway children and philosophy filters now read the micro-to-session reuse layer

Cloud status: the session layer and updated root metadata have been uploaded to Drive and verified by download/readback validation. The Drive-backed library now contains 365 cards and `micro_session_reuse.json` with 1087 entries.

Next session step: review app pathway behavior with named-philosophy micro cards to confirm reused mainstream sessions and specific session cards appear together correctly.
