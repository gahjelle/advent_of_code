"""AoC 1, 2024: Historian Hysteria."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return list(
        zip(
            *[
                [int(number) for number in line.split()]
                for line in puzzle_input.split("\n")
            ]
        )
    )


def part1(data):
    """Solve part 1."""
    left, right = data
    return sum(
        abs(first - second) for first, second in zip(sorted(left), sorted(right))
    )


def part2(data):
    """Solve part 2."""
    left, right = data
    counts = collections.Counter(right)
    return sum(number * counts.get(number, 0) for number in left)


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
