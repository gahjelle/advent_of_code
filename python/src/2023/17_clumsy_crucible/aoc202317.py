"""AoC 17, 2023: Clumsy Crucible."""

# Standard library imports
import heapq
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return {
        (row, col): int(ch)
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, ch in enumerate(line)
    }


def part1(grid):
    """Solve part 1."""
    return find_path(grid, 0, 3)


def part2(grid):
    """Solve part 2."""
    return find_path(grid, 4, 10)


def find_path(grid, min_straight, max_straight):
    """Find the path with the least loss, observing limitations.

    ## Example:

        12345    X23..
        23456    ..4..
        34567    ..567
        45678    ....8
        56789    ....9

    >>> grid = {(0, 0): 1, (0, 1): 2, (0, 2): 3, (0, 3): 4, (0, 4): 5,
    ...         (1, 0): 2, (1, 1): 3, (1, 2): 4, (1, 3): 5, (1, 4): 6,
    ...         (2, 0): 3, (2, 1): 4, (2, 2): 5, (2, 3): 6, (2, 4): 7,
    ...         (3, 0): 4, (3, 1): 5, (3, 2): 6, (3, 3): 7, (3, 4): 8,
    ...         (4, 0): 5, (4, 1): 6, (4, 2): 7, (4, 3): 8, (4, 4): 9}
    >>> find_path(grid, 2, 3)
    44
    """
    max_row = max(row for row, _ in grid) + 1
    max_col = max(col for _, col in grid) + 1

    def push(queue, loss, row, col, drow, dcol, straight):
        if 0 <= row < max_row and 0 <= col < max_col:
            heapq.heappush(
                queue, (loss + grid[row, col], row, col, drow, dcol, straight)
            )

    seen = set()
    queue = [(0, 0, 0, 0, 0, 0)]
    while queue:
        loss, row, col, drow, dcol, straight = heapq.heappop(queue)

        if row == max_row - 1 and col == max_col - 1 and straight >= min_straight:
            return loss

        if (row, col, drow, dcol, straight) in seen:
            continue
        seen.add((row, col, drow, dcol, straight))

        if straight < max_straight and (drow, dcol) != (0, 0):
            push(queue, loss, row + drow, col + dcol, drow, dcol, straight + 1)

        if straight >= min_straight or (drow, dcol) == (0, 0):
            for ndrow, ndcol in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndrow, ndcol) not in [(drow, dcol), (-drow, -dcol)]:
                    push(queue, loss, row + ndrow, col + ndcol, ndrow, ndcol, 1)


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
