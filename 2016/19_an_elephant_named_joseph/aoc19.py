"""An Elephant Named Joseph

Advent of Code 2016, day 19
Solution by Geir Arne Hjelle, 2017-05-28
"""

# Standard library imports
import pathlib
import sys
from collections import deque


def steal_left(num_elves):
    elves = deque(idx + 1 for idx in range(num_elves))

    while num_elves > 1:
        elves.append(elves.popleft())
        elves.popleft()
        num_elves -= 1

    return elves[0]


def steal_across(num_elves):
    stealers = deque(idx + 1 for idx in range(num_elves // 2))
    stealees = deque(idx + 1 for idx in range(num_elves // 2, num_elves))
    move = len(stealees) > len(stealers)

    while stealers:
        stealees.append(stealers.popleft())
        stealees.popleft()
        if move:
            stealers.append(stealees.popleft())
        move = not move

    return stealees[0]


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        for line in fid:
            num_elves = int(line.strip())
            print(f"Elf {steal_left(num_elves)} steals all the presents")
            print(f"Elf {steal_across(num_elves)} steals all the presents")


if __name__ == "__main__":
    main(sys.argv[1:])
