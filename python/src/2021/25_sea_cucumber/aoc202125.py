"""AoC 25, 2021: Sea Cucumber."""

# Standard library imports
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    easts, souths = set(), set()
    for row, line in enumerate(puzzle_input.split("\n")):
        for col, cucumber in enumerate(line):
            if cucumber == ">":
                easts.add((row, col))
            elif cucumber == "v":
                souths.add((row, col))

    return row + 1, col + 1, easts, souths


def part1(data):
    """Solve part 1."""
    num_rows, num_cols, easts, souths = data
    for step in itertools.count(start=1):
        easts, souths, did_move = do_step(num_rows, num_cols, easts, souths)
        if not did_move:
            return step


def part2(data):
    """There is no part two."""


def do_step(num_rows, num_cols, easts, souths):
    """Perform one sea cucumber step.

    >>> easts, souths, did_move = do_step(1, 8, {(0, 3), (0, 4), (0, 5)}, set())
    >>> sorted(easts), sorted(souths), did_move
    ([(0, 3), (0, 4), (0, 6)], [], True)

    >>> easts, souths, did_move = do_step(4, 9, {(1, 1), (2, 7)}, {(1, 2), (1, 7)})
    >>> sorted(easts), sorted(souths), did_move
    ([(1, 1), (2, 8)], [(2, 2), (2, 7)], True)

    >>> easts, souths, did_move = do_step(7, 7, {(0, 3), (2, 6), (3, 6), (4, 6)},
    ...                                         {(3, 0), (6, 2), (6, 3), (6, 4)})
    >>> sorted(easts), sorted(souths), did_move
    ([(0, 4), (2, 0), (3, 6), (4, 0)], [(0, 2), (0, 3), (3, 0), (6, 4)], True)

    >>> easts, souths, did_move = do_step(2, 2, {(0, 0), (1, 1)}, {(0, 1), (1, 0)})
    >>> sorted(easts), sorted(souths), did_move
    ([(0, 0), (1, 1)], [(0, 1), (1, 0)], False)
    """
    occupied = easts | souths
    new_easts = {
        (y, x) if (moved := (y, (x + 1) % num_cols)) in occupied else moved
        for y, x in easts
    }

    occupied = new_easts | souths
    new_souths = {
        (y, x) if (moved := ((y + 1) % num_rows, x)) in occupied else moved
        for y, x in souths
    }

    return new_easts, new_souths, new_easts != easts or new_souths != souths


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
