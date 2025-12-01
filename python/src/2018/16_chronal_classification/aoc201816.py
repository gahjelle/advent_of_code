"""AoC 16, 2018: Chronal Classification."""

# Standard library imports
import collections
import pathlib
import sys

# Advent of Code imports
from aoc import wristdevice


def parse_data(puzzle_input):
    """Parse input."""
    tests, program = puzzle_input.split("\n\n\n\n")
    return [parse_test(test) for test in tests.split("\n\n")], [
        [int(num) for num in line.split()] for line in program.split("\n")
    ]


def parse_test(string):
    """Parse one test."""
    before, code, after = string.split("\n")
    return (
        {
            idx: int(num)
            for idx, num in enumerate(
                before.removeprefix("Before: [").removesuffix("]").split(",")
            )
        },
        [int(num) for num in code.split()],
        {
            idx: int(num)
            for idx, num in enumerate(
                after.removeprefix("After:  [").removesuffix("]").split(",")
            )
        },
    )


def part1(data):
    """Solve part 1."""
    tests, _ = data
    return sum(len(find_valid(*test)) >= 3 for test in tests)


def part2(data):
    """Solve part 2."""
    tests, program = data
    opcodes = find_opcodes(tests)
    registers = wristdevice.run_program(
        [(opcodes[opcode], *regs) for opcode, *regs in program]
    )
    return registers[0]


def find_valid(before, code, after):
    """Count how many opcodes give the expected result"""
    return {
        opcode
        for opcode in wristdevice.ALL_OPCODES
        if wristdevice.evaluate(before, opcode, *code[1:]) == after
    }


def find_opcodes(tests):
    """Use tests to find valid opcodes"""
    valid = collections.defaultdict(list)
    for before, code, after in tests:
        valid[code[0]].append(find_valid(before, code, after))
    alternatives = {
        opcode: set.intersection(*instructions)
        for opcode, instructions in valid.items()
    }

    opcodes = {}
    while any(alternatives.values()):
        for opcode, instructions in alternatives.items():
            if len(instructions) == 1 and opcode not in opcodes:
                opcodes[opcode] = list(instructions)[0]
                alternatives = {
                    op: alts - instructions for op, alts in alternatives.items()
                }
    return opcodes


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
