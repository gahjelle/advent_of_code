"""AoC 2019: IntCode Computer"""

# Standard library imports
from dataclasses import dataclass, field
from typing import Callable

OPCODES = {}


def register_command(code, description, num_params):
    """Decorator for registering an IntCode command"""

    def _register(func):
        OPCODES[code] = OpCode(code, description, func, num_params)

    return _register


@dataclass
class OpCode:
    """General opcode information"""

    code: int
    description: str
    operation: Callable[[int, int], int]
    num_params: int


@dataclass
class Jump:
    """Marker for jumping to a new location in the program"""

    pointer: int


@dataclass
class Store:
    """Marker for storing a value in the program"""

    position: int
    value: int


@dataclass
class ExitType:
    """Marker for when to exit the program"""


Exit = ExitType()


@dataclass
class IntcodeComputer:
    program: list[int]
    input: list[int] = field(default_factory=list)
    pointer: int = 0
    debug: bool = False

    def __post_init__(self):
        """Copy program to avoid any mutation"""
        self.program = self.program.copy()
        self._input = iter(self.input)

    def run(self):
        """Run program to end"""
        outputs = []
        while True:
            try:
                output = next(self)
            except StopIteration:
                break
            if output is None:
                break
            outputs.append(output)
        return outputs

    def __next__(self):
        """Run program to next output"""
        while True:
            output = self.step()
            if output is Exit:
                raise StopIteration
            elif output is not None:
                return output

    def __iter__(self):
        """Iterate over computer to iterate over outputs"""
        return self

    def step(self):
        """Take one step in a program"""
        opcode, params = self.get_operation(self.pointer)
        output = opcode.operation(self, params)
        if self.debug:
            print(
                f"{self.program[self.pointer]:5d} ({opcode.description:^5}): "
                f"{str(params):<40} -> {output}"
            )

        self.pointer += 1 + opcode.num_params
        match output:
            case Jump(pointer):
                self.pointer = pointer
            case Store(position, value):
                self.program[position] = value
            case _:
                return output

    def get_operation(self, pointer):
        """Get opcode and parameters"""
        param_modes, code = divmod(self.program[pointer], 100)
        opcode = OPCODES[code]

        params = []
        for param in self.program[pointer + 1 : pointer + 1 + opcode.num_params]:
            param_modes, param_mode = divmod(param_modes, 10)
            match param_mode:
                case 0:
                    params.append((self.program[param], param))
                case 1:
                    params.append((param, param))
                case _:
                    raise ValueError(f"unknown parameter mode: {param_mode}")

        return opcode, params

    @register_command(1, "+", 3)
    def op_add(self, params):
        """Add two numbers"""
        (first, _), (second, _), (_, store) = params
        return Store(store, first + second)

    @register_command(2, "x", 3)
    def op_add(self, params):
        """Multiply two numbers"""
        (first, _), (second, _), (_, store) = params
        return Store(store, first * second)

    @register_command(3, "in", 1)
    def op_input(self, params):
        """Input one value"""
        ((_, store),) = params
        return Store(store, next(self._input))

    @register_command(4, "out", 1)
    def op_output(self, params):
        """Output one value"""
        ((value, _),) = params
        return value

    @register_command(5, "jmp_T", 2)
    def op_jmp_true(self, params):
        """Jump if value is non-zero"""
        ((value, _), (pos, _)) = params
        if value:
            return Jump(pos)

    @register_command(6, "jmp_F", 2)
    def op_jmp_false(self, params):
        """Jump if value is zero"""
        ((value, _), (pos, _)) = params
        if not value:
            return Jump(pos)

    @register_command(7, "<", 3)
    def op_less_than(self, params):
        """Store 1 if first number is less than second, 0 otherwise"""
        (first, _), (second, _), (_, store) = params
        return Store(store, int(first < second))

    @register_command(8, "==", 3)
    def op_equals(self, params):
        """Store 1 if first number is equal to second, 0 otherwise"""
        (first, _), (second, _), (_, store) = params
        return Store(store, int(first == second))

    @register_command(99, "exit", 0)
    def op_exit(self, _params):
        """Exit the program"""
        return Exit


def run_program(program, input=None, debug=False):
    """Run an intcode program and return the final state

    >>> run_program([1, 0, 0, 0, 99])
    [2, 0, 0, 0, 99]

    >>> run_program([2, 3, 0, 3, 99])
    [2, 3, 0, 6, 99]
    """
    computer = IntcodeComputer(program, [] if input is None else input, debug=debug)
    computer.run()
    return computer.program
