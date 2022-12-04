"""AoC 4, 2022: Camp Cleanup."""

# Standard library imports
import pathlib
import re
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [parse_pair(line) for line in puzzle_input.split("\n")]


def parse_pair(line):
    """Parse one pair of assignments.

    ## Example:

    >>> parse_pair("5-7,6-9")
    ({5, 6, 7}, {8, 9, 6, 7})
    """
    low_1, high_1, low_2, high_2 = re.split(r"[,-]", line)
    return (
        set(range(int(low_1), int(high_1) + 1)),
        set(range(int(low_2), int(high_2) + 1)),
    )


def part1(pairs):
    """Solve part 1."""
    return sum(not (first - second) or not (second - first) for first, second in pairs)


def part2(pairs):
    """Solve part 2."""
    return sum(1 for first, second in pairs if first & second)


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
