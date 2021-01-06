"""Assembunny Computer

Part of Advent of Code 2016
Programmed by Geir Arne Hjelle
"""

# Standard library imports
import sys
from dataclasses import dataclass
from typing import Union

# Simple debug command
debug = print if "--debug_code" in sys.argv else lambda *_: None


@dataclass
class Instruction:
    code: str
    x: Union[str, int]
    y: Union[str, int] = ""

    def __post_init__(self):
        """Convert x and y parameters to numbers if possible

        Modify instruction code so that X and Y suffixes indicate instructions
        using registers.
        """
        try:
            self.x = int(self.x)
        except ValueError:
            if self.x:
                self.code += "X"

        try:
            self.y = int(self.y)
        except ValueError:
            if self.y:
                self.code += "Y"

        self.tpl = self.code, self.x, self.y

    @classmethod
    def toggle(cls, instruction):
        """Toggle instruction

        - For one-argument instructions, inc becomes dec, and all other
          one-argument instructions become inc.
        - For two-argument instructions, jnz becomes cpy, and all other
          two-instructions become jnz.
        - The arguments of a toggled instruction are not affected.
        """
        # One-argument instruction
        if not instruction.y:
            toggled = "dec" if instruction.code[:3] == "inc" else "inc"
            return cls(toggled, instruction.x)

        # Two-argumnent instruction
        else:
            toggled = "cpy" if instruction.code[:3] == "jnz" else "jnz"
            return cls(toggled, instruction.x, instruction.y)


class AssembunnyComputer:
    def __init__(self, program, max_outputs=50, **initial_registers):
        """Initialize computer"""
        self.program = [Instruction(*ln.split()) for ln in program.strip().split("\n")]
        self.initial_registers = {"a": 0, "b": 0, "c": 0, "d": 0, **initial_registers}
        self.max_outputs = max_outputs

    def run(self):
        """Run the program"""
        registers = self.initial_registers.copy()
        outputs = registers["outputs"] = []
        pointer = 0
        num_instructions = len(self.program)

        while 0 <= pointer < num_instructions:
            instruction, ix, iy = self.program[pointer].tpl
            jump = 1

            if instruction == "cpyXY":
                registers[iy] = registers[ix]

            elif instruction == "cpyY":
                registers[iy] = ix

            elif instruction == "incX":
                registers[ix] += 1

            elif instruction == "decX":
                registers[ix] -= 1

            elif instruction == "jnz":
                if ix:
                    jump = iy

            elif instruction == "jnzX":
                if registers[ix]:
                    jump = iy

            elif instruction == "jnzY":
                if ix:
                    jump = registers[iy]

            elif instruction == "tglX":
                tgl_idx = pointer + registers[ix]
                if 0 <= tgl_idx < num_instructions:
                    self.program[tgl_idx] = Instruction.toggle(self.program[tgl_idx])

            elif instruction == "outX":
                outputs.append(registers[ix])
                if len(outputs) >= self.max_outputs:
                    return registers

            pointer += jump

        return registers
