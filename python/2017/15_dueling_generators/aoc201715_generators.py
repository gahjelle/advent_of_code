"""AoC 15, 2017: Dueling Generators."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return tuple(int(generator.split()[-1]) for generator in puzzle_input.split("\n"))


def part1(generators, comparer=65_535, num_rounds=40_000_000):
    """Solve part 1."""
    seed_a, seed_b = generators
    return sum(
        gen_a & comparer == gen_b & comparer
        for gen_a, gen_b, _ in zip(
            generator(seed_a, factor=16807),
            generator(seed_b, factor=48271),
            range(num_rounds),
        )
    )


def part2(generators, comparer=65_535, num_rounds=5_000_000):
    """Solve part 2."""
    seed_a, seed_b = generators
    return sum(
        (gen_a & comparer) == (gen_b & comparer)
        for gen_a, gen_b, _ in zip(
            restricted_generator(seed_a, factor=16807, multiple=4),
            restricted_generator(seed_b, factor=48271, multiple=8),
            range(num_rounds),
        )
    )


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
