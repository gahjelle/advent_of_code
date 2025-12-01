"""AoC 13, 2022: Distress Signal."""

# Standard library imports
import functools
import math
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return eval("[(" + puzzle_input.replace("\n\n", "),(").replace("\n", ",") + ")]")


def part1(pairs):
    """Solve part 1."""
    return sum(
        idx
        for idx, (left, right) in enumerate(pairs, start=1)
        if compare(left, right) < 0
    )


def part2(pairs):
    """Solve part 2."""
    packets = sorted(
        [packet for pair in pairs for packet in pair] + [[[2]], [[6]]],
        key=functools.cmp_to_key(compare),
    )
    return math.prod(
        idx for idx, packet in enumerate(packets, start=1) if packet in ([[2]], [[6]])
    )


def compare(left, right):
    """Compare left and right signals.

    - If both values are integers, the lower integer should come first. If the
      left integer is lower than the right integer, the inputs are in the right
      order. If the left integer is higher than the right integer, the inputs
      are not in the right order. Otherwise, the inputs are the same integer;
      continue checking the next part of the input.
    - If both values are lists, compare the first value of each list, then the
      second value, and so on. If the left list runs out of items first, the
      inputs are in the right order. If the right list runs out of items first,
      the inputs are not in the right order. If the lists are the same length
      and no comparison makes a decision about the order, continue checking the
      next part of the input.
    - If exactly one value is an integer, convert the integer to a list which
      contains that integer as its only value, then retry the comparison. For
      example, if comparing [0,0,0] and 2, convert the right value to [2] (a
      list containing 2); the result is then found by instead comparing [0,0,0]
      and [2].

    ## Examples:

    >>> compare(1, 1)
    0
    >>> compare(1, 2)
    -1
    >>> compare(2, 1)
    1
    >>> compare([1, 2, 3, 2], [1, 2, 4, 2])
    -1
    >>> compare([1, 3, 2, 4], [1, 2, 3, 4])
    1
    >>> compare([1, [2, 3]], [1, 2, 3])
    1
    >>> compare([[1], [2, 3]], [[1], 3])
    -1
    >>> compare([2, 3], 3)
    -1
    """
    if isinstance(left, int) and isinstance(right, int):
        return -1 if left < right else 1 if left > right else 0
    elif isinstance(left, int):
        return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])
    else:
        for lf, rg in zip(left, right):
            if (cmp := compare(lf, rg)) != 0:
                return cmp
        return compare(len(left), len(right))


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
