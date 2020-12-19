"""Rambunctious Recitation

Advent of Code 2020, day 15
Solution by Geir Arne Hjelle, 2020-12-15
"""
# Standard library imports
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def count(start, num_turns):
    """Brute force, recite the numbers"""
    last_counted = {n: e for e, n in enumerate(start[:-1], start=1)}
    previous = start[-1]

    for turn in range(len(start), num_turns):
        say = turn - last_counted.get(previous, turn)
        last_counted[previous] = turn
        previous = say

    return previous


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    numbers = [
        [int(n) for n in line.split(",")]
        for line in file_path.read_text().strip().split()
    ]

    # Part 1
    part_1 = [count(start, num_turns=2020) for start in numbers]
    print(f"The 2020th number spoken is {', '.join(str(n) for n in part_1)}")

    # Part 2
    part_2 = [count(start, num_turns=30_000_000) for start in numbers]
    print(f"The 30,000,000th number spoken is {', '.join(str(n) for n in part_2)}")


if __name__ == "__main__":
    main(sys.argv[1:])
