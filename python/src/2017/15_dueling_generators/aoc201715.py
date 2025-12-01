"""AoC 15, 2017: Dueling Generators."""

# Standard library imports
import functools
import pathlib
import sys

# Third party imports
import numpy as np


def parse_data(puzzle_input):
    """Parse input."""
    return tuple(int(generator.split()[-1]) for generator in puzzle_input.split("\n"))


def part1(seeds, num_rounds=40_000_000):
    """Solve part 1."""
    generated = generate(seeds, num_rounds)
    gen_a, gen_b = generated[:num_rounds].T
    return np.sum(gen_a == gen_b)


def part2(seeds, num_rounds=5_000_000, min_num=40_000_000):
    """Solve part 2."""
    gen_a, gen_b = generate(seeds, min_num).T
    gen_a4 = gen_a[gen_a & 0b11 == 0]
    gen_b8 = gen_b[gen_b & 0b111 == 0]
    return np.sum(gen_a4[:num_rounds] == gen_b8[:num_rounds])


@functools.cache
def generate(seeds, min_num=40_000_000):
    """Precompute values from the generators.

    To create its next value, a generator will take the previous value it
    produced, multiply it by a factor (generator A uses 16807; generator B uses
    48271), and then keep the remainder of dividing that resulting product by
    2147483647. That final remainder is the value it produces next.

    Borrowed from
    https://www.reddit.com/r/adventofcode/comments/nfwj9p/2017_day_15_at_most_15_seconds_on_tenyearold/

    ## Example:

    >>> generate((65, 8921), min_num=4)
    array([[43879, 54071],
           [63289, 34184],
           [58186, 58186],
           [ 5831, 52231]])
    """
    compare_bits = 0xFFFF
    divisor = 0x7FFFFFFF
    factor_a, factor_b = 16_807, 48_271
    seed_a, seed_b = seeds

    values = np.array([[seed_a, seed_b]]) * (factor_a, factor_b) % divisor
    while (num := len(values)) < min_num:
        factors = pow(factor_a, num, divisor), pow(factor_b, num, divisor)
        values = np.vstack([values, values * factors % divisor])

    return values & compare_bits


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
