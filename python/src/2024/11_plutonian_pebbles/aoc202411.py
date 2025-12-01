"""AoC 11, 2024: Plutonian Pebbles."""

# Standard library imports
import pathlib
import sys
from collections import defaultdict

cache = {}


def parse_data(puzzle_input):
    """Parse input."""
    stones = defaultdict(int)
    for stone in puzzle_input.split():
        stones[int(stone)] += 1
    return stones


def part1(stones, rounds=25):
    """Solve part 1."""
    for _ in range(rounds):
        stones = blink(stones)
    return sum(stones.values())


def part2(stones, rounds=75):
    """Solve part 2."""
    return part1(stones, rounds=rounds)


def blink(stones):
    """Blink at stones.

    If the stone is engraved with the number 0, it is replaced by a stone
    engraved with the number 1.

    If the stone is engraved with a number that has an even number of digits,
    it is replaced by two stones. The left half of the digits are engraved on
    the new left stone, and the right half of the digits are engraved on the
    new right stone. (The new numbers don't keep extra leading zeroes: 1000
    would become stones 10 and 0.)

    If none of the other rules apply, the stone is replaced by a new stone;
    the old stone's number multiplied by 2024 is engraved on the new stone.

    ## Example

       0 -> 1 -> 2024 -> 20 24 -> 2 0 2 4 -> 4048 1 4048 8096 -> 40 48 2024 40 48 80 96

    >>> stones = {0: 1}
    >>> for _ in range(6):
    ...     stones = blink(stones)
    >>> stones == {40: 2, 48: 2, 80: 1, 96: 1, 2024: 1}
    True
    """
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone not in cache:
            if stone == 0:
                cache[stone] = (1,)
            elif (len_stone := len(str(stone))) % 2 == 0:
                cache[stone] = divmod(stone, 10 ** (len_stone // 2))
            else:
                cache[stone] = (stone * 2024,)
        for new_stone in cache[stone]:
            new_stones[new_stone] += count
    return new_stones


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
