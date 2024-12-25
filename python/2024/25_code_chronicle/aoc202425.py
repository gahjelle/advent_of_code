"""AoC 25, 2024: Code Chronicle."""

# Standard library imports
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    keys, locks = [], []
    for keylock in puzzle_input.split("\n\n"):
        [keys, locks][keylock.startswith("#")].append(parse_schematic(keylock))
    return keys, locks


def parse_schematic(schematic):
    """Parse one schematic drawing into heights"""
    pins = list(zip(*schematic.split("\n")))
    return [pin.count("#") - 1 for pin in pins]


def part1(data):
    """Solve part 1."""
    keys, locks = data
    return sum(
        all(kh + lh <= 5 for kh, lh in zip(key, lock))
        for key, lock in itertools.product(keys, locks)
    )


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
