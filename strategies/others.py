from moves import Move
from strategy import Strategy


class TitForTwoTats(Strategy):
    """Only retaliates after two consecutive betrayals. More forgiving than TitForTat."""
    name = "TitForTwoTats"

    def choose(self, my_history, opp_history):
        if len(opp_history) >= 2 and opp_history[-1] is opp_history[-2] is Move.BETRAY:
            return Move.BETRAY
        return Move.COOPERATE


class Pavlov(Strategy):
    """Win-stay, lose-shift: repeat the last move if it scored well (R or T), else switch."""
    name = "Pavlov"

    def choose(self, my_history, opp_history):
        if not my_history:
            return Move.COOPERATE
        # Both did the same thing -> good outcome (CC = R, or BB... see note) -> stay
        if my_history[-1] is opp_history[-1]:
            return Move.COOPERATE
        return Move.BETRAY

class Grudger(Strategy):
    """Cooperates until the opponent betrays once, then betrays forever."""
    name = "Grudger"

    def choose(self, my_history, opp_history):
        return Move.BETRAY if Move.BETRAY in opp_history else Move.COOPERATE