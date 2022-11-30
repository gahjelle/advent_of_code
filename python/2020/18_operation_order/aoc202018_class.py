"""AoC 18, 2020: Operation Order."""

# Standard library imports
import pathlib
import re
import sys


class EvaluatingInt(int):
    """Integers that can evaluate expressions."""

    @classmethod
    def evaluate(cls, expression):
        """Evaluate the given expression."""
        wrapped_expression = re.sub(
            r"(\d+)", rf"{cls.__name__}(\1)", expression.translate(cls.ops)
        )
        return eval(wrapped_expression)


class LeftRightInt(EvaluatingInt):
    """Integers where addition and multiplication have the same precedence."""

    ops = str.maketrans({"*": "-"})

    def __add__(self, other):
        """Make sure to return an evaluating integer."""
        cls = self.__class__
        return cls(super().__add__(other))

    def __sub__(self, other):
        """Use - for multiplication since it has the same precedence as +"""
        cls = self.__class__
        return cls(super().__mul__(other))


class PlusFirstInt(EvaluatingInt):
    """Integers where addition have higher precedence than multiplication."""

    ops = str.maketrans({"+": "*", "*": "+"})

    def __add__(self, other):
        """Make sure to return an evaluating integer."""
        cls = self.__class__
        return cls(super().__mul__(other))

    def __mul__(self, other):
        """Use * for addition since it has higher precedence than +"""
        cls = self.__class__
        return cls(super().__add__(other))


def parse_data(puzzle_input):
    """Parse input."""
    return [f"({ln})" for ln in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1."""
    return sum(LeftRightInt.evaluate(line) for line in data)


def part2(data):
    """Solve part 2."""
    return sum(PlusFirstInt.evaluate(line) for line in data)


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
