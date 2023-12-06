"""AoC 6, 2023: Wait For It."""

# Standard library imports
import math
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    part1 = [
        [int(num) for num in line.split()[1:]] for line in puzzle_input.split("\n")
    ]
    part2 = tuple(
        int(line.split(":")[1].replace(" ", "")) for line in puzzle_input.split("\n")
    )

    return list(zip(*part1)), part2


def part1(data):
    """Solve part 1."""
    records, _ = data
    return math.prod(find_num_records(time, distance) for time, distance in records)


def part2(data):
    """Solve part 2."""
    _, (time, distance) = data
    return find_num_records(time, distance)


def find_num_records(time, distance):
    """Find the number of records.

    The boat runs a speed of t for (T - t) seconds where T = time, resulting in
    a distance of t * (T - t). The formula d(t) = t * (T - t) = Tt - t² is zero
    at 0 and T and symmetric between.

    Use Newton's method to find a solution of d(t) = D = distance.

    ## Example:

    >>> find_num_records(8, 12)
    3
    """

    def f(t):
        return t * (time - t) - distance

    def df(t):
        return time - 2 * t

    first = math.ceil(newtons_method(distance / time, f, df) + 1e-14)
    last = math.floor(newtons_method(time - distance / time, f, df) - 1e-14)
    return last - first + 1


def newtons_method(guess, f, fprime, tol=1e-8):
    """Apply Newton's method to solve an equation.

    To solve f(x) = 0, we start with an initial guess of x0. Then new
    approximations are calculated as:

        x1 = x0 - f(x0) / f'(x0)

    Iterate on this until two consecutive solutions are within the given
    tolerance of each other.

    ## Example:

    >>> newtons_method(3, lambda x: x**2 - 4, lambda x: 2*x)
    2.0
    """
    while abs((x := guess - f(guess) / fprime(guess)) - guess) > tol:
        guess = x
    return x


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
