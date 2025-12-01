"""AoC 7, 2021: The Treachery of Whales."""

# Standard library imports
import collections
import functools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return collections.Counter([int(pos) for pos in puzzle_input.split(",")])


def part1(data):
    """Solve part 1."""
    return optimize(data, metric=linear_fuel(data))


def part2(data):
    """Solve part 2."""
    return optimize(data, metric=triangular_fuel(data))


def optimize(crabs, metric):
    """Find the best position based on the metric function."""

    # Guess a first to-position
    pos = round(
        sum(num_crabs * pos for pos, num_crabs in crabs.items()) / crabs.total()
    )
    pos_left, pos_right = pos - 1, pos + 1
    step = -1 if metric(pos_left) < metric(pos_right) else 1

    # Move towards the global minimum
    while metric(pos + step) < metric(pos):
        pos += step

    return metric(pos)


def linear_fuel(crabs):
    """Factory for linear fuel metrics."""

    @functools.cache
    def _linear_fuel(to_pos):
        """Calculate total fuel needed to move to a given position, each step
        costs 1 fuel."""
        return sum(num_crabs * abs(to_pos - pos) for pos, num_crabs in crabs.items())

    return _linear_fuel


def triangular_fuel(crabs):
    """Factory for triangular fuel metrics."""

    @functools.cache
    def _triangular_fuel(to_pos):
        """Calculate total fuel needed to move to a given position, each step
        costs 1 extra fuel."""
        return sum(
            num_crabs * (steps := abs(to_pos - pos)) * (steps + 1) // 2
            for pos, num_crabs in crabs.items()
        )

    return _triangular_fuel


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
