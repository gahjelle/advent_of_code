"""AoC 20, 2015: Infinite Elves and Infinite Houses."""

# Standard library imports
import functools
import math
import pathlib
import sys

A_FEW_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def parse_data(puzzle_input):
    """Parse input."""
    return int(puzzle_input)


def part1(data, per_elf=10):
    """Solve part 1."""
    threshold = data // per_elf
    return first_house(threshold)


def part2(data, per_elf=11, max_houses=50):
    """Solve part 2."""
    threshold = data // per_elf
    presents = deliver(threshold, max_houses=max_houses)
    return next(house for house, p in enumerate(presents) if p >= threshold)


@functools.cache
def first_house(num_presents, p_idx=None):
    """Find first house that gets num_presents.

    See https://www.reddit.com/r/adventofcode/comments/po1zel/2015_day_20_there_must_be_a_more_efficient_way_to/
    and highly abundant numbers, https://en.wikipedia.org/wiki/Highly_abundant_number

    ## Example:

    >>> first_house(25)
    12
    """
    """
    TODO> first_house(25, max_houses=3)
    18

     1 - 1 = 1
     2 - 1 2 = 3
     3 - 1   3 = 4
     4 -   2   4 = 6
     5 -         5 = 5
     6 -   2 3     6 = 11
     7 -             7 = 7
     8 -       4       8 = 12
     9 -     3           9 = 12
    10 -         5         10 = 15
    11 -                     11 = 11
    12 -       4   6           12 = 22
    13 -                         13 = 13
    14 -             7             14 = 21
    15 -         5                   15 = 20
    16 -               8               16 = 24
    17 -                                 17 = 17
    18 -           6     9                 18 = 33
    """
    p_idx = len(A_FEW_PRIMES) - 1 if p_idx is None else p_idx
    if p_idx < 0:
        return num_presents

    p = A_FEW_PRIMES[p_idx]
    pn = 1  # p^n
    ps = 1  # 1 + p + p² + ... + p^n

    best = first_house(num_presents, p_idx=p_idx - 1)
    while ps < num_presents:
        pn *= p
        ps += pn
        with_smaller = math.ceil(num_presents / ps)
        best = min(best, pn * first_house(with_smaller, p_idx=p_idx - 1))
    return best


def deliver(num_houses, max_houses):
    """Deliver presents to houses.

    ## Examples:

    >>> deliver(9, max_houses=9)
    [0, 1, 3, 4, 7, 6, 12, 8, 15, 13]
    >>> deliver(12, max_houses=3)
    [0, 1, 3, 4, 6, 5, 11, 7, 12, 12, 15, 11, 22]
    """
    houses = [0, 1] + [n + (n <= max_houses) for n in range(2, num_houses + 1)]
    for elf in range(2, num_houses + 1):
        for present in range(2, min(max_houses, num_houses // elf) + 1):
            houses[elf * present] += elf
    return houses


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
