"""AoC 13, 2024: Claw Contraption."""

# Standard library imports
import pathlib
import sys
from typing import NamedTuple

# Third party imports
import parse

BUTTON = parse.compile("Button {}: X{x:d}, Y{y:d}")
PRIZE = parse.compile("Prize: X={x:d}, Y={y:d}")


class Coordinate(NamedTuple):
    """2D coordinates"""

    x: int
    y: int

    def __add__(self, scalar):
        """Add a scalar to coordinates"""
        cls = type(self)
        return cls(x=self.x + scalar, y=self.y + scalar)


def parse_data(puzzle_input):
    """Parse input."""
    return [parse_machine(machine) for machine in puzzle_input.split("\n\n")]


def parse_machine(puzzle_input):
    """Parse one machine"""
    return [
        Coordinate(**pattern.parse(line).named)
        for pattern, line in zip([BUTTON, BUTTON, PRIZE], puzzle_input.split("\n"))
    ]


def part1(machines):
    """Solve part 1."""
    return sum(
        play_machine(button_a, button_b, prize)
        for button_a, button_b, prize in machines
    )


def part2(machines):
    """Solve part 2."""
    return sum(
        play_machine(button_a, button_b, prize + 10_000_000_000_000)
        for button_a, button_b, prize in machines
    )


def play_machine(button_a, button_b, prize, token_a=3, token_b=1):
    """Calculate cost of winning on one machine

    Solve for A and B in the two equations:

        a_x * A + b_x * B = p_x
        a_y * A + b_y * B = p_y

    ## Example:

    >>> play_machine(Coordinate(94, 34), Coordinate(22, 67), Coordinate(8400, 5400))
    280
    """
    det = button_a.x * button_b.y - button_a.y * button_b.x
    push_a = (button_b.y * prize.x - button_b.x * prize.y) // det
    push_b = (button_a.x * prize.y - button_a.y * prize.x) // det
    if (  # Check if the integer solution solves the original equation
        push_a * button_a.x + push_b * button_b.x == prize.x
        and push_a * button_a.y + push_b * button_b.y == prize.y
    ):
        return push_a * token_a + push_b * token_b
    return 0


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
