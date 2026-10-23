from moves import Move
from strategy import Strategy


class AlwaysCooperate(Strategy):
    name = "AlwaysCooperate"
    def choose(self, my_history, opp_history):
        return Move.COOPERATE

class AlwaysBetray(Strategy):
    name = "AlwaysBetray"
    def choose(self, my_history, opp_history):
        return Move.BETRAY