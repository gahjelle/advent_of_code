"""AoC 25, 2015: Let It Snow"""

# Standard library imports
import pathlib
import sys

import parse

MANUAL_PATTERN = parse.compile("Enter the code at row {row:d}, column {col:d}.")


def parse_data(puzzle_input):
    """Parse input"""
    match = MANUAL_PATTERN.search(puzzle_input)
    return match["row"], match["col"]


def part1(data):
    """Solve part 1"""
    idx_of_code = get_index(*data)
    for idx, code in enumerate(generate_codes(), start=1):
        if idx == idx_of_code:
            return code


def part2(data):
    """There is no part two"""


def get_index(row, col):
    """Find the index corresponding to a row and column.

    The index is zero-based.

    ## Examples:

    >>> get_index(1, 1)
    0
    >>> get_index(3, 4)
    18
    >>> get_index(5, 6)
    50
    """
    band = (row - 1) + (col - 1)
    first_idx = band * (band + 1) // 2
    return first_idx + (col - 1)


def generate_codes(seed=20151125):
    """Generate an infinite sequence of codes.

    ## Examples:

    >>> codes = generate_codes()
    >>> next(codes)
    31916031
    >>> next(codes)
    18749137
    >>> next(codes)
    16080970
    """
    while True:
        seed = (seed * 252533) % 33554393
        yield seed


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
