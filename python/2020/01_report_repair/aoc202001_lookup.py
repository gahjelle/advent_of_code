"""AoC 1, 2020: Report Repair"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return set([int(line) for line in puzzle_input.split()])


def find_summands(numbers, target=2020):
    """Find two summands that add up to target"""
    for first in numbers:
        if (second := target - first) in numbers and first != second:
            return first, second


def part1(data):
    """Solve part 1"""
    first, second = find_summands(data)
    return first * second


def part2(data):
    """Solve part 2"""
    for first in data:
        summands = find_summands(data, target=2020 - first)
        if summands:
            second, third = summands
            return first * second * third


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
