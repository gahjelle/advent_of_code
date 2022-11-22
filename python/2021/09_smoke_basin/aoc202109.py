"""AoC 9, 2021: Smoke Basin"""

# Standard library imports
import pathlib
import sys

# Third party imports
import numpy as np


def parse(puzzle_input):
    """Parse input"""
    return np.array(
        [[int(height) for height in row] for row in puzzle_input.split("\n")]
    )


def part1(data):
    """Solve part 1"""
    return np.sum(data[low_points(data)] + 1)


def part2(data):
    """Solve part 2"""
    return np.prod(sorted(basin_sizes(data, low_points(data)), reverse=True)[:3])


def low_points(heights):
    """Find indices of low points (surrounded by higher points)

       7 6 9        7(6)9
       9 9 6   ->   9 9 6
       5 3 2        5 3(2)

    >>> low_points(np.array([[7, 6, 9], [9, 9, 6], [5, 3, 2]]))
    array([[False,  True, False],
           [False, False, False],
           [False, False,  True]])
    """
    buffered = np.full((heights.shape[0] + 2, heights.shape[1] + 2), 10, dtype=np.int8)
    buffered[1:-1, 1:-1] = heights

    return (
        (heights < buffered[:-2, 1:-1])
        & (heights < buffered[2:, 1:-1])
        & (heights < buffered[1:-1, :-2])
        & (heights < buffered[1:-1, 2:])
    )


def basin_sizes(heights, basin_idx):
    """Find the size of each basin

       7 6 9        1 1 .
       9 9 6   ->   . . 2   ->   [2, 4]
       5 3 2        2 2 2

    >>> basin_sizes(np.array([[7, 6, 9], [9, 9, 6], [5, 3, 2]]),
    ...             np.array([[0, 1, 0], [0, 0, 0], [0, 0, 1]], dtype=bool))
    [2, 4]
    """
    return [basin_size(heights, row, col) for row, col in zip(*np.where(basin_idx))]


def basin_size(heights, row, col):
    """Depth first search to find size of basin

       7 6 9        . . .
       9 9 6   ->   . . #   ->   4
      (5)3 2        # # #

    >>> basin_size(np.array([[7, 6, 9], [9, 9, 6], [5, 3, 2]]), 2, 0)
    4
    """
    visited = np.zeros_like(heights, dtype=bool)
    explore(visited, heights, row, col)

    return np.sum(visited)


def explore(visited, heights, row, col):
    """Recursively explore the height map"""
    num_rows, num_cols = heights.shape
    if (
        row < 0
        or col < 0
        or row >= num_rows
        or col >= num_cols
        or visited[row, col]
        or heights[row, col] >= 9
    ):
        return

    visited[row, col] = True

    explore(visited, heights, row - 1, col)
    explore(visited, heights, row + 1, col)
    explore(visited, heights, row, col - 1)
    explore(visited, heights, row, col + 1)


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
