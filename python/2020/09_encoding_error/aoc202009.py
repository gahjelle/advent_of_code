"""AoC 9, 2020: Encoding Error"""

# Standard library imports
import pathlib
import sys
from functools import cache


def parse(puzzle_input):
    """Parse input"""
    return tuple(int(number) for number in puzzle_input.split("\n"))


@cache
def part1(data, preamble=25):
    """Solve part 1"""
    return locate_weakness(data, preamble)


def part2(data, preamble=25):
    """Solve part 2"""
    run = exploit_weakness(data, target=part1(data, preamble))
    return min(run) + max(run)


def find_adders(numbers, target):
    """Find two numbers that add up to target

    ## Examples

    >>> find_adders((1, 2, 4), 5)
    [1, 4]
    >>> find_adders((1, 2, 4), 7)
    """
    lookup = set(numbers)

    for first in numbers:
        if (target - first) in lookup and first + first != target:
            return [first, target - first]


def locate_weakness(numbers, preamble):
    """Find the first error in the encoding

    ## Example

    >>> locate_weakness((1, 2, 4, 6, 7, 9), preamble=3)
    7
    """
    for idx, number in enumerate(numbers[preamble:], start=preamble):
        if not find_adders(numbers[idx - preamble : idx], number):
            return number


def exploit_weakness(numbers, target):
    """Find a contigous run of numbers that adds up to target

    ## Example

    >>> exploit_weakness((1, 2, 4, 6, 7, 9), target=7)
    (1, 2, 4)
    """
    for idx in range(len(numbers), 0, -1):
        for run_length in range(2, idx + 1):
            run_total = sum(run := numbers[idx - run_length : idx])
            if run_total > target:
                break
            if run_total == target:
                return run


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
