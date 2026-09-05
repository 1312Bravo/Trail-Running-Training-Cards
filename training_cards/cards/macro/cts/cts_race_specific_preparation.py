from training_cards.philosophy_profiles import CTS
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

cts_race_specific_preparation = MacroCard(
    id = 'macro_022',
    slug = 'cts-race-specific-preparation',
    title = 'CTS Race-Specific Preparation',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [CTS],
    summary = 'An event-demand-led phase that prepares the consequential demands of the target trail or ultra event.',
    purpose = 'Identify and rehearse the event demands most likely to shape performance, safety, and execution.',
    tags = ['cts', 'race_specific', 'event_demands', 'ultrarunning'],
    goal_race_context = [
        'Final substantial preparation phase before a trail or ultra goal.',
        'When event demands such as climbing, descent, heat, altitude, fueling, hiking, or technicality need practice.',
        'When the athlete must learn what the race will ask rather than copy a generic distance plan.',
        'After the main workload and limiter development are adequate for specific work.'
    ],
    training_profile = [
        'The phase begins with the demands and likely limiters of the target event.',
        'Specific work rehearses only consequential demands, not every race detail.',
        'Training uses terrain-appropriate cues such as time, RPE, vertical gain, and recovery cost.',
        'Fueling, equipment, pacing, hiking, and environmental practice are included when they answer a real race question.'
    ],
    expected_adaptations = [
        'Improved readiness for the actual event demands.',
        'Better race-execution decisions under relevant fatigue.',
        'Reduced uncertainty about fueling, pacing, terrain, and logistical choices.'
    ],
    progression_rules = [
        'Progress from partial demand exposure toward more relevant rehearsal only when recovery allows.',
        'Use each rehearsal to answer a specific question and adjust the next one.',
        'Move to mainstream peak and taper when specific demands have been practised enough.'
    ],
    regression_rules = [
        'Return to capacity development if a key limiter blocks useful rehearsal.',
        'Reduce specificity when the recovery cost exceeds the learning value.',
        'Use honest substitutions when direct terrain access is unavailable.'
    ],
    references = [
        CardReference(card_id = 'macro_004', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_021', relationship = CardRelationship.PREVIOUS, tags = ['cts_sequence']),
        CardReference(card_id = 'macro_023', relationship = CardRelationship.ALTERNATIVE, tags = ['race_series'])
    ],
    recommended_duration_weeks = '4-10',
    timing_guidance = [
        'Use when specificity can still be absorbed before the race.',
        'The exact shape should come from event demands, athlete limiters, and access constraints.'
    ],
    watchouts = [
        'Do not make every long run a full dress rehearsal.',
        'Avoid copying race terrain without knowing which demand is being trained.',
        'Do not ignore descent, heat, or travel cost because mileage looks normal.',
        'A rehearsal with no review question is often just extra complexity.'
    ],
    additional_information = 'CTS race-specific preparation starts with the race problem. The coach decides what demands matter most, creates enough exposure to learn and adapt, and avoids using specificity as a disguise for unmanaged fatigue.'
)
