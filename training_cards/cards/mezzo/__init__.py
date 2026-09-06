from importlib import import_module

from training_cards.cards.mezzo.cts import CTS_MEZZO_CARDS
from training_cards.cards.mezzo.evoke_endurance import EVOKE_MEZZO_CARDS
from training_cards.cards.mezzo.lydiard import LYDIARD_MEZZO_CARDS
from training_cards.cards.mezzo.mainstream_endurance.mainstream_mezzo_cards import MAINSTREAM_MEZZO_CARDS
from training_cards.cards.mezzo.sharman_ultra import SHARMAN_MEZZO_CARDS
from training_cards.cards.mezzo.swap import SWAP_MEZZO_CARDS

ENDURANCE_80_20_MEZZO_CARDS = import_module(
    "training_cards.cards.mezzo.80_20_endurance"
).ENDURANCE_80_20_MEZZO_CARDS

MEZZO_CARDS = [
    *MAINSTREAM_MEZZO_CARDS,
    *ENDURANCE_80_20_MEZZO_CARDS,
    *LYDIARD_MEZZO_CARDS,
    *CTS_MEZZO_CARDS,
    *EVOKE_MEZZO_CARDS,
    *SWAP_MEZZO_CARDS,
    *SHARMAN_MEZZO_CARDS,
]
