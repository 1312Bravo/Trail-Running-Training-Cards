from training_cards.philosophy_profiles import LYDIARD
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
        philosophy_profile_ids=[LYDIARD],
        summary=summary,
        purpose=purpose,
        tags=["lydiard", "mezzo", *tags],
        goal_race_context=[
            "Use when Lydiard sequencing changes the block decision.",
            "Most useful when aerobic conditioning, hill transition, integration, or taper expression are the main planning questions.",
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


lydiard_response_regulated_reduced_load_block = _card(
    id="mezzo_039",
    slug="lydiard-response-regulated-reduced-load-block",
    title="Lydiard Response-Regulated Reduced-Load Block",
    parent_macro_id="macro_007",
    parent_tag="recovery_transition",
    summary="A reduced-load block that waits for absorption before the next Lydiard layer.",
    purpose="Use athlete response to decide whether the next sequence layer is earned or whether more recovery is needed.",
    tags=["recovery", "response_regulation", "sequence"],
    training_profile=[
        "Training is simplified enough that fatigue response becomes visible.",
        "Easy aerobic movement remains present, but volume and intensity are reduced until the athlete feels springier.",
        "The next layer is delayed if the athlete is still flat, sore, or emotionally resistant.",
    ],
    expected_adaptations=[
        "Better absorption of the previous layer.",
        "Clearer readiness signals for returning to aerobic, hill, or race-preparation work.",
        "Lower risk of forcing sequence progression by calendar alone.",
    ],
    progression_rules=[
        "Progress when easy running feels natural and recovery markers are stable.",
        "Use strides or light hills only if they improve rhythm without adding fatigue.",
        "Return to the next layer gradually rather than jumping to full load.",
    ],
    regression_rules=[
        "Stay reduced if the athlete remains heavy-legged or unusually irritable.",
        "Remove intensity until ordinary aerobic running feels absorbable.",
    ],
    watchouts=[
        "Do not confuse Lydiard patience with passive waiting.",
        "Avoid moving to the next layer because the written plan says it is time.",
    ],
    placement_guidance=[
        "Place after a demanding base, hill, race-preparation, or racing period.",
        "Use before resuming the next Lydiard layer when readiness is uncertain.",
    ],
    additional_information="This card keeps the sequence human. The layer only works if the athlete has absorbed the previous one.",
)


lydiard_sustainable_aerobic_conditioning_block = _card(
    id="mezzo_040",
    slug="lydiard-sustainable-aerobic-conditioning-block",
    title="Lydiard Sustainable Aerobic Conditioning Block",
    parent_macro_id="macro_016",
    parent_tag="lydiard_base",
    summary="A base block that builds the greatest aerobic load the athlete can absorb consistently.",
    purpose="Develop broad aerobic conditioning without turning base into strain, monotony, or fragile mileage chasing.",
    tags=["base", "aerobic_conditioning", "sustainable_volume"],
    training_profile=[
        "Frequent aerobic running is the center of the block.",
        "Volume is high relative to the athlete's history, but not higher than the athlete can recover from.",
        "Effort is guided by feel and repeatability, with terrain chosen to support durable aerobic work.",
    ],
    expected_adaptations=[
        "Stronger aerobic foundation.",
        "Improved ability to handle later hill and race-specific layers.",
        "Better internal sense of sustainable effort.",
    ],
    progression_rules=[
        "Increase volume only while daily running remains relaxed and repeatable.",
        "Use rolling terrain carefully when it supports aerobic strength without becoming a hill phase.",
        "Hold steady when the athlete is adapting rather than adding load reflexively.",
    ],
    regression_rules=[
        "Reduce volume if the athlete loses natural running rhythm.",
        "Simplify terrain or frequency when easy effort becomes forced.",
    ],
    watchouts=[
        "Do not turn base into a mileage contest.",
        "Avoid premature speedwork that interrupts aerobic consolidation.",
    ],
    placement_guidance=[
        "Place early in Lydiard base development.",
        "Use before long aerobic conditioning or hill-resistance transition work.",
    ],
    additional_information="The Lydiard distinction is not just 'more easy running.' It is the largest useful aerobic base that still leaves the athlete absorbing, not surviving.",
)


lydiard_long_aerobic_conditioning_block = _card(
    id="mezzo_041",
    slug="lydiard-long-aerobic-conditioning-block",
    title="Lydiard Long Aerobic Conditioning Block",
    parent_macro_id="macro_016",
    parent_tag="lydiard_base",
    summary="A long-aerobic block that extends endurance inside a base-first sequence.",
    purpose="Use long aerobic work to deepen conditioning before hill or race-specific layers are emphasized.",
    tags=["base", "long_run", "aerobic_endurance"],
    training_profile=[
        "Long runs are aerobic, controlled, and supported by the rest of the week.",
        "The athlete learns to finish long work with form and appetite for more training intact.",
        "Trail routes are chosen for steady aerobic demand unless climbing durability is the explicit limiter.",
    ],
    expected_adaptations=[
        "Improved long-duration aerobic resilience.",
        "Greater confidence in base readiness.",
        "Better tolerance for later sequence demands.",
    ],
    progression_rules=[
        "Progress long-run duration only when weekly aerobic rhythm stays healthy.",
        "Keep long work mostly aerobic before adding sharper or more specific stress.",
        "Use step-back weeks when long duration begins to dominate recovery.",
    ],
    regression_rules=[
        "Shorten long runs if they flatten the next several days.",
        "Use smoother terrain if technical fatigue obscures aerobic conditioning.",
    ],
    watchouts=[
        "Do not make long runs secretly race-specific too early.",
        "Avoid using long-run heroics to compensate for weak weekly consistency.",
    ],
    placement_guidance=[
        "Place after sustainable aerobic conditioning is established.",
        "Use before hill-resistance transition if long aerobic readiness is the limiter.",
    ],
    additional_information="This card treats the long run as part of a sequence, not as a weekly monument. It should support what comes next.",
)


lydiard_hill_resistance_development_block = _card(
    id="mezzo_042",
    slug="lydiard-hill-resistance-development-block",
    title="Lydiard Hill Resistance Development Block",
    parent_macro_id="macro_017",
    parent_tag="lydiard_hill_transition",
    summary="A hill-transition block that introduces resistance, coordination, and resilient mechanics.",
    purpose="Bridge aerobic base toward later faster or more integrated work through controlled hill resistance.",
    tags=["hill_transition", "coordination", "strength"],
    training_profile=[
        "Hill work develops spring, coordination, and strength without becoming maximal climbing practice.",
        "The block uses enough recovery and aerobic support to keep mechanics clean.",
        "Trail hills can be used if footing and descent cost do not hijack the purpose.",
    ],
    expected_adaptations=[
        "Improved hill mechanics and elastic strength.",
        "Better readiness for later integrated speed or race-preparation work.",
        "Stronger connection between aerobic base and forceful running.",
    ],
    progression_rules=[
        "Progress hill exposure by control and rhythm before steepness or volume.",
        "Keep downhill return easy enough that the uphill work remains the main stress.",
        "Move onward only when the athlete handles hill resistance without lingering heaviness.",
    ],
    regression_rules=[
        "Reduce hill volume if coordination deteriorates.",
        "Use gentler grades when local muscular soreness lasts too long.",
    ],
    watchouts=[
        "Do not turn Lydiard hill resistance into all-out hill repeats.",
        "Avoid technical descents that add damage unrelated to the intended transition.",
    ],
    placement_guidance=[
        "Place after Lydiard base development.",
        "Use before Lydiard capacity integration or race-specific preparation.",
    ],
    additional_information="The block should feel like a bridge from base to expression: stronger, springier running, not a mountain sufferfest.",
)


lydiard_hill_transition_absorption_block = _card(
    id="mezzo_043",
    slug="lydiard-hill-transition-absorption-block",
    title="Lydiard Hill Transition Absorption Block",
    parent_macro_id="macro_017",
    parent_tag="lydiard_hill_transition",
    summary="A consolidation block that checks whether hill resistance has been absorbed.",
    purpose="Confirm readiness to progress from hill resistance to later race-preparation layers.",
    tags=["hill_transition", "absorption", "readiness"],
    training_profile=[
        "Hill stimulus is reduced or stabilized while the coach observes freshness, rhythm, and soreness.",
        "Aerobic running remains present enough to preserve base continuity.",
        "Small coordination touches may remain if they support movement quality.",
    ],
    expected_adaptations=[
        "Better absorption of local muscular and coordination stress.",
        "Clearer readiness for integration work.",
        "Reduced risk of carrying hill fatigue into later phases.",
    ],
    progression_rules=[
        "Progress when the athlete feels stronger after hills rather than dulled by them.",
        "Use light rhythm work before full integration if readiness is promising but incomplete.",
        "Move to race-specific preparation only when mechanics and recovery are stable.",
    ],
    regression_rules=[
        "Return to reduced hill volume if soreness persists.",
        "Extend absorption if easy running remains heavy or awkward.",
    ],
    watchouts=[
        "Do not skip absorption because the hill block was completed on paper.",
        "Avoid testing fitness while the athlete is still adapting to force work.",
    ],
    placement_guidance=[
        "Place at the end of hill-resistance transition.",
        "Use before Lydiard capacity integration or sequence-expression taper work.",
    ],
    additional_information="This card protects the sequence from being rushed. Absorbed work is useful work; dragged fatigue is not.",
)


lydiard_capacity_integration_block = _card(
    id="mezzo_044",
    slug="lydiard-capacity-integration-block",
    title="Lydiard Capacity Integration Block",
    parent_macro_id="macro_018",
    parent_tag="lydiard_race_specific",
    summary="A race-preparation block that integrates already built capacities instead of inventing fitness late.",
    purpose="Bring aerobic base, hill resistance, rhythm, and event needs together without abandoning sequence logic.",
    tags=["race_specific", "integration", "sequence"],
    training_profile=[
        "Workouts connect previous layers to the athlete's target race demands.",
        "Specificity is added after base and hill readiness, not as a substitute for them.",
        "The block keeps enough aerobic support to maintain the foundation while sharpening expression.",
    ],
    expected_adaptations=[
        "Better transfer from general conditioning to race demands.",
        "Improved confidence in the completed sequence.",
        "Clearer sense of what still needs sharpening before taper.",
    ],
    progression_rules=[
        "Integrate one race demand at a time so fatigue sources remain visible.",
        "Keep workouts controlled enough that they express capacity rather than test desperation.",
        "Progress toward specificity only while recovery and rhythm remain stable.",
    ],
    regression_rules=[
        "Return to simpler aerobic or hill support if integration work exposes a gap.",
        "Reduce specificity if it erodes the foundation built earlier.",
    ],
    watchouts=[
        "Do not use race-specific sessions to compensate for missing base.",
        "Avoid last-minute complexity that the athlete cannot absorb.",
    ],
    placement_guidance=[
        "Place after Lydiard base and hill-resistance transition.",
        "Use before sequence-expression taper when the athlete is ready to sharpen.",
    ],
    additional_information="This card is Lydiard-specific because the question is sequence transfer: what have we built, and how should it now show up?",
)


lydiard_sequence_expression_taper_block = _card(
    id="mezzo_045",
    slug="lydiard-sequence-expression-taper-block",
    title="Lydiard Sequence Expression Taper Block",
    parent_macro_id="macro_019",
    parent_tag="lydiard_peak_taper",
    summary="A taper block that expresses completed preparation rather than trying to create it late.",
    purpose="Freshen the athlete while preserving the rhythm and confidence earned through the Lydiard sequence.",
    tags=["taper", "sequence_expression", "freshness"],
    training_profile=[
        "Training load reduces while familiar rhythm and light sharpening remain.",
        "The taper protects the capacities already built instead of adding new demands.",
        "Race confidence comes from completed preparation, not from last-minute workouts.",
    ],
    expected_adaptations=[
        "Improved freshness.",
        "Better expression of previous aerobic, hill, and integration work.",
        "Reduced anxiety-driven training close to race day.",
    ],
    progression_rules=[
        "Keep touches short and familiar.",
        "Reduce load enough that the athlete feels increasingly eager to race.",
        "Use confidence checks based on sequence completion rather than new tests.",
    ],
    regression_rules=[
        "Remove sharpening if the athlete is carrying fatigue.",
        "Extend easy freshening if soreness or heaviness appears late.",
    ],
    watchouts=[
        "Do not try to manufacture missing fitness in the taper.",
        "Avoid unfamiliar workouts, routes, or strength stress close to the goal race.",
    ],
    placement_guidance=[
        "Place after Lydiard race-specific integration.",
        "Use in the final weeks before a priority race.",
    ],
    additional_information="A good Lydiard taper has a calm feeling: nothing dramatic is added, because the work has already been done.",
)


LYDIARD_MEZZO_CARDS = [
    lydiard_response_regulated_reduced_load_block,
    lydiard_sustainable_aerobic_conditioning_block,
    lydiard_long_aerobic_conditioning_block,
    lydiard_hill_resistance_development_block,
    lydiard_hill_transition_absorption_block,
    lydiard_capacity_integration_block,
    lydiard_sequence_expression_taper_block,
]
