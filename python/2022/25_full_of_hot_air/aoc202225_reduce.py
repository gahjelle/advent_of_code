"""AoC 25, 2022: Full of Hot Air."""

# Standard library imports
import functools
import itertools
import pathlib
import sys

TO_SNAFU = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
FROM_SNAFU = {snafu: dec for dec, snafu in TO_SNAFU.items()}


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def part1(fuel):
    """Solve part 1."""
    return functools.reduce(add, fuel)


def add(first, second):
    """Add two SNAFU numbers together.

    ## Example:

    >>> add("22", "1==")
    '100'
    >>> add("2222", "1")
    '1===='
    """
    snafu = []
    carry = 0
    for one, two in itertools.zip_longest(first[::-1], second[::-1], fillvalue="0"):
        sum = carry + FROM_SNAFU[one] + FROM_SNAFU[two]
        carry, digit = (
            (1, sum - 5) if sum > 2 else (-1, sum + 5) if sum < -2 else (0, sum)
        )
        snafu.append(TO_SNAFU[digit])
    if carry:
        snafu.append(TO_SNAFU[carry])
    return "".join(snafu[::-1])


def part2(data):
    """There is no part 2."""


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
