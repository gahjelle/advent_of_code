"""AoC 11, 2017: Hex Ed"""

# Standard library imports
import pathlib
import sys

# Third party imports
import numpy as np

# Using 3D cube coordinates: https://math.stackexchange.com/a/2643016
DIRECTIONS = {
    "n": (1, -1, 0),
    "ne": (0, -1, 1),
    "se": (-1, 0, 1),
    "s": (-1, 1, 0),
    "sw": (0, 1, -1),
    "nw": (1, 0, -1),
}


def parse_data(puzzle_input):
    """Parse input"""
    return np.array([DIRECTIONS[step] for step in puzzle_input.split(",")])


def part1(data):
    """Solve part 1"""
    return np.max(np.abs(data.sum(axis=0)))


def part2(data):
    """Solve part 2"""
    return np.max(np.abs(data.cumsum(axis=0)))


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
