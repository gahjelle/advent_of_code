"""AoC 2019: IntCode Computer"""

# Standard library imports
from dataclasses import dataclass
from typing import Callable, NamedTuple

OPCODES = {}


def register_command(code, description, num_params):
    """Decorator for registering an IntCode command"""

    def _register(func):
        OPCODES[code] = OpCode(code, description, func, num_params)

    return _register


class OpCode(NamedTuple):
    """General opcode information"""

    code: int
    description: str
    operation: Callable[[int, int], int]
    num_params: int


@dataclass
class ExitType:
    """Marker for when to exit the program"""


Exit = ExitType()


@dataclass
class IntcodeComputer:
    program: list[int]
    pointer: int = 0
    debug: bool = False

    def __post_init__(self):
        """Copy program to avoid any mutation"""
        self.program = self.program.copy()

    def run(self):
        """Run program to end"""
        next(self)

    def __next__(self):
        """Run program to end"""
        while True:
            output = self.step()
            if output is Exit:
                return None
            elif output is not None:
                return output

    def step(self):
        """Take one step in a program"""
        opcode = OPCODES[self.program[self.pointer]]
        params = self.program[self.pointer + 1 : self.pointer + 1 + opcode.num_params]
        output = opcode.operation(self, params)
        if self.debug:
            print(f"{opcode.code:2d}: {params} -> {output}")

        self.pointer += 1 + opcode.num_params

        return output

    @register_command(1, "add", 3)
    def op_add(self, params):
        """Add two numbers"""
        first, second, store = params
        self.program[store] = self.program[first] + self.program[second]

    @register_command(2, "mul", 3)
    def op_add(self, params):
        """Multiply two numbers"""
        first, second, store = params
        self.program[store] = self.program[first] * self.program[second]

    @register_command(99, "exit", 0)
    def op_exit(self, _params):
        """Exit the program"""
        return Exit


def run_program(program, debug=False):
    """Run an intcode program and return the final state

    >>> run_program([1, 0, 0, 0, 99])
    [2, 0, 0, 0, 99]

    >>> run_program([2, 3, 0, 3, 99])
    [2, 3, 0, 6, 99]
    """
    computer = IntcodeComputer(program, debug=debug)
    computer.run()
    return computer.program
