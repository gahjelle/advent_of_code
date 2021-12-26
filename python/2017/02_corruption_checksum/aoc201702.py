"""AoC 2, 2017: Corruption Checksum"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [
        [int(number) for number in line.split()] for line in puzzle_input.split("\n")
    ]


def part1(data):
    """Solve part 1"""
    return sum(max(row) - min(row) for row in data)


def part2(data):
    """Solve part 2"""
    return sum(evenly_divisible_ratio(row) for row in data)


def evenly_divisible_ratio(numbers):
    """Find ratio of numbers that are evenly divisible

    >>> evenly_divisible_ratio([9, 3, 4, 5])
    3

    >>> evenly_divisible_ratio([3, 14, 15])
    5
    """
    big, small = next(
        (first, second)
        for first in numbers
        for second in numbers
        if first != second and first % second == 0
    )
    return big // small


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
