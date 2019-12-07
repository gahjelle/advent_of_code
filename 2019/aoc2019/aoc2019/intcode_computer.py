"""IntCode Computer

Part of Advent of Code 2019
Programmed by Geir Arne Hjelle
"""
import sys
from dataclasses import dataclass
from typing import Callable, NamedTuple

# Simple debug command
debug = print if "--debug" in sys.argv else lambda *_: None


@dataclass
class ExitType:
    """Marker for when to exit the program"""


Exit = ExitType()


@dataclass
class Jump:
    """Marker for jumping to a new pointer"""

    pointer: int


class OpCode(NamedTuple):
    code: int
    description: str
    operation: Callable[[int, int], int]
    num_params: int


class IntcodeComputer:
    def __init__(self, program, input):
        self.program = program.copy()
        self.input = input
        self.pointer = 0

    def op_add(self, params, input):
        (val1, _), (val2, _), (_, pos) = params
        self.program[pos] = val1 + val2

    def op_multiply(self, params, input):
        (val1, _), (val2, _), (_, pos) = params
        self.program[pos] = val1 * val2

    def op_input(self, params, input):
        (_, pos), = params
        self.program[pos] = next(self.input)

    def op_output(self, params, input):
        (val, _), = params
        return val

    def op_jump_true(self, params, input):
        (val1, _), (val2, _) = params
        if val1 != 0:
            return Jump(val2)

    def op_jump_false(self, params, input):
        (val1, _), (val2, _) = params
        if val1 == 0:
            return Jump(val2)

    def op_less_than(self, params, input):
        (val1, _), (val2, _), (_, pos) = params
        self.program[pos] = 1 if val1 < val2 else 0

    def op_equals(self, params, input):
        (val1, _), (val2, _), (_, pos) = params
        self.program[pos] = 1 if val1 == val2 else 0

    OPCODES = {
        99: OpCode(99, "exit", lambda self, pms, ip: Exit, 0),
        1: OpCode(1, "+", op_add, 3),
        2: OpCode(2, "x", op_multiply, 3),
        3: OpCode(3, "input", op_input, 1),
        4: OpCode(4, "output", op_output, 1),
        5: OpCode(5, "jmp_true", op_jump_true, 2),
        6: OpCode(6, "jmp_false", op_jump_false, 2),
        7: OpCode(7, "<", op_less_than, 3),
        8: OpCode(8, "==", op_equals, 3),
    }

    def run(self):
        next(self)

    def __next__(self):
        while True:
            code_str = str(self.program[self.pointer])
            opcode = self.OPCODES[int(code_str[-2:])]
            param_modes = (code_str[:-2][::-1] + "0" * 4)[: opcode.num_params]
            params = self.get_params(self.pointer + 1, self.program, param_modes)
            output = opcode.operation(self, params, input)

            debug(f"Running {opcode.description} on {params} -> {output!r}")

            if output is Exit:
                return

            if isinstance(output, Jump):
                self.pointer = output.pointer
                continue

            self.pointer += 1 + opcode.num_params

            if output is not None:
                return output

    @staticmethod
    def get_params(pointer, program, param_modes):
        return [
            (program[pt] if pm == "1" else program[program[pt]], program[pt])
            for pt, pm in enumerate(param_modes, start=pointer)
        ]
