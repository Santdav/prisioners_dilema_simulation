# main.py
from itertools import combinations

from game import Game
from strategies.alwaysStrategies import AlwaysBetray, AlwaysCooperate
from strategies.random import RandomStrategy
from strategies.titForTat import TitForTat
from tracker import Tracker
from strategies.others import *



def main():
    strategies = [
    AlwaysCooperate(), AlwaysBetray(), TitForTat(),
    Grudger(), TitForTwoTats(), Pavlov(), RandomStrategy(seed=42),
]

    game = Game(rounds=200)   # standard payoffs by default
    tracker = Tracker()

    # Round-robin: every strategy plays every other one once
    for match_id, (a, b) in enumerate(combinations(strategies, 2)):
        round_results = game.play_match(a, b, match_id=match_id)
        tracker.record(round_results)

    print_ranking(tracker)
    print_matrix(tracker)
    print_records(tracker)


def print_ranking(tracker: Tracker):
    stats = tracker.summary()
    ranking = sorted(stats.items(), key=lambda kv: kv[1]["avg"], reverse=True)

    print(f"{'Strategy':<20}{'Total':>8}{'Avg/round':>12}{'Coop %':>9}")
    print("-" * 49)
    for name, s in ranking:
        print(f"{name:<20}{s['total']:>8}{s['avg']:>12.2f}{s['coop_rate']:>8.0%}")


def print_matrix(tracker: Tracker):
    matrix = tracker.head_to_head()
    names = sorted(matrix)

    print("\nHead-to-head (avg score/round of ROW vs COLUMN)")
    print(" " * 18 + "".join(f"{n:>16}" for n in names))
    for row in names:
        cells = "".join(
            f"{matrix[row][col]:>16.2f}" if col in matrix[row] else f"{'-':>16}"
            for col in names
        )
        print(f"{row:<18}{cells}")


def print_records(tracker: Tracker):
    print("\nMatch records")
    for name, rec in tracker.match_records().items():
        print(f"{name:<20} W{rec['wins']}  L{rec['losses']}  D{rec['draws']}")


if __name__ == "__main__":
    main()