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
    """Precompute values from the generators"""
    compare_bits = 0xFFFF
    divisor = 0x7FFFFFFF
    factor_a, factor_b = 16_807, 48_271
    seed_a, seed_b = seeds

    values = np.array([[seed_a, seed_b]]) * (factor_a, factor_b) % divisor
    while (num := len(values)) < min_num:
        factors = pow(factor_a, num, divisor), pow(factor_b, num, divisor)
        values = np.vstack([values, values * factors % divisor])

    return values & compare_bits


def generator(seed, factor, divisor=2_147_483_647):
    """Generate consecutive numbers.

    To create its next value, a generator will take the previous value it
    produced, multiply it by a factor, and then keep the remainder of dividing
    that resulting product by 2147483647 (2³¹ - 1).
    """
    while True:
        yield (seed := (seed * factor) % divisor)


def restricted_generator(seed, factor, multiple=1, divisor=2_147_483_647):
    """Generate consecutive numbers.

    The generators still generate values in the same way, but now they only hand
    a value to the judge when it meets a criteria. Each generator looks for
    values that are multiples of some number.
    """
    mask = multiple * 2 - 1  # Because the multiples are of the form 2^n
    while True:
        seed = (seed * factor) % divisor
        masked = seed & mask
        if masked == 0 or masked == multiple:
            yield seed


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
