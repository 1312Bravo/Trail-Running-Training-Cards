from training_cards.philosophy_profiles import EVOKE_ENDURANCE
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

evoke_race_specific_preparation = MacroCard(
    id = 'macro_026',
    slug = 'evoke-race-specific-preparation',
    title = 'Evoke Race-Specific Preparation',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [EVOKE_ENDURANCE],
    summary = 'A utilisation phase that combines developed capacities in increasingly objective-like mountain work.',
    purpose = 'Prepare the athlete to use aerobic capacity, strength reserve, muscular endurance, and skill in the goal context.',
    tags = ['evoke', 'race_specific', 'utilisation', 'mountain_endurance'],
    goal_race_context = [
        'Late in preparation for a mountain or climbing-heavy running objective.',
        'When the athlete has developed enough capacity to practise using it together.',
        'When terrain, duration, hiking, gear, fueling, or pacing must be integrated.',
        'Before taper, once capacity training needs to become objective rehearsal.'
    ],
    training_profile = [
        'Specific work combines multiple developed capacities rather than replacing missing ones.',
        'Sessions may integrate climbing, hiking, duration, fueling, terrain, equipment, and pacing.',
        'The phase distinguishes utilisation from capacity training.',
        'Recovery cost determines whether the rehearsal was useful enough to repeat or progress.'
    ],
    expected_adaptations = [
        'Improved ability to use developed capacities on goal-relevant terrain.',
        'Better confidence and pacing judgement under mountain-specific fatigue.',
        'Clearer readiness for taper and the objective itself.'
    ],
    progression_rules = [
        'Progress from partial utilisation toward more objective-like rehearsals.',
        'Add complexity only when the athlete can absorb the previous version.',
        'Move to mainstream peak and taper when utilisation is practised and freshness is the priority.'
    ],
    regression_rules = [
        'Return to capacity development if a missing layer limits the rehearsal.',
        'Reduce duration, grade, load, descent, or technicality if recovery cost is disproportionate.',
        'Use honest substitutions when ideal mountain access is unavailable.'
    ],
    references = [
        CardReference(card_id = 'macro_004', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_025', relationship = CardRelationship.PREVIOUS, tags = ['evoke_layering']),
        CardReference(card_id = 'macro_005', relationship = CardRelationship.NEXT, tags = ['taper'])
    ],
    recommended_duration_weeks = '3-8',
    timing_guidance = [
        'Use after the needed layers are sufficiently developed.',
        'Do not start utilisation so early that it becomes repeated race simulation without prerequisites.'
    ],
    watchouts = [
        'Do not mistake event-like difficulty for readiness.',
        'Avoid full simulations that cost more than they teach.',
        'Do not hide missing capacity behind gear, motivation, or terrain selection.',
        'If recovery collapses, the rehearsal is too advanced or too late.'
    ],
    additional_information = 'Evoke race-specific preparation asks the mountain-endurance question directly: can the athlete use the capacities they have built, on terrain and under conditions that resemble the objective enough to matter?'
)
