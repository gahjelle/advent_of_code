"""AoC 24, 2015: It Hangs in the Balance."""

# Standard library imports
import math
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return sorted((int(number) for number in puzzle_input.split("\n")), reverse=True)


def part1(data):
    """Solve part 1."""
    return find_best_entanglement(data, num_groups=3, max_length=6)


def part2(data):
    """Solve part 2."""
    return find_best_entanglement(data, num_groups=4, max_length=4)


def find_best_entanglement(weights, num_groups, max_length):
    """Find the best quantum entanglement of a group of weights.

    ## Example:

    >>> find_best_entanglement([6, 5, 4, 3, 2, 1], num_groups=3, max_length=2)
    6
    """
    group_weight = sum(weights) // num_groups
    return min(
        (len(group), math.prod(group), group)
        for group in find_short_groups(weights, group_weight, max_length)
    )[1]


def find_short_groups(weights, target_weight, max_length, already_used=()):
    """Find weights that make up the target weight.

    ## Example:

    >>> list(find_short_groups([6, 5, 4, 3, 2, 1], target_weight=7, max_length=2))
    [(6, 1), (5, 2), (4, 3)]
    """
    if len(already_used) >= max_length:
        return
    for idx, weight in enumerate(weights):
        if weight == target_weight:
            yield already_used + (weight,)
        elif weight < target_weight:
            yield from find_short_groups(
                weights=weights[idx + 1 :],
                target_weight=target_weight - weight,
                max_length=max_length,
                already_used=already_used + (weight,),
            )


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
