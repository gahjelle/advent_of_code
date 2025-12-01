"""AoC 8, 2022: Treetop Tree House."""

# Standard library imports
import math
import pathlib
import sys

# Third party imports
import matplotlib.pyplot as plt


def parse_data(puzzle_input):
    """Parse input."""
    trees_row_col = [
        [int(height) for height in line] for line in puzzle_input.split("\n")
    ]
    trees_col_row = [list(col) for col in zip(*trees_row_col)]
    save_viz("forest.png", trees_row_col)
    return trees_row_col, trees_col_row


def part1(trees):
    """Solve part 1."""
    trees_rc, trees_cr = trees
    rows, cols = len(trees_rc), len(trees_cr)
    visible = [
        [is_visible(row, col, trees_rc[row], trees_cr[col]) for row in range(rows)]
        for col in range(cols)
    ]
    if "--viz" in sys.argv:
        plt.imsave("visible.png", visible, cmap="Greens")

    return sum(
        is_visible(row, col, trees_rc[row], trees_cr[col])
        for row in range(rows)
        for col in range(cols)
    )


def part2(trees):
    """Solve part 2."""
    trees_rc, trees_cr = trees
    rows, cols = len(trees_rc), len(trees_cr)
    scores = [
        [
            math.log10(1 + scenic_score(row, col, trees_rc[row], trees_cr[col]))
            for row in range(rows)
        ]
        for col in range(cols)
    ]
    if "--viz" in sys.argv:
        plt.imsave("scenic.png", scores, cmap="Greens")
    return max(
        scenic_score(row, col, trees_rc[row], trees_cr[col])
        for row in range(rows)
        for col in range(cols)
    )


def lines(row, col, tree_row, tree_col):
    """Yield all four lines from a tree: up, down, left, right.

    ## Example:

    >>> list(lines(2, 1, [5, 4, 2, 4], [4, 3, 4, 5]))
    [[4, 3, 4], [4, 5], [4, 5], [4, 2, 4]]
    """
    yield from [tree_col[row::-1], tree_col[row:], tree_row[col::-1], tree_row[col:]]


def is_visible(row, col, tree_row, tree_col):
    """Check if a tree is visible from any side.

    ## Examples:

    >>> is_visible(0, 0, [4, 2, 9, 5], [4, 4, 4, 4])
    True
    >>> is_visible(2, 1, [5, 4, 2, 4], [4, 3, 4, 5])
    False
    """
    height = tree_row[col]
    return any(
        all(h < height for h in trees[1:])
        for trees in lines(row, col, tree_row, tree_col)
    )


def scenic_score(row, col, tree_row, tree_col):
    """Calculate the view from a tree.

    ## Examples:

    >>> scenic_score(0, 0, [1, 2, 4, 5], [1, 4, 4, 4])
    0
    >>> scenic_score(1, 2, [4, 5, 6, 7], [8, 6, 4, 2])
    4
    """
    height = tree_row[col]
    return math.prod(
        _score_line(height, trees) for trees in lines(row, col, tree_row, tree_col)
    )


def _score_line(height, trees):
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
        (score for score, h in enumerate(trees[1:], start=1) if h >= height),
        len(trees) - 1,
    )


def save_viz(path, array):
    """Save an array as a Matplotlib plot to a file."""
    if "--viz" in sys.argv:
        plt.imsave(path, array, cmap="Greens")
    return array


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.startswith("-"):
            continue
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
