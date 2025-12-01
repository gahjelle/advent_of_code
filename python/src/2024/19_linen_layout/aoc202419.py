"""AoC 19, 2024: Linen Layout."""

# Standard library imports
import functools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    towels, patterns = puzzle_input.split("\n\n")
    return frozenset(towels.split(", ")), patterns.split("\n")


def part1(data):
    """Solve part 1."""
    towels, patterns = data
    return sum(is_possible(pattern, towels) for pattern in patterns)


def part2(data):
    """Solve part 2."""
    towels, patterns = data
    return sum(count_possible(pattern, towels) for pattern in patterns)


@functools.cache
def is_possible(pattern, towels):
    if pattern in towels:
        return True

    return any(
        is_possible(pattern.removesuffix(towel), towels)
        for towel in towels
        if pattern.endswith(towel)
    )


@functools.cache
def count_possible(pattern, towels):
    if not pattern:
        return 1

    return sum(
        count_possible(pattern.removesuffix(towel), towels)
        for towel in towels
        if pattern.endswith(towel)
    )


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
