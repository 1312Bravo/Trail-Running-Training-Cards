from training_cards.philosophy_profiles import EVOKE_ENDURANCE
from training_cards.schemas import CardRelationship, CardReference, CardType, MezzoCard, TrainingLevel


def _parent(macro_id: str, tag: str) -> list[CardReference]:
    return [CardReference(card_id=macro_id, relationship=CardRelationship.PARENT, tags=[tag])]


def _card(
    *,
    id: str,
    slug: str,
    title: str,
    parent_macro_id: str,
    parent_tag: str,
    summary: str,
    purpose: str,
    tags: list[str],
    training_profile: list[str],
    expected_adaptations: list[str],
    progression_rules: list[str],
    regression_rules: list[str],
    watchouts: list[str],
    placement_guidance: list[str],
    additional_information: str,
) -> MezzoCard:
    return MezzoCard(
        id=id,
        slug=slug,
        title=title,
        card_type=CardType.MEZZO,
        suitable_levels=[TrainingLevel.ALL],
        philosophy_profile_ids=[EVOKE_ENDURANCE],
        summary=summary,
        purpose=purpose,
        tags=["evoke_endurance", "mezzo", *tags],
        goal_race_context=[
            "Use when the Evoke layer model changes the block structure.",
            "Most useful for mountain or trail athletes whose limiters involve aerobic capacity, strength reserve, muscular endurance, or objective-specific utilisation.",
        ],
        training_profile=training_profile,
        expected_adaptations=expected_adaptations,
        progression_rules=progression_rules,
        regression_rules=regression_rules,
        references=_parent(parent_macro_id, parent_tag),
        recommended_duration_weeks="2-6",
        placement_guidance=placement_guidance,
        watchouts=watchouts,
        additional_information=additional_information,
    )


evoke_layer_absorption_recovery_block = _card(
    id="mezzo_055",
    slug="evoke-layer-absorption-recovery-block",
    title="Evoke Layer Absorption Recovery Block",
    parent_macro_id="macro_007",
    parent_tag="recovery_transition",
    summary="A recovery block that absorbs high-cost mountain or muscular-endurance layers before more work.",
    purpose="Let local muscular and connective-tissue stress settle before progressing the Evoke layer sequence.",
    tags=["recovery", "absorption", "layer_model"],
    training_profile=[
        "Load is reduced enough that local soreness, heaviness, and movement quality can normalize.",
        "Aerobic work remains low cost and does not compete with tissue recovery.",
        "The coach watches local muscular fatigue as closely as cardiovascular freshness.",
    ],
    expected_adaptations=[
        "Better absorption of muscular-endurance or mountain-specific stress.",
        "Clearer readiness for the next layer.",
        "Lower risk of compounding local damage.",
    ],
    progression_rules=[
        "Progress only after soreness, power, and easy-run mechanics normalize.",
        "Use simple aerobic work before returning to force-heavy sessions.",
        "Keep the next layer smaller if recovery took longer than expected.",
    ],
    regression_rules=[
        "Extend recovery if downhill soreness or uphill heaviness persists.",
        "Remove intensity when local tissue response remains the limiter.",
    ],
    watchouts=[
        "Do not judge readiness from heart rate alone.",
        "Avoid adding muscular endurance while the athlete still feels locally damaged.",
    ],
    placement_guidance=[
        "Place after muscular-endurance or high-cost mountain blocks.",
        "Use before returning to base, capacity, or race-specific utilisation work.",
    ],
    additional_information="Evoke-style mountain work can leave the heart ready before the legs are ready. This card makes that mismatch visible.",
)


evoke_aerobic_capacity_development_block = _card(
    id="mezzo_056",
    slug="evoke-aerobic-capacity-development-block",
    title="Evoke Aerobic Capacity Development Block",
    parent_macro_id="macro_024",
    parent_tag="evoke_base",
    summary="A base block that builds substantial aerobic capacity before specialised mountain layers.",
    purpose="Develop the aerobic engine that later strength reserve, muscular endurance, and utilisation work depend on.",
    tags=["base", "aerobic_capacity", "layer_model"],
    training_profile=[
        "Aerobic volume is progressed with attention to sustainable intensity and terrain cost.",
        "Most work supports capacity rather than early race simulation.",
        "Threshold control and durability are watched so the athlete does not build capacity on chronic strain.",
    ],
    expected_adaptations=[
        "Greater aerobic capacity.",
        "Better readiness for strength-reserve and muscular-endurance layers.",
        "Improved ability to handle longer mountain objectives later.",
    ],
    progression_rules=[
        "Progress volume or vertical only when aerobic control remains stable.",
        "Use enough low-intensity work to build capacity without drifting upward.",
        "Move to specialised layers only once base durability is credible.",
    ],
    regression_rules=[
        "Reduce volume if aerobic work becomes forced or threshold-adjacent too often.",
        "Simplify terrain if climbing cost prevents stable aerobic development.",
    ],
    watchouts=[
        "Do not skip capacity because muscular endurance looks more specific.",
        "Avoid building on a weak aerobic base just because the athlete is strong.",
    ],
    placement_guidance=[
        "Place early in Evoke base development.",
        "Use before strength reserve or uphill muscular-endurance development.",
    ],
    additional_information="The layer logic starts here: specific mountain power is more useful when it sits on a real aerobic platform.",
)


evoke_strength_reserve_support_block = _card(
    id="mezzo_057",
    slug="evoke-strength-reserve-support-block",
    title="Evoke Strength Reserve Support Block",
    parent_macro_id="macro_024",
    parent_tag="evoke_base",
    summary="A support block that develops strength reserve for later muscular-endurance and mountain work.",
    purpose="Build enough general and hill-relevant strength that later specific force work can be absorbed.",
    tags=["base", "strength_reserve", "support"],
    training_profile=[
        "Strength work supports running and mountain readiness without overwhelming aerobic development.",
        "Exercises target useful reserve, control, and tissue tolerance rather than gym fatigue for its own sake.",
        "The athlete should leave strength work better prepared for future hills, not too sore to train.",
    ],
    expected_adaptations=[
        "Improved strength reserve.",
        "Better tolerance for uphill muscular-endurance work.",
        "More robust movement under fatigue.",
    ],
    progression_rules=[
        "Progress load or complexity only while running quality remains intact.",
        "Keep strength work general before moving to highly specific hill force.",
        "Use recovery response to decide whether strength reserve is helping or competing.",
    ],
    regression_rules=[
        "Reduce volume or load if soreness compromises aerobic training.",
        "Simplify exercise selection when movement quality declines.",
    ],
    watchouts=[
        "Do not confuse strength reserve with maximal lifting focus.",
        "Avoid placing heavy unfamiliar strength too close to hill-specific work.",
    ],
    placement_guidance=[
        "Place during Evoke base development.",
        "Use before uphill muscular-endurance blocks when force capacity is a limiter.",
    ],
    additional_information="Strength reserve is not the race goal. It is the support layer that makes later mountain-specific force work safer and more useful.",
)


evoke_aerobic_threshold_control_block = _card(
    id="mezzo_058",
    slug="evoke-aerobic-threshold-control-block",
    title="Evoke Aerobic Threshold Control Block",
    parent_macro_id="macro_024",
    parent_tag="evoke_base",
    summary="A monitoring block that keeps aerobic development anchored to the right intensity range.",
    purpose="Improve the athlete's ability to train below, around, and away from threshold deliberately during base work.",
    tags=["base", "aerobic_threshold", "intensity_control"],
    training_profile=[
        "Runs are organized around sustainable aerobic control rather than pace targets alone.",
        "The athlete learns how terrain, altitude, heat, and fatigue change threshold perception.",
        "Intensity discipline is used to protect future layer progression.",
    ],
    expected_adaptations=[
        "Better aerobic intensity awareness.",
        "More stable base development.",
        "Reduced risk of turning capacity work into uncontrolled moderate stress.",
    ],
    progression_rules=[
        "Use metrics and perception together when available.",
        "Progress only when the athlete can keep intended intensity on varied terrain.",
        "Add complexity after control is reliable on simple routes.",
    ],
    regression_rules=[
        "Return to simpler terrain if intensity control is inconsistent.",
        "Reduce duration when threshold drift appears from fatigue rather than planned stimulus.",
    ],
    watchouts=[
        "Do not treat a single threshold estimate as permanent.",
        "Avoid using pace as the main guide on steep or technical terrain.",
    ],
    placement_guidance=[
        "Place alongside or after aerobic capacity development.",
        "Use before muscular-endurance work if the athlete lacks intensity discipline.",
    ],
    additional_information="This card is a guardrail for the Evoke layer model: the base layer needs real aerobic control, not optimistic labeling.",
)


evoke_uphill_muscular_endurance_block = _card(
    id="mezzo_059",
    slug="evoke-uphill-muscular-endurance-block",
    title="Evoke Uphill Muscular Endurance Block",
    parent_macro_id="macro_025",
    parent_tag="evoke_muscular_endurance",
    summary="A defining Evoke block for repeated uphill force after aerobic and strength prerequisites are credible.",
    purpose="Develop mountain-specific muscular endurance through controlled uphill force work with clear recovery boundaries.",
    tags=["muscular_endurance", "uphill", "force"],
    training_profile=[
        "Uphill work creates repeated local muscular demand without becoming random hard climbing.",
        "The athlete enters with adequate aerobic capacity and strength reserve.",
        "Recovery spacing respects soreness and local fatigue, not just breathing or heart rate.",
    ],
    expected_adaptations=[
        "Improved uphill force endurance.",
        "Better fatigue resistance for sustained climbing.",
        "Greater confidence applying strength to mountain objectives.",
    ],
    progression_rules=[
        "Progress duration, grade, load, or repetitions one variable at a time.",
        "Keep form and intent clean before increasing total dose.",
        "Use absorption weeks if local fatigue accumulates.",
    ],
    regression_rules=[
        "Reduce force demand if mechanics degrade.",
        "Return to aerobic capacity or strength reserve if prerequisites are not actually present.",
    ],
    watchouts=[
        "Do not chase soreness as proof of effectiveness.",
        "Avoid adding downhill damage when the target is uphill muscular endurance.",
    ],
    placement_guidance=[
        "Place after Evoke base and strength reserve work.",
        "Use before objective utilisation when uphill force is a limiter.",
    ],
    additional_information="Readiness is built into this card rather than split into a separate block: if the athlete lacks the base or reserve, this block is premature.",
)


evoke_muscular_endurance_absorption_block = _card(
    id="mezzo_060",
    slug="evoke-muscular-endurance-absorption-block",
    title="Evoke Muscular Endurance Absorption Block",
    parent_macro_id="macro_025",
    parent_tag="evoke_muscular_endurance",
    summary="A consolidation block that lets muscular-endurance work turn into usable capacity.",
    purpose="Protect adaptation after uphill force work by reducing stress and observing whether the layer was absorbed.",
    tags=["muscular_endurance", "absorption", "recovery"],
    training_profile=[
        "Muscular-endurance stimulus is paused, reduced, or held steady while the athlete recovers.",
        "Low-cost aerobic running maintains continuity.",
        "The coach watches local freshness, climbing feel, and movement quality.",
    ],
    expected_adaptations=[
        "Better conversion of force work into usable endurance.",
        "Improved readiness for objective-specific utilisation.",
        "Lower risk of soreness chasing.",
    ],
    progression_rules=[
        "Progress when uphill movement feels stronger and soreness resolves predictably.",
        "Use light climbing touches before another full muscular-endurance dose.",
        "Move to utilisation only when the athlete can express the layer without lingering heaviness.",
    ],
    regression_rules=[
        "Extend absorption if soreness or fatigue persists.",
        "Return to easier aerobic work if movement quality remains poor.",
    ],
    watchouts=[
        "Do not stack muscular-endurance blocks without absorption.",
        "Avoid interpreting short-term toughness as long-term adaptation.",
    ],
    placement_guidance=[
        "Place after uphill muscular-endurance development.",
        "Use before race-specific or objective-specific utilisation.",
    ],
    additional_information="This card keeps the Evoke sequence from becoming a pile of hard mountain work. The layer has to settle before it can be used.",
)


evoke_objective_utilisation_block = _card(
    id="mezzo_061",
    slug="evoke-objective-utilisation-block",
    title="Evoke Objective Utilisation Block",
    parent_macro_id="macro_026",
    parent_tag="evoke_race_specific",
    summary="A race-specific block that teaches the athlete to use developed capacity for the objective.",
    purpose="Translate aerobic capacity, strength reserve, and muscular endurance into race- or objective-specific execution.",
    tags=["race_specific", "utilisation", "objective"],
    training_profile=[
        "Specific work combines the layers needed for the target objective.",
        "Sessions are chosen to express capacity under relevant terrain and duration, not to simulate everything.",
        "Fueling, pacing, and gear may be practiced when they affect the use of capacity.",
    ],
    expected_adaptations=[
        "Better transfer from training layers to the target objective.",
        "Improved confidence on race-relevant terrain.",
        "More practical pacing and effort decisions under fatigue.",
    ],
    progression_rules=[
        "Combine demands gradually after individual layers are absorbed.",
        "Use objective relevance to choose which variables to include.",
        "Keep enough recovery to preserve the capacity being expressed.",
    ],
    regression_rules=[
        "Return to the missing layer if utilisation exposes a clear gap.",
        "Simplify sessions if combined demands become too costly.",
    ],
    watchouts=[
        "Do not simulate the objective before the athlete has built the layers to use.",
        "Avoid mistaking exhaustion for specificity.",
    ],
    placement_guidance=[
        "Place after Evoke base and muscular-endurance development.",
        "Use before taper or final event preparation.",
    ],
    additional_information="Utilisation is the payoff layer: the athlete learns how to spend the capacity that was deliberately built earlier.",
)


EVOKE_MEZZO_CARDS = [
    evoke_layer_absorption_recovery_block,
    evoke_aerobic_capacity_development_block,
    evoke_strength_reserve_support_block,
    evoke_aerobic_threshold_control_block,
    evoke_uphill_muscular_endurance_block,
    evoke_muscular_endurance_absorption_block,
    evoke_objective_utilisation_block,
]
