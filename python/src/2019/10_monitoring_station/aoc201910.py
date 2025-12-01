"""AoC 10, 2019: Monitoring Station."""

# Standard library imports
import collections
import math
import pathlib
import sys

# Third party imports
from codetiming import Timer


def parse_data(puzzle_input):
    """Parse input."""
    grid = {
        (row, col)
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
        if char == "#"
    }
    return [(count_los(grid, row, col), row, col) for row, col in grid]


def part1(stations):
    """Solve part 1."""
    return max(stations)[0]


def part2(stations):
    """Solve part 2."""
    _, row, col = max(stations)
    grid = {(row, col) for _, row, col in stations}

    asteroids = sort_by_angle(grid, row, col)
    vrow, vcol = vaporize(asteroids, row, col)
    return vrow + vcol * 100


def count_los(grid, row, col):
    """Count the number of asteroids in line-of-sight from the given position."""
    return sum(in_sight(grid, row, col, to_row, to_col) for to_row, to_col in grid)


def in_sight(grid, row, col, to_row, to_col):
    """Check if (to_row, to_col) is in line-of-sight from (row, col)."""
    if to_row == row and to_col == col:
        return False

    drow, dcol = to_row - row, to_col - col
    num_steps = math.gcd(drow, dcol)
    step_row, step_col = drow / num_steps, dcol / num_steps

    return all(
        (row + step * step_row, col + step * step_col) not in grid
        for step in range(1, num_steps)
    )


def sort_by_angle(grid, row, col):
    """Sort asteroids by angle, as seen from (row, col)."""
    return sorted(
        (
            math.atan2(c - col, row - r) % (2 * math.pi),
            -abs(r - row) + -abs(c - col),
            r,
            c,
        )
        for r, c in grid - {(row, col)}
    )


def vaporize(asteroids, row, col, number=200):
    """Vaporize asteroids in order."""
    number = min(len(asteroids), number)
    queue = collections.deque(asteroids)
    grid = {(row, col) for _, _, row, col in asteroids}
    num_vaporized = 0
    while num_vaporized < number:
        angle, distance, to_row, to_col = queue.popleft()
        if in_sight(grid, row, col, to_row, to_col):
            grid -= {(to_row, to_col)}
            num_vaporized += 1
        else:
            queue.append((angle, distance, to_row, to_col))

    return to_row, to_col


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
