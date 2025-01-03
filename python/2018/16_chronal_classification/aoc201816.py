"""AoC 16, 2018: Chronal Classification."""

# Standard library imports
import collections
import pathlib
import sys

ALL_OPCODES = [
    "addr",
    "addi",
    "mulr",
    "muli",
    "banr",
    "bani",
    "borr",
    "bori",
    "setr",
    "seti",
    "gtir",
    "gtri",
    "gtrr",
    "eqir",
    "eqri",
    "eqrr",
]


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
    registers = run_program(program, opcodes)
    return registers[0]


def find_valid(before, code, after):
    """Count how many opcodes give the expected result"""
    is_valid = set()
    for start in range(len(ALL_OPCODES)):
        opcodes = dict(
            zip(
                range(len(ALL_OPCODES)),
                ALL_OPCODES[start:] + ALL_OPCODES[:start],
            )
        )
        if evaluate(*code, opcodes, before) == after:
            is_valid.add(opcodes[code[0]])
    return is_valid


def find_opcodes(tests):
    """Use tests to find valid opcodes"""
    valid = {idx: [set(ALL_OPCODES)] for idx in range(len(ALL_OPCODES))}
    for before, code, after in tests:
        valid[code[0]].append(find_valid(before, code, after))

    alternatives = {
        opcode: set.intersection(*instructions)
        for opcode, instructions in valid.items()
    }

    opcodes = {}
    while any(alternatives.values()):
        new_alternatives = alternatives.copy()
        for opcode, instructions in alternatives.items():
            if len(instructions) == 1 and opcode not in opcodes:
                opcodes[opcode] = list(instructions)[0]
                new_alternatives = {
                    op: alts - instructions for op, alts in new_alternatives.items()
                }
        if alternatives == new_alternatives:
            break
        alternatives = new_alternatives
    return opcodes


def run_program(program, opcodes):
    """Run the given program."""
    registers = {0: 0, 1: 0, 2: 0, 3: 0}
    for line in program:
        registers = evaluate(*line, opcodes, registers)

    return registers


def evaluate(instruction, in_a, in_b, out, opcodes, registers):
    """Evaluate one instruction"""
    match (opcodes.get(instruction, ""), in_a, in_b, out):
        case ("addr", reg_a, reg_b, out_c):
            return registers | {out_c: registers[reg_a] + registers[reg_b]}
        case ("addi", reg_a, val_b, out_c):
            return registers | {out_c: registers[reg_a] + val_b}
        case ("mulr", reg_a, reg_b, out_c):
            return registers | {out_c: registers[reg_a] * registers[reg_b]}
        case ("muli", reg_a, val_b, out_c):
            return registers | {out_c: registers[reg_a] * val_b}
        case ("banr", reg_a, reg_b, out_c):
            return registers | {out_c: registers[reg_a] & registers[reg_b]}
        case ("bani", reg_a, val_b, out_c):
            return registers | {out_c: registers[reg_a] & val_b}
        case ("borr", reg_a, reg_b, out_c):
            return registers | {out_c: registers[reg_a] | registers[reg_b]}
        case ("bori", reg_a, val_b, out_c):
            return registers | {out_c: registers[reg_a] | val_b}
        case ("setr", reg_a, _, out_c):
            return registers | {out_c: registers[reg_a]}
        case ("seti", val_a, _, out_c):
            return registers | {out_c: val_a}
        case ("gtir", val_a, reg_b, out_c):
            return registers | {out_c: val_a > registers[reg_b]}
        case ("gtri", reg_a, val_b, out_c):
            return registers | {out_c: registers[reg_a] > val_b}
        case ("gtrr", reg_a, reg_b, out_c):
            return registers | {out_c: registers[reg_a] > registers[reg_b]}
        case ("eqir", val_a, reg_b, out_c):
            return registers | {out_c: val_a == registers[reg_b]}
        case ("eqri", reg_a, val_b, out_c):
            return registers | {out_c: registers[reg_a] == val_b}
        case ("eqrr", reg_a, reg_b, out_c):
            return registers | {out_c: registers[reg_a] == registers[reg_b]}
        case _:
            print(f"unknown instruction: {opcodes[instruction]} ({instruction})")
            return registers


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
