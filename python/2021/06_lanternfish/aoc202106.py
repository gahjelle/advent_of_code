"""AoC 6, 2021: Lanternfish."""

# Standard library imports
import collections
import functools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return collections.Counter(int(timer) for timer in puzzle_input.split(","))


def part1(data):
    """Solve part 1."""
    return count_lanternfish(data, 80)


def part2(data):
    """Solve part 2."""
    return count_lanternfish(data, 256)


def count_lanternfish(fish_count, days):
    """Count the total number of lanternfish after the given number of days."""
    return sum(
        num_fish * lanternfish(days - timer) for timer, num_fish in fish_count.items()
    )


@functools.cache
def lanternfish(days):
    """Calculate how many lanternfish one lanternfish create in a given number
    of days.

    >>> lanternfish(0)
    1

    >>> lanternfish(1)
    2

    >>> lanternfish(16)
    5

    >>> lanternfish(17)
    7
    """
    if days < 1:
        return 1

    return lanternfish(days - 7) + lanternfish(days - 9)


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
