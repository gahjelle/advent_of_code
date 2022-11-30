"""AoC 24, 2021: Arithmetic Logic Unit."""

# Standard library imports
import pathlib
import sys
from dataclasses import dataclass


@dataclass
class Constraint:
    first: int
    second: int
    diff: int

    def deduce_max(self, digits):
        """The largest digits satisying the constraint."""
        if self.diff > 0:
            digits[self.first] = 9 - self.diff
            digits[self.second] = 9
        else:
            digits[self.first] = 9
            digits[self.second] = 9 + self.diff

    def deduce_min(self, digits):
        """The smallest digits satisying the constraint."""
        if self.diff > 0:
            digits[self.first] = 1
            digits[self.second] = 1 + self.diff
        else:
            digits[self.first] = 1 - self.diff
            digits[self.second] = 1


def parse_data(puzzle_input):
    """Parse input."""
    program = [line.split() for line in puzzle_input.split("\n")]
    return find_constraints([minimize(subprogram) for subprogram in decompose(program)])


def part1(data):
    """Solve part 1."""
    digits = [None] * (len(data) * 2)
    for constraint in data:
        constraint.deduce_max(digits)

    return int("".join(str(digit) for digit in digits))


def part2(data):
    """Solve part 2."""
    digits = [None] * (len(data) * 2)
    for constraint in data:
        constraint.deduce_min(digits)

    return int("".join(str(digit) for digit in digits))


def decompose(program):
    """The program consists of 14 subprograms, each starting with an inp w
    instruction."""
    subprograms = []
    for instruction in program:
        if instruction[0] == "inp":
            subprogram = []
            subprograms.append(subprogram)
        subprogram.append(instruction)
    return subprograms


def minimize(program):
    """Get the only changing arguments used in a subprogram.

    Each subprogram consists of the same 18 lines, with different arguments only
    in line 4, 5, and 15:

         0: inp w
         1: mul x 0
         2: add x z
         3: mod x 26
         4: div z <Z_DIV>  # 1 or 26
         5: add x <X_ADD>  # -14, -13, ..., -5, or 12, 13, ..., 15
         6: eql x w
         7: eql x 0
         8: mul y 0
         9: add y 25
        10: mul y x
        11: add y 1
        12: mul z y
        13: mul y 0
        14: add y w
        15: add y <Y_ADD>  # 1, 2, ..., 15
        16: mul y x
        17: add z y
    """
    return int(program[4][2]), int(program[5][2]), int(program[15][2])


def find_constraints(program):
    """Convert the program into digit constraints.

    Think of z as a stack for base 26 numbers. We can translate each subprogram
    as follows:

        next_digit -> w
        peek(Z) + X_ADD -> x
        if Z_DIV == 26:
            pop(Z)
        if x != w:
            push(Z, Y_ADD)

    We need the stack to be empty (z = 0) after the program has run. In practice,
    that means that we want to do as many pops as pushes on the stack.

    Looking at the program, we see that there are 7 subprograms with Z_DIV == 1
    and 7 subprogram with Z_DIV == 26. Additionally, each time Z_DIV == 1,
    X_ADD > 10 so that x is necessarily different from w, while X_ADD < 0 each
    time Z_DIV == 26.

    To empty the stack we therefore need x == w each time X_ADD < 0. This creates
    some constraints on our digits.
    """
    constraints = []
    stack, idx_stack = [], []
    for idx, (z_div, x_add, y_add) in enumerate(program):
        x = x_add + stack[-1] if stack else 0
        if z_div == 26:
            stack.pop()
            match_idx = idx_stack.pop()
        if x_add > 0:
            stack.append(y_add)
            idx_stack.append(idx)
        else:
            constraints.append(Constraint(match_idx, idx, x))
    return constraints


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
