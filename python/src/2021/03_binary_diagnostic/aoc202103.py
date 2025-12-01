"""AoC 3, 2021: Binary Diagnostic."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [[int(bn) for bn in row] for row in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1."""
    columns = transpose(data)

    gamma, epsilon = [], []
    for column in columns:
        most_common = 1 if 2 * sum(column) > len(column) else 0
        gamma.append(most_common)
        epsilon.append(1 - most_common)

    return bin2int(gamma) * bin2int(epsilon)


def part2(data):
    """Solve part 2."""
    oxygen = filter_rows(data, 1)
    co2 = filter_rows(data, 0)

    return bin2int(oxygen) * bin2int(co2)


def transpose(report):
    """Transpose nested lists of lists.

    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    return [list(col) for col in zip(*report)]


def filter_rows(rows, high_bit):
    """Filter rows column by column based on the high_bit.

    >>> rows = [[1, 0, 1], [0, 1, 1], [1, 1, 0]]
    >>> filter_rows(rows, 1)
    [1, 1, 0]

    >>> filter_rows(rows, 0)
    [0, 1, 1]
    """
    col = 0
    while len(rows) > 1:
        match transpose(rows)[col]:
            case column if 2 * sum(column) >= len(column):
                matcher = high_bit
            case column:
                matcher = 1 - high_bit

        rows = [row for row, item in zip(rows, column) if item == matcher]
        col += 1

    return rows[0]


def bin2int(binary):
    """Convert a sequence of binary digits into a base 10 integer.

    >>> bin2int([1, 0, 1, 1, 0, 0])
    44
    """
    return int("".join(str(b) for b in binary), 2)


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
