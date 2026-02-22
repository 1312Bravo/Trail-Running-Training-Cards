from .macro_cards_class import MacroCard

macro_rebuild = MacroCard(
    title="Rebuild",
    card_id=1,

    tags = [
        "Aerobic",
        "Base Building",
        "Recovery",
        "Foundation",
    ],

    level = "All levels",
    recommended_duration = "2-3 weeks",

    primary_focus=[
        "Rebuilding the fitness after a period of reduced training or detraining.",
        "Restoring lost fitness and building a general endurance foundation for future training.",
    ],

    primary_focus_summary="Safely restore endurance, recondition muscles, and rebuild consistency in training.",

    adaptations=[
        "Restore aerobic endurance safely and progressively.",
        "Recondition muscles, tendons, and connective tissue to handle training load.",
        "Re-establish neuromuscular coordination and economy.",
        "Rebuild mental confidence and consistency in training.",
        "Lay a foundation for future volume and intensity progression.",
    ],

    training_types=[
        "Mostly easy to moderate aerobic sessions, focusing on efficient movement.",
        "Shorter sessions, focus on technique, cadence, and efficient movement patterns.",
        "Gradual increase in weekly training volume, introducing higher loads progressively.",
        "Optional low-impact cross-training to maintain aerobic stimulus without overloading the body.",
        "No high-intensity sessions; focus is on building endurance capacity, not speed.",
    ],

    expectations=[
        "Sessions may feel easy but controlled, early fatigue is normal as the body adapts.",
        "Noticeable improvements in endurance, tissue resilience, and confidence.",
        "Mental benefit: reduces fear of losing general fitness after a break.",
    ],
    
    when_to_choose=[
        "Athletes returning from injury, illness, or long breaks, seeking structured reintroduction to consistent training.",
        "Ideal off-season or post-recovery, before more demanding Macro cycles.",
    ],

    when_to_choose_summary="Use after injury, illness, or long breaks to reintroduce structured training before higher-intensity blocks.",

    next_mezzo_options=[
        "Repeat this macro cycle with slightly higher load if needed to further rebuild fitness and confidence.",
        "Base Endurance Block (restore volume and consolidate aerobic foundation).",
        "Threshold Development Block (if aerobic base is sufficient and athlete is ready to reintroduce intensity - higher level athletes).",
    ]

)