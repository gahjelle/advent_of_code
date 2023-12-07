"""AoC 15, 2022: Beacon Exclusion Zone."""

# Standard library imports
import itertools
import pathlib
import re
import sys
from functools import reduce


def parse_data(puzzle_input):
    """Parse input.

    ## Example:

    >>> parse_data(
    ...     "Sensor at x=14, y=17: closest beacon is at x=10, y=16\\n"
    ...     "Sensor at x=8, y=7: closest beacon is at x=2, y=10"
    ... )
    ([(14, 17, 5), (8, 7, 9)], [(10, 16), (2, 10)])
    """
    sensors, beacons = zip(*[parse_sensor(line) for line in puzzle_input.split("\n")])
    size = 20 if max(sx for sx, _, _ in sensors) <= 30 else 4_000_000
    return list(sensors), list(beacons), size


def parse_sensor(line):
    """Parse information about one sensor.

    ## Example:

    >>> parse_sensor("Sensor at x=13, y=2: closest beacon is at x=15, y=3")
    ((13, 2, 3), (15, 3))
    """
    sx, sy, bx, by = map(int, re.findall(r"[xy]=(-?\d+)", line))
    d = abs(bx - sx) + abs(by - sy)
    return (sx, sy, d), (bx, by)


def part1(data):
    """Solve part 1."""
    sensors, beacons, size = data
    row = size // 2
    intervals = sorted(
        (x - (d - abs(row - y)), x + (d - abs(row - y)))
        for x, y, d in sensors
        if d >= abs(row - y)
    )
    coverage = sum(
        last - first + 1 for first, last in reduce(collapse_interval, intervals, [])
    )
    beacons_in_row = {bx for bx, by in beacons if by == row}
    return coverage - len(beacons_in_row)


def part2(data):
    """Solve part 2."""
    sensors, _, size = data

    # List diagonal lines one unit outside the borders of the diamonds
    nes = {xy for x, y, d in sensors for xy in [x + y + d + 1, x + y - d - 1]}
    ses = {xy for x, y, d in sensors for xy in [x - y + d + 1, x - y - d - 1]}

    # Loop over and check candidate intersection points
    for ne, se in itertools.product(nes, ses):
        x, y = (ne + se) // 2, (ne - se) // 2
        if (
            0 <= x <= size
            and 0 <= y <= size
            and all(abs(sx - x) + abs(sy - y) > d for sx, sy, d in sensors)
        ):
            return 4_000_000 * x + y


def collapse_interval(intervals, interval):
    """Collapse interval into intervals if it's overlapping.

    Assumes that intervals + [interval] is sorted.

    ## Example:

    >>> collapse_interval([(0, 2), (4, 7)], (5, 9))
    [(0, 2), (4, 9)]
    >>> collapse_interval([(1, 4)], (6, 11))
    [(1, 4), (6, 11)]
    >>> collapse_interval([(3, 9)], (4, 7))
    [(3, 9)]
    """
    if not intervals:
        return [interval]
    first_prev, last_prev = intervals[-1]
    first_new, last_new = interval
    if first_new <= last_prev + 1:
        return intervals[:-1] + [(first_prev, max(last_new, last_prev))]
    else:
        return intervals + [interval]


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
