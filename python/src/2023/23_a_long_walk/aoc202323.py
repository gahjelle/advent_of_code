"""AoC 23, 2023: A Long Walk."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return {
        (row, col): ch
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, ch in enumerate(line)
        if ch != "#"
    }


def part1(grid):
    """Solve part 1."""
    segments, start, goal = find_segments(
        grid, slopes={">": [(0, 1)], "v": [(1, 0)], "<": [(0, -1)], "^": [(-1, 0)]}
    )
    return longest_path(segments, start, goal)


def part2(grid):
    """Solve part 2."""
    segments, start, goal = find_segments(grid, slopes={})

    # Modify last intersection since we can't not go to the goal
    last_intersection = list(segments[goal])[0]
    segments[last_intersection] = {goal: segments[last_intersection][goal]}

    return longest_path(segments, start, goal)


def longest_path(segments, start, goal):
    """Find the longest path on a graph"""
    num_steps = []
    stack = [(0, start, {start})]
    while stack:
        steps, pos, seen = stack.pop()
        if pos == goal:
            num_steps.append(steps)
            continue

        for npos, dsteps in segments[pos].items():
            if npos not in seen:
                stack.append((steps + dsteps, npos, seen | {npos}))

    return max(num_steps)


def find_segments(grid, slopes):
    """Find path segments in the grid."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_row = max(row for row, _ in grid) + 1
    start = next((row, col) for row, col in grid if row == 0)
    goal = next((row, col) for row, col in grid if row == max_row - 1)

    points = {start, goal}
    for row, col in grid:
        num_neighbors = sum(
            (row + drow, col + dcol) in grid for drow, dcol in directions
        )
        if num_neighbors >= 3:
            points.add((row, col))

    segments = {pos: {} for pos in points}
    for srow, scol in points:
        seen = {(srow, scol)}
        queue = collections.deque([(0, srow, scol)])
        while queue:
            steps, row, col = queue.popleft()
            if steps > 0 and (row, col) in points:
                segments[srow, scol][row, col] = steps
                continue

            for drow, dcol in slopes.get(grid[row, col], directions):
                nrow = row + drow
                ncol = col + dcol
                if (nrow, ncol) in grid and (nrow, ncol) not in seen:
                    queue.append((steps + 1, nrow, ncol))
                    seen.add((nrow, ncol))
    return segments, start, goal


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
