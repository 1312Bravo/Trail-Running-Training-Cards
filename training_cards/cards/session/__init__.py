from importlib import import_module

from training_cards.cards.session.cts import CTS_SESSION_CARDS
from training_cards.cards.session.evoke_endurance import EVOKE_SESSION_CARDS
from training_cards.cards.session.lydiard import LYDIARD_SESSION_CARDS
from training_cards.cards.session.mainstream_endurance import MAINSTREAM_SESSION_CARDS
from training_cards.cards.session.sharman_ultra import SHARMAN_SESSION_CARDS
from training_cards.cards.session.swap import SWAP_SESSION_CARDS


ENDURANCE_80_20_SESSION_CARDS = import_module(
    "training_cards.cards.session.80_20_endurance"
).ENDURANCE_80_20_SESSION_CARDS

SESSION_CARDS = [
    *MAINSTREAM_SESSION_CARDS,
    *ENDURANCE_80_20_SESSION_CARDS,
    *LYDIARD_SESSION_CARDS,
    *CTS_SESSION_CARDS,
    *EVOKE_SESSION_CARDS,
    *SWAP_SESSION_CARDS,
    *SHARMAN_SESSION_CARDS,
]
