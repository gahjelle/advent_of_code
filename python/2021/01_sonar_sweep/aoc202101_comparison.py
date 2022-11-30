"""AoC 1, 2021: Sonar Sweep"""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return [int(depth) for depth in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    return sum(current > prev for prev, current in zip(data[:-1], data[1:]))


def part2(data):
    """Solve part 2"""
    return sum(next > prev for prev, next in zip(data[:-3], data[3:]))


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
