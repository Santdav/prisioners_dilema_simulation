# main.py
from itertools import combinations

from game import Game
from tracker import Tracker
from strategies import AlwaysCooperate, AlwaysBetray, TitForTat


def main():
    strategies = [AlwaysCooperate(), AlwaysBetray(), TitForTat()]

    game = Game(rounds=200)   # standard payoffs by default
    tracker = Tracker()

    # Round-robin: every strategy plays every other one once
    for match_id, (a, b) in enumerate(combinations(strategies, 2)):
        round_results = game.play_match(a, b, match_id=match_id)
        tracker.record(round_results)

    print_ranking(tracker)


def print_ranking(tracker: Tracker):
    stats = tracker.summary()
    ranking = sorted(stats.items(), key=lambda kv: kv[1]["total"], reverse=True)

    print(f"{'Strategy':<20}{'Total':>8}{'Avg/round':>12}{'Coop %':>9}")
    print("-" * 49)
    for name, s in ranking:
        print(f"{name:<20}{s['total']:>8}{s['avg']:>12.2f}{s['coop_rate']:>8.0%}")


if __name__ == "__main__":
    main()