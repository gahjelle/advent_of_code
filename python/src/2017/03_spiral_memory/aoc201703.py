"""AoC 3, 2017: Spiral Memory."""

# Standard library imports
import math
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return int(puzzle_input)


def part1(data):
    """Solve part 1."""
    return sum(abs(xy) for xy in spiral_to_xy(data))


def part2(data):
    """Solve part 2."""
    for number in spiral_sequence():
        if number > data:
            return number


def spiral_to_xy(index):
    """Convert spiral index to xy-coordinates.

    >>> spiral_to_xy(1)
    (0, 0)

    >>> spiral_to_xy(2)
    (1, 0)

    >>> spiral_to_xy(3)
    (1, 1)

    >>> spiral_to_xy(6)
    (-1, 0)

    >>> spiral_to_xy(22)
    (-1, -2)

    >>> spiral_to_xy(25)
    (2, -2)
    """
    spiral = (1 + math.isqrt(index - 1)) // 2

    corner_idx = (2 * spiral - 1) ** 2
    corner_xy = spiral - spiral * 1j
    direction = 1j

    while index > corner_idx + 2 * spiral:
        corner_idx += 2 * spiral
        corner_xy += 2 * spiral * direction
        direction *= 1j

    xy = corner_xy + (index - corner_idx) * direction
    return int(xy.real), int(xy.imag)


def spiral_sequence():
    """Generate spiral sequence.

    >>> spiral = spiral_sequence()
    >>> next(spiral)
    1

    >>> next(spiral)
    2

    >>> next(spiral)
    4

    >>> next(spiral)
    5
    """
    neighbors = (1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j, -1j, 1 - 1j)
    grid = {0: 1}

    xy = 0
    step = 1
    while True:
        xy += step
        numbers = [number for dxy in neighbors if (number := grid.get(xy + dxy))]
        grid[xy] = sum(numbers)
        yield grid[xy]

        if len(numbers) < 3:
            step *= 1j


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
