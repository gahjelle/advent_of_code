"""AoC 5, 2018: Alchemical Reduction."""

# Standard library imports
import pathlib
import sys

# Third party imports
import numpy as np


def parse_data(puzzle_input):
    """Parse input."""
    polymer = np.array(
        [
            ord(letter) - 96 if letter >= "a" else 64 - ord(letter)
            for letter in puzzle_input
        ]
    )
    return reduce(polymer)


def part1(polymer):
    """Solve part 1."""
    return len(polymer)


def part2(polymer):
    """Solve part 2."""
    elements = {abs(unit) for unit in polymer}
    polymer_lengths = [
        len(reduce(polymer[np.abs(polymer) != element])) for element in elements
    ]
    return min(polymer_lengths)


def reduce(polymer):
    """Reduce one polymer as much as possible"""
    while True:
        reductions = polymer[:-1] + polymer[1:]
        if not np.any(reductions == 0):
            return polymer

        idx, *_ = np.where(reductions == 0)
        reduce_idx = idx[np.concatenate(([True], np.diff(idx) != 1))]
        polymer[reduce_idx] = 99
        polymer[reduce_idx + 1] = 99
        polymer = polymer[polymer != 99]


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
