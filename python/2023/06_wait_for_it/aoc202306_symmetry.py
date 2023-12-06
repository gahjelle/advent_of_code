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

    We can also note that d(t) <= f(t) = Tt. This means that the smallest t such
    that d(t) > distance has to be bigger than the smallest t such that f(t) >
    distance. The latter happens at t = distance / T.

    ## Example:

    >>> find_num_records(8, 12)
    3
    """
    for t in range(distance // time, time):
        if t * (time - t) > distance:
            break

    return (time + 1) - 2 * t


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
