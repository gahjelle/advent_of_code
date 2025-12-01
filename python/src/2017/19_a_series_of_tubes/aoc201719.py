"""AoC 19, 2017: A Series of Tubes."""

# Standard library imports
import functools
import itertools
import pathlib
import sys

TUBES = {}
MAP2DICT = {"+": "t", "|": "s", "-": "s"}
TURNS = {
    (1, 0): [(0, 1), (0, -1)],
    (-1, 0): [(0, 1), (0, -1)],
    (0, 1): [(1, 0), (-1, 0)],
    (0, -1): [(1, 0), (-1, 0)],
}


def parse_data(puzzle_input):
    """Parse input."""
    key = hash(puzzle_input)
    TUBES[key] = {
        (row, col): MAP2DICT.get(char, char)
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
        if char != " "
    }
    return key


def part1(tube_key):
    """Solve part 1."""
    _, letters = walk_tubes(tube_key)
    return letters


def part2(tube_key):
    """Solve part 2."""
    steps, _ = walk_tubes(tube_key)
    return steps


@functools.cache
def walk_tubes(tube_key):
    """Walk along the tubes. Pick up letters along the way.

    ## Example:

        |
        A +B
        | |
        +-+

    >>> TUBES[1] = {
    ...     (0, 1): "s", (1, 1): "A", (1, 3): "t", (1, 4): "B", (2, 1): "s",
    ...     (2, 3): "s", (3, 1): "t", (3, 2): "s", (3, 3): "t",
    ... }
    >>> walk_tubes(1)
    (9, 'AB')
    """
    tubes = TUBES[tube_key]
    row, col = pos = next((row, col) for row, col in tubes if row == 0)
    dir = (1, 0)

    letters = []
    for count in itertools.count(1):
        # Turn
        if tubes[pos] == "t":
            for drow, dcol in TURNS[dir]:
                if (row + drow, col + dcol) in tubes:
                    dir = (drow, dcol)
                    break
        # Pick up letter
        elif tubes[pos] != "s":
            letters.append(tubes[pos])

        # Step
        drow, dcol = dir
        row, col = pos = (row + drow, col + dcol)
        if pos not in tubes:
            break

    return count, "".join(letters)


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
