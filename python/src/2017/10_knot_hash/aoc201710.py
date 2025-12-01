"""AoC 10, 2017: Knot Hash."""

# Standard library imports
import pathlib
import sys

# Advent of Code imports
from aoc import knothash


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data, circle_length=256):
    """Solve part 1."""
    lengths = [int(number) for number in data.split(",")]
    first, second, *_ = knothash.hash_list(lengths, circle_length=circle_length)
    return first * second


def part2(data, circle_length=256):
    """Solve part 2."""
    return knothash.hash_string(data, circle_length=circle_length)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
