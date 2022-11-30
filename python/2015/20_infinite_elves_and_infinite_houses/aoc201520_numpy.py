"""AoC 20, 2015: Infinite Elves and Infinite Houses"""

# Standard library imports
import pathlib
import sys

import numpy as np


def parse_data(puzzle_input):
    """Parse input"""
    return int(puzzle_input)


def part1(data, per_elf=10):
    """Solve part 1"""
    threshold = data // per_elf
    presents = deliver(threshold, max_houses=threshold)
    return next(house for house, p in enumerate(presents) if p >= threshold)


def part2(data, per_elf=11, max_houses=50):
    """Solve part 2"""
    threshold = data // per_elf
    presents = deliver(threshold, max_houses=max_houses)
    return next(house for house, p in enumerate(presents) if p >= threshold)


def deliver(num_houses, max_houses):
    """Deliver presents to houses

    ## Examples:

    >>> deliver(9, max_houses=9)
    array([ 0,  1,  3,  4,  7,  6, 12,  8, 15, 13])
    >>> deliver(12, max_houses=3)
    array([ 0,  1,  3,  4,  6,  5, 11,  7, 12, 12, 15, 11, 22])
    """
    houses = np.zeros(num_houses + 1, dtype=int)
    for elf in range(1, num_houses + 1):
        houses[elf : (max_houses * elf) + 1 : elf] += elf
    return houses


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
