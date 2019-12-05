"""Sunny With A Chance of Asteroids

Advent of Code 2019, day 5
Solution by Geir Arne Hjelle, 2019-12-05
"""
import pathlib
import sys
from typing import Callable, NamedTuple


class Exit:
    """Marker for when to exit the program"""


class Jump:
    """Marker for jumping to a new pointer"""

    def __init__(self, new_pointer):
        self.pointer = new_pointer


class OpCode(NamedTuple):
    code: int
    description: str
    operation: Callable[[int, int], int]
    num_params: int


class ParamMode(NamedTuple):
    ...


def op_add(program, params, input, pointer):
    (val1, _), (val2, _), (_, pos) = params
    program[pos] = val1 + val2


def op_multiply(program, params, input, pointer):
    (val1, _), (val2, _), (_, pos) = params
    program[pos] = val1 * val2


def op_input(program, params, input, pointer):
    (_, pos), = params
    program[pos] = input


def op_output(program, params, input, pointer):
    (val, _), = params
    return val


def op_jump_true(program, params, input, pointer):
    (val1, _), (val2, _) = params
    if val1 != 0:
        return Jump(val2)


def op_jump_false(program, params, input, pointer):
    (val1, _), (val2, _) = params
    if val1 == 0:
        return Jump(val2)


def op_less_than(program, params, input, pointer):
    (val1, _), (val2, _), (_, pos) = params
    program[pos] = 1 if val1 < val2 else 0


def op_equals(program, params, input, pointer):
    (val1, _), (val2, _), (_, pos) = params
    program[pos] = 1 if val1 == val2 else 0


OPCODES = {
    99: OpCode(99, "exit", lambda prg, pms, ip, ptr: Exit, 0),
    1: OpCode(1, "+", op_add, 3),
    2: OpCode(2, "x", op_multiply, 3),
    3: OpCode(3, "input", op_input, 1),
    4: OpCode(4, "output", op_output, 1),
    5: OpCode(5, "jmp_true", op_jump_true, 2),
    6: OpCode(6, "jmp_false", op_jump_false, 2),
    7: OpCode(7, "<", op_less_than, 3),
    8: OpCode(8, "==", op_equals, 3),
}


def run_program(program, input=1):
    codes = program.copy()
    outputs = []

    pointer = 0
    while True:
        opcode, param_modes = parse_opcode(codes[pointer], codes)
        params = get_params(pointer + 1, codes, param_modes)
        output = opcode.operation(codes, params, input, pointer)
        debug(f"Running {opcode.description} on {params} -> {output!r}")

        if output is Exit:
            return outputs

        if isinstance(output, Jump):
            pointer = output.pointer
            continue

        if output is not None:
            outputs.append(output)

        pointer += 1 + opcode.num_params


def parse_opcode(code, program):
    code_str = str(code)
    opcode = OPCODES[int(code_str[-2:])]
    param_modes = (code_str[:-2][::-1] + "0" * opcode.num_params)[: opcode.num_params]

    return opcode, param_modes


def get_params(pointer, program, param_modes):
    return [
        (program[pt] if pm == "1" else program[program[pt]], program[pt])
        for pt, pm in enumerate(param_modes, start=pointer)
    ]


def main():
    for file_path in [pathlib.Path(p) for p in sys.argv[1:] if not p.startswith("-")]:
        print(f"\n{file_path}:")
        program = [int(c) for c in file_path.read_text().strip().split(",")]

        # Part 1
        part_1 = run_program(program, input=1)
        print(f"Diagnostic code for Air Conditioner: {part_1[-1]}")

        # Part 2
        part_2 = run_program(program, input=5)
        print(f"Diagnostic code for Thermal Radiator Controller: {part_2[0]}")


if __name__ == "__main__":
    debug = print if "--debug" in sys.argv else lambda *_: None
    main()
