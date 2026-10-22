from strategy import Move, Strategy


class AlwaysCooperate(Strategy):
    name = "AlwaysCooperate"
    def choose(self, my_history, opp_history):
        return Move.COOPERATE

class AlwaysBetray(Strategy):
    name = "AlwaysBetray"
    def choose(self, my_history, opp_history):
        return Move.BETRAY

class TitForTat(Strategy):
    name = "TitForTat"
    def choose(self, my_history, opp_history):
        return opp_history[-1] if opp_history else Move.COOPERATE