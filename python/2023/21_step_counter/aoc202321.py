"""AoC 21, 2023: Step Counter."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    start = next(
        (row, col)
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, ch in enumerate(line)
        if ch == "S"
    )
    return start, {
        (row, col)
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, ch in enumerate(line)
        if ch in ".S"
    }


def part1(data, num_steps=64):
    """Solve part 1."""
    start, grid = data
    return explore(start, grid, num_steps)


def part2(data, num_steps=26_501_365):
    """Solve part 2."""
    start, grid = data
    start_row, start_col = start
    size = max(row for row, _ in grid) + 1
    num_grids = num_steps // size - 1

    # Assumptions
    assert size == max(col for _, col in grid) + 1, "Grid is square"
    assert start[0] == size // 2, "Start in the middle of the grid"
    assert start[1] == size // 2, "Start in the middle of the grid"
    assert size % 2 == 1, "Size is odd"
    assert (num_steps - size // 2) % size == 0, "Walk to the end of a grid"

    # Completely reachable squares
    num_odd = (num_grids // 2 * 2 + 1) ** 2
    odd_points = explore(start, grid, 2 * size + 1)
    num_even = ((num_grids + 1) // 2 * 2) ** 2
    even_points = explore(start, grid, 2 * size)

    # Four corner squares
    c_right = explore((start_row, 0), grid, size - 1)
    c_bottom = explore((0, start_col), grid, size - 1)
    c_left = explore((start_row, size - 1), grid, size - 1)
    c_top = explore((size - 1, start_col), grid, size - 1)

    # Small squares on the diagonal
    s_topright = explore((size - 1, 0), grid, size // 2 - 1)
    s_bottomright = explore((0, 0), grid, size // 2 - 1)
    s_bottomleft = explore((0, size - 1), grid, size // 2 - 1)
    s_topleft = explore((size - 1, size - 1), grid, size // 2 - 1)

    # Large squares on the diagonal
    l_topright = explore((size - 1, 0), grid, 3 * size // 2 - 1)
    l_bottomright = explore((0, 0), grid, 3 * size // 2 - 1)
    l_bottomleft = explore((0, size - 1), grid, 3 * size // 2 - 1)
    l_topleft = explore((size - 1, size - 1), grid, 3 * size // 2 - 1)

    return (
        num_odd * odd_points
        + num_even * even_points
        + (c_right + c_bottom + c_left + c_top)
        + (s_topright + s_bottomright + s_bottomleft + s_topleft) * (num_grids + 1)
        + (l_topright + l_bottomright + l_bottomleft + l_topleft) * num_grids
    )


def explore(start, grid, num_steps):
    """Explore a grid from the starting position."""
    seen = set()
    final_pos = set()
    queue = collections.deque([(0, start)])
    while queue:
        steps, (row, col) = queue.popleft()
        if steps == num_steps:
            final_pos.add((row, col))
            continue
        if (num_steps - steps) % 2 == 0:
            final_pos.add((row, col))

        if (row, col) in seen:
            continue
        seen.add((row, col))

        for nrow, ncol in [
            (row, col + 1),
            (row + 1, col),
            (row, col - 1),
            (row - 1, col),
        ]:
            if (nrow, ncol) in grid:
                queue.append((steps + 1, (nrow, ncol)))

    return len(final_pos)


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
