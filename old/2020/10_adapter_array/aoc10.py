"""Adapter Array

Advent of Code 2020, day 10
Solution by Geir Arne Hjelle, 2020-12-10
"""
# Standard library imports
import pathlib
import sys

# Third party imports
import numpy as np

debug = print if "--debug" in sys.argv else lambda *_: None

FORBIDDEN = {0: {}, 1: {}, 2: {}, 3: {}, 4: {"000"}}


def count_jumps(jumps):
    """Count number of 1- and 3-jumps"""
    size, count = np.unique(jumps, return_counts=True)
    jump_counts = {s: c for s, c in zip(size, count)}
    return jump_counts[1], jump_counts[3]


def find_runs(jumps):
    """Find runs of 1 jumps"""
    # Add a 3 at front to be sure the run starts with 3s
    return np.diff(np.where(np.diff([3] + list(jumps)))[0])[::2]


def forbidden_combos(run_length):
    """Find forbidden combinations based on run lengths"""
    if run_length not in FORBIDDEN:
        previous = forbidden_combos(run_length - 1)
        FORBIDDEN[run_length] = set.union(
            *[{f"0{c}", f"1{c}", f"{c}0", f"{c}1"} for c in previous]
        )

    return FORBIDDEN[run_length]


def runs_to_combinations(run_lengths):
    """Count possible combinations based on run lengths"""
    return [2 ** (rl - 1) - len(forbidden_combos(rl)) for rl in run_lengths]


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    numbers = sorted(int(n) for n in file_path.open())
    joltage_jumps = np.diff([0] + numbers + [max(numbers) + 3])

    # Part 1
    part_1 = np.prod(count_jumps(joltage_jumps))
    print(f"The product of 1- and 3-jumps is {part_1}")

    # Part 2
    part_2 = np.prod(runs_to_combinations(find_runs(joltage_jumps)))
    print(f"There are {part_2} distinct arrangements")


if __name__ == "__main__":
    main(sys.argv[1:])
