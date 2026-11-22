from __future__ import annotations

from collections import Counter
from pathlib import Path

from training_cards.cloud_config import GOOGLE_DRIVE_LIBRARY
from training_cards.json_store import load_library_bundle_from_json, read_json
from training_cards.pathway import PathwayIndex


# Check coaching contracts as well as structural reachability in each effective library.
def audit_pipeline(bundle_path: Path) -> dict[str, object]:
    cards, _, macro_reuse, mezzo_reuse, session_reuse, library_index = load_library_bundle_from_json(bundle_path)
    bundle = read_json(bundle_path)
    by_id = {card.id: card for card in cards}
    issues = []
    profile_counts = {}
    configs = [macro_reuse, mezzo_reuse, session_reuse]
    for profile in library_index['levels']['macro']:
        ids = {
            entry['card_id']
            for profiles in library_index['levels'].values()
            for entry in profiles.get(profile, [])
        }
        selected = [card for card in cards if card.id in ids]
        scoped_configs = [
            {'entries': [entry for entry in config['entries'] if entry['philosophy_profile_id'] == profile]}
            for config in configs
        ]
        graph = PathwayIndex(selected, *scoped_configs)
        reached = set()
        pending = [card.id for card in selected if str(card.card_type) == 'macro']
        while pending:
            cid = pending.pop()
            if cid in reached:
                continue
            reached.add(cid)
            card = by_id[cid]
            children = graph.children(cid)
            if str(card.card_type) != 'session' and not children:
                issues.append(f'{profile}/{cid}: hierarchy dead end')
            pending.extend(child.id for child in children)
        if ids - reached:
            issues.append(f'{profile}: unreachable cards {sorted(ids - reached)}')
        profile_counts[profile] = dict(Counter(str(card.card_type) for card in selected))

    graph = PathwayIndex(cards, macro_reuse, mezzo_reuse, session_reuse)
    micros = [card for card in cards if str(card.card_type) == 'micro']
    for week in micros:
        if len(week.week_structure) < 2 or any('Anchor the week around' in value for value in week.week_structure):
            issues.append(f'{week.id}: weekly rhythm is still a generic authoring instruction')
        if not any(value.startswith('Entry requirement:') for value in week.goal_race_context):
            issues.append(f'{week.id}: no standalone entry condition')
        if not week.expected_adaptations or not week.progression_rules or not week.regression_rules:
            issues.append(f'{week.id}: missing response or adjustment guidance')
        if not any(str(reference.relationship) == 'alternative' for reference in week.references):
            issues.append(f'{week.id}: missing lower-cost alternative')

    # These recovery jobs explicitly exclude the corresponding development stimulus.
    incompatible = {
        'micro_025': {'session_028','session_029','session_030'},
        'micro_069': {'session_048'},
        'micro_075': {'session_050'},
        'micro_078': {'session_030','session_051'},
        'micro_096': {'session_030','session_054'},
        'micro_106': {'session_057'},
        'micro_108': {'session_056'},
        'micro_111': {'session_058'},
        'micro_129': {'session_063'},
        'micro_135': {'session_064'},
        'micro_136': {'session_064'},
        'micro_147': {'session_069'},
        'micro_152': {'session_068'},
        'micro_154': {'session_070'},
    }
    for week_id, prohibited in incompatible.items():
        if week_id not in by_id:
            continue
        offered = {card.id for card in graph.children(week_id, 'session')}
        if offered & prohibited:
            issues.append(f'{week_id}: development choices contradict recovery role: {sorted(offered & prohibited)}')

    required = {
        'micro_005': {'session_004','session_009'},
        'micro_025': {'session_001','session_009'},
        'micro_013': {'session_005','session_006','session_031'},
        'micro_015': {'session_017','session_018','session_019','session_020'},
        'micro_016': {'session_017','session_019','session_020'},
        'micro_071': {'session_009'},
        'micro_178': {'session_009','session_024'},
        'micro_179': {'session_009','session_024'},
        'micro_180': {'session_001','session_009','session_012','session_013'},
        'micro_181': {'session_040'},
        'micro_182': {'session_040'},
    }
    for week_id, expected in required.items():
        if week_id not in by_id:
            continue
        offered = {card.id for card in graph.children(week_id, 'session')}
        if expected - offered:
            issues.append(f'{week_id}: promised session roles are missing {sorted(expected - offered)}')
    for cid, card in by_id.items():
        for reference in card.references:
            is_transition = str(reference.relationship) in {'next', 'previous', 'alternative'}
            target = by_id[reference.card_id]
            if is_transition and target.card_type != card.card_type:
                issues.append(f'{cid}: transition crosses hierarchy levels')
    if issues:
        raise ValueError('\n'.join(issues))
    return {
        'library_version': bundle['manifest']['library_version'],
        'cards': len(cards),
        'counts': dict(Counter(str(card.card_type) for card in cards)),
        'micro_rhythms': len({tuple(card.week_structure) for card in micros}),
        'profiles': profile_counts,
    }


def main() -> None:
    result = audit_pipeline(GOOGLE_DRIVE_LIBRARY.local_cache_dir / 'training_cards_library.json')
    print(f'Pipeline audit passed: {result}')


if __name__ == '__main__':
    main()
