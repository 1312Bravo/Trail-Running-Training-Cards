# Card Matrix

This file is the working build map for the training card library.

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

The justified macro cards have been created as active Python seed cards. This section records build status without duplicating the full card content.

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

The accepted mainstream mezzo cards have been created as active Python seed cards. This section records build status without duplicating the full card content.

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
