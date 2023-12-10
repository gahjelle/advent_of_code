"""AoC 10, 2023: Pipe Maze."""


# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    grid = {}
    for row, line in enumerate(puzzle_input.split("\n")):
        for col, char in enumerate(line):
            match char:
                case "|":
                    grid[(row, col)] = {(row - 1, col), (row + 1, col)}
                case "-":
                    grid[(row, col)] = {(row, col - 1), (row, col + 1)}
                case "L":
                    grid[(row, col)] = {(row - 1, col), (row, col + 1)}
                case "J":
                    grid[(row, col)] = {(row, col - 1), (row - 1, col)}
                case "7":
                    grid[(row, col)] = {(row, col - 1), (row + 1, col)}
                case "F":
                    grid[(row, col)] = {(row + 1, col), (row, col + 1)}
                case "S":
                    grid[(row, col)] = {
                        (row, col - 1),
                        (row, col + 1),
                        (row - 1, col),
                        (row + 1, col),
                    }
                case ".":
                    pass
                case _:
                    raise ValueError(f"unknown character: '{char}'")

    start = next(pos for pos, pipes in grid.items() if len(pipes) == 4)
    grid[start] = {pos for pos in grid[start] if start in grid.get(pos, set())}

    return start, grid


def part1(data):
    """Solve part 1."""
    start, grid = data
    return len(find_cycle(grid, start)) // 2


def part2(data):
    """Solve part 2."""
    start, grid = data
    cycle = find_cycle(grid, start)
    inside = find_inside(grid, cycle)

    if "--plot" in sys.argv:
        max_row = max(row for row, _ in grid.keys()) + 1
        max_col = max(col for _, col in grid.keys()) + 1
        for row in range(max_row):
            for col in range(max_col):
                pos = (row, col)
                print("+" if pos in cycle else "I" if pos in inside else " ", end="")
            print()

    return len(inside)


def find_cycle(grid, start):
    """Find the biggest cycle in the pipe grid.

    ## Example:

    >>> grid = {
    ...     (1, 1): {(1, 2), (2, 1)},
    ...     (1, 2): {(1, 1), (1, 3)},
    ...     (1, 3): {(1, 2), (2, 3)},
    ...     (2, 1): {(1, 1), (3, 1)},
    ...     (2, 3): {(1, 3), (3, 3)},
    ...     (3, 1): {(2, 1), (3, 2)},
    ...     (3, 2): {(3, 1), (3, 3)},
    ...     (3, 3): {(3, 2), (2, 3)},
    ... }
    >>> sorted(find_cycle(grid, (1, 1)))
    [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]
    """
    pos = sorted(grid[start])[0]
    cycle = {start, pos}

    while True:
        next_pos = grid[pos] - cycle
        if not next_pos:
            break
        pos = next_pos.pop()
        cycle.add(pos)

    return cycle


def find_inside(grid, cycle):
    """Find positions inside the cycle.

    Keep track of the number of pipes pointing north to the west of the current
    position. If this is odd, then the position is inside the cycle.

    ## Example:

    >>> grid = {
    ...     (1, 1): {(1, 2), (2, 1)},
    ...     (1, 2): {(1, 1), (1, 3)},
    ...     (1, 3): {(1, 2), (2, 3)},
    ...     (2, 1): {(1, 1), (3, 1)},
    ...     (2, 3): {(1, 3), (3, 3)},
    ...     (3, 1): {(2, 1), (3, 2)},
    ...     (3, 2): {(3, 1), (3, 3)},
    ...     (3, 3): {(3, 2), (2, 3)},
    ... }
    >>> cycle = {(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)}
    >>> sorted(find_inside(grid, cycle))
    [(2, 2)]
    """
    max_row = max(row for row, _ in grid.keys()) + 1
    max_col = max(col for _, col in grid.keys()) + 1

    inside = set()
    for row in range(max_row):
        num_north = 0
        for col in range(max_col):
            if (row, col) in cycle:
                if (row - 1, col) in grid[(row, col)]:
                    num_north += 1
            elif num_north % 2 == 1:
                inside.add((row, col))

    return inside


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
