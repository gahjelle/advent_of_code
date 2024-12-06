"""AoC 6, 2024: Guard Gallivant."""

# Standard library imports
import collections
import itertools
import pathlib
import sys

TURN = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


class StuckInLoop(Exception):
    """Indicate that guard is stuck in a loop"""


def parse_data(puzzle_input):
    """Parse input."""
    return {
        (row, col): char
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
    }


def part1(grid):
    """Solve part 1."""
    print(grid)
    start = next(pos for pos, char in grid.items() if char == "^")
    return len(walk(grid, start))


def part2(grid):
    """Solve part 2."""
    start = next(pos for pos, char in grid.items() if char == "^")

    num_obstacles = 0
    for pos in walk(grid, start):
        if pos == start:
            continue
        if not walk(grid | {pos: "#"}, start):
            num_obstacles += 1
    return num_obstacles


def walk(grid, pos, dir=(-1, 0)):
    path = set()
    seen = set()
    while pos in grid:
        path.add(pos)
        while grid.get(new_pos := (pos[0] + dir[0], pos[1] + dir[1])) == "#":
            dir = TURN[dir]
        pos = new_pos
        if (pos, dir) in seen:
            return set()
        seen.add((pos, dir))
    return path


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
