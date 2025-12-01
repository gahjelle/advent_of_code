"""AoC 8, 2016: Two-Factor Authentication."""

# Standard library imports
import pathlib
import sys

# Third party imports
import numpy as np
import parse
from advent_of_code_ocr import convert_array_6

OPERATIONS = {}
PARSERS = {}


def register_operation(parser):
    """Decorator for registering operation functions."""

    def _register(func):
        OPERATIONS[func.__name__] = func
        PARSERS[func.__name__] = parse.compile(parser)
        return func

    return _register


def parse_data(puzzle_input):
    """Parse input."""
    return [parse_operation(line) for line in puzzle_input.split("\n")]


def parse_operation(line):
    """Parse one operation.

    ## Examples:

    >>> parse_operation("rect 4x8")
    ('rect', 4, 8)
    >>> parse_operation("rotate row y=19 by 3")
    ('rotate_row', 19, 3)
    >>> parse_operation("rotate column x=7 by 1")
    ('rotate_column', 7, 1)
    """
    for operation, parser in PARSERS.items():
        if match := parser.parse(line):
            return operation, *match.named.values()


def part1(operations, rows=6, cols=50):
    """Solve part 1."""
    return perform_operations(operations, rows, cols).sum()


def part2(operations, rows=6, cols=50):
    """Solve part 2."""
    screen = perform_operations(operations, rows, cols)
    if "--viz" in sys.argv:
        print(show_screen(screen))

    try:
        return convert_array_6(screen, fill_pixel=True, empty_pixel=False)
    except KeyError:  # Simple examples don't give letters
        return show_screen(screen[:3, :7], joiner="|")


def perform_operations(operations, rows, cols):
    """Run screen operations.

    ## Example:

    >>> operations = [("rect", 3, 2), ("rotate_column", 1, 1), ("rotate_row", 0, 4),]
    >>> perform_operations(operations, rows=3, cols=7)
    array([[False, False, False, False,  True, False,  True],
           [ True,  True,  True, False, False, False, False],
           [False,  True, False, False, False, False, False]])
    """
    screen = np.zeros((rows, cols), dtype=bool)
    for operation, *params in operations:
        OPERATIONS[operation](screen, *params)
    return screen


@register_operation("rect {width:d}x{height:d}")
def rect(screen, width, height):
    """Turn on all pixels in a rectangle."""
    screen[:height, :width] = True


@register_operation("rotate row y={row:d} by {offset:d}")
def rotate_row(screen, row, offset):
    """Shift all pixels in a row to the right."""
    screen[row, :] = np.hstack((screen[row, -offset:], screen[row, :-offset]))


@register_operation("rotate column x={col:d} by {offset:d}")
def rotate_column(screen, col, offset):
    """Shift all pixels in a column down."""
    screen[:, col] = np.hstack((screen[-offset:, col], screen[:-offset, col]))


def show_screen(screen, joiner="\n"):
    """Visualize the screen.

    ## Example:

    >>> show_screen(
    ...     [[0, 1, 0, 0, 0, 1, 1], [1, 1, 1, 0, 1, 0, 0], [1, 0, 1, 0, 0, 1, 1]]
    ... )
     O   OO
    OOO O
    O O  OO
    """
    return joiner.join("".join("O" if cell else " " for cell in row) for row in screen)


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
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
