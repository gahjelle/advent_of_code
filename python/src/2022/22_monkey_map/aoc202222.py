"""AoC 22, 2022: Monkey Map."""

# Standard library imports
import enum
import functools
import pathlib
import re
import sys
import time

# Third party imports
import colorama
import numpy as np
from colorama import Cursor

colorama.init(autoreset=True)


class Cell(enum.IntEnum):
    WALL = 0
    ROOM = 1
    TELEPORT = 2
    VISITED = 3
    CURRENT = 4


class Dir(enum.IntEnum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


class Turn(enum.IntEnum):
    RIGHT = 1
    LEFT = -1


MAP2CELL = {".": Cell.ROOM, "#": Cell.WALL, " ": Cell.TELEPORT}
MOVE = {Dir.RIGHT: (0, 1), Dir.DOWN: (1, 0), Dir.LEFT: (0, -1), Dir.UP: (-1, 0)}
CELL2VIZ = {
    Cell.ROOM: " ",
    Cell.WALL: "#",
    Cell.TELEPORT: ".",
    Cell.VISITED: "o",
    Cell.CURRENT: "■",
}


def parse_data(puzzle_input):
    """Parse input."""
    map, path = puzzle_input.split("\n\n")
    return parse_map(map), parse_path(path)


def parse_map(puzzle_input):
    """Parse the map part of the puzzle input."""
    lines = puzzle_input.split("\n")
    rows, cols = len(lines), max(len(line) for line in lines)
    map = np.ones((rows, cols), dtype=np.int8) * 2

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            map[row, col] = MAP2CELL[char]

    return map


def parse_path(line):
    """Parse the path from the puzzle input.

    Add one extra 'R' at the beginning for consistency.

    ## Example:

    >>> parse_path("4R3L1L3R2")
    [('RIGHT', 4), ('RIGHT', 3), ('LEFT', 1), ('LEFT', 3), ('RIGHT', 2)]
    """
    return [
        ("RIGHT" if rl == "R" else "LEFT", int(steps))
        for rl, steps in re.findall(r"([RL])(\d+)", f"R{line}")
    ]


def part1(data):
    """Solve part 1."""
    return follow_path(*data, step_func=step_on_map)


def part2(data):
    """Solve part 2."""
    map, path = data
    cube_size = 50 if len(map) > 50 else 4
    return follow_path(
        map, path, step_func=functools.partial(step_on_cube, size=cube_size)
    )


def follow_path(map, path, step_func):
    """Follow the path through the map.

    Return the password associated with the final position.

    Facing is 0 for right, 1 for down, 2 for left, and 3 for up. The final
    password is the sum of 1000 times the row, 4 times the column, and the
    facing.
    """
    # Clean up map for visualization
    do_viz = "--viz" in sys.argv
    map[map > Cell.TELEPORT] = Cell.ROOM

    # Initial position, face up as we've added a turn RIGHT in front of the path
    pos, dir = (0, np.where(map[0] == Cell.ROOM)[0][0]), Dir.UP

    # Step through the path
    for turn, steps in path:
        dir = (dir + Turn[turn]) % 4
        for _ in range(steps):
            next_pos, next_dir = step_func(map, pos, dir)
            if map[next_pos] == Cell.WALL:
                break
            pos, dir = next_pos, next_dir

            if do_viz:
                map[pos] = Cell.CURRENT
                viz(map)
                map[pos] = Cell.VISITED

    # Calculate password
    row, col = pos
    return 1000 * (row + 1) + 4 * (col + 1) + dir


def step_on_map(map, pos, dir):
    """Take one step on the map."""
    rows, cols = map.shape
    while True:
        step_row, step_col = tuple(p + s for p, s in zip(pos, MOVE[dir]))
        pos = step_row % rows, step_col % cols
        if map[pos] != Cell.TELEPORT:
            return pos, dir


def step_on_cube(map, pos, dir, size):
    """Take one step on the map folded as a cube."""
    max_row, max_col = map.shape
    rows, cols = size * 5, size * 5

    step_row, step_col = tuple(p + s for p, s in zip(pos, MOVE[dir]))
    next_row, next_col = next_pos = step_row % rows, step_col % cols
    if next_row < max_row and next_col < max_col and map[next_pos] != Cell.TELEPORT:
        return next_pos, dir

    # Handle transitions to other faces of the cube
    row, col, other = next_row % size, next_col % size, size - 1
    if size == 50:
        match (next_row // size, next_col // size, dir):
            case (0, 0, Dir.LEFT):  # from 0, 1
                return (2 * size + other - row, 0 * size), Dir.RIGHT
            case (0, 3, Dir.RIGHT):  # from 0, 2
                return (2 * size + other - row, 1 * size + other), Dir.LEFT
            case (1, 0, Dir.LEFT):  # from 1, 1
                return (2 * size, 0 * size + row), Dir.DOWN
            case (1, 0, Dir.UP):  # from 2, 0
                return (1 * size + col, 1 * size), Dir.RIGHT
            case (1, 2, Dir.RIGHT):  # from 1, 1
                return (0 * size + other, 2 * size + row), Dir.UP
            case (1, 2, Dir.DOWN):  # from 0, 2
                return (1 * size + col, 1 * size + other), Dir.LEFT
            case (2, 2, Dir.RIGHT):  # from 2, 1
                return (0 * size + other - row, 2 * size + other), Dir.LEFT
            case (2, 4, Dir.LEFT):  # from 2, 0
                return (0 * size + other - row, 1 * size), Dir.RIGHT
            case (3, 1, Dir.RIGHT):  # from 3, 0
                return (2 * size + other, 1 * size + row), Dir.UP
            case (3, 1, Dir.DOWN):  # from 2, 1
                return (3 * size + col, 0 * size + other), Dir.LEFT
            case (3, 4, Dir.LEFT):  # from 3, 0
                return (0 * size, 1 * size + row), Dir.DOWN
            case (4, 0, Dir.DOWN):  # from 3, 0
                return (0 * size, 2 * size + col), Dir.DOWN
            case (4, 1, Dir.UP):  # from 0, 1
                return (3 * size + col, 0 * size), Dir.RIGHT
            case (4, 2, Dir.UP):  # from 0, 2
                return (3 * size + other, 0 * size + col), Dir.UP
            case _:
                raise ValueError(
                    f"unhandled transition: {next_row // size, next_col // size, dir}"
                )

    # Example cube
    elif size == 4:
        match (next_row // size, next_col // size, dir):
            case (0, 1, Dir.UP):  # from 1, 1
                return (0 * size + col, 2 * size), Dir.RIGHT
            case (1, 3, Dir.RIGHT):  # from 1, 2
                return (2 * size, 3 * size + other - row), Dir.DOWN
            case (3, 2, Dir.DOWN):  # from 3, 1
                return (1 * size + other, 0 * size + other - col), Dir.UP


def viz(map):
    """Quick and dirty terminal visualization."""
    print(
        Cursor.POS(1, 5)
        + "\n".join("".join(CELL2VIZ[cell] for cell in row) for row in map)
    )
    time.sleep(0.12)


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
