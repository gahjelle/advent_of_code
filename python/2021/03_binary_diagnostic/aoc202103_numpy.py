"""AoC 3, 2021: Binary Diagnostic"""

# Standard library imports
import pathlib
import sys

# Third party imports
import numpy as np


def parse(puzzle_input):
    """Parse input"""
    return np.array([[int(bn) for bn in row] for row in puzzle_input.split("\n")])


def part1(data):
    """Solve part 1"""
    most_common = data.mean(axis=0) >= 0.5
    gamma = bin2int("1" if γ else "0" for γ in most_common)
    epsilon = bin2int("0" if ε else "1" for ε in most_common)

    return gamma * epsilon


def part2(data):
    """Solve part 2"""
    oxygen = bin2int(filter_rows(data, lambda col: 1 if col.mean() >= 0.5 else 0))
    co2 = bin2int(filter_rows(data, lambda col: 0 if col.mean() >= 0.5 else 1))

    return oxygen * co2


def filter_rows(report, chooser):
    """Filter rows column by column based on the chooser

    >>> report = np.array([[1, 0, 1], [0, 1, 1], [1, 1, 0]])
    >>> filter_rows(report, lambda col: 1 if col.mean() >= 0.5 else 0)
    array([1, 1, 0])

    >>> filter_rows(report, lambda col: 0 if col.mean() >= 0.5 else 1)
    array([0, 1, 1])
    """
    col = 0
    idx = np.ones(len(report), dtype=np.bool_)
    while sum(idx) > 1:
        idx &= report[:, col] == chooser(report[idx, col])
        col += 1

    return report[idx][0]


def bin2int(binary):
    """Convert a sequence of binary digits into a base 10 integer

    >>> bin2int([1, 0, 1, 1, 0, 0])
    44
    """
    return int("".join(str(b) for b in binary), 2)


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
