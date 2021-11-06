"""AoC 1, 2020: Report Repair"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]


def part1(data):
    """Solve part 1"""
    for first in data:
        for second in data:
            if first < second and first + second == 2020:
                return first * second


def part2(data):
    """Solve part 2"""
    for first in data:
        for second in data:
            for third in data:
                if first < second < third and first + second + third == 2020:
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
