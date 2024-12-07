"""AoC 7, 2024: Bridge Repair."""

# Standard library imports
import multiprocessing
import pathlib
import sys
from functools import partial
from operator import add, mul


def parse_data(puzzle_input):
    """Parse input."""
    return [
        [int(number) for number in line.split()]
        for line in puzzle_input.replace(":", "").split("\n")
    ]


def part1(data):
    """Solve part 1."""
    with multiprocessing.Pool() as pool:
        return sum(pool.map(partial(check_equation, operators=[add, mul]), data))


def part2(data):
    """Solve part 2."""
    with multiprocessing.Pool() as pool:
        return sum(
            pool.map(partial(check_equation, operators=[add, mul, concat]), data)
        )


def concat(first, second):
    """Concatenate two numbers.

    ## Examples

    >>> concat(12, 42)
    1242
    >>> concat(10, 0)
    100
    >>> concat(0, 28)
    28
    >>> concat(4, 92387294)
    492387294
    """
    n = 10
    while n <= second:
        n *= 10
    return n * first + second


def check_equation(equation, operators):
    """Check that the equation can be satisfied

    ## Examples

    >>> check_equation([3267, 81, 40, 27], [add, mul])
    3267
    >>> check_equation([1977, 28, 1, 77], [add, mul])
    0
    """
    target = equation[0]
    if len(equation) == 2:
        return target if equation[1] == target else 0
    first, second, *rest = equation[1:]
    for operator in operators:
        if check_equation([target, operator(first, second)] + rest, operators):
            return target
    return 0


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
