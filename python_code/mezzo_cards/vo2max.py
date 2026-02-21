from .mezzo_cards_class import MezzoCard

mezzo_vo2_intro = MezzoCard(
    title="VO₂max Development - Intro Week",
    card_id=4001,
    parent_macro="VO₂max Development",
    week_type="Intro",
    tags=["VO₂max", "Intro", "High Intensity"],
    volume_target="75-85% of threshold peak volume",
    fatigue_risk="Moderate",

    focus=[
        "Introduce short VO₂max intervals with full recovery.",
        "Maintain threshold base volume.",
        "Prepare neuromuscular system for high intensity.",
    ],

    weekly_structure=[
        "4 aerobic sessions.",
        "1 short VO₂max session.",
        "1 long aerobic session.",
        "1 rest day.",
    ],

    key_sessions=[
        "VO₂max intervals: 5-6x2 min at VO₂max intensity, full recovery.",
        "Long aerobic session 90-110 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 65-70%",
        "Threshold: 20-25%",
        "VO₂max: 10-15%",
    ],

    volume_guidance=[
        "Do not exceed previous threshold peak volume.",
        "Focus on interval quality.",
    ],

    athlete_feel=[
        "Short high-intensity efforts feel sharp.",
        "Legs recover well between intervals.",
    ],

    progression_logic=[
        "Next → Stabilization Week to handle VO₂max load safely.",
    ]
)

mezzo_vo2_stabilization = MezzoCard(
    title="VO₂max Development - Stabilization Week",
    card_id=4002,
    parent_macro="VO₂max Development",
    week_type="Stabilization",
    tags=["VO₂max", "Consistency", "Intensity Management"],
    volume_target="80-90% of previous week",
    fatigue_risk="Moderate",

    focus=[
        "Consolidate VO₂max adaptations.",
        "Maintain threshold and aerobic base.",
    ],

    weekly_structure=[
        "4-5 sessions including 1-2 VO₂max sessions.",
        "1 long aerobic session.",
        "1 rest day.",
    ],

    key_sessions=[
        "VO₂max intervals: 6x2-3 min at high intensity, full recovery.",
        "Threshold session: 2x12-15 min steady.",
    ],

    intensity_distribution=[
        "Low aerobic: 60-65%",
        "Threshold: 20-25%",
        "VO₂max: 15-20%",
    ],

    volume_guidance=[
        "Keep weekly volume stable.",
        "Focus on interval consistency.",
    ],

    athlete_feel=[
        "Short VO₂max efforts feel challenging but manageable.",
        "Recovery between sessions adequate.",
    ],

    progression_logic=[
        "Next → Build Week if athlete adapts well.",
    ]
)

mezzo_vo2_build = MezzoCard(
    title="VO₂max Development - Build Week",
    card_id=4003,
    parent_macro="VO₂max Development",
    week_type="Build",
    tags=["VO₂max", "Volume Increase", "High Intensity"],
    volume_target="90-100% of previous week",
    fatigue_risk="High",

    focus=[
        "Increase VO₂max interval duration or repetitions.",
        "Improve high-intensity endurance and recovery.",
    ],

    weekly_structure=[
        "5 sessions with 2 VO₂max sessions.",
        "1 long aerobic session.",
        "1 rest day.",
    ],

    key_sessions=[
        "VO₂max intervals: 6-8x3 min at VO₂max intensity, full recovery.",
        "Threshold session: 2x15 min steady.",
        "Long aerobic session: 100-130 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 55-60%",
        "Threshold: 25-30%",
        "VO₂max: 15-20%",
    ],

    volume_guidance=[
        "Gradually increase total VO₂max interval duration by 5-10%.",
        "Monitor fatigue carefully.",
    ],

    athlete_feel=[
        "High fatigue accumulation midweek.",
        "VO₂max intervals feel challenging but controlled.",
    ],

    progression_logic=[
        "Next → Peak Week for maximal VO₂max overload.",
    ]
)

mezzo_vo2_peak = MezzoCard(
    title="VO₂max Development - Peak Week",
    card_id=4004,
    parent_macro="VO₂max Development",
    week_type="Peak",
    tags=["VO₂max", "High Load", "Overload"],
    volume_target="100-110% of previous week",
    fatigue_risk="High",

    focus=[
        "Maximize VO₂max interval volume and intensity.",
        "Develop high-intensity fatigue tolerance.",
        "Prepare athlete for final Race Preparation macro.",
    ],

    weekly_structure=[
        "5-6 sessions with 3 VO₂max sessions.",
        "1 long aerobic session.",
        "1 rest day.",
    ],

    key_sessions=[
        "VO₂max intervals: 7-8x3 min high intensity with full recovery.",
        "Threshold session: 2x15-20 min steady.",
        "Long aerobic session: 120-140 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 50-55%",
        "Threshold: 25-30%",
        "VO₂max: 20-25%",
    ],

    volume_guidance=[
        "Highest VO₂max load of macro.",
        "Deload next week mandatory.",
    ],

    athlete_feel=[
        "High cumulative fatigue.",
        "VO₂max efforts feel intense but sustainable.",
    ],

    progression_logic=[
        "Next → Deload Week or Transition to Race Preparation.",
    ]
)

mezzo_vo2_deload = MezzoCard(
    title="VO₂max Development - Deload Week",
    card_id=4005,
    parent_macro="VO₂max Development",
    week_type="Deload",
    tags=["Recovery", "Regeneration"],
    volume_target="65-75% of previous peak",
    fatigue_risk="Low",

    focus=[
        "Reduce accumulated fatigue.",
        "Consolidate VO₂max adaptations.",
        "Prepare for final Race Preparation macro.",
    ],

    weekly_structure=[
        "3-4 short aerobic sessions.",
        "1 reduced VO₂max session.",
        "1 threshold session optional.",
        "2 rest days.",
    ],

    key_sessions=[
        "VO₂max intervals: 4x2 min at moderate intensity",
        "Short aerobic session 40-60 min",
    ],

    intensity_distribution=[
        "Low aerobic: 70-75%",
        "VO₂max: 15-20%",
    ],

    volume_guidance=[
        "Reduce total volume 25-30%.",
    ],

    athlete_feel=[
        "Legs feel lighter, recovery improved.",
    ],

    progression_logic=[
        "Next → Race Preparation & Taper macro.",
    ]
)

mezzo_vo2_race_bridge = MezzoCard(
    title="VO₂max Development - Race Prep Bridge Week",
    card_id=4006,
    parent_macro="VO₂max Development",
    week_type="Bridge",
    tags=["Transition", "Race Prep", "Sharpening"],
    volume_target="80-90% of VO₂max peak volume",
    fatigue_risk="Moderate",

    focus=[
        "Transition from VO₂max overload to race-specific intensity.",
        "Maintain VO₂max adaptations while reducing fatigue.",
        "Introduce race pace simulations.",
    ],

    weekly_structure=[
        "4 sessions including 1 VO₂max + 1 threshold + 1 race pace session",
        "1 long aerobic session",
        "1 rest day",
    ],

    key_sessions=[
        "VO₂max intervals: 4-5x3 min",
        "Threshold session: 2x15 min",
        "Race pace simulation: 20-30 min",
    ],

    intensity_distribution=[
        "Low aerobic: 60-65%",
        "Threshold: 20-25%",
        "VO₂max: 10-15%",
        "Race pace: 10-15%",
    ],

    volume_guidance=[
        "Keep intensity high but reduce total VO₂max load.",
    ],

    athlete_feel=[
        "Fatigue controlled, sharpness increasing.",
    ],

    progression_logic=[
        "Next → Race Preparation & Taper macro.",
    ]
)

VO2MAX_MEZZO_LIBRARY = [
    mezzo_vo2_intro,
    mezzo_vo2_stabilization,
    mezzo_vo2_build,
    mezzo_vo2_peak,
    mezzo_vo2_deload,
    mezzo_vo2_race_bridge,
]