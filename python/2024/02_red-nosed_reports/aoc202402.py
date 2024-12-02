"""AoC 2, 2024: Red-Nosed Reports."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [
        [int(number) for number in line.split()] for line in puzzle_input.split("\n")
    ]


def part1(data):
    """Solve part 1."""
    return sum(is_safe(report) for report in data)


def part2(data):
    """Solve part 2."""
    return sum(is_safe_if_dampened(report) for report in data)


def is_safe(report):
    """Check if a report is safe.

    A report consistst of consecutive levels and is safe if:

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

    ## Examples:

    >>> is_safe([1, 2, 4, 7, 8, 10, 13])
    True
    >>> is_safe([7, 6, 4, 2, 1])
    True
    >>> is_safe([8, 6, 4, 4, 1])
    False
    >>> is_safe([1, 5])
    False
    """
    incs = [second - first for first, second in zip(report, report[1:])]
    return all(1 <= inc <= 3 for inc in incs) or all(-3 <= inc <= -1 for inc in incs)


def is_safe_if_dampened(report):
    """Check if a report is safe if it's dampened.

    Tolerate a single bad level, and count the report as a safe if removing a
    single level makes it safe.

    ## Examples:

    >>> is_safe_if_dampened([8, 6, 4, 4, 1])
    True
    >>> is_safe_if_dampened([1, 5])
    True
    >>> is_safe_if_dampened([9, 7, 6, 2, 1])
    False
    """
    return any(is_safe(report[:idx] + report[idx + 1 :]) for idx in range(len(report)))


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
