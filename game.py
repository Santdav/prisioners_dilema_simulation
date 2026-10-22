# game.py
from payoff import PAYOFFS
from tracker import RoundResult


class Game:
    def __init__(self, payoffs=PAYOFFS, rounds=200):
        self.payoffs = payoffs
        self.rounds = rounds

    def play_match(self, a, b, match_id=0) -> list[RoundResult]:
        a.reset()
        b.reset()
        hist_a, hist_b = [], []
        results = []

        for round_no in range(1, self.rounds + 1):
            move_a = a.choose(hist_a, hist_b)
            move_b = b.choose(hist_b, hist_a)
            score_a, score_b = self.payoffs[(move_a, move_b)]

            hist_a.append(move_a)
            hist_b.append(move_b)
            results.append(RoundResult(match_id, round_no, a.name, b.name,
                                       move_a, move_b, score_a, score_b))
        return results