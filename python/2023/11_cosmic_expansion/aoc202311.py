"""AoC 11, 2023: Cosmic Expansion."""

# Standard library imports
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return {
        (row, col)
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
        if char == "#"
    }


def part1(galaxies):
    """Solve part 1."""
    expanded = expand(galaxies, 2)
    return sum(
        manhattan(first, second)
        for first, second in itertools.combinations(expanded, 2)
    )


def part2(galaxies, step=1_000_000):
    """Solve part 2."""
    expanded = expand(galaxies, step)
    return sum(
        manhattan(first, second)
        for first, second in itertools.combinations(expanded, 2)
    )


def manhattan(first, second):
    """Calculate the Manhattan distance.

    ## Example:

    >>> manhattan((3, -2), (1, 5))
    9
    """
    return abs(first[0] - second[0]) + abs(first[1] - second[1])


def expand(galaxies, step):
    """Expand galaxies.

    Empty rows and columns are replaced by step empty rows and columns

    ## Example:

    >>> sorted(
    ...     expand({(0, 3), (1, 7), (2, 0), (4, 6), (5, 1), (6, 9), (8, 7), (9, 4)}, 2)
    ... )
    [(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 5)]
    """
    max_row = max(row for row, _ in galaxies) + 1
    rows = set(range(max_row)) - {row for row, _ in galaxies}
    expand_rows = {
        row: sum(r < row for r in rows) * (step - 1) for row in range(max_row)
    }

    max_col = max(col for _, col in galaxies) + 1
    cols = set(range(max_col)) - {col for _, col in galaxies}
    expand_cols = {
        col: sum(c < col for c in cols) * (step - 1) for col in range(max_col)
    }

    return {(row + expand_rows[row], col + expand_cols[col]) for row, col in galaxies}


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
