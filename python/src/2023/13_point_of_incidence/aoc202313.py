"""AoC 13, 2023: Point of Incidence."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [
        {
            (row, col)
            for row, line in enumerate(block.split("\n"), start=1)
            for col, char in enumerate(line, start=1)
            if char == "#"
        }
        for block in puzzle_input.split("\n\n")
    ]


def part1(data):
    """Solve part 1."""
    return sum(
        find_mirror(grid) * 100 + find_mirror({(col, row) for row, col in grid})
        for grid in data
    )


def part2(data):
    """Solve part 2."""
    return sum(
        find_mirror(grid, 1) * 100 + find_mirror({(col, row) for row, col in grid}, 1)
        for grid in data
    )


def find_mirror(grid, num_smudges=0):
    """Find a row mirror."""
    max_row = max(row for row, _ in grid)
    for flip_row in range(1, max_row):
        flipped = {(2 * flip_row + 1 - row, col) for row, col in grid}
        not_mirrored = set(
            range(1, flip_row - (max_row - flip_row) + 1)
            if flip_row > max_row / 2
            else range(2 * flip_row + 1, max_row + 1)
        )
        remaining = {
            (row, col) for row, col in grid - flipped if row not in not_mirrored
        }
        if len(remaining) == num_smudges:
            return flip_row
    return 0


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
