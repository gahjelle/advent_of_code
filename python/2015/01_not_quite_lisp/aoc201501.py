"""AoC 1, 2015: Not Quite Lisp"""

# Standard library imports
import itertools
import pathlib
import sys

STEPS = {"(": 1, ")": -1}


def parse(puzzle_input):
    """Parse input"""
    return [STEPS[paren] for paren in puzzle_input]


def part1(data):
    """Solve part 1"""
    return sum(data)


def part2(data):
    """Solve part 2"""
    steps = enumerate(itertools.accumulate(data), start=1)
    return next(itertools.dropwhile(lambda d: d[1] >= 0, steps))[0]


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
