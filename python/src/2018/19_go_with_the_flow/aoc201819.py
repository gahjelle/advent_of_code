"""AoC 19, 2018: Go With The Flow."""

# Standard library imports
import pathlib
import sys

# Advent of Code imports
from aoc import wristdevice


def parse_data(puzzle_input):
    """Parse input."""
    return [
        [instr] + [int(c) for c in code]
        for line in puzzle_input.split("\n")
        for instr, *code in [line.split()]
    ]


def part1(data):
    """Solve part 1."""
    (_, reg_pointer), *program = data
    registers = wristdevice.run_program(program, reg_pointer=reg_pointer)
    return registers[0]


def part2(data):
    """Solve part 2."""
    return data


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
