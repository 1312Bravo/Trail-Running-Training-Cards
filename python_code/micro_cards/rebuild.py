from .micro_cards_class import MicroCard

micro_rebuild_easy = MicroCard(
    title="Rebuilding - Easy / Low Aerobic",
    card_id=9001,
    parent_mezzo="Rebuilding",
    
    tags=["Aerobic", "Easy", "Recovery"],
    session_type="Easy Aerobic",
    duration="30-40 min",
    intensity="Low aerobic",
    main_focus=[
        "Reintroduce consistent aerobic training",
        "Maintain relaxed form and rhythm"
    ],
    key_workouts=[
        "Continuous low-intensity aerobic session"
    ],
    guidance=[
        "Keep heart rate low",
        "Focus on smooth breathing and movement"
    ],
    expected_fatigue="Low",
    notes=[
        "Optional 5-10 min warmup and cooldown",
        "Include light mobility work"
    ]
)

micro_rebuild_steady = MicroCard(
    title="Rebuilding - Moderate / Steady Aerobic",
    card_id=9002,
    parent_mezzo="Rebuilding",
    
    tags=["Aerobic", "Moderate"],
    session_type="Steady-State Aerobic",
    duration="35-45 min",
    intensity="Moderate aerobic",
    main_focus=[
        "Introduce slightly higher intensity safely",
        "Improve aerobic efficiency"
    ],
    key_workouts=[
        "Continuous moderate pace 35-45 min"
    ],
    guidance=[
        "Do not exceed moderate aerobic heart rate",
        "Focus on smooth, controlled effort"
    ],
    expected_fatigue="Low to Moderate",
    notes=[
        "Include warmup and cooldown"
    ]
)

micro_rebuild_strides = MicroCard(
    title="Rebuilding - Easy + Strides",
    card_id=9003,
    parent_mezzo="Rebuilding",
    
    tags=["Aerobic", "Strides", "Neuromuscular"],
    session_type="Easy Aerobic with Short Strides",
    duration="30-40 min",
    intensity="Low aerobic with short bursts",
    main_focus=[
        "Maintain aerobic rhythm",
        "Activate neuromuscular system gently"
    ],
    key_workouts=[
        "Easy pace 30-35 min",
        "3-4x20 sec strides with full recovery"
    ],
    guidance=[
        "Strides should feel controlled, not maximal",
        "Keep main session easy"
    ],
    expected_fatigue="Low",
    notes=[
        "Include warmup and cooldown",
        "Focus on smooth acceleration during strides"
    ]
)

micro_rebuild_mobility = MicroCard(
    title="Rebuilding - Mobility & Strength",
    card_id=9004,
    parent_mezzo="Rebuilding",
    
    tags=["Mobility", "Strength", "Recovery"],
    session_type="Mobility & Light Strength",
    duration="30-45 min",
    intensity="Low",
    main_focus=[
        "Restore movement quality and joint health",
        "Maintain functional strength"
    ],
    key_workouts=[
        "Bodyweight exercises, foam rolling, stretching, mobility drills"
    ],
    guidance=[
        "Focus on form over load",
        "Keep intensity low"
    ],
    expected_fatigue="Very Low",
    notes=[
        "Can combine with light aerobic warmup",
        "Avoid heavy resistance this week"
    ]
)

micro_rebuild_rest = MicroCard(
    title="Rebuilding - Recovery / Rest",
    card_id=9005,
    parent_mezzo="Rebuilding",
    
    tags=["Recovery", "Rest"],
    session_type="Rest",
    duration=None,
    intensity=None,
    main_focus=[
        "Allow body to recover",
        "Consolidate adaptations"
    ],
    key_workouts=[
        "Optional gentle mobility or walking"
    ],
    guidance=[
        "Do not perform structured training",
        "Prioritize sleep and nutrition"
    ],
    expected_fatigue="None",
    notes=[
        "Active recovery optional but keep very easy"
    ]
)

REBUILD_MICRO_LIBRARY = [
    micro_rebuild_easy,
    micro_rebuild_steady,
    micro_rebuild_strides,
    micro_rebuild_mobility,
    micro_rebuild_rest
]