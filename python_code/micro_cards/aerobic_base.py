from .micro_cards_class import MicroCard

micro_aerobic_easy = MicroCard(
    title="Aerobic Base - Easy / Low Session",
    card_id=7001,
    parent_mezzo="Aerobic Base",
    tags=["Aerobic", "Easy"],
    session_type="Aerobic Endurance",
    duration="45-60 min",
    intensity="Low aerobic",
    main_focus=[
        "Develop aerobic capacity",
        "Maintain relaxed form and rhythm"
    ],
    key_workouts=[
        "Continuous low-intensity pace"
    ],
    guidance=[
        "Keep heart rate in low aerobic zone",
        "Conversational pace is ideal"
    ],
    expected_fatigue="Low",
    notes=[
        "Optional 5-10 min warmup and cooldown",
        "Include light mobility work"
    ]
)

micro_aerobic_steady = MicroCard(
    title="Aerobic Base - Moderate / Steady-State",
    card_id=7002,
    parent_mezzo="Aerobic Base",
    tags=["Aerobic", "Moderate"],
    session_type="Steady-State Aerobic",
    duration="50-70 min",
    intensity="Moderate aerobic",
    main_focus=[
        "Improve ability to sustain moderate pace",
        "Enhance aerobic efficiency"
    ],
    key_workouts=[
        "Continuous moderate pace 50-70 min",
        "Optional 2x8-10 min slightly harder segments"
    ],
    guidance=[
        "Do not exceed moderate aerobic heart rate",
        "Focus on smooth, controlled effort"
    ],
    expected_fatigue="Moderate",
    notes=[
        "Include warmup and cooldown",
        "Focus on good running or cycling form"
    ]
)

micro_aerobic_long = MicroCard(
    title="Aerobic Base - Long Session",
    card_id=7003,
    parent_mezzo="Aerobic Base",
    tags=["Aerobic", "Endurance", "Long"],
    session_type="Long Duration Aerobic",
    duration="90-150 min",
    intensity="Low to moderate aerobic",
    main_focus=[
        "Increase endurance and fatigue resistance",
        "Accumulate aerobic volume safely"
    ],
    key_workouts=[
        "Continuous long-duration session at low-moderate intensity"
    ],
    guidance=[
        "Keep pace controlled",
        "Fuel and hydrate appropriately"
    ],
    expected_fatigue="Moderate to High",
    notes=[
        "Long sessions can be broken into two segments if needed",
        "Include cooldown and optional light strides at the end"
    ]
)

micro_aerobic_recovery = MicroCard(
    title="Aerobic Base - Recovery / Rest",
    card_id=7004,
    parent_mezzo="Aerobic Base",
    tags=["Recovery", "Rest"],
    session_type="Recovery / Rest",
    duration="N/A",
    intensity="N/A",
    main_focus=[
        "Allow physical and mental recovery",
        "Consolidate adaptations"
    ],
    key_workouts=[
        "Optional light activity: walking, easy cycling, or mobility"
    ],
    guidance=[
        "No structured training",
        "Focus on hydration, nutrition, and sleep"
    ],
    expected_fatigue="None",
    notes=[
        "Active recovery can include yoga or gentle stretching",
        "Keep effort very light if moving"
    ]
)

micro_aerobic_strides = MicroCard(
    title="Aerobic Base - Easy + Strides",
    card_id=7005,
    parent_mezzo="Aerobic Base",
    tags=["Aerobic", "Strides", "Neuromuscular"],
    session_type="Aerobic Endurance with Strides",
    duration="50-65 min",
    intensity="Low aerobic with short bursts",
    main_focus=[
        "Maintain aerobic rhythm",
        "Activate neuromuscular system"
    ],
    key_workouts=[
        "Continuous easy pace 45-50 min",
        "4-6x20 sec strides with full recovery"
    ],
    guidance=[
        "Keep main session easy",
        "Strides should feel sharp but controlled"
    ],
    expected_fatigue="Low",
    notes=[
        "Include warmup and cooldown 5-10 min",
        "Focus on form and smooth acceleration during strides"
    ]
)

AEROBIC_BASE_MICRO_LIBRARY = [
    micro_aerobic_easy,
    micro_aerobic_steady,
    micro_aerobic_long,
    micro_aerobic_recovery,
    micro_aerobic_strides
]