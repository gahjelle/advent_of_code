"""AoC 2, 2023: Cube Conundrum."""

# Standard library imports
import math
import pathlib
import sys

# Third party imports
import parse

GAME_PATTERN = parse.compile("Game {game:d}: {cubes}")
CUBE_PATTERNS = (
    parse.compile("{num:d} red"),
    parse.compile("{num:d} green"),
    parse.compile("{num:d} blue"),
)


def parse_data(puzzle_input):
    """Parse input."""
    return {
        match["game"]: parse_cubes(match["cubes"])
        for line in puzzle_input.split("\n")
        if (match := GAME_PATTERN.parse(line))
    }


def parse_cubes(cube_descriptions):
    """Parse cubes into tuples, in a (red, green, blue) order

    ## Examples:

    >>> parse_cubes("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    [(4, 0, 3), (1, 2, 6), (0, 2, 0)]
    """
    return [
        tuple(
            match["num"] if (match := pattern.search(description)) else 0
            for pattern in CUBE_PATTERNS
        )
        for description in cube_descriptions.split(";")
    ]


def part1(data):
    """Solve part 1."""
    bag = (12, 13, 14)
    return sum(
        id
        for id, reveals in data.items()
        if all(all(r <= b for r, b in zip(reveal, bag)) for reveal in reveals)
    )


def part2(data):
    """Solve part 2."""
    return sum(math.prod(minimum_cubes(reveals)) for reveals in data.values())


def minimum_cubes(reveals):
    """Find the minimum number of cubes necessary to support the reveals.

    ## Example:

    >>> minimum_cubes([(0, 4, 4), (1, 5, 2), (1, 0, 9), (0, 0, 1)])
    (1, 5, 9)
    """
    return tuple(max(cubes) for cubes in zip(*reveals))


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
