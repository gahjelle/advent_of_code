"""AoC 2, 2019: 1202 Program Alarm."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [int(number) for number in puzzle_input.split(",")]


def part1(data):
    """Solve part 1."""
    return run_program(data.copy(), 12, 2)


def part2(data, moon_landing=19690720):
    """Solve part 2."""
    base = run_program(data.copy(), 0, 0)
    dn = run_program(data.copy(), 1, 0) - base
    dv = run_program(data.copy(), 0, 1) - base

    noun = (moon_landing - base) // dn
    verb = (moon_landing - base) % dn // dv
    return noun * 100 + verb


def run_program(program, noun, verb):
    """Modify program with noun and verb and run it.

    ## Example:

    >>> run_program([1, 2, 3, 3, 2, 3, 9, 0, 99, 30, 40, 50], 11, 10)
    2700
    """
    program[1:3] = [noun, verb]

    pointer = 0
    while True:
        opcode = program[pointer]
        if opcode == 99:
            break

        first, second, output = program[pointer + 1 : pointer + 4]
        if opcode == 1:
            program[output] = program[first] + program[second]
        elif opcode == 2:
            program[output] = program[first] * program[second]

        pointer += 4

    return program[0]


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
