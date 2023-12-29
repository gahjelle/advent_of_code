"""AoC 9, 2019: Sensor Boost."""

# Standard library imports
import pathlib
import sys

# Advent of Code imports
from aoc import intcode


def parse_data(puzzle_input):
    """Parse input."""
    return [int(number) for number in puzzle_input.split(",")]


def part1(program):
    """Solve part 1."""
    computer = intcode.IntcodeComputer(program, input=[1])
    return next(computer)


def part2(program):
    """Solve part 2."""
    computer = intcode.IntcodeComputer(program, input=[2])
    return next(computer)


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
