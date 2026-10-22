# tracker.py
from collections import defaultdict
from dataclasses import dataclass, asdict

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

    # ---------- per-strategy totals (unchanged) ----------
    def summary(self) -> dict[str, dict]:
        total = defaultdict(int)
        rounds = defaultdict(int)
        coops = defaultdict(int)

        for r in self.results:
            for name, score, move in self._sides(r):
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

    # ---------- head-to-head ----------
    def head_to_head(self) -> dict[str, dict[str, float]]:
        """matrix[row][col] = average score per round of `row` when facing `col`."""
        totals = defaultdict(lambda: defaultdict(int))
        rounds = defaultdict(lambda: defaultdict(int))

        for r in self.results:
            totals[r.player_a][r.player_b] += r.score_a
            totals[r.player_b][r.player_a] += r.score_b
            rounds[r.player_a][r.player_b] += 1
            rounds[r.player_b][r.player_a] += 1

        return {
            row: {col: totals[row][col] / rounds[row][col] for col in totals[row]}
            for row in totals
        }

    # ---------- match outcomes ----------
    def match_records(self) -> dict[str, dict[str, int]]:
        """Wins / losses / draws per strategy, decided by total score in each match."""
        match_totals = defaultdict(lambda: defaultdict(int))
        for r in self.results:
            match_totals[r.match_id][r.player_a] += r.score_a
            match_totals[r.match_id][r.player_b] += r.score_b

        records = defaultdict(lambda: {"wins": 0, "losses": 0, "draws": 0})
        for scores in match_totals.values():
            (p1, s1), (p2, s2) = scores.items()
            if s1 > s2:
                records[p1]["wins"] += 1
                records[p2]["losses"] += 1
            elif s2 > s1:
                records[p2]["wins"] += 1
                records[p1]["losses"] += 1
            else:
                records[p1]["draws"] += 1
                records[p2]["draws"] += 1
        return dict(records)

    # ---------- export ----------
    def to_dataframe(self):
        import pandas as pd  # imported here so pandas stays optional
        rows = [
            {**asdict(r), "move_a": r.move_a.value, "move_b": r.move_b.value}
            for r in self.results
        ]
        return pd.DataFrame(rows)

    # ---------- helpers ----------
    @staticmethod
    def _sides(r: RoundResult):
        yield r.player_a, r.score_a, r.move_a
        yield r.player_b, r.score_b, r.move_b