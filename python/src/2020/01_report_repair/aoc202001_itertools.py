"""AoC 1, 2020: Report Repair."""

# Standard library imports
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [int(line) for line in puzzle_input.split()]


def part1(data):
    """Solve part 1."""
    for first, second in itertools.combinations(data, 2):
        if first + second == 2020:
            return first * second


def part2(data):
    """Solve part 2."""
    for first, second, third in itertools.combinations(data, 3):
        if first + second + third == 2020:
            return first * second * third


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
