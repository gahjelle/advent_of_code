"""AoC 4, 2024: Ceres Search."""

# Standard library imports
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return {
        (row, col): char
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
    }


def part1(grid):
    """Solve part 1."""
    return count_in_grid(
        grid,
        is_xmas,
        [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],
    )


def part2(grid):
    """Solve part 2."""
    return count_in_grid(
        grid,
        is_cross_mas,
        [
            [(-1, -1), (-1, 1)],
            [(-1, -1), (1, -1)],
            [(1, 1), (-1, 1)],
            [(1, 1), (1, -1)],
        ],
    )


def count_in_grid(grid, find_one, directions):
    """Count how many times something is found in the grid"""
    num_rows = max(row for row, _ in grid) + 1
    num_cols = max(col for _, col in grid) + 1
    return sum(
        find_one(grid, row, col, dir)
        for row, col, dir in itertools.product(
            range(num_rows), range(num_cols), directions
        )
    )


def is_xmas(grid, row, col, dir, word="XMAS"):
    """Check if XMAS is written at a specific location in a given direction

    ## Example

    >>> grid = {(row, 0): char for row, char in enumerate("SAMXMAS")}
    >>> is_xmas(grid, 3, 0, (-1, 0))
    True
    >>> is_xmas(grid, 3, 0, (1, 1))
    False
    >>> is_xmas(grid, 0, 0, (1, 0))
    False
    """
    drow, dcol = dir
    for offset, char in enumerate(word):
        r, c = row + offset * drow, col + offset * dcol
        if grid.get((r, c)) != char:
            return False
    return True


def is_cross_mas(grid, row, col, dirs):
    """Check if MAS is written in a cross at a specific location in given directions

    ## Example

    >>> grid = {(0, 0): "M", (2, 0): "M", (1, 1): "A", (0, 2): "S", (2, 2): "S"}
    >>> is_cross_mas(grid, 1, 1, [(-1, 1), (1, 1)])
    True
    >>> is_cross_mas(grid, 1, 1, [(1, -1), (1, 1)])
    False
    >>> is_cross_mas(grid, 0, 0, [(-1, 1), (1, 1)])
    False
    """
    return all(is_xmas(grid, row - r, col - c, (r, c), word="MAS") for r, c in dirs)


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
