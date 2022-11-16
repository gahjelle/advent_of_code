"""Subterranean Sustainability

Advent of Code 2018, day 12
Solution by Geir Arne Hjelle, 2018-12-19
"""
# Standard library imports
import sys
from collections import defaultdict

# Third party imports
import numpy as np

debug = print if "--debug" in sys.argv else lambda *_: None


def parse_input(fid):
    state_str = next(fid).strip().split()[-1]
    state = tuple(s == "#" for s in state_str)

    rules = defaultdict(lambda: False)
    for line in fid:
        if "=>" in line:
            key, _, value = line.strip().split()
            rules[tuple(k == "#" for k in key)] = value == "#"

    return state, rules


def grow(init_state, rules, num_gen):
    forever_pattern = np.array((False, True, False, True, False))
    summer = 0
    sum_cnt = 0

    offset = 20
    state = np.zeros(len(init_state) + 2 * offset, dtype=bool)
    state[offset : offset + len(init_state)] = init_state

    for gen in range(num_gen):
        print_state(state, gen)
        prev_state = state.copy()
        for idx in range(2, len(state) - 3):
            state[idx] = rules[tuple(prev_state[idx - 2 : idx + 3])]

        summer += sum_cnt

        # Take care of plants moving forever
        if np.all(state[-7:-2] == forever_pattern):
            state[-7:-2] = False
            summer += 2 * (len(state) - offset) - 10
            sum_cnt += 2

        # Stop when no new plants are created
        if not np.any(state):
            summer += sum_cnt * (num_gen - gen - 1)
            break

    print_state(state, num_gen)
    return score(state, offset, summer)


def score(state, offset, summer):
    idxs = np.where(state)[0] - offset
    return np.sum(idxs) + summer


def print_state(state, num):
    state_str = "".join("#" if s else "." for s in state)
    debug(f"{num:>12}: {state_str}")


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            state, rules = parse_input(fid)

            # Part 1
            num_gen = 20
            plant_sum = grow(state, rules, num_gen=num_gen)
            print(f"Sum of pots after {num_gen:,} generations: {plant_sum}")

            # Part 2
            num_gen = 50_000_000_000
            plant_sum = grow(state, rules, num_gen=num_gen)
            print(f"Sum of pots after {num_gen:,} generations: {plant_sum}")


if __name__ == "__main__":
    main(sys.argv[1:])
