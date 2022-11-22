"""AoC 13, 2015: Knights of the Dinner Table"""

# Standard library imports
import itertools
import pathlib
import sys

import parse

HAPPINESS_PATTERN = parse.compile(
    "{name} would {gain_lose} {value:d} happiness units by sitting next to {other}."
)


def parse(puzzle_input):
    """Parse input"""
    gain_lose = {"gain": 1, "lose": -1}
    family = {}
    for happiness in puzzle_input.split("\n"):
        match = HAPPINESS_PATTERN.parse(happiness)
        neighbors = family.setdefault(match["name"], {})
        neighbors[match["other"]] = gain_lose[match["gain_lose"]] * match["value"]
    return family


def part1(data):
    """Solve part 1"""
    return most_happiness(data)


def part2(data):
    """Solve part 2"""
    return most_happiness(data, circle=False)


def most_happiness(family, circle=True):
    """Calculate the happiness of the best seating.

    ## Example:

    >>> family = {
    ...     "A": {"B": 13, "C": 55, "D": -4},
    ...     "B": {"A": 42, "C": -19, "D": 99},
    ...     "C": {"A": -4, "B": 44, "D": 16},
    ...     "D": {"A": 64, "B": -2, "C": 32},
    ... }
    >>> most_happiness(family)
    251
    """
    members = list(family.keys())
    head = members[0]
    return max(
        total_happiness(family, seating, circle=circle)
        for seating in itertools.permutations(members)
        if not circle or seating[0] == head
    )


def total_happiness(family, seating, circle=True):
    """Calculate total happiness for a given seating.

    ## Example:

    >>> family = {
    ...     "A": {"B": 13, "C": 55, "D": -4},
    ...     "B": {"A": 42, "C": -19, "D": 99},
    ...     "C": {"A": -4, "B": 44, "D": 16},
    ...     "D": {"A": 64, "B": -2, "C": 32},
    ... }
    >>> total_happiness(family, ("A", "B", "C", "D"))
    188
    >>> total_happiness(family, ("A", "B", "C", "D"), circle=False)
    128
    """
    return sum(
        family[right][left] + family[left][right]
        for right, left in zip(seating, seating[1:] + ((seating[0],) if circle else ()))
    )


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
