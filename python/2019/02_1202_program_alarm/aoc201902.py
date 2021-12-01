"""AoC 2, 2019: 1202 Program Alarm"""

# Standard library imports
import itertools
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(number) for number in puzzle_input.split(",")]


def part1(data):
    """Solve part 1"""
    program = data.copy()
    program[1:3] = [12, 2]
    state = run_intcode_program(program)
    return state[0]


def part2(data):
    """Solve part 2"""
    moon_landing = 19690720

    for noun, verb in itertools.product(range(100), range(100)):
        program = data.copy()
        program[1:3] = [noun, verb]
        state = run_intcode_program(program)

        if state[0] == moon_landing:
            return noun * 100 + verb


def run_intcode_program(program):
    """Run an intcode program and return the final state

    >>> run_intcode_program([1, 0, 0, 0, 99])
    [2, 0, 0, 0, 99]

    >>> run_intcode_program([2, 3, 0, 3, 99])
    [2, 3, 0, 6, 99]
    """
    pointer = 0
    while True:
        command = program[pointer]

        if command == 1:
            first, second, store = program[pointer + 1 : pointer + 4]
            program[store] = program[first] + program[second]
            pointer += 4

        if command == 2:
            first, second, store = program[pointer + 1 : pointer + 4]
            program[store] = program[first] * program[second]
            pointer += 4

        if command == 99:
            break

    return program


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
