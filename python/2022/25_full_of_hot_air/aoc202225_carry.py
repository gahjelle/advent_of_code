"""AoC 25, 2022: Full of Hot Air."""

# Standard library imports
import collections
import pathlib
import sys

TO_SNAFU = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
FROM_SNAFU = {snafu: dec for dec, snafu in TO_SNAFU.items()}


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def part1(fuel):
    """Solve part 1."""
    digits = collections.defaultdict(int)

    # Add each digit separately
    for snafu in fuel:
        for idx, digit in enumerate(snafu[::-1]):
            digits[idx] += FROM_SNAFU[digit]

    # Carry digits forward
    for idx in digits:
        while digits[idx] < -2:
            digits[idx] += 5
            digits[idx + 1] -= 1
        while digits[idx] > 2:
            digits[idx] -= 5
            digits[idx + 1] += 1

    return "".join(TO_SNAFU[digit] for _, digit in sorted(digits.items()))[::-1]


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
