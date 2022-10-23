"""AoC 5, 2019: Sunny with a Chance of Asteroids"""

# Standard library imports
import pathlib
import sys

# Advent of Code imports
from aoc import intcode


def parse(puzzle_input):
    """Parse input"""
    return [int(number) for number in puzzle_input.split(",")]


def part1(data):
    """Solve part 1"""
    computer = intcode.IntcodeComputer(data, input=[1])
    for output in computer:
        """Ignore all but the last output"""
    return output


def part2(data):
    """Solve part 2"""
    computer = intcode.IntcodeComputer(data, input=[5])
    for output in computer:
        """Ignore all but the last output"""
    return output


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
