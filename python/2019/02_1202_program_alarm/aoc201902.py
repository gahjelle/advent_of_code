"""AoC 2, 2019: 1202 Program Alarm"""

# Standard library imports
import itertools
import pathlib
import sys

# Third party imports
from aoc import intcode


def parse(puzzle_input):
    """Parse input"""
    return [int(number) for number in puzzle_input.split(",")]


def part1(data):
    """Solve part 1"""
    program = data.copy()
    program[1:3] = [12, 2]
    state = intcode.run_program(program)
    return state[0]


def part2(data):
    """Solve part 2"""
    moon_landing = 19690720

    for noun, verb in itertools.product(range(100), range(100)):
        program = data.copy()
        program[1:3] = [noun, verb]
        state = intcode.run_program(program)

        if state[0] == moon_landing:
            return noun * 100 + verb


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
