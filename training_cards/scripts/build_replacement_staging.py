from __future__ import annotations

import shutil
from pathlib import Path

from training_cards.json_store import (
    build_display_config,
    build_manifest,
    export_cards_to_json,
    write_json,
    write_library_bundle,
)
from training_cards.pathway import validate_pathway_publish_ready
from training_cards.schemas import (
    CardReference,
    CardRelationship,
    CardType,
    MacroCard,
    MezzoCard,
    MicroCard,
    SessionCard,
    SessionPart,
    TrainingLevel,
)
from training_cards.session_families import (
    AEROBIC_POWER_SESSION_FAMILY,
    EASY_SESSION_FAMILY,
    ENDURANCE_SESSION_FAMILY,
    HILL_POWER_SESSION_FAMILY,
    NEUROMUSCULAR_SESSION_FAMILY,
    RACE_PRACTICE_SESSION_FAMILY,
    RECOVERY_SESSION_FAMILY,
    STRENGTH_ENDURANCE_SESSION_FAMILY,
    THRESHOLD_SESSION_FAMILY,
    TRAIL_SPECIFIC_SESSION_FAMILY,
)


STAGING_DIR = Path(__file__).resolve().parents[1] / "local_cache" / "rebuild_staging"


def parent(card_id: str, tag: str) -> list[CardReference]:
    return [CardReference(card_id=card_id, relationship=CardRelationship.PARENT, tags=[tag])]


def profile_application(profile_ids: list[str], explanation: str) -> str:
    return (
        "Profile application: "
        + ", ".join(profile_ids)
        + ". "
        + explanation
    )


def macro(
    id: str,
    title: str,
    profiles: list[str],
    summary: str,
    purpose: str,
    timing: list[str],
    profile_note: str,
) -> MacroCard:
    return MacroCard(
        id=id,
        slug=id.replace("_", "-"),
        title=title,
        card_type=CardType.MACRO,
        suitable_levels=[TrainingLevel.ALL],
        summary=summary,
        purpose=purpose,
        philosophy_profile_ids=profiles,
        tags=["rebuild", "macro", *profiles],
        goal_race_context=timing,
        training_profile=["A phase-level decision framework, not a workout schedule."],
        expected_adaptations=["A coherent next training direction and better sequencing decisions."],
        watchouts=["Do not use a macro label to skip readiness, recovery, or course-specific judgement."],
        progression_rules=["Progress only when the work in the phase is repeatable and the next layer is justified."],
        regression_rules=["Extend the current phase or return to a simpler phase when response shows the next layer is premature."],
        additional_information=profile_application(profiles, profile_note),
        recommended_duration_weeks="4-12 weeks, adjusted to history, goal timing, and response",
        timing_guidance=timing,
    )


def mezzo(
    id: str,
    title: str,
    profiles: list[str],
    parent_id: str,
    summary: str,
    purpose: str,
    stress: str,
    profile_note: str,
) -> MezzoCard:
    return MezzoCard(
        id=id,
        slug=id.replace("_", "-"),
        title=title,
        card_type=CardType.MEZZO,
        suitable_levels=[TrainingLevel.INTERMEDIATE, TrainingLevel.ADVANCED],
        summary=summary,
        purpose=purpose,
        philosophy_profile_ids=profiles,
        tags=["rebuild", "mezzo", *profiles],
        goal_race_context=["Use when the parent phase and athlete readiness make this focused block appropriate."],
        training_profile=[stress],
        expected_adaptations=["A clearly targeted capacity that supports the next planning layer."],
        watchouts=["Do not add this block because its sessions look impressive; it must solve a current performance problem."],
        progression_rules=["Increase one meaningful variable at a time while protecting the purpose and surrounding recovery."],
        regression_rules=["Reduce density, duration, terrain cost, or intensity while preserving the main capacity when possible."],
        additional_information=profile_application(profiles, profile_note),
        references=parent(parent_id, "phase_context"),
        recommended_duration_weeks="2-6 weeks",
        placement_guidance=["Place only after the parent phase has supplied the stated prerequisites."],
    )


def micro(
    id: str,
    title: str,
    profiles: list[str],
    parent_id: str,
    summary: str,
    purpose: str,
    structure: list[str],
    profile_note: str,
) -> MicroCard:
    return MicroCard(
        id=id,
        slug=id.replace("_", "-"),
        title=title,
        card_type=CardType.MICRO,
        suitable_levels=[TrainingLevel.INTERMEDIATE, TrainingLevel.ADVANCED],
        summary=summary,
        purpose=purpose,
        philosophy_profile_ids=profiles,
        tags=["rebuild", "micro", *profiles],
        goal_race_context=["Use inside the matching block when the runner can absorb the planned key stress."],
        training_profile=["Weekly structure with deliberate contrast between key stress and recovery.", *structure],
        expected_adaptations=["A repeatable weekly rhythm that makes the block's main work absorbable."],
        watchouts=["Do not preserve the calendar at the expense of recovery, movement quality, or the week's central purpose."],
        progression_rules=["Progress the key stress only after the whole week remains repeatable."],
        regression_rules=["Keep the weekly rhythm but remove a secondary stressor or reduce the main dose."],
        additional_information=profile_application(profiles, profile_note),
        references=parent(parent_id, "block_context"),
        recommended_duration_days="7 days",
        week_structure=structure,
        key_sessions=["Choose the key sessions from the linked session cards; do not stack competing hard demands."],
        load_pattern="One primary focus with deliberately protected lower-stress days.",
        placement_guidance=["Move key work when terrain, life stress, or recovery changes the actual dose."],
        recovery_requirements=["Easy days remain genuinely easy; reduce or move key work when readiness is poor."],
    )


def session(
    id: str,
    title: str,
    profiles: list[str],
    parent_id: str,
    summary: str,
    purpose: str,
    family,
    parts: list[SessionPart],
    stress: list[str],
    profile_note: str,
    adaptations: list[str],
    watchouts: list[str],
) -> SessionCard:
    return SessionCard(
        id=id,
        slug=id.replace("_", "-"),
        title=title,
        card_type=CardType.SESSION,
        suitable_levels=[TrainingLevel.INTERMEDIATE, TrainingLevel.ADVANCED],
        summary=summary,
        purpose=purpose,
        philosophy_profile_ids=profiles,
        tags=["rebuild", "session", *profiles, *family.tags],
        goal_race_context=["Use only when the parent week gives this session an appropriate place and recovery space."],
        training_profile=stress,
        expected_adaptations=adaptations,
        watchouts=watchouts,
        progression_rules=["Progress duration, repetitions, terrain demand, or execution quality one at a time."],
        regression_rules=["Keep the intended stimulus with fewer repetitions, shorter duration, gentler terrain, or a lower-cost alternative."],
        additional_information=profile_application(profiles, profile_note),
        references=parent(parent_id, "week_context"),
        session_family=family,
        typical_duration="45-180 minutes depending on the card and athlete context",
        workout_parts=parts,
    )


def build_cards() -> list:
    cards = [
        macro("macro_002", "Aerobic Base And Sequential Development", ["lydiard"], "Build the aerobic base that later hill strength and intensity can use.", "Develop broad running capacity, internal effort judgement, and the readiness for later phases.", ["Use when enough time exists before a target event to earn later specific work.", "Work backward from the goal rather than rushing into race simulation."], "Lydiard changes this phase from generic easy mileage into an intentionally base-first stage: the runner develops an inner coach, regulates response, and earns the next phase."),
        macro("macro_003", "Mountain Capacity Development", ["evoke_endurance"], "Build aerobic capacity and force reserve before demanding mountain utilisation.", "Prepare the layers that make later climbing-specific and event-like work productive.", ["Use for mountain objectives when the runner needs more aerobic capacity, strength reserve, or local muscular durability."], "Evoke defines this phase as capacity building, not early race simulation: aerobic threshold-informed work and strength reserve come before muscular endurance and utilisation."),
        macro("macro_004", "Event-Demand Specific Preparation", ["cts"], "Turn durable capacity into preparation for the actual performance problem.", "Match training emphasis to the goal event's duration, terrain, execution, and recovery demands.", ["Use after a durable base exists and the event demands can guide meaningful specificity."], "CTS makes the event-demand analysis the organising principle. Specificity is selected because it solves a known demand, not because a session resembles an impressive race rehearsal."),
        macro("macro_005", "Sustainable Economy And Speed Development", ["swap"], "Develop economical faster movement while protecting long-term engagement.", "Add speed, coordination, and fatigue-resistance thinking without sacrificing the athlete's sustainable relationship with running.", ["Use when the runner can absorb faster work and needs more efficient movement, confidence, or late-race durability."], "SWAP makes economy, speed skill, curiosity, and long-term fulfilment part of the performance objective. The phase is not a licence to chase intensity at the expense of consistency."),
        macro("macro_006", "Individualised Ultra Execution And Peak", ["sharman_ultra"], "Integrate fitness with practical ultra execution for the runner's real event and life context.", "Use adaptive planning to rehearse relevant pacing, fueling, terrain, and decision-making while arriving fresh enough to race.", ["Use near an ultra goal after the athlete and course demands are understood.", "Adjust the phase to the runner's practical constraints and recovery response."], "Sharman Ultra gives this phase its athlete-specific and execution-led character: the plan adapts to life, course, and response rather than treating a generic simulation as mandatory."),
        mezzo("mezzo_002", "Aerobic Base Block", ["lydiard"], "macro_002", "Accumulate aerobic work while teaching effort regulation and protecting musculoskeletal adaptation.", "Build the base that supports later hill strength and higher-intensity phases.", "Frequent aerobic running with effort kept responsive rather than locked to a universal pace.", "Lydiard makes the base a primary adaptation phase, not filler. The athlete uses easy and moderate-feeling running to develop internal judgement and observes recovery before progressing."),
        mezzo("mezzo_003", "Intensity Distribution Block", ["80_20_endurance"], "macro_002", "Keep most work low intensity and place quality where it can be executed well.", "Create clear contrast between aerobic volume, selected quality, and recovery.", "A low-intensity majority, structured quality, and a weekly pattern that avoids accidental moderate training.", "80/20 shapes the block through deliberate distribution and precise execution. The goal is not a mathematical badge; it is enough easy work to make the selected quality useful."),
        mezzo("mezzo_004", "Mountain Aerobic Capacity Block", ["evoke_endurance"], "macro_003", "Raise sustainable aerobic output before local-muscle or race-specific mountain work dominates.", "Develop repeatable low-intensity mountain movement at an individualised aerobic cost.", "Large aerobic exposure below the relevant aerobic threshold, using terrain and hiking to control impact and intensity.", "Evoke defines this as capacity work. The runner improves the aerobic system first, using threshold-informed cues and access-aware terrain choices rather than replacing base work with hard climbs."),
        mezzo("mezzo_005", "Muscular Endurance Block", ["evoke_endurance"], "macro_003", "Build repeated uphill propulsive force on top of an established aerobic base.", "Develop local muscular endurance for sustained climbing or steep hiking without sacrificing the aerobic foundation.", "High local-muscle demand with continued aerobic volume and generous recovery from the specific sessions.", "Evoke makes muscular endurance a distinct layer: repeated force in the propelling muscles, added to adequate aerobic capacity and strength reserve, not a generic hard-hill block."),
        mezzo("mezzo_006", "Goal-Demand Endurance Block", ["cts"], "macro_004", "Develop the capacities that most directly limit the target event.", "Use event analysis to select only the duration, terrain, fueling, intensity, and execution work the goal truly requires.", "Purposeful specific sessions supported by a durable workload and protected recovery.", "CTS defines the block from the performance problem. Course features and race demands guide the work, but the block avoids copying the entire race when a narrower stimulus solves the limiter better."),
        mezzo("mezzo_007", "Economy And Speed Block", ["swap"], "macro_005", "Improve economical faster movement through purposeful speed skill and consistent training.", "Develop coordination, confidence, and speed endurance while keeping the athlete engaged and recoverable.", "Short fast touches and selected quality work surrounded by enjoyable, sustainable aerobic running.", "SWAP gives this block a speed-and-economy purpose with a whole-person boundary. Faster work is a skill and opportunity for growth, not a test of worth or toughness."),
        mezzo("mezzo_008", "Ultra Execution Block", ["sharman_ultra"], "macro_006", "Rehearse the decisions that let fitness become useful during the actual ultra.", "Integrate pacing, fueling, hiking, terrain, gear, and adjustment skills in the athlete's real context.", "Selective event-relevant practice, practical substitutions, and adaptation to life and recovery response.", "Sharman Ultra makes coaching and education visible: the runner learns why the rehearsal matters, what can change, and how to preserve its purpose when exact terrain or timing is unavailable."),
        mezzo("mezzo_009", "Peak Integration And Taper Block", ["cts", "lydiard"], "macro_006", "Integrate earned capacities, then reduce fatigue without losing event readiness.", "Arrive at the target with specific confidence and freshness rather than with the largest final training load.", "A decreasing total load, retained sharpness, and carefully selected event-relevant reminders.", "CTS contributes event-demand specificity and Lydiard contributes sequence and timing. Together they make taper a planned expression of preparation, not a last-minute attempt to create fitness."),
        micro("micro_002", "Aerobic Base Week", ["lydiard"], "mezzo_002", "A base-focused week that develops aerobic capacity and effort judgement.", "Accumulate aerobic work while using the runner's response to regulate daily effort and recovery.", ["One longer aerobic run.", "Several easy-to-steady aerobic runs by feel.", "Recovery is adjusted from sleep, mood, soreness, and ordinary running response."], "Lydiard makes the week sequential: aerobic work is the current priority and prepares later hill strength. The runner practises the inner-coach skill instead of treating external numbers as the only truth."),
        micro("micro_003", "Structured Intensity Distribution Week", ["80_20_endurance"], "mezzo_003", "A week with protected low-intensity volume and one clearly structured quality stimulus.", "Make the intended distribution visible so easy days stay easy and the key workout has value.", ["Predominantly low-intensity running.", "One selected quality session with clear targets.", "Easy or recovery movement around the quality day."], "80/20 makes contrast non-negotiable. The week is successful when the athlete avoids unplanned moderate work and can execute the chosen quality session with control."),
        micro("micro_004", "Mountain Aerobic Capacity Week", ["evoke_endurance"], "mezzo_004", "Accumulate individualised aerobic mountain movement without turning climbs into threshold work.", "Build aerobic capacity through repeatable below-threshold running, hiking, or incline movement.", ["Two or more aerobic mountain or incline exposures.", "One longer low-intensity outing.", "No muscular-endurance session unless separately planned."], "Evoke makes the intensity boundary central. Hiking, incline treadmill, or gentler gradients are correct when they preserve aerobic metabolism and repeatability better than forced running."),
        micro("micro_005", "Muscular Endurance Week", ["evoke_endurance"], "mezzo_005", "Place one local-muscle climbing stimulus inside an otherwise protected aerobic week.", "Expose the propelling muscles to repeated force while keeping enough aerobic volume for the block to work.", ["One muscular-endurance uphill or stair session.", "Continued low-intensity aerobic volume.", "Recovery days that account for delayed local fatigue."], "Evoke keeps the session from becoming random suffering: local muscular fatigue is the target, but the week protects the aerobic base and does not stack another equivalent high-cost climb."),
        micro("micro_006", "Goal-Demand Long Week", ["cts"], "mezzo_006", "Use one selected event-demand session while preserving the workload needed to absorb it.", "Practise the target event's most relevant duration, terrain, fueling, or pacing problem.", ["One goal-demand long session.", "Easy running that preserves total workload.", "A recovery response check before and after the key session."], "CTS makes the week's key session answer a real event-demand question. The rest of the week is deliberately simple so the runner can learn from and recover from that work."),
        micro("micro_007", "Economy And Speed Week", ["swap"], "mezzo_007", "Develop faster economical movement without losing the joy and consistency that support long-term progress.", "Use one focused speed or economy session and low-cost coordination touches in a sustainable weekly rhythm.", ["One speed or aerobic-power session.", "Optional relaxed strides.", "Enough easy running to keep the work fresh rather than forced."], "SWAP makes speed a trainable skill and keeps athlete engagement in the decision. The runner should finish the week with confidence and curiosity, not a sense that every run had to prove something."),
        micro("micro_008", "Ultra Execution Week", ["sharman_ultra"], "mezzo_008", "Practise an ultra-relevant decision while adapting the week to the athlete's life and course access.", "Integrate one execution session with practical fueling, pacing, hiking, or terrain judgement.", ["One purpose-defined ultra execution session.", "Flexible route or modality choices that preserve the main demand.", "Recovery spacing based on the actual cost of the terrain."], "Sharman Ultra makes the adjustment logic explicit. The athlete learns what must be preserved in the session and what may change when life, weather, or access prevents the ideal route."),
        micro("micro_009", "Integration And Taper Week", ["cts", "lydiard"], "mezzo_009", "Reduce fatigue while keeping the runner connected to the event's key sensations.", "Integrate preparation and arrive fresh, confident, and clear about race execution.", ["Reduced total load.", "One short, controlled event-relevant reminder.", "More recovery than the athlete's anxiety may initially request."], "CTS keeps the reminder tied to the event demand, while Lydiard keeps the week in the correct final sequence. Neither philosophy supports cramming missed fitness into taper."),
        session("session_001", "Easy Aerobic Run", ["80_20_endurance"], "micro_003", "Low-intensity running that protects the distribution and supports repeatable volume.", "Accumulate aerobic running without drifting into unplanned moderate effort.", EASY_SESSION_FAMILY, [SessionPart("Main run", "30-90 minutes", "RPE 2-4", "Keep breathing conversational; slow or use short walks before effort becomes steady-moderate.", "On hills, regulate effort rather than preserving road pace.")], ["Low intensity is the primary stimulus.", "The route must allow the runner to stay genuinely easy."], "80/20 defines success as protecting the low-intensity majority. The runner adjusts pace, route, or walk breaks instead of converting the day into hidden quality.", ["Aerobic volume", "Recovery between quality sessions", "Effort discipline"], ["Do not chase pace because the terrain is rolling.", "Do not turn a tired day into a steady run." ]),
        session("session_002", "Response-Led Recovery Run", ["lydiard"], "micro_002", "Very easy movement guided by whether it leaves the runner better, not by a target pace.", "Support recovery while practising the ability to read the body's response.", RECOVERY_SESSION_FAMILY, [SessionPart("Easy movement", "20-45 minutes", "RPE 1-3", "Start conservatively; shorten, walk, or stop if movement does not become easier.", "Choose low-consequence terrain with minimal technical or descent cost.")], ["Recovery response is more important than distance.", "The session may become a walk or rest day."], "Lydiard makes the runner's internal state the key measure. This is not a missed workout; it is the appropriate side of the stress-and-recovery cycle when the body has not rebuilt.", ["Freshness", "Athlete self-regulation", "Readiness for later work"], ["Do not use this to add mileage.", "Do not force a run through persistent pain or illness symptoms." ]),
        session("session_003", "Aerobic Base Long Run", ["lydiard"], "micro_002", "A sustained aerobic run that builds the base needed for later phases.", "Extend aerobic capacity and confidence without turning the long run into premature race work.", ENDURANCE_SESSION_FAMILY, [SessionPart("Settling in", "15-20 minutes", "RPE 2-3", "Begin easier than planned and let effort, not anxiety, determine the day.", "Use terrain that lets the runner maintain relaxed movement."), SessionPart("Aerobic running", "60-150 minutes", "RPE 3-4", "Stay controlled enough to finish feeling that the effort was repeatable.", "Hike steep grades when that preserves the aerobic purpose."), SessionPart("Recovery check", "5 minutes", "RPE 1-2", "Note breathing, coordination, and next-day response for future progression.", "Avoid adding technical descent late only to increase distance.")], ["Sustained aerobic duration", "Response-led pacing", "No race-pace finish requirement"], "Lydiard makes this a base deposit, not a weekly test. The runner practises internal pacing and lets musculoskeletal readiness limit progression even when cardiovascular fitness feels ahead.", ["Aerobic capacity", "Durable time on feet", "Effort regulation"], ["Do not force a historic mileage target.", "Do not add intensity because the run feels good early." ]),
        session("session_004", "Aerobic Threshold Assessment Run", ["evoke_endurance"], "micro_004", "A controlled repeatable run used to estimate aerobic response and guide easy-volume intensity.", "Observe whether a chosen aerobic output remains metabolically and mechanically sustainable.", EASY_SESSION_FAMILY, [SessionPart("Warm-up", "15-20 minutes", "RPE 2-3", "Run easily until breathing and stride feel settled.", "Use a consistent route or treadmill setting for repeat comparisons."), SessionPart("Controlled assessment", "45-60 minutes", "RPE 3-4", "Hold a sustainable controlled output; record pace, heart rate, breathing, and drift without racing.", "Prefer steady terrain; steep terrain can be used only if repeated consistently."), SessionPart("Cool-down", "10 minutes", "RPE 1-2", "Finish easily and record conditions that could alter interpretation.", "Heat, altitude, fatigue, and terrain are part of the result.")], ["Individual intensity assessment", "Below-threshold aerobic control", "Repeatable conditions"], "Evoke uses threshold-informed assessment to individualise the aerobic base. The number is evidence for a training decision, not a verdict or a reason to turn the run into a maximal test.", ["More accurate aerobic intensity guidance", "Better progression decisions"], ["Do not compare different routes or weather as if they were identical.", "Do not use one result to diagnose the whole athlete." ]),
        session("session_005", "Uphill Muscular Endurance Repeats", ["evoke_endurance"], "micro_005", "Sustained climbing repetitions that create local propulsive-muscle fatigue on an aerobic base.", "Develop the ability to repeat meaningful uphill force without confusing the session with a maximal interval workout.", STRENGTH_ENDURANCE_SESSION_FAMILY, [SessionPart("Warm-up", "20 minutes", "RPE 2-3", "Include easy running or hiking and a few short controlled climbs.", "Choose a steady climb that permits safe repeatable movement."), SessionPart("Uphill repetitions", "3-6 x 6-12 minutes", "RPE 6-7", "Climb steadily until the propelling muscles work hard; recover easily downhill or on flat ground before the next repeat.", "Use hiking when gradient makes running distort the intended force and control."), SessionPart("Cool-down", "10-20 minutes", "RPE 1-2", "Finish easily; assess local fatigue over the next 24-48 hours.", "Reduce descent exposure if it would add unrelated eccentric damage.")], ["High local muscle demand", "Controlled cardiovascular cost", "Meaningful delayed recovery cost"], "Evoke makes the local muscular stimulus explicit. This belongs only after adequate aerobic capacity and strength reserve exist, and it must sit on top of rather than replace the athlete's aerobic volume.", ["Uphill muscular endurance", "Climbing force durability", "Better use of aerobic capacity on steep terrain"], ["Do not add this to a week already heavy with hard climbing.", "Do not mistake crippling soreness for a successful dose." ]),
        session("session_006", "Incline Muscular Endurance Climb", ["evoke_endurance"], "micro_005", "A controlled incline alternative that reproduces repeated uphill force when mountains are unavailable.", "Provide accessible muscular-endurance work while being honest about the specificity it does not reproduce.", STRENGTH_ENDURANCE_SESSION_FAMILY, [SessionPart("Warm-up", "15-20 minutes", "RPE 2-3", "Move easily before adding incline or resistance.", "Treadmill incline, stairs, or a safe sustained hill are all acceptable."), SessionPart("Continuous climb", "25-45 minutes", "RPE 6-7", "Use a steady incline and cadence that creates substantial local work without sprinting.", "Use rails only for safety, not to unload the propelling movement."), SessionPart("Easy finish", "10 minutes", "RPE 1-2", "Return to easy movement and note local fatigue.", "This alternative does not practise outdoor footing or descent." )], ["Repeated propulsive force", "Accessible controlled incline", "No required outdoor race simulation"], "Evoke prioritises the capacity over the sacred route. This alternative can preserve the local-muscle stimulus, but the card states clearly that it does not replace technical climbing, traction, or downhill practice.", ["Accessible climbing-specific capacity", "Local muscular durability"], ["Do not add load simply because the route feels controlled.", "Do not claim this replaces all mountain skills." ]),
        session("session_007", "Goal-Demand Long Run", ["cts"], "micro_006", "A long run that rehearses one clearly selected demand of the target event.", "Solve an event-relevant duration, terrain, fueling, or pacing problem without copying the whole race.", ENDURANCE_SESSION_FAMILY, [SessionPart("Easy start", "20-30 minutes", "RPE 2-3", "Start below target effort and settle into the purpose of the day.", "Choose terrain that exposes the selected demand."), SessionPart("Selected rehearsal", "90-240 minutes", "RPE 3-6", "Practise the chosen demand, such as sustained climbing, fueling cadence, or late-run pacing; keep all other demands modest.", "Use route, terrain, and duration only as specific as the performance problem requires."), SessionPart("Debrief", "10 minutes", "RPE 1-2", "Record what held up, what failed, and what should change next time.", "Account for descent and technical cost, not only pace.")], ["One defined event demand", "Durable workload context", "Fueling and pacing may be part of the stimulus"], "CTS defines this run from the event problem. It is not a generic very-long outing or a full race simulation; the design deliberately limits unrelated stress so the coach can learn from the selected rehearsal.", ["Specific endurance", "Practical event execution", "Better next-block decisions"], ["Do not turn every long run into a race.", "Do not increase every variable at once." ]),
        session("session_008", "Event-Specific Progression Run", ["cts"], "micro_006", "A controlled progression that practises changing output under a clearly defined event demand.", "Develop pacing discipline and the ability to use durable capacity more specifically without racing training sessions.", ENDURANCE_SESSION_FAMILY, [SessionPart("Easy running", "20 minutes", "RPE 2-3", "Settle into relaxed aerobic movement.", "Use a route where effort can be adjusted safely."), SessionPart("Progressive work", "30-60 minutes", "RPE 4-7", "Increase only toward the event-relevant effort or terrain demand; stop the progression before form, pacing, or judgement deteriorates.", "On trail, progress by effort, climbing output, or movement quality rather than road pace."), SessionPart("Cool-down", "10-15 minutes", "RPE 1-2", "Return to easy running and assess whether the session was controlled.", "Avoid a hard technical descent after the main work.")], ["Purposeful progression", "Event-demand pacing", "Controlled finish rather than maximal effort"], "CTS uses progression only when it rehearses an identified demand. The runner is not proving fitness; they are learning how to apply existing capacity with appropriate restraint.", ["Pacing judgement", "Specific sustained output", "Confidence in controlled execution"], ["Do not turn the final segment into a race.", "Do not use if accumulated fatigue prevents accurate pacing practice." ]),
        session("session_009", "Threshold Intervals", ["80_20_endurance"], "micro_003", "Structured threshold work with clear targets and protected recovery around it.", "Develop controlled hard running while preserving the low-intensity majority of the week.", THRESHOLD_SESSION_FAMILY, [SessionPart("Warm-up", "15-20 minutes", "RPE 2-3", "Warm up easily with optional short relaxed strides.", "Use stable terrain or effort-based control when pace is distorted."), SessionPart("Threshold intervals", "3-5 x 6-10 minutes", "RPE 7-8", "Run comfortably hard with even execution; take easy recoveries long enough to maintain form and control.", "Use perceived effort or power on hills; heart rate may lag."), SessionPart("Cool-down", "10-15 minutes", "RPE 1-2", "Finish easily and keep the following day low intensity.", "Avoid adding technical descent for extra fatigue.")], ["Deliberate moderate-to-high intensity", "Structured work and recovery", "Hard/easy contrast"], "80/20 gives this session its role inside the wider distribution. The intervals are specific quality, not an excuse for every surrounding run to become moderately hard.", ["Threshold tolerance", "Pacing discipline", "More useful quality through better recovery"], ["Do not run the recoveries hard.", "Do not add another quality session when easy days have already drifted upward." ]),
        session("session_010", "Aerobic Power Intervals", ["swap"], "micro_007", "Short higher-intensity intervals that develop economical fast movement with quality preserved.", "Train aerobic power and confidence at speed while keeping the session purposeful and recoverable.", AEROBIC_POWER_SESSION_FAMILY, [SessionPart("Warm-up", "20 minutes", "RPE 2-3", "Warm up thoroughly with relaxed drills or strides if useful.", "Use a surface that supports good mechanics."), SessionPart("Intervals", "4-8 x 2-4 minutes", "RPE 8-9", "Run fast enough to require focus but preserve relaxed, coordinated mechanics; recover easily between efforts.", "Flat, smooth terrain is usually best; use a gentle hill only if it improves mechanics."), SessionPart("Cool-down", "15 minutes", "RPE 1-2", "Finish easily and protect the next day.", "Do not add extra fast work because the early repetitions felt easy.")], ["High-quality faster running", "Economy and coordination", "Substantial but bounded recovery cost"], "SWAP makes speed an economy skill and a long-term opportunity, not a punishment. Stop the set when mechanics become forced; the session's value is in quality movement, not squeezing out a final compromised repetition.", ["Aerobic power", "Running economy", "Confidence at faster rhythm"], ["Do not use when fatigue makes mechanics poor.", "Do not stack with heavy downhill or long-run stress." ]),
        session("session_011", "Relaxed Economy Strides", ["swap"], "micro_007", "Brief relaxed accelerations that practise fast economical movement without becoming a hard workout.", "Maintain coordination, rhythm, and confidence at speed with minimal fatigue.", NEUROMUSCULAR_SESSION_FAMILY, [SessionPart("Easy running", "20-45 minutes", "RPE 2-4", "Run easily before the strides.", "Choose flat smooth ground with clear footing."), SessionPart("Strides", "4-8 x 15-25 seconds", "RPE 6-7", "Accelerate smoothly, stay relaxed, and stop each stride before straining; walk or jog fully between repetitions.", "Do not use technical terrain."), SessionPart("Easy finish", "5-10 minutes", "RPE 1-2", "Return to easy movement.", "Skip strides if coordination is poor or the surface is unsafe.")], ["Short coordinated speed", "Low total load", "No lactate-oriented interval target"], "SWAP uses this as playful, purposeful economy practice. The athlete should finish sharper and more confident, not depleted or judged by the exact speed of the strides.", ["Coordination", "Economy", "Fast relaxed mechanics"], ["Do not sprint.", "Do not add strides when soreness or poor mechanics make them forced." ]),
        session("session_012", "Fatigue-Resistance Fartlek", ["swap"], "micro_007", "Variable controlled faster running that asks the athlete to retain economical movement late in an aerobic outing.", "Explore fatigue resistance through pacing, movement quality, and athlete feedback rather than maximal exhaustion.", AEROBIC_POWER_SESSION_FAMILY, [SessionPart("Aerobic lead-in", "25-40 minutes", "RPE 3-4", "Run steadily easy enough to preserve later quality.", "Use rolling or varied terrain only if footing stays safe."), SessionPart("Fartlek", "6-10 x 1-3 minutes", "RPE 7-8", "Insert purposeful faster segments with easy running between them; keep the final repetitions as coordinated as the first.", "Use effort on hills rather than chasing pace."), SessionPart("Easy finish", "10-20 minutes", "RPE 1-2", "Finish easy and note whether form, fueling, or pacing limited the work.", "Reduce terrain complexity if it hides the movement-quality signal.")], ["Economy under accumulated aerobic fatigue", "Variable pacing", "Qualitative feedback"], "SWAP treats fatigue resistance as a question to investigate, not a reason to seek collapse. The runner learns which factors erode movement quality and the coach adjusts future work from that evidence.", ["Late-run movement quality", "Pacing awareness", "Economical speed endurance"], ["Do not turn this into a race simulation.", "Stop if form deteriorates rather than chasing the planned count." ]),
        session("session_013", "Lydiard Hill Circuit", ["lydiard"], "micro_002", "A flowing hill session that bridges aerobic base work toward later faster development.", "Develop hill strength, coordination, and effort judgement as a sequential preparation step.", HILL_POWER_SESSION_FAMILY, [SessionPart("Aerobic warm-up", "20 minutes", "RPE 2-3", "Arrive at the hill relaxed and fully warmed up.", "Use a safe moderate hill with room to descend under control."), SessionPart("Hill circuit", "20-40 minutes", "RPE 5-7", "Use flowing uphill running, controlled downhill movement, and relaxed flat strides according to current readiness; keep the work coordinated rather than maximal.", "Adapt terrain to preserve smooth mechanics, not a historic route."), SessionPart("Easy cool-down", "10-20 minutes", "RPE 1-2", "Finish easy and assess next-day response.", "Reduce descent if it creates disproportionate soreness.")], ["Hill strength bridge", "Feeling-based regulation", "Preparation for later intensity"], "Lydiard gives the hills their sequential role: this is neither generic hill punishment nor race-specific climbing. It builds a stronger platform between the aerobic base and later anaerobic work.", ["Hill strength", "Coordination", "Internal effort judgement"], ["Do not force intensity when recovery is incomplete.", "Do not turn controlled downhill into a damage session." ]),
        session("session_014", "Short Hill Power Repeats", ["lydiard"], "micro_002", "Brief uphill repetitions that reinforce strong coordinated mechanics without replacing the base.", "Add a low-volume hill-strength or neuromuscular stimulus once aerobic work is established.", HILL_POWER_SESSION_FAMILY, [SessionPart("Warm-up", "20 minutes", "RPE 2-3", "Run easily with a few relaxed accelerations.", "Use a safe moderate-to-steep hill with reliable footing."), SessionPart("Short hills", "6-10 x 20-45 seconds", "RPE 7-8", "Run with tall posture and quick controlled steps; walk or jog back fully before the next repetition.", "Stop when mechanics lose spring or coordination."), SessionPart("Cool-down", "10-15 minutes", "RPE 1-2", "Finish easily.", "Avoid adding extra volume solely because the repetitions are short.")], ["Brief hill strength", "Mechanical coordination", "Low total intensity volume"], "Lydiard keeps this in the wider sequence: the session supports a base-trained runner's transition toward later quality, and its dose is regulated by response rather than a compulsory rep count.", ["Uphill mechanics", "Strength and coordination", "Confidence on climbs"], ["Do not use as a substitute for aerobic development.", "Do not sprint on unsafe or technical terrain." ]),
        session("session_015", "Practical Power-Hiking Practice", ["sharman_ultra"], "micro_008", "Purposeful power-hiking practice that teaches a usable ultra movement and pacing decision.", "Develop efficient hiking, gear use where relevant, and judgement about when hiking preserves the event goal better than forced running.", TRAIL_SPECIFIC_SESSION_FAMILY, [SessionPart("Easy approach", "15-20 minutes", "RPE 2-3", "Warm up with easy running or hiking.", "Choose a sustained climb or accessible incline alternative."), SessionPart("Power-hiking sets", "3-6 x 8-15 minutes", "RPE 5-7", "Hike with purposeful posture and sustainable force; practise the transition back to running when relevant.", "Use poles only if they are part of the athlete's goal and practiced safely."), SessionPart("Easy return", "10-20 minutes", "RPE 1-2", "Finish easily and note what made the movement effective or awkward.", "A treadmill or stairs can preserve climbing movement but not outdoor technical skill.")], ["Ultra-relevant movement skill", "Practical pacing judgement", "Accessible terrain alternatives"], "Sharman Ultra makes the session practical and educative. The runner learns when hiking is the efficient event choice and how to adapt the session when the exact course, poles, or terrain are unavailable.", ["Uphill hiking economy", "Transitions", "Course-specific execution confidence"], ["Do not prescribe poles without relevant event need and skill.", "Do not treat hiking as failure to run." ]),
        session("session_016", "Ultra Execution Long Run", ["sharman_ultra"], "micro_008", "A controlled long outing that rehearses one or two practical ultra decisions in the athlete's real context.", "Integrate fitness with pacing, fueling, gear, terrain, or hiking choices without recreating every race demand.", RACE_PRACTICE_SESSION_FAMILY, [SessionPart("Easy opening", "20-30 minutes", "RPE 2-3", "Start conservatively and establish fueling or gear routine early.", "Choose terrain related to the selected execution question."), SessionPart("Execution rehearsal", "90-240 minutes", "RPE 3-6", "Practise the selected decisions deliberately; adjust route, duration, or modality while preserving the main learning goal.", "Use accessible alternatives honestly and record the specificity not practised."), SessionPart("Debrief", "10 minutes", "RPE 1-2", "Review what the athlete learned and how recovery compares with expectation.", "Technical descent and heat may require extra recovery beyond the pace data.")], ["Practical ultra execution", "Athlete-specific adjustment", "Controlled event relevance"], "Sharman Ultra shapes this as coached problem-solving. The session is defined by what the athlete needs to learn for their event and life, not by copying a universal long-run formula.", ["Fueling and pacing practice", "Terrain and gear judgement", "Adaptive execution skill"], ["Do not rehearse every race variable at once.", "Do not force a route that creates unsafe conditions or excessive recovery cost." ]),
        session("session_017", "Race-Simulation Decision Rehearsal", ["sharman_ultra"], "micro_008", "A selective event rehearsal focused on making better decisions under controlled fatigue.", "Practise a limited sequence of event decisions before race day without turning training into a race.", RACE_PRACTICE_SESSION_FAMILY, [SessionPart("Set intention", "5 minutes", "RPE 1", "Choose one decision sequence to rehearse, such as fueling after a climb or pacing before a descent.", "Check conditions and route safety before starting."), SessionPart("Controlled rehearsal", "60-150 minutes", "RPE 3-7", "Execute the selected sequence with planned restraint; collect useful observations rather than chasing a result.", "Use terrain that makes the decision relevant but not needlessly hazardous."), SessionPart("Review", "10 minutes", "RPE 1", "Write the decision, outcome, and the next adjustment.", "Include environmental and terrain factors in the review.")], ["Decision-making under moderate fatigue", "Specific learning", "No full-race requirement"], "Sharman Ultra makes coaching guidance itself part of the workout. The runner learns how to adapt training and racing more effectively, while the coach keeps the rehearsal proportional to the athlete's readiness.", ["Race judgement", "Practical confidence", "Better course-specific choices"], ["Do not use this as a final fitness test.", "Do not pursue race intensity when the learning goal can be reached more safely." ]),
        session("session_018", "Controlled Steady Run", ["80_20_endurance"], "micro_003", "A deliberately selected steady effort that avoids becoming the default intensity of every run.", "Use moderate running only when it has a clear purpose and fits the larger intensity distribution.", THRESHOLD_SESSION_FAMILY, [SessionPart("Warm-up", "15 minutes", "RPE 2-3", "Start easy and establish the difference between easy and steady effort.", "Choose terrain where effort can remain controlled."), SessionPart("Steady segment", "20-50 minutes", "RPE 5-6", "Run at a purposeful sustained effort below threshold; stay even and avoid a late uncontrolled surge.", "On rolling terrain use RPE, power, or breathing rather than pace alone."), SessionPart("Cool-down", "10 minutes", "RPE 1-2", "Return to easy running.", "Keep the following day clearly low intensity.")], ["Selected moderate intensity", "Clear distinction from easy running", "Structured placement"], "80/20 permits steady work when it has a job, but prevents it from becoming the automatic pace of the week. The session must be counted and recovered from as quality, not hidden inside ordinary volume.", ["Sustained controlled output", "Pacing discipline", "Clear intensity awareness"], ["Do not add this when most easy days have become steady.", "Do not use road pace rigidly on trail." ]),
        session("session_020", "Taper Activation Session", ["cts", "lydiard"], "micro_009", "A short event-relevant reminder that preserves sharpness without creating new fatigue.", "Maintain confidence in the target movement and effort while allowing accumulated training to express itself.", NEUROMUSCULAR_SESSION_FAMILY, [SessionPart("Easy warm-up", "15-20 minutes", "RPE 2-3", "Warm up calmly; the goal is readiness, not proof.", "Use familiar safe terrain."), SessionPart("Activation", "4-8 x 30-90 seconds", "RPE 6-7", "Include short controlled event-relevant efforts with full easy recovery; finish wanting more.", "Use terrain related to the goal only if it does not add technical risk or soreness."), SessionPart("Easy finish", "10 minutes", "RPE 1-2", "Finish relaxed and stop before fatigue accumulates.", "Avoid a long downhill or unfamiliar surface." )], ["Low-volume event relevance", "Retained coordination", "Minimal fatigue cost"], "CTS ties the reminder to a real event demand and Lydiard places it at the correct end of the sequence. The session confirms preparation; it does not create last-minute fitness.", ["Freshness", "Event confidence", "Movement sharpness"], ["Do not extend the session because it feels good.", "Do not use it to compensate for missed training." ]),
    ]
    return cards


def main() -> None:
    cards = build_cards()
    validate_pathway_publish_ready(cards)
    if STAGING_DIR.exists():
        shutil.rmtree(STAGING_DIR)
    STAGING_DIR.mkdir(parents=True)
    export_cards_to_json(cards, STAGING_DIR / "cards")
    manifest = build_manifest(cards)
    manifest["library_version"] = "1.0.0"
    manifest["updated_at"] = "2026-08-18"
    display_config = build_display_config()
    write_json(STAGING_DIR / "manifest.json", manifest)
    write_json(STAGING_DIR / "display_config.json", display_config)
    write_library_bundle(STAGING_DIR, cards, manifest, display_config)
    print(f"Built replacement staging library: {len(cards)} cards at {STAGING_DIR}")


if __name__ == "__main__":
    main()
