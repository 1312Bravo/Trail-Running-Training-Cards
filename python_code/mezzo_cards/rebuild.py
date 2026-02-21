from .mezzo_cards_class import MezzoCard

mezzo_rebuild_intro = MezzoCard(
    title="Rebuilding - Intro Week",
    card_id=1001,
    parent_macro="Rebuilding",
    week_type="Intro",
    tags=["Return", "Low Stress", "Consistency"],
    volume_target="50-60% of previous peak",
    fatigue_risk="Low",

    focus=[
        "Restore routine and frequency.",
        "Avoid fatigue accumulation.",
        "Re-establish aerobic rhythm.",
    ],

    weekly_structure=[
        "3-4 short aerobic sessions.",
        "2 rest days.",
        "Optional light mobility or core work.",
    ],

    key_sessions=[
        "All sessions easy, conversational pace.",
        "Longest session 45-60 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 100%",
    ],

    volume_guidance=[
        "Do not add intensity or extend duration.",
        "Focus on consistency and habit.",
    ],

    athlete_feel=[
        "Sessions feel easy.",
        "Energy gradually improves.",
    ],

    progression_logic=[
        "If recovery smooth → move to Build Week.",
        "If fatigue persists → repeat Intro.",
    ]
)

mezzo_rebuild_stabilization = MezzoCard(
    title="Rebuilding - Stabilization Week",
    card_id=1002,
    parent_macro="Rebuilding",
    week_type="Stabilization",
    tags=["Consistency", "Low Intensity", "Adaptation"],
    volume_target="60-70% of previous peak",
    fatigue_risk="Low to Moderate",

    focus=[
        "Maintain low-level aerobic activity.",
        "Rebuild muscular endurance slowly.",
        "Prepare for gradual volume increase.",
    ],

    weekly_structure=[
        "4 short aerobic sessions.",
        "1 moderate long session.",
        "2 rest days.",
    ],

    key_sessions=[
        "Long session 60-75 min.",
        "Optional 10-15 min steady segment.",
    ],

    intensity_distribution=[
        "Low aerobic: 100%",
    ],

    volume_guidance=[
        "Keep volume stable or slightly increase (~5%).",
    ],

    athlete_feel=[
        "Legs feel fresh but active.",
        "Fatigue minimal.",
    ],

    progression_logic=[
        "Next → Build Week if adaptation stable.",
    ]
)

mezzo_rebuild_build = MezzoCard(
    title="Rebuilding - Build Week",
    card_id=1003,
    parent_macro="Rebuilding",
    week_type="Build",
    tags=["Gradual Volume", "Low Intensity", "Durability"],
    volume_target="65-80% of previous peak",
    fatigue_risk="Moderate",

    focus=[
        "Increase aerobic duration slightly.",
        "Improve general endurance.",
    ],

    weekly_structure=[
        "4-5 aerobic sessions.",
        "1 long session (progressive duration).",
        "1-2 rest days.",
    ],

    key_sessions=[
        "Long session 75-90 min.",
        "Optional 2x10 min steady segments.",
    ],

    intensity_distribution=[
        "Low aerobic: 95-100%",
    ],

    volume_guidance=[
        "Increase total weekly volume 5-10% if adaptation is stable.",
    ],

    athlete_feel=[
        "Slight fatigue accumulation.",
        "Legs may feel heavier than breathlessness.",
    ],

    progression_logic=[
        "Next → Peak Week or Stabilization Week based on recovery.",
    ]
)

mezzo_rebuild_peak = MezzoCard(
    title="Rebuilding - Peak Week",
    card_id=1004,
    parent_macro="Rebuilding",
    week_type="Peak",
    tags=["High Volume", "Durability Check"],
    volume_target="85-100% of previous peak",
    fatigue_risk="Moderate to High",

    focus=[
        "Reach highest safe volume before deload.",
        "Test aerobic and muscular endurance.",
    ],

    weekly_structure=[
        "5 aerobic sessions.",
        "1 long session 90-120 min.",
        "1 rest day.",
    ],

    key_sessions=[
        "Longest session 90-120 min.",
        "1 moderate aerobic steady session.",
    ],

    intensity_distribution=[
        "Low aerobic: 85-90%",
        "Moderate aerobic: 10-15%",
    ],

    volume_guidance=[
        "Ensure fatigue is manageable.",
        "Next week → Deload mandatory.",
    ],

    athlete_feel=[
        "Noticeable fatigue by end of week.",
        "Leg heaviness more than breathlessness.",
    ],

    progression_logic=[
        "Follow with Deload Week.",
    ]
)

mezzo_rebuild_deload = MezzoCard(
    title="Rebuilding - Deload Week",
    card_id=1005,
    parent_macro="Rebuilding",
    week_type="Deload",
    tags=["Recovery", "Regeneration"],
    volume_target="50-65% of previous peak",
    fatigue_risk="Low",

    focus=[
        "Reduce cumulative fatigue.",
        "Consolidate adaptations.",
        "Prepare for Aerobic Base Macro.",
    ],

    weekly_structure=[
        "3-4 short aerobic sessions.",
        "1 moderate long session.",
        "2 rest days.",
    ],

    key_sessions=[
        "Long session 60-80 min.",
        "Optional short mobility or stride work.",
    ],

    intensity_distribution=[
        "Low aerobic: 90-95%",
    ],

    volume_guidance=[
        "Reduce weekly volume 20-30%.",
    ],

    athlete_feel=[
        "Feel fresher by week's end.",
        "Leg heaviness reduced.",
    ],

    progression_logic=[
        "After deload → move to Aerobic Base Development or repeat Rebuilding if needed.",
    ]
)

REBUILD_MEZZO_LIBRARY = [
    mezzo_rebuild_intro,
    mezzo_rebuild_stabilization,
    mezzo_rebuild_build,
    mezzo_rebuild_peak,
    mezzo_rebuild_deload,
]