import random
from moves import Move
from strategy import Strategy


class RandomStrategy(Strategy):
    def __init__(self, p_cooperate: float = 0.5, seed: int | None = None):
        self.name = f"Random({p_cooperate:.2f})"
        self.p = p_cooperate
        self.rng = random.Random(seed)

    def choose(self, my_history, opp_history):
        return Move.COOPERATE if self.rng.random() < self.p else Move.BETRAY