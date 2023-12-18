"""AoC 18, 2023: Lavaduct Lagoon."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    steps = []
    for line in puzzle_input.split("\n"):
        dir, num, color = line.split()
        steps.append((dir, int(num), color[2:-1]))
    return steps


def part1(steps):
    """Solve part 1."""
    return calculate_area([(dir, num) for (dir, num, _) in steps])


def part2(steps):
    """Solve part 2."""
    n2d = {"0": "R", "1": "D", "2": "L", "3": "U"}
    return calculate_area([(n2d[hex[-1]], int(hex[:-1], 16)) for _, _, hex in steps])


def calculate_area(steps):
    """Use shoelace formula to calculate area of polygon.

    Adjust with Pick's formula to find area of whole blocks, not through midpoints.

    ## Example:

    >>> calculate_area([("R", 3), ("D", 4), ("L", 3), ("U", 4)])
    20
    """
    d2c = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
    row, col = 0, 0

    ys, xs = [row], [col]
    circumference = 0
    for dir, num in steps:
        drow, dcol = d2c[dir]
        circumference += num
        row, col = row + drow * num, col + dcol * num
        ys.append(row)
        xs.append(col)

    area = abs(sum(xs[i] * (ys[i - 1] - ys[i + 1]) for i in range(len(xs) - 1))) // 2
    interior = area - circumference // 2 + 1
    return interior + circumference


def dig_lagoon(steps):
    """Manually dig a lagoon."""
    d2c = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
    grid = set()
    row, col = (0, 0)

    for dir, num, _ in steps:
        drow, dcol = d2c[dir]
        for _ in range(num):
            row, col = (row + drow, col + dcol)
            grid.add((row, col))

    return grid


def fill_lagoon(grid, start):
    """Manually fill a lagoon."""
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    seen = set()
    min_row, max_row = min(row for row, _ in grid), max(row for row, _ in grid)
    min_col, max_col = min(col for _, col in grid), max(col for _, col in grid)

    filled = grid.copy()
    queue = collections.deque([start])
    while queue:
        row, col = queue.popleft()
        filled.add((row, col))

        if row < min_row or row > max_row or col < min_col or col > max_col:
            return None
        if (row, col) in seen:
            continue
        seen.add((row, col))
        for drow, dcol in dirs:
            if (row + drow, col + dcol) not in filled:
                queue.append((row + drow, col + dcol))
    return filled


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
