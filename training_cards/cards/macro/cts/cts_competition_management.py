from training_cards.philosophy_profiles import CTS
from training_cards.schemas import CardRelationship, CardReference, CardType, MacroCard, TrainingLevel

cts_competition_management = MacroCard(
    id = 'macro_023',
    slug = 'cts-competition-management',
    title = 'CTS Competition Management',
    card_type = CardType.MACRO,
    suitable_levels = [TrainingLevel.ALL],
    philosophy_profile_ids = [CTS],
    summary = 'A race-season phase that manages each event as both a demand-specific stress and a source of information.',
    purpose = 'Use race stress and race feedback to guide only the work that improves readiness for the next event.',
    tags = ['cts', 'competition', 'race_series', 'event_demands'],
    goal_race_context = [
        'During closely spaced ultras, tune-up races, or race blocks.',
        'When each event has different terrain, duration, and recovery cost.',
        'When between-race training must be chosen from demand and response, not habit.',
        'When the athlete needs to stay ready without adding a full development block.'
    ],
    training_profile = [
        'Race cost is evaluated through total duration, terrain, descent, conditions, travel, and recovery response.',
        'Between-race work is limited to recovery, maintenance, or specific touchpoints that clearly improve readiness.',
        'The plan reviews what each race revealed about pacing, fueling, terrain, and limiter status.',
        "Training density changes according to the next event and the athlete's actual response."
    ],
    expected_adaptations = [
        'Better race-to-race decision-making.',
        'Improved ability to learn from competition without overtraining between events.',
        'More accurate matching of training touchpoints to the next race demand.'
    ],
    progression_rules = [
        'Add between-race stress only when the previous race has been absorbed.',
        "Choose touchpoints that address the next event's likely limiter.",
        'Move to recovery and transition when the race block is complete or fatigue becomes dominant.'
    ],
    regression_rules = [
        'Use recovery only if race cost remains high.',
        'Remove nonessential work when travel, soreness, or life stress reduces adaptability.',
        'Use mainstream competition management if no ultra-specific demand is shaping the gap.'
    ],
    references = [
        CardReference(card_id = 'macro_006', relationship = CardRelationship.ALTERNATIVE, tags = ['same_type_mainstream']),
        CardReference(card_id = 'macro_022', relationship = CardRelationship.ALTERNATIVE, tags = ['single_goal_specificity'])
    ],
    recommended_duration_weeks = '2-12+',
    timing_guidance = [
        'Use only when race timing and race demands materially shape training.',
        'Every between-race decision should answer what the next event requires and what the athlete can absorb.'
    ],
    watchouts = [
        'Do not squeeze a normal build between races that only allow recovery and touchpoints.',
        'Avoid treating all races as equal stress because they share a distance.',
        'Do not ignore what the previous race taught.',
        'If readiness declines race to race, the management phase is too costly.'
    ],
    additional_information = 'CTS competition management is tactical. It treats each race as a stress test of the athlete and the plan, then uses the gap before the next race to make the smallest useful training decision.'
)
