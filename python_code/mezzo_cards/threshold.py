from .mezzo_cards_class import MezzoCard

mezzo_threshold_intro = MezzoCard(
    title="Threshold Development - Intro Week",
    card_id=3001,
    parent_macro="Threshold Development",
    week_type="Intro",
    tags=["Threshold", "Intro", "Controlled Intensity"],
    volume_target="80-85% of base peak volume",
    fatigue_risk="Moderate",

    focus=[
        "Introduce threshold intervals in a controlled way.",
        "Maintain aerobic base.",
    ],

    weekly_structure=[
        "4-5 aerobic sessions.",
        "1 threshold interval session.",
        "1 rest day.",
    ],

    key_sessions=[
        "Threshold intervals: 2x10-12 min steady at upper aerobic / lower threshold.",
        "Long aerobic session 90-110 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 70-75%",
        "Threshold: 20-25%",
    ],

    volume_guidance=[
        "Keep total volume stable.",
        "Do not extend threshold duration too long yet.",
    ],

    athlete_feel=[
        "Threshold segments feel controlled but challenging.",
        "Legs slightly heavier than usual aerobic sessions.",
    ],

    progression_logic=[
        "Next → Build Week if threshold adaptation feels manageable.",
    ]
)

mezzo_threshold_stabilization = MezzoCard(
    title="Threshold Development - Stabilization Week",
    card_id=3002,
    parent_macro="Threshold Development",
    week_type="Stabilization",
    tags=["Threshold", "Consistency", "Controlled Volume"],
    volume_target="85-90% of previous week",
    fatigue_risk="Moderate",

    focus=[
        "Solidify threshold adaptation.",
        "Maintain steady aerobic base.",
    ],

    weekly_structure=[
        "4-5 sessions with 1-2 threshold sessions.",
        "1 long aerobic session.",
        "1 rest day.",
    ],

    key_sessions=[
        "Threshold intervals: 2-3x12-15 min steady.",
        "Long aerobic session 100-120 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 65-70%",
        "Threshold: 25-30%",
    ],

    volume_guidance=[
        "Keep weekly volume stable.",
    ],

    athlete_feel=[
        "Sustained fatigue manageable.",
        "Threshold pacing feels smoother.",
    ],

    progression_logic=[
        "Next → Build / Peak Week if athlete handles threshold sessions well.",
    ]
)

mezzo_threshold_build = MezzoCard(
    title="Threshold Development - Build Week",
    card_id=3003,
    parent_macro="Threshold Development",
    week_type="Build",
    tags=["Threshold", "Volume", "Overload"],
    volume_target="90-100% of previous week",
    fatigue_risk="Moderate to High",

    focus=[
        "Increase duration and intensity of threshold efforts.",
        "Improve sustainable pace at threshold.",
    ],

    weekly_structure=[
        "5 aerobic sessions with 2 threshold sessions.",
        "1 long aerobic session.",
        "1 rest day.",
    ],

    key_sessions=[
        "Threshold intervals: 3x12-18 min steady at threshold.",
        "Long aerobic session 100-130 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 60-65%",
        "Threshold: 35-40%",
    ],

    volume_guidance=[
        "Progress threshold duration gradually.",
        "Monitor cumulative fatigue carefully.",
    ],

    athlete_feel=[
        "Leg heaviness accumulates by midweek.",
        "Threshold sessions feel challenging but sustainable.",
    ],

    progression_logic=[
        "Next → Peak Week for maximal sustainable threshold volume.",
    ]
)

mezzo_threshold_peak = MezzoCard(
    title="Threshold Development - Peak Week",
    card_id=3004,
    parent_macro="Threshold Development",
    week_type="Peak",
    tags=["Threshold", "High Load", "Durability"],
    volume_target="100-105% of previous week",
    fatigue_risk="High",

    focus=[
        "Maximize threshold volume and intensity safely.",
        "Prepare athlete for VO₂max or race block.",
    ],

    weekly_structure=[
        "5-6 sessions including 2-3 threshold sessions.",
        "1 long aerobic session.",
        "1 rest day.",
    ],

    key_sessions=[
        "Threshold intervals: 3x15-20 min steady at threshold.",
        "Long aerobic session 120-140 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 55-60%",
        "Threshold: 40-45%",
    ],

    volume_guidance=[
        "Highest threshold load of macro.",
        "Deload next week mandatory.",
    ],

    athlete_feel=[
        "High cumulative fatigue.",
        "Threshold pacing increasingly sustainable with practice.",
    ],

    progression_logic=[
        "Next → Deload Week or VO₂max Bridge Week.",
    ]
)

mezzo_threshold_deload = MezzoCard(
    title="Threshold Development - Deload Week",
    card_id=3005,
    parent_macro="Threshold Development",
    week_type="Deload",
    tags=["Recovery", "Regeneration"],
    volume_target="70-80% of previous peak",
    fatigue_risk="Low",

    focus=[
        "Reduce cumulative fatigue.",
        "Consolidate threshold adaptations.",
    ],

    weekly_structure=[
        "3-4 short aerobic sessions.",
        "1 threshold session reduced volume.",
        "2 rest days.",
    ],

    key_sessions=[
        "Threshold interval: 2x8-10 min",
        "Short aerobic session 40-60 min",
    ],

    intensity_distribution=[
        "Low aerobic: 75-80%",
        "Threshold: 20-25%",
    ],

    volume_guidance=[
        "Reduce overall volume 20-30%.",
    ],

    athlete_feel=[
        "Noticeably fresher by week's end.",
    ],

    progression_logic=[
        "Next → VO₂max Development or repeat Threshold cycle.",
    ]
)

mezzo_threshold_vo2_bridge = MezzoCard(
    title="Threshold Development - VO₂max Bridge Week",
    card_id=3006,
    parent_macro="Threshold Development",
    week_type="Bridge",
    tags=["VO₂max Prep", "Intensity Transition"],
    volume_target="85-95% of previous peak",
    fatigue_risk="Moderate",

    focus=[
        "Introduce short VO₂max intervals.",
        "Maintain threshold volume.",
        "Prepare athlete for next macro.",
    ],

    weekly_structure=[
        "4-5 sessions including 1 threshold + 1 VO₂max session.",
        "1 long aerobic session.",
        "1 rest day.",
    ],

    key_sessions=[
        "VO₂max intervals: 6x2-3 min at VO₂max with full recovery",
        "Threshold session: 2x12-15 min steady",
    ],

    intensity_distribution=[
        "Low aerobic: 60-65%",
        "Threshold: 25-30%",
        "VO₂max: 10-15%",
    ],

    volume_guidance=[
        "Do not increase total volume beyond threshold peak.",
        "Focus on quality VO₂max execution.",
    ],

    athlete_feel=[
        "Threshold feels easier relative to VO₂max spikes.",
        "Legs recover faster from short VO₂max efforts.",
    ],

    progression_logic=[
        "Next → VO₂max Development Macro.",
    ]
)


# -------------------------------------------------------
# Threshold Macro Mezzo Library
# -------------------------------------------------------

THRESHOLD_MEZZO_LIBRARY = [
    mezzo_threshold_intro,
    mezzo_threshold_stabilization,
    mezzo_threshold_build,
    mezzo_threshold_peak,
    mezzo_threshold_deload,
    mezzo_threshold_vo2_bridge,
]