"""AoC 23, 2015: Opening the Turing Lock"""

# Standard library imports
import pathlib
import sys

INSTRUCTIONS = {}


def register_instruction(func):
    """Decorator for registering valid instructions."""
    INSTRUCTIONS[func.__name__] = func
    return func


def parse(puzzle_input):
    """Parse input"""
    return [parse_instruction(line) for line in puzzle_input.split("\n")]


def parse_instruction(line):
    """Parse one line of instruction"""
    instruction, _, arguments = line.partition(" ")
    return instruction, arguments.replace(",", " ").split()


def part1(data):
    """Solve part 1"""
    return run_program(data)["b"]


def part2(data):
    """Solve part 2"""
    return run_program(data, a=1)["b"]


def run_program(program, a=0, b=0):
    """Run program.

    ## Examples:

    >>> program = [("inc", ["b"]), ("jio", ["b", 2]), ("tpl", ["b"]), ("inc", ["b"])]
    >>> run_program(program)
    {'a': 0, 'b': 2}
    >>> run_program(program, b=1)
    {'a': 0, 'b': 7}
    """
    pointer = 0
    registers = {"a": a, "b": b}
    while pointer < len(program):
        instruction, arguments = program[pointer]
        registers, dpointer = INSTRUCTIONS[instruction](registers, *arguments)
        pointer += dpointer
    return registers


@register_instruction
def hlf(registers, register):
    return registers | {register: registers[register] // 2}, 1


@register_instruction
def tpl(registers, register):
    return registers | {register: registers[register] * 3}, 1


@register_instruction
def inc(registers, register):
    return registers | {register: registers[register] + 1}, 1


@register_instruction
def jmp(registers, offset):
    return registers, int(offset)


@register_instruction
def jie(registers, register, offset):
    return registers, int(offset) if registers[register] % 2 == 0 else 1


@register_instruction
def jio(registers, register, offset):
    return registers, int(offset) if registers[register] == 1 else 1


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
