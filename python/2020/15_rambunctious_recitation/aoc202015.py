"""AoC 15, 2020: Rambunctious Recitation"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(number) for number in puzzle_input.split(",")]


def part1(data):
    """Solve part 1"""
    return recitate(data, 2020)


def part2(data):
    """Solve part 2"""
    return recitate(data, 30_000_000)


def recitate(initial, length):
    """Recitate numbers for the given length

    ## Example:

    >>> recitate([0, 3, 6], 9)
    4
    """
    *heads, last = initial
    spoken = {number: idx for idx, number in enumerate(heads, start=1)}
    for idx in range(len(initial), length):
        spoken[last], last = idx, idx - spoken.get(last, idx)

    return last


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
