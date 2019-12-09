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
        self.relative_base = 0

    def op_add(self, params, input):
        (val1, _), (val2, _), (_, pos) = params
        self.set_value(pos, val1 + val2)

    def op_multiply(self, params, input):
        (val1, _), (val2, _), (_, pos) = params
        self.set_value(pos, val1 * val2)

    def op_input(self, params, input):
        (_, pos), = params
        self.set_value(pos, next(self.input))

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
        self.set_value(pos, 1 if val1 < val2 else 0)

    def op_equals(self, params, input):
        (val1, _), (val2, _), (_, pos) = params
        self.set_value(pos, 1 if val1 == val2 else 0)

    def op_adjust_relative(self, params, input):
        (val, _), = params
        self.relative_base += val

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
        9: OpCode(9, "adj_rel", op_adjust_relative, 1),
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

    def get_params(self, pointer, program, param_modes):
        param_list = []
        for ptr, param_mode in enumerate(param_modes, start=pointer):
            value = self.get_value(ptr)
            if param_mode == "0":
                param = self.get_value(value)
            elif param_mode == "1":
                param = value
            elif param_mode == "2":
                value += self.relative_base
                param = self.get_value(value)
            else:
                raise ValueError(f"Unknown parameter mode: {param_mode!r}")
            param_list.append((param, value))
        return param_list

    def get_value(self, pointer=None):
        pointer = self.pointer if pointer is None else pointer
        if pointer >= len(self.program):
            self.program.extend([0] * (pointer - len(self.program) + 1))
        return self.program[pointer]

    def set_value(self, pointer, value):
        if pointer >= len(self.program):
            self.program.extend([0] * (pointer - len(self.program) + 1))

        self.program[pointer] = value
