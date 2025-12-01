"""AoC 2, 2016: Bathroom Security."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [[parse_move(move) for move in moves] for moves in puzzle_input.split("\n")]


def parse_move(move):
    """Parse one move into coordinate deltas.

    ## Example:

    >>> parse_move("D")
    (0, -1)
    """
    return {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}[move]


def part1(data):
    """Solve part 1."""
    keys = (
        {(-1, 1): "1", (0, 1): "2", (1, 1): "3"}
        | {(-1, 0): "4", (0, 0): "5", (1, 0): "6"}
        | {(-1, -1): "7", (0, -1): "8", (1, -1): "9"}
    )
    return "".join(moves_to_keys(data, keys))


def part2(data):
    """Solve part 2."""
    keys = (
        {(2, 2): "1"}
        | {(1, 1): "2", (2, 1): "3", (3, 1): "4"}
        | {(0, 0): "5", (1, 0): "6", (2, 0): "7", (3, 0): "8", (4, 0): "9"}
        | {(1, -1): "A", (2, -1): "B", (3, -1): "C"}
        | {(2, -2): "D"}
    )
    return "".join(moves_to_keys(data, keys))


def moves_to_keys(moves, keys, pos_x=0, pos_y=0):
    """Convert a list of move sequences to key codes.

    ## Example:

    >>> keys = {(-1, 0): "1", (0, -1): "2", (0, 0): "3"}
    >>> list(moves_to_keys([[(-1, 0)], [(1, 0), (0, 1), (0, -1)]], keys))
    ['1', '2']
    """
    for move_sequence in moves:
        for dx, dy in move_sequence:
            if (pos_x + dx, pos_y + dy) in keys:
                pos_x += dx
                pos_y += dy
        yield keys[(pos_x, pos_y)]


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
