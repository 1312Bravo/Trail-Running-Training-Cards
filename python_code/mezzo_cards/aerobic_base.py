from .mezzo_cards_class import MezzoCard

mezzo_aerobic_base_intro = MezzoCard(
    title="Aerobic Base - Intro Week",
    card_id=2001,
    parent_macro="Aerobic Base Development",
    week_type="Intro",
    tags=["Foundation", "Low Intensity"],
    level="All Levels",
    volume_target="75-85% of peak base volume",
    fatigue_risk="Moderate",

    focus=[
        "Stabilize consistent aerobic volume.",
    ],

    focus_summary="Establish consistent aerobic volume to build a solid endurance foundation.",

    weekly_structure=[
        "4-5 aerobic sessions.",
        "1 long session.",
        "1 rest day.",
    ],

    key_sessions=[
        "Long session 90-120 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 85-90%",
        "Moderate aerobic: 10-15%",
    ],

    volume_guidance=[
        "Slight increase only if adapting well.",
    ],

    athlete_feel=[
        "Manageable fatigue.",
    ],

    progression_logic=[
        "Move to Build Week if stable.",
    ]
)

mezzo_base_stabilization = MezzoCard(
    title="Aerobic Base - Stabilization Week",
    card_id=2101,
    parent_macro="Aerobic Base Development",
    week_type="Stabilization",
    tags=["Consistency", "Low Intensity", "Durability"],
    level="All Levels",
    volume_target="80-90% of peak base volume",
    fatigue_risk="Moderate",

    focus=[
        "Stabilize aerobic volume without increasing stress.",
        "Improve aerobic efficiency.",
        "Solidify durability before progression.",
    ],

    focus_summary="Solidify aerobic consistency and efficiency while maintaining manageable weekly load.",

    weekly_structure=[
        "4-5 aerobic sessions.",
        "1 moderate long session.",
        "1 rest day.",
    ],

    key_sessions=[
        "Long aerobic session 90-110 min.",
        "Optional short steady insert 2x8-10 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 85-90%",
        "Moderate aerobic: 10-15%",
    ],

    volume_guidance=[
        "Keep weekly volume stable.",
        "No increases this week.",
    ],

    athlete_feel=[
        "Manageable fatigue.",
        "Smooth aerobic rhythm.",
    ],

    progression_logic=[
        "If feeling strong → move to Volume Progression Week.",
        "If fatigue present → maintain another stabilization week.",
    ]
)

mezzo_base_volume_progression = MezzoCard(
    title="Aerobic Base - Volume Progression Week",
    card_id=2102,
    parent_macro="Aerobic Base Development",
    week_type="Build",
    tags=["Volume Increase", "Durability Expansion"],
    level="All Levels",
    volume_target="90-100% of base volume",
    fatigue_risk="Moderate to High",

    focus=[
        "Increase total weekly aerobic load.",
        "Expand fatigue resistance.",
    ],

    focus_summary="Increase total weekly aerobic load to expand endurance and fatigue resistance.",

    weekly_structure=[
        "5 aerobic sessions.",
        "1 extended long session.",
        "1 rest day.",
    ],

    key_sessions=[
        "Long aerobic session 110-130 min.",
        "1 aerobic steady workout 3x10-12 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 80-85%",
        "Moderate aerobic: 15-20%",
    ],

    volume_guidance=[
        "Increase total weekly volume 5-8%.",
        "Do not increase intensity simultaneously.",
    ],

    athlete_feel=[
        "Cumulative fatigue by end of week.",
        "Leg heaviness more than breathlessness.",
    ],

    progression_logic=[
        "After 1-2 progression weeks → insert Deload Week.",
    ]
)

mezzo_base_long_emphasis = MezzoCard(
    title="Aerobic Base - Long Session Emphasis Week",
    card_id=2103,
    parent_macro="Aerobic Base Development",
    week_type="Specific Emphasis",
    tags=["Long Session", "Endurance Capacity"],
    level="All Levels",
    volume_target="95-105% of base volume",
    fatigue_risk="High",

    focus=[
        "Extend long-duration endurance.",
        "Improve fuel utilization at moderate intensities.",
    ],

    focus_summary="Extend long-duration endurance and improve fuel utilization at moderate intensities.",

    weekly_structure=[
        "4-5 aerobic sessions.",
        "1 very long aerobic session.",
        "1 rest day.",
    ],

    key_sessions=[
        "Long aerobic session 130-160 min.",
        "All other sessions short and easy.",
    ],

    intensity_distribution=[
        "Low aerobic: 90%",
        "Moderate aerobic: 10%",
    ],

    volume_guidance=[
        "Do not add additional intensity.",
        "Next week should reduce volume slightly.",
    ],

    athlete_feel=[
        "Deep muscular fatigue.",
        "Mental endurance challenged.",
    ],

    progression_logic=[
        "Follow with Recovery or Stabilization Week.",
    ]
)

mezzo_base_tempo_intro = MezzoCard(
    title="Aerobic Base - Tempo Introduction Week",
    card_id=2104,
    parent_macro="Aerobic Base Development",
    week_type="Bridge",
    tags=["Tempo", "Upper Aerobic", "Transition"],
    level="All Levels",
    volume_target="90-95% of peak base volume",
    fatigue_risk="Moderate",

    focus=[
        "Introduce controlled upper aerobic intensity.",
        "Prepare for threshold development.",
    ],

    focus_summary="Introduce controlled upper-aerobic intensity to prepare for Threshold development.",

    weekly_structure=[
        "4 aerobic sessions.",
        "1 aerobic tempo session.",
        "1 long aerobic session.",
        "1 rest day.",
    ],

    key_sessions=[
        "Tempo workout 2x15-20 min steady.",
        "Long aerobic session 100-120 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 75-80%",
        "Moderate/Tempo: 20-25%",
    ],

    volume_guidance=[
        "Do not increase total volume this week.",
        "Focus on quality tempo execution.",
    ],

    athlete_feel=[
        "Controlled discomfort during tempo.",
        "Manageable weekly fatigue.",
    ],

    progression_logic=[
        "Next macro option → Threshold Development.",
    ]
)

mezzo_aerobic_base_peak = MezzoCard(
    title="Aerobic Base - Peak Volume Week",
    card_id=2002,
    parent_macro="Aerobic Base Development",
    week_type="Peak",
    tags=["High Volume", "Durability"],
    level="All Levels",
    volume_target="100% peak base volume",
    fatigue_risk="High",

    focus=[
        "Maximize aerobic durability.",
    ],

    focus_summary="Maximize aerobic durability with the highest weekly volume of the macro cycle.",

    weekly_structure=[
        "5 aerobic sessions.",
        "1 long session 120-150 min.",
        "1 rest day.",
    ],

    key_sessions=[
        "Long aerobic session extended.",
        "1 aerobic steady workout.",
    ],

    intensity_distribution=[
        "Low aerobic: 80-85%",
        "Moderate aerobic: 15-20%",
    ],

    volume_guidance=[
        "Highest volume of macro.",
        "Next week must deload.",
    ],

    athlete_feel=[
        "Cumulative fatigue.",
    ],

    progression_logic=[
        "Follow with Deload Week.",
    ]
)

mezzo_base_deload = MezzoCard(
    title="Aerobic Base - Deload Week",
    card_id=2105,
    parent_macro="Aerobic Base Development",
    week_type="Deload",
    tags=["Recovery", "Regeneration"],
    level="All Levels",
    volume_target="65-75% of peak base volume",
    fatigue_risk="Low",

    focus=[
        "Reduce accumulated fatigue.",
        "Consolidate aerobic adaptations.",
    ],

    focus_summary="Reduce accumulated fatigue and consolidate aerobic adaptations for recovery.",

    weekly_structure=[
        "3-4 short aerobic sessions.",
        "1 moderate long session.",
        "2 rest days.",
    ],

    key_sessions=[
        "Long aerobic session 80-100 min.",
        "Optional short strides for neuromuscular freshness.",
    ],

    intensity_distribution=[
        "Low aerobic: 90-95%",
        "Short neuromuscular strides: minimal",
    ],

    volume_guidance=[
        "Reduce total weekly volume 20-30%.",
    ],

    athlete_feel=[
        "Increasing freshness by end of week.",
        "Reduced heaviness.",
    ],

    progression_logic=[
        "After deload → resume Build or move to Threshold Macro.",
    ]
)

AEROBIC_BASE_MEZZO_LIBRARY = [
    mezzo_aerobic_base_intro,
    mezzo_base_stabilization,
    mezzo_base_volume_progression,
    mezzo_base_long_emphasis,
    mezzo_base_tempo_intro,
    mezzo_aerobic_base_peak,
    mezzo_base_deload,
]