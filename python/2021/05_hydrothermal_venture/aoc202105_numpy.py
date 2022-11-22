"""AoC 5, 2021: Hydrothermal Venture"""

# Standard library imports
import pathlib
import sys

# Third party imports
import numpy as np
import pandas as pd
import parse

PATTERN = parse.compile("{x1:d},{y1:d} -> {x2:d},{y2:d}")


def parse(puzzle_input):
    """Parse input"""
    return pd.DataFrame(
        [parse_line(line) for line in puzzle_input.split("\n")],
        columns=["x1", "y1", "x2", "y2"],
    )


def parse_line(line):
    """Parse one line of input

    >>> parse_line("5,2 -> 3,2")
    (5, 2, 3, 2)
    """
    match = PATTERN.parse(line)
    return (match["x1"], match["y1"], match["x2"], match["y2"])


def part1(data):
    """Solve part 1"""
    return count_overlaps(data.query("x1 == x2 or y1 == y2"))


def part2(data):
    """Solve part 2"""
    return count_overlaps(data)


def count_overlaps(lines):
    """Count the number of points where more than one line overlaps"""
    max_x = max(lines.loc[:, ["x1", "x2"]].max(axis=1))
    max_y = max(lines.loc[:, ["y1", "y2"]].max(axis=1))
    matrix = np.zeros((max_y + 1, max_x + 1))

    for _, line in lines.iterrows():
        if line.x1 == line.x2:
            step_y = 1 if line.y1 < line.y2 else -1
            for y in range(line.y1, line.y2 + step_y, step_y):
                matrix[y, line.x1] += 1
        elif line.y1 == line.y2:
            step_x = 1 if line.x1 < line.x2 else -1
            for x in range(line.x1, line.x2 + step_x, step_x):
                matrix[line.y1, x] += 1
        else:
            step_y = 1 if line.y1 < line.y2 else -1
            step_x = 1 if line.x1 < line.x2 else -1
            for x, y in zip(
                range(line.x1, line.x2 + step_x, step_x),
                range(line.y1, line.y2 + step_y, step_y),
            ):
                matrix[y, x] += 1

    return np.sum(matrix > 1)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
