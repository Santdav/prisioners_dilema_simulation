# tracker.py
from collections import defaultdict
from dataclasses import dataclass

from moves import Move


@dataclass
class RoundResult:
    match_id: int
    round_no: int
    player_a: str
    player_b: str
    move_a: Move
    move_b: Move
    score_a: int
    score_b: int


class Tracker:
    def __init__(self):
        self.results: list[RoundResult] = []

    def record(self, round_results: list[RoundResult]) -> None:
        self.results.extend(round_results)

    def summary(self) -> dict[str, dict]:
        total = defaultdict(int)
        rounds = defaultdict(int)
        coops = defaultdict(int)

        for r in self.results:
            for name, score, move in (
                (r.player_a, r.score_a, r.move_a),
                (r.player_b, r.score_b, r.move_b),
            ):
                total[name] += score
                rounds[name] += 1
                coops[name] += move is Move.COOPERATE

        return {
            name: {
                "total": total[name],
                "avg": total[name] / rounds[name],
                "coop_rate": coops[name] / rounds[name],
            }
            for name in total
        }