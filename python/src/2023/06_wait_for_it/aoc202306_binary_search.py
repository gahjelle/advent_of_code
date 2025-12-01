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

    Use a binary search to find the smallest t such that d(t) > distance. During
    the search, low will always be less than t while high will always be greater
    than or equal than t. At the end of the search, high represents the smallest
    t such that d(t) > distance.

    We want the number of records. If first is the smallest t such that d(t) >
    distance and last is the greatest t such that d(t) > distance, then the
    number of records is (last - first + 1). Because of symmetry last = time / 2
    + time / 2 - first = time - first. The number of records can therefore be
    calculated as (last - first + 1) = time - 2*first + 1.

    ## Example:

    >>> find_num_records(8, 12)
    3
    """
    low, high = 0, time // 2
    while low + 1 < high:
        mid = (high + low) // 2
        if mid * (time - mid) > distance:
            high = mid
        else:
            low = mid

    return time - 2 * high + 1


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
