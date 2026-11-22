import unittest

from training_cards.mezzo_micro_reuse import build_mezzo_micro_reuse_config
from training_cards.philosophy_profiles import CTS, LYDIARD, MAINSTREAM_ENDURANCE
from training_cards.schemas import CardType, MezzoCard, MicroCard, TrainingLevel


def card(kind, cid, profile):
    cls = MezzoCard if kind == CardType.MEZZO else MicroCard
    return cls(id=cid, slug=cid.replace('_','-'), title=cid, card_type=kind,
               suitable_levels=[TrainingLevel.ADVANCED], philosophy_profile_ids=[profile],
               summary='Summary.', purpose='Purpose.')


class ExplicitWeekReuseTests(unittest.TestCase):
    def test_philosophy_owned_block_can_offer_a_shared_mainstream_week(self):
        block = card(CardType.MEZZO, 'mezzo_047', CTS)
        week = card(CardType.MICRO, 'micro_180', MAINSTREAM_ENDURANCE)
        config = build_mezzo_micro_reuse_config('1.3.0', cards=[block,week], macro_mezzo_reuse_config={'entries':[]})
        self.assertEqual(1, config['entry_count'])
        entry = config['entries'][0]
        self.assertEqual(CTS, entry['philosophy_profile_id'])
        self.assertEqual('micro_180', entry['reused_micro_card_id'])
        self.assertEqual('reuse_mainstream', entry['reuse_type'])

    def test_missing_or_philosophy_owned_week_is_not_claimed_as_mainstream(self):
        block = card(CardType.MEZZO, 'mezzo_047', CTS)
        foreign_week = card(CardType.MICRO, 'micro_180', LYDIARD)
        for cards in [[block], [block,foreign_week]]:
            config = build_mezzo_micro_reuse_config('1.3.0', cards=cards, macro_mezzo_reuse_config={'entries':[]})
            self.assertEqual([], config['entries'])

    def test_repeated_inherited_links_do_not_duplicate_the_shared_week(self):
        block = card(CardType.MEZZO, 'mezzo_047', CTS)
        week = card(CardType.MICRO, 'micro_180', MAINSTREAM_ENDURANCE)
        from training_cards.schemas import CardReference, CardRelationship
        week.references = [CardReference('mezzo_047', CardRelationship.PARENT)]
        entry = {'philosophy_profile_id':CTS,'reused_mezzo_card_id':'mezzo_047','reuse_type':'reuse_mainstream'}
        config = build_mezzo_micro_reuse_config('1.3.0', cards=[block,week], macro_mezzo_reuse_config={'entries':[entry,entry]})
        self.assertEqual(1, config['entry_count'])


if __name__ == '__main__':
    unittest.main()
