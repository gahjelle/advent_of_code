"""AoC 2018: Wrist Device"""

# Standard library imports
import collections

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


def run_program(program, reg_pointer=99):
    """Run one program"""
    registers = collections.defaultdict(int)
    pointer = registers[reg_pointer]
    while pointer < len(program):
        registers = evaluate(registers | {reg_pointer: pointer}, *program[pointer])
        pointer = registers[reg_pointer] + 1
    return registers


def evaluate(registers, instruction, in_a, in_b, out):
    """Evaluate one instruction"""
    match (instruction, in_a, in_b, out):
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
            print(f"unknown instruction: {instruction}")
            return registers
