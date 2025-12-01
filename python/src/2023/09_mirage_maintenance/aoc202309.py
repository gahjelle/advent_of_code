"""AoC 9, 2023: Mirage Maintenance."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [[int(num) for num in line.split()] for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1."""
    return sum(extrapolate(numbers) for numbers in data)


def part2(data):
    """Solve part 2."""
    return sum(extrapolate(numbers[::-1]) for numbers in data)


def extrapolate(numbers):
    """Extrapolate a number series to find the next number in the series.

    ## Example:

    >>> extrapolate([1, 3, 6, 10, 15, 21])
    28
    """
    last_diff = [numbers[-1]]
    while any(diff != 0 for diff in numbers):
        numbers = [second - first for first, second in zip(numbers, numbers[1:])]
        last_diff.append(numbers[-1])

    return sum(last_diff)


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
