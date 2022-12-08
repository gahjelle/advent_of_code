"""AoC 8, 2022: Treetop Tree House."""

# Standard library imports
import math
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    heights_row_col = [
        [int(height) for height in line] for line in puzzle_input.split("\n")
    ]
    heights_col_row = [list(col) for col in zip(*heights_row_col)]
    return heights_row_col, heights_col_row


def part1(heights):
    """Solve part 1."""
    heights_rc, heights_cr = heights
    rows, cols = len(heights_rc), len(heights_cr)
    return sum(
        is_visible(row, col, heights_rc[row], heights_cr[col])
        for row in range(rows)
        for col in range(cols)
    )


def part2(heights):
    """Solve part 2."""
    heights_rc, heights_cr = heights
    rows, cols = len(heights_rc), len(heights_cr)
    return max(
        scenic_score(row, col, heights_rc[row], heights_cr[col])
        for row in range(rows)
        for col in range(cols)
    )


def is_visible(idx_r, idx_c, row, col):
    """Check if tree is visible from any size.

    ## Examples:

    >>> is_visible(0, 0, [1, 2, 4, 5], [4, 4, 4, 4])
    True
    >>> is_visible(2, 1, [4, 3, 4, 5], [5, 4, 2, 4])
    False
    """
    height = row[idx_c]
    return (
        all(h < height for h in row[:idx_c])
        or all(h < height for h in row[idx_c + 1 :])
        or all(h < height for h in col[:idx_r])
        or all(h < height for h in col[idx_r + 1 :])
    )


def scenic_score(idx_r, idx_c, row, col):
    """Check if tree is visible from any size.

    ## Examples:

    >>> scenic_score(0, 0, [1, 2, 4, 5], [4, 4, 4, 4])
    0
    >>> scenic_score(1, 2, [4, 5, 6, 7], [8, 6, 4, 2])
    4
    """
    height = row[idx_c]
    return math.prod(
        [
            _score_line(height, row[idx_c::-1]),
            _score_line(height, row[idx_c:]),
            _score_line(height, col[idx_r::-1]),
            _score_line(height, col[idx_r:]),
        ]
    )


def _score_line(height, heights):
    """Score one sight line.

    ## Examples:

    >>> _score_line(3, [3])
    0
    >>> _score_line(3, [3, 3, 4])
    1
    >>> _score_line(3, [3, 2, 3])
    2
    >>> _score_line(3, [3, 0, 1, 2])
    3
    """
    return next(
        (score for score, hgt in enumerate(heights[1:], start=1) if hgt >= height),
        len(heights) - 1,
    )


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
