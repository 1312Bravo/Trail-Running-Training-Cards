from training_cards.philosophy_profiles import ENDURANCE_80_20
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

endurance_80_20_maintenance = MacroCard(
    id = 'macro_015',
    slug = '80-20-maintenance',
    title = '80/20 Maintenance',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [ENDURANCE_80_20],
    summary = 'A low-cost holding phase built around easy-volume discipline and small purposeful quality touches.',
    purpose = 'Preserve useful fitness without letting constrained training become unplanned moderate effort.',
    tags = ['80_20', 'maintenance', 'low_cost', 'easy_discipline'],
    goal_race_context = [
        'Between goals, during busy life periods, or when a full build is not appropriate.',
        'When the athlete wants structure but not progressive overload.',
        'When limited time tempts every run to become moderately hard.',
        'When trail qualities should be touched without creating race-preparation load.'
    ],
    training_profile = [
        'Most training remains low intensity and low enough cost to repeat.',
        'Small intensity touches preserve readiness when recovery allows.',
        'The phase avoids filling limited time with constant steady running.',
        'Trail exposure is chosen to maintain familiarity, not create hidden fatigue.'
    ],
    expected_adaptations = [
        'Preserved aerobic rhythm and basic performance readiness.',
        'Reduced loss of hard/easy discipline during constrained periods.',
        'Better transition into a later base or capacity phase.'
    ],
    progression_rules = [
        'Progress to base development when time and readiness allow a real build.',
        'Keep quality touches small and purposeful rather than frequent.',
        'Review whether limited training is still low cost enough to be sustainable.'
    ],
    regression_rules = [
        'Remove quality touches if life stress or fatigue rises.',
        'Use return-to-consistency if routine becomes unreliable.',
        'Use off-season if the athlete needs decompression rather than maintenance.'
    ],
    references = [
        CardReference(card_id = 'macro_009', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_010', relationship = CardRelationship.NEXT, tags = ['resume_80_20_build']),
        CardReference(card_id = 'macro_014', relationship = CardRelationship.ALTERNATIVE, tags = ['race_season'])
    ],
    recommended_duration_weeks = '2-12+',
    timing_guidance = [
        'Use when preserving fitness is smarter than pushing adaptation.',
        'The ratio should reduce decision noise, not create stress during an already constrained phase.'
    ],
    watchouts = [
        'Do not make every short run moderately hard because time is limited.',
        'Avoid pretending a maintenance phase is a hidden build.',
        'Do not keep intensity touches when recovery is poor.',
        'If easy discipline becomes mentally exhausting, simplify the structure.'
    ],
    additional_information = '80/20 maintenance is useful because it gives constrained training a clear shape: mostly easy, occasionally purposeful, and intentionally low cost. It keeps the athlete ready without making every available minute carry too much stress.'
)
