"""AoC 6, 2020: Custom Customs"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [
        [set(answers) for answers in group.split("\n")]
        for group in puzzle_input.split("\n\n")
    ]


def part1(data):
    """Solve part 1"""
    return sum(len(set.union(*group)) for group in data)


def part2(data):
    """Solve part 2"""
    return sum(len(set.intersection(*group)) for group in data)


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
