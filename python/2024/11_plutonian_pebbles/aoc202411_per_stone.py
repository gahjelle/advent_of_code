"""AoC 11, 2024: Plutonian Pebbles."""

# Standard library imports
import functools
import pathlib
import sys
from collections import defaultdict


def parse_data(puzzle_input):
    """Parse input."""
    return [int(stone) for stone in puzzle_input.split()]


def part1(stones, rounds=25):
    """Solve part 1."""
    return sum(count(stone, rounds) for stone in stones)


def part2(stones, rounds=75):
    """Solve part 2."""
    return part1(stones, rounds=rounds)


@functools.cache
def count(stone, rounds):
    """Blink at one stone

    ## Example

       0 -> 1 -> 2024 -> 20 24 -> 2 0 2 4 -> 4048 1 4048 8096 -> 40 48 2024 40 48 80 96

    >>> count(0, 6)
    7
    """
    if rounds == 0:
        return 1
    if stone == 0:
        return count(1, rounds - 1)
    if (len_stone := len(str(stone))) % 2 == 0:
        first, second = divmod(stone, 10 ** (len_stone // 2))
        return count(first, rounds - 1) + count(second, rounds - 1)
    return count(stone * 2024, rounds - 1)


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
