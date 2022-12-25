"""AoC 25, 2022: Full of Hot Air."""

# Standard library imports
import pathlib
import sys

TO_SNAFU = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
FROM_SNAFU = {snafu: dec for dec, snafu in TO_SNAFU.items()}


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def part1(fuel):
    """Solve part 1."""
    return to_snafu(sum(from_snafu(number) for number in fuel))


def part2(data):
    """There is no part 2."""


def from_snafu(snafu):
    """Convert a number from SNAFU to decimal.

    ## Examples:

    >>> from_snafu("22")
    12
    >>> from_snafu("2022")
    262
    >>> from_snafu("1=11-2")
    2022
    """
    return sum(
        5**power * FROM_SNAFU[digit] for power, digit in enumerate(snafu[::-1])
    )


def to_snafu(decimal):
    """Convert a number from decimal to SNAFU.

    ## Examples:

    >>> to_snafu(13)
    '1=='
    >>> to_snafu(1234)
    '20-2-'
    """
    snafu = []
    while decimal > 0:
        decimal, digit = divmod(decimal + 2, 5)
        snafu.append(TO_SNAFU[digit - 2])
    return "".join(snafu[::-1])


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
