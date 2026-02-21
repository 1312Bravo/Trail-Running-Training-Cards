from .mezzo_cards_class import MezzoCard

mezzo_taper_sharpen_intro = MezzoCard(
    title="Race Preparation - Sharpening Intro Week",
    card_id=5000,
    parent_macro="Race Preparation & Taper",
    week_type="Intro",
    tags=["Sharpening", "Controlled Intensity"],
    volume_target="85-90% of peak training volume",
    fatigue_risk="Moderate",

    focus=[
        "Introduce race-specific intensity.",
        "Maintain aerobic support volume.",
        "Avoid excessive fatigue accumulation.",
    ],

    weekly_structure=[
        "2 quality sessions.",
        "3-4 aerobic sessions.",
        "1 rest day.",
    ],

    key_sessions=[
        "3x8-10 min at race pace.",
        "VO2 sharpening 5-6x2 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 65-70%",
        "Race pace / Threshold: 20-25%",
        "VO2: 5-10%",
    ],

    volume_guidance=[
        "Maintain high but controlled volume.",
        "Do not extend long session excessively.",
    ],

    athlete_feel=[
        "Sharp but manageable fatigue.",
        "Intensity feels reintroduced.",
    ],

    progression_logic=[
        "Progress to Specific Sharpening Week.",
    ]
)

mezzo_taper_simulation = MezzoCard(
    title="Race Preparation - Simulation Week",
    card_id=5002,
    parent_macro="Race Preparation & Taper",
    week_type="Specific Emphasis",
    tags=["Race Simulation", "Pacing Practice"],
    volume_target="85-95% of peak volume",
    fatigue_risk="Moderate to High",

    focus=[
        "Practice race pacing.",
        "Build psychological confidence.",
        "Stress race-specific systems.",
    ],

    weekly_structure=[
        "1 race simulation session.",
        "1 short VO2 sharpening session.",
        "3 aerobic sessions.",
        "1 rest day.",
    ],

    key_sessions=[
        "Continuous race pace effort 20-40 min.",
        "Short VO2 6x2 min.",
    ],

    intensity_distribution=[
        "Low aerobic: 60-65%",
        "Race pace: 25-30%",
        "VO2: 5-10%",
    ],

    volume_guidance=[
        "Keep total volume stable.",
        "Avoid stacking intensity days.",
    ],

    athlete_feel=[
        "High quality fatigue.",
        "Confidence building week.",
    ],

    progression_logic=[
        "After 1-2 weeks → move to Volume Reduction Phase 1.",
    ]
)

mezzo_taper_phase1 = MezzoCard(
    title="Race Preparation - Taper Phase 1",
    card_id=5003,
    parent_macro="Race Preparation & Taper",
    week_type="Volume Reduction",
    tags=["Taper", "Freshness Build"],
    volume_target="75-85% of normal volume",
    fatigue_risk="Low to Moderate",

    focus=[
        "Reduce cumulative fatigue.",
        "Maintain intensity exposure.",
    ],

    weekly_structure=[
        "1 race pace session.",
        "1 short sharpening session.",
        "3 short aerobic sessions.",
        "1-2 rest days.",
    ],

    key_sessions=[
        "2x12-15 min race pace.",
        "6x1 min fast but relaxed.",
    ],

    intensity_distribution=[
        "Low aerobic: 70-75%",
        "Race pace: 20-25%",
    ],

    volume_guidance=[
        "Reduce weekly volume by ~15-20%.",
        "Keep intensity duration shorter.",
    ],

    athlete_feel=[
        "Fatigue decreasing.",
        "Legs beginning to feel lighter.",
    ],

    progression_logic=[
        "Progress to Final Taper Week.",
    ]
)

mezzo_race_taper = MezzoCard(
    title="Race Preparation - Final Taper Week",
    card_id=5001,
    parent_macro="Race Preparation & Taper",
    week_type="Taper",
    tags=["Peak", "Freshness"],
    volume_target="60-70% normal volume",
    fatigue_risk="Low",

    focus=[
        "Maximize freshness.",
        "Maintain neuromuscular sharpness.",
    ],

    weekly_structure=[
        "1 race pace session.",
        "1 short sharpening session.",
        "2-3 short aerobic sessions.",
        "2 rest days.",
    ],

    key_sessions=[
        "2x8-12 min race pace.",
        "6x1 min sharp efforts.",
    ],

    intensity_distribution=[
        "Low aerobic: 75-80%",
        "Race pace: 15-20%",
    ],

    volume_guidance=[
        "Reduce volume 30-40%.",
        "Avoid any session inducing soreness.",
    ],

    athlete_feel=[
        "Increasing freshness.",
        "Slight restlessness possible.",
    ],

    progression_logic=[
        "Race at end of week.",
    ]
)

mezzo_taper_micro_taper = MezzoCard(
    title="Race Preparation - Micro Taper",
    card_id=5004,
    parent_macro="Race Preparation & Taper",
    week_type="Micro",
    tags=["Short Taper", "Maintenance"],
    volume_target="70-80% of normal volume",
    fatigue_risk="Low",

    focus=[
        "Short taper for secondary race.",
        "Maintain rhythm.",
    ],

    weekly_structure=[
        "1 short race pace session.",
        "2 short aerobic sessions.",
        "1-2 rest days.",
    ],

    key_sessions=[
        "1x15-20 min race pace.",
        "4x1 min sharpening efforts.",
    ],

    intensity_distribution=[
        "Low aerobic: 70-75%",
        "Race pace: 20-25%",
    ],

    volume_guidance=[
        "Reduce volume slightly.",
        "Do not fully unload.",
    ],

    athlete_feel=[
        "Sharp but not fully rested.",
    ],

    progression_logic=[
        "Race mid-week or weekend.",
    ]
)