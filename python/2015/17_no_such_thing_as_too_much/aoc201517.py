"""AoC 17, 2015: No Such Thing as Too Much"""

# Standard library imports
import collections
import pathlib
import sys


def parse(puzzle_input):
    """Parse input

    Order numbers so that breadth-first search breaks out as early as possible.
    """
    return sorted(
        (int(capacity) for capacity in puzzle_input.split("\n")), reverse=True
    )


def part1(data, eggnog_volume=150):
    """Solve part 1"""
    return len(list(breadth_first(data, eggnog_volume)))


def part2(data, eggnog_volume=150):
    """Solve part 2"""
    num_containers = collections.Counter(
        len(containers) for containers in breadth_first(data, eggnog_volume)
    )
    return min(num_containers.items())[1]


def breadth_first(numbers, target, current=()):
    """Do a breadth-first search for numbers adding up to target.

    ## Example:

    >>> list(breadth_first([1, 2, 4, 5], target=5))
    [(1, 4), (5,)]
    """
    current_sum = sum(current)
    if current_sum == target:
        yield current
    if current_sum < target:
        for idx, number in enumerate(numbers):
            yield from breadth_first(numbers[idx + 1 :], target, current + (number,))


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
