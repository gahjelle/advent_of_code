"""AoC 13, 2021: Transparent Origami"""

# Standard library imports
import pathlib
import sys

# Third party imports
import advent_of_code_ocr
import colorama
import parse
from colorama import Cursor

colorama.init()

FOLD_PATTERN = parse.compile("fold along {xy}={line:d}")


def parse(puzzle_input):
    """Parse input"""
    dots, _, folds = puzzle_input.partition("\n\n")
    return (parse_dots(dots), parse_folds(folds))


def parse_dots(dots):
    """Parse list of dots"""
    return {(int(x), int(y)) for x, y in [dot.split(",") for dot in dots.split("\n")]}


def parse_folds(folds):
    """Parse list of folds"""
    return [
        (match["xy"], match["line"])
        for match in [FOLD_PATTERN.parse(line) for line in folds.split("\n")]
    ]


def part1(data):
    """Solve part 1"""
    dots, folds = data
    return len(fold(dots, folds[:1]))


def part2(data):
    """Solve part 2"""
    text = draw_dots(fold(*data))

    if "-v" in sys.argv:
        print(text)

    return advent_of_code_ocr.convert_6(text)


def fold(dots, folds):
    """Perform folds on dots

    >>> dots = fold({(0, 0), (1, 1), (3, 0), (4, 0)}, [("x", 2)])
    >>> sorted(dots)
    [(0, 0), (1, 0), (1, 1)]
    """
    for fold in folds:
        match fold:
            case ("x", line):
                dots = {(x, y) if x < line else (2 * line - x, y) for x, y in dots}
            case ("y", line):
                dots = {(x, y) if y < line else (x, 2 * line - y) for x, y in dots}
    return dots


def draw_dots(dots):
    """Create a text string visualizing the dots

    >>> print(draw_dots({(0, 0), (0, 2), (1,0), (1, 1), (1, 2), (2, 0), (2, 2)}))
    ###
    .#.
    ###
    """
    num_rows, num_cols = max(y for _, y in dots), max(x for x, _ in dots)
    rows = []
    for row in range(num_rows + 1):
        cols = {x for x, y in dots if y == row}
        rows.append("".join(".#"[x in cols] for x in range(num_cols + 1)))
    return "\n".join(rows)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.startswith("-"):
            continue

        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
