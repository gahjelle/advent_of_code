"""AoC day 6, 2025: Trash Compactor."""

import math


def parse_data(puzzle_input: str) -> tuple[list[str], list[str]]:
    """Parse puzzle input."""
    *numbers, operators = puzzle_input.splitlines()
    return operators.split(), numbers


def part1(data: tuple[list[str], list[str]]) -> int:
    """Solve part 1."""
    operators, lines = data
    flipped = zip(*[[int(number) for number in line.split()] for line in lines])
    operands = [list(numbers) for numbers in flipped]
    return calculate(operators, operands)


def part2(data: tuple[list[str], list[str]]) -> int:
    """Solve part 2."""
    operators, lines = data
    flipped = "\n".join("".join(line).strip() for line in list(zip(*lines))[::-1])
    operands = [
        [int(number) for number in group.split()] for group in flipped.split("\n\n")
    ]
    return calculate(operators[::-1], operands)


def calculate(operators: list[str], operands: list[list[int]]) -> int:
    """Calculate the grand total."""
    return sum(
        sum(numbers) if operator == "+" else math.prod(numbers)
        for operator, numbers in zip(operators, operands)
    )
