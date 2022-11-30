"""AoC 8, 2017: I Heard You Like Registers"""

# Standard library imports
import collections
import pathlib
import sys
from typing import NamedTuple

# Third party imports
import parse

CHECKS = {
    "==": lambda n1, n2: n1 == n2,
    "!=": lambda n1, n2: n1 != n2,
    ">": lambda n1, n2: n1 > n2,
    ">=": lambda n1, n2: n1 >= n2,
    "<": lambda n1, n2: n1 < n2,
    "<=": lambda n1, n2: n1 <= n2,
}
PARSER = parse.compile(
    "{register} {instruction} {value:d} if {cond_reg} {cond_op} {cond_val:d}"
)


class Instruction(NamedTuple):
    """Single instruction"""

    register: str
    instruction: str
    value: int
    cond_reg: str
    cond_op: str
    cond_val: int


class Registers(collections.UserDict):
    """State of registers"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max = 0

    def check(self, register, operator, value):
        return CHECKS[operator](self[register], value)

    def process(self, lines):
        for line in lines:
            self.process_line(line)

    def process_line(self, line):
        if not self.check(line.cond_reg, line.cond_op, line.cond_val):
            return

        if line.instruction == "inc":
            self[line.register] += line.value
        elif line.instruction == "dec":
            self[line.register] -= line.value

        if self[line.register] > self.max:
            self.max = self[line.register]

    def __missing__(self, key):
        self.data[key] = 0
        return self.data[key]


def parse_data(puzzle_input):
    """Parse input"""
    return [Instruction(**PARSER.parse(ln).named) for ln in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    registers = Registers()
    registers.process(data)

    return max(registers.values())


def part2(data):
    """Solve part 2"""
    registers = Registers()
    registers.process(data)

    return registers.max


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
