"""AoC 8, 2020: Handheld Halting"""

# Standard library imports
import pathlib
import sys

OPERATIONS = {}


def register_operation(func):
    OPERATIONS[func.__name__] = func
    return func


def parse(puzzle_input):
    """Parse input"""
    return [parse_line(line) for line in puzzle_input.split("\n")]


def parse_line(line):
    """Parse one line of input

    ## Examples:

    >>> parse_line("nop +0")
    ('nop', 0)
    >>> parse_line("acc +1")
    ('acc', 1)
    >>> parse_line("jmp -2")
    ('jmp', -2)
    """
    operation, _, argument = line.partition(" ")
    return operation, int(argument)


def part1(data):
    """Solve part 1"""
    accumulator, _ = run_code(data)
    return accumulator


def part2(data):
    """Solve part 2"""
    for code in mutate_code(data):
        accumulator, finished = run_code(code)
        if finished:
            return accumulator


def run_code(code):
    """Run the given code until its done or it repeats a line

    Return the accumulator and whether or not the code finished.

    ## Examples

    >>> run_code([("jmp", 2), ("acc", 4), ("acc", -2)])
    (-2, True)
    >>> run_code([("jmp", 2), ("acc", 4), ("acc", -2), ("jmp", -2)])
    (2, False)
    """
    pointer, accumulator = 0, 0
    visited = [False] * len(code) + [True]

    while not visited[pointer]:
        visited[pointer] = True
        operation, argument = code[pointer]

        dpointer, daccumulator = OPERATIONS[operation](argument)
        pointer += dpointer
        accumulator += daccumulator

    return accumulator, pointer == len(code)


def mutate_code(code):
    """Mutate the given code by flipping nop and jmp operations

    ## Example

    >>> list(mutate_code([("nop", 2), ("acc", 1), ("jmp", -2)]))
    [[('jmp', 2), ('acc', 1), ('jmp', -2)], [('nop', 2), ('acc', 1), ('nop', -2)]]
    """
    for pointer, (operation, argument) in enumerate(code):
        if operation == "acc":
            continue
        mutated_op = "jmp" if operation == "nop" else "nop"
        yield code[:pointer] + [(mutated_op, argument)] + code[pointer + 1 :]


@register_operation
def acc(argument):
    """Change accumulator

    acc increases or decreases a single global value called the accumulator by
    the value given in the argument. For example, acc +7 would increase the
    accumulator by 7. The accumulator starts at 0. After an acc instruction, the
    instruction immediately below it is executed next.

    ## Example

    >>> acc(-3)
    (1, -3)
    """
    return 1, argument


@register_operation
def jmp(argument):
    """Jump to a new instruction

    jmp jumps to a new instruction relative to itself. The next instruction
    to execute is found using the argument as an offset from the jmp
    instruction; for example, jmp +2 would skip the next instruction, jmp +1
    would continue to the instruction immediately below it, and jmp -20 would
    cause the instruction 20 lines above to be executed next.

    ## Example

    >>> jmp(6)
    (6, 0)
    """
    return argument, 0


@register_operation
def nop(argument):
    """Do nothing

    nop stands for No OPeration - it does nothing. The instruction
    immediately below it is executed next.

    ## Example

    >>> nop(3)
    (1, 0)
    """
    return 1, 0


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
