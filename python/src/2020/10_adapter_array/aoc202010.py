"""AoC 10, 2020: Adapter Array."""

# Standard library imports
import math
import pathlib
import sys
from collections import Counter
from functools import cache


def parse_data(puzzle_input):
    """Parse input."""
    adapters = sorted(int(value) for value in puzzle_input.split("\n"))
    return [second - first for first, second in zip([0] + adapters, adapters)] + [3]


def part1(data):
    """Solve part 1."""
    jolts = Counter(data)
    return jolts[1] * jolts[3]


def part2(data):
    """Solve part 2."""
    return math.prod(combos(run) for run in run_lengths(data))


def run_lengths(jolts):
    """Find lengths of runs of 1 jolts.

    ## Example

    >>> run_lengths([1, 1, 1, 3, 3, 1, 3, 1, 1, 3])
    [3, 1, 2]
    """
    runs = []
    for idx, (prev, jolt) in enumerate(zip([3] + jolts, jolts + [3])):
        if prev == 3 and jolt == 1:
            first = idx
        elif prev == 1 and jolt == 3:
            runs.append(idx - first)
    return runs


@cache
def combos(run_length):
    """Calculate number of combinations based on run length.

    - For run length 1 there is only one valid combination, as there are
      3-jumps before and after the run.
    - For run length 2 (1-2-3) there are two valid combinations: 1-2-3 and 1-3
    - For run length 3 (1-2-3-4) there are four valid combinations: 1-2-3-4,
      1-2-4, 1-3-4, and 1-4
    - For run length 4 (1-2-3-4-5) there are seven valid combinations:
      1-2-3-4-5, 1-2-3-5, 1-2-4-5, 1-3-4-5, 1-2-5, 1-3-5, 1-4-5
    - For run length 5 (1-2-3-4-5-6) there are thirteen valid combinations:
      1-2-3-4-5-6, 1-2-3-4-6, 1-2-3-5-6, 1-2-4-5-6, 1-3-4-5-6, 1-2-3-6, 1-2-4-6,
      1-2-5-6, 1-3-4-6, 1-3-5-6, 1-4-5-6, 1-4-6, 1-3-6

    In general, the number of combos follow a Fibonacci-like pattern:

      C(n) = C(n-3) + C(n-2) + C(n-1)

    ## Examples

    >>> combos(3)
    4
    >>> combos(7)
    44
    """
    if run_length > 3:
        return combos(run_length - 3) + combos(run_length - 2) + combos(run_length - 1)
    else:
        return 2 ** (run_length - 1)


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
