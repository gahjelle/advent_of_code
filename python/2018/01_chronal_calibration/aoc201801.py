"""AoC 1, 2018: Chronal Calibration"""

# Standard library imports
import itertools
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]


def part1(data):
    """Solve part 1"""
    return sum(data)


def part2(data):
    """Solve part 2"""
    frequency, seen = 0, set([0])
    for freq_change in itertools.cycle(data):
        frequency += freq_change
        if frequency in seen:
            return frequency
        seen.add(frequency)


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
