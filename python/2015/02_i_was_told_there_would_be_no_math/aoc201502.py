"""AoC 2, 2015: I Was Told There Would Be No Math"""

# Standard library imports
import math
import pathlib
import sys
from typing import NamedTuple

# Third party imports
import parse

PARSER = parse.compile("{length:d}x{width:d}x{height:d}")


class Present(NamedTuple):
    """Dimension of present"""

    length: int
    width: int
    height: int

    @classmethod
    def from_string(cls, present):
        """Convert present description to Present object

        ## Example:

        >>> Present.from_string("12x9x32")
        Present(length=12, width=9, height=32)
        """
        return cls(**PARSER.parse(present).named)


def parse(puzzle_input):
    """Parse input"""
    return [Present.from_string(present) for present in puzzle_input.split()]


def part1(data):
    """Solve part 1"""
    return sum(wrapping_paper(present) for present in data)


def part2(data):
    """Solve part 2"""
    return sum(ribbon(present) for present in data)


def wrapping_paper(present):
    """Amount of wrapping paper for one present

    ## Example:

    >>> wrapping_paper(Present(length=12, width=9, height=32))
    1668
    """
    return (
        2 * present.length * present.width
        + 2 * present.length * present.height
        + 2 * present.width * present.height
        + math.prod(present) // max(present)
    )


def ribbon(present):
    """Amount of ribbon for one present

    ## Example:

    >>> ribbon(Present(length=12, width=9, height=32))
    3498
    """
    return 2 * (sum(present) - max(present)) + math.prod(present)


def solve(puzzle_input):
    """Solve the puzzle for the given puzzle_input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
