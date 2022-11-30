"""AoC 5, 2021: Hydrothermal Venture"""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return [
        [int(xy) for points in line.split(" -> ") for xy in points.split(",")]
        for line in puzzle_input.split("\n")
    ]


def part1(data):
    """Solve part 1"""
    return count_overlaps(
        line for line in data if line[0] == line[2] or line[1] == line[3]
    )


def part2(data):
    """Solve part 2"""
    return count_overlaps(data)


def count_overlaps(lines):
    """Count overlaps between a list of lines

    ## Example:

    >>> count_overlaps([[3, 3, 6, 6], [3, 3, 6, 3], [6, 6, 6, 3]])
    3
    """
    return sum(
        overlaps >= 2
        for overlaps in collections.Counter(
            point for line in lines for point in points(line)
        ).values()
    )


def points(line):
    """List all points making up a line

    ## Examples:

    >>> list(points([0, 3, 3, 3]))
    [(0, 3), (1, 3), (2, 3), (3, 3)]
    >>> list(points([3, 3, 3, 0]))
    [(3, 3), (3, 2), (3, 1), (3, 0)]
    >>> list(points([1, 2, 3, 4]))
    [(1, 2), (2, 3), (3, 4)]
    """
    match line:
        case [x1, y1, x2, y2] if x1 == x2:
            yield from ((x1, y) for y in coords(y1, y2))
        case [x1, y1, x2, y2] if y1 == y2:
            yield from ((x, y1) for x in coords(x1, x2))
        case [x1, y1, x2, y2]:
            yield from ((x, y) for x, y in zip(coords(x1, x2), coords(y1, y2)))
        case _:
            raise ValueError(f"invalid line: {line}")


def coords(start, stop):
    """List coordinates between start and stop, inclusive.

    ## Examples:

    >>> list(coords(0, 3))
    [0, 1, 2, 3]
    >>> list(coords(2, -2))
    [2, 1, 0, -1, -2]
    """
    if start <= stop:
        yield from range(start, stop + 1)
    else:
        yield from range(start, stop - 1, -1)


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
