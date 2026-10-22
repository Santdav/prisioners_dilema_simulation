# payoffs.py
from moves import Move

PAYOFFS = {
    (Move.COOPERATE, Move.COOPERATE): (3, 3),
    (Move.COOPERATE, Move.BETRAY):    (0, 5),
    (Move.BETRAY,    Move.COOPERATE): (5, 0),
    (Move.BETRAY,    Move.BETRAY):    (1, 1),
}