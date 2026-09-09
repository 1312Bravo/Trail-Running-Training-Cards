from importlib import import_module

from training_cards.cards.micro.mainstream_endurance import MAINSTREAM_MICRO_CARDS
from training_cards.cards.micro.cts import CTS_MICRO_CARDS
from training_cards.cards.micro.evoke_endurance import EVOKE_MICRO_CARDS
from training_cards.cards.micro.lydiard import LYDIARD_MICRO_CARDS
from training_cards.cards.micro.sharman_ultra import SHARMAN_MICRO_CARDS
from training_cards.cards.micro.swap import SWAP_MICRO_CARDS


ENDURANCE_80_20_MICRO_CARDS = import_module(
    "training_cards.cards.micro.80_20_endurance"
).ENDURANCE_80_20_MICRO_CARDS


MICRO_CARDS = [
    *MAINSTREAM_MICRO_CARDS,
    *ENDURANCE_80_20_MICRO_CARDS,
    *LYDIARD_MICRO_CARDS,
    *CTS_MICRO_CARDS,
    *EVOKE_MICRO_CARDS,
    *SWAP_MICRO_CARDS,
    *SHARMAN_MICRO_CARDS,
]
