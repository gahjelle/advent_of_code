"""AoC 16, 2023: The Floor Will Be Lava."""

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
        if ch != "."
    }


def part1(grid):
    """Solve part 1."""
    return energize(grid, 0, 0, 0, 1)


def part2(grid):
    """Solve part 2."""
    max_row = max(row for row, _ in grid) + 1
    max_col = max(col for _, col in grid) + 1

    energies = [energize(grid, row, 0, 0, 1) for row in range(max_row)]
    energies.extend(energize(grid, 0, col, 1, 0) for col in range(max_col))
    energies.extend(energize(grid, row, max_col - 1, 0, -1) for row in range(max_row))
    energies.extend(energize(grid, max_row - 1, col, -1, 0) for col in range(max_col))

    return max(energies)


def energize(grid, row, col, drow, dcol):
    """Energize a grid.

    ## Example:

        .-.＼.    # Use unicode slash/backslash to avoid unintended escape sequences
        .／.-.
        .-|.／

    >>> grid = {(0, 1): "-", (0, 3): "\\\\", (1, 1): "/", (1, 3): "-", (2, 1): "-", (2, 2): "|", (2, 4): "/"}
    >>> energize(grid, 0, 0, 0, 1)
    11
    """
    max_row = max(row for row, _ in grid) + 1
    max_col = max(col for _, col in grid) + 1

    seen = set()
    energized = set()
    beams = collections.deque([((row, col), (drow, dcol))])
    while beams:
        (row, col), (drow, dcol) = beams.popleft()
        if row < 0 or row >= max_row or col < 0 or col >= max_col:
            continue
        if (row, col, drow, dcol) in seen:
            continue

        energized.add((row, col))
        seen.add((row, col, drow, dcol))
        if (row, col) not in grid:
            beams.append(((row + drow, col + dcol), (drow, dcol)))
        elif (grid[(row, col)] == "|" and dcol == 0) or (
            grid[(row, col)] == "-" and drow == 0
        ):
            beams.append(((row + drow, col + dcol), (drow, dcol)))
        elif grid[(row, col)] == "|" and drow == 0:
            beams.append(((row - 1, col), (-1, 0)))
            beams.append(((row + 1, col), (1, 0)))
        elif grid[(row, col)] == "-" and dcol == 0:
            beams.append(((row, col - 1), (0, -1)))
            beams.append(((row, col + 1), (0, 1)))
        elif grid[(row, col)] == "\\":
            beams.append(((row + dcol, col + drow), (dcol, drow)))
        elif grid[(row, col)] == "/":
            beams.append(((row - dcol, col - drow), (-dcol, -drow)))

    return len(energized)


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
