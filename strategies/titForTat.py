from strategy import Move, Strategy




class TitForTat(Strategy):
    name = "TitForTat"
    def choose(self, my_history, opp_history):
        return opp_history[-1] if opp_history else Move.COOPERATE