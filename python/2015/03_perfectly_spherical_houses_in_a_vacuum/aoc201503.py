"""AoC 3, 2015: Perfectly Spherical Houses in a Vacuum."""

# Standard library imports
import pathlib
import sys

DIRECTIONS = {">": (1, 0), "<": (-1, 0), "^": (0, 1), "v": (0, -1)}


def parse_data(puzzle_input):
    """Parse input."""
    return [DIRECTIONS[arrow] for arrow in puzzle_input]


def part1(data):
    """Solve part 1."""
    return len(visit(data))


def part2(data):
    """Solve part 2."""
    santa = visit(data[::2])
    robosanta = visit(data[1::2])

    return len(santa | robosanta)


def visit(moves):
    """Visit houses based on moves.

    ## Example:

    >>> sorted(visit([(1, 0), (1, 0), (0, 1), (0, -1), (0, -1), (-1, 0), (0, 1)]))
    [(0, 0), (1, -1), (1, 0), (2, -1), (2, 0), (2, 1)]

    >>> sorted({(0, 0), (1, 0), (2, 0), (2, 1), (2, 0), (2, -1), (1, -1), (1, 0)})
    [(0, 0), (1, -1), (1, 0), (2, -1), (2, 0), (2, 1)]
    """
    pos_x, pos_y = 0, 0
    houses = {(pos_x, pos_y)}

    for dx, dy in moves:
        pos_x, pos_y = pos_x + dx, pos_y + dy
        houses.add((pos_x, pos_y))

    return houses


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
