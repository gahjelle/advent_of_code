"""AoC 15, 2022: Beacon Exclusion Zone."""

# Standard library imports
import itertools
import pathlib
import sys
from functools import reduce
from typing import NamedTuple

# Third party imports
import parse

PATTERN = parse.compile(
    "Sensor at x={sx:d}, y={sy:d}: closest beacon is at x={bx:d}, y={by:d}"
)


class Sensor(NamedTuple):
    """Represent a sensor, its beacon, and its transformed coordinates."""

    x: int
    y: int
    bx: int
    by: int
    d: int
    ulx: int
    uly: int
    lrx: int
    lry: int


def parse_data(puzzle_input):
    """Parse input."""
    return [parse_sensor(line) for line in puzzle_input.split("\n")]


def parse_sensor(line):
    """Parse information about one sensor.

    Also do some processing on the data:
    - Calculate the Manhattan distance to the closest beacon (d)
    - Calculate the corners of the "sensor diamond" in diagonal coordinates

    The sensor diamonds become squares aligned to the axis in diagonal
    coordinates:

       A          E B A
      BCD          F C
     EFGHI   ->   J G D
      JKL          K H
       M          M L I

    ## Example:

    >>> parse_sensor("Sensor at x=13, y=2: closest beacon is at x=15, y=3")
    Sensor(x=13, y=2, bx=15, by=3, d=3, ulx=8, uly=12, lrx=14, lry=18)
    """
    coords = PATTERN.parse(line)
    sx, sy, bx, by = coords["sx"], coords["sy"], coords["bx"], coords["by"]
    d = abs(bx - sx) + abs(by - sy)
    dx, dy = to_diagonal_coords(sx, sy)
    return Sensor(
        x=sx, y=sy, bx=bx, by=by, d=d, ulx=dx - d, uly=dy - d, lrx=dx + d, lry=dy + d
    )


def to_diagonal_coords(x, y):
    """Convert Cartesian coordinates to diagonal ones.

    Use the following formulas:

      X = x - y
      Y = x + y

    ## Examples:

    >>> to_diagonal_coords(0, 0)
    (0, 0)
    >>> to_diagonal_coords(1, 0)
    (1, 1)
    >>> to_diagonal_coords(0, 1)
    (-1, 1)
    >>> to_diagonal_coords(1, 1)
    (0, 2)
    >>> to_diagonal_coords(3, -1)
    (4, 2)
    """
    return x - y, x + y


def to_cartesian_coords(x, y):
    """Convert diagonal coordintes to Cartesian ones.

    Use the following formulas:

      X = (y + x) / 2
      Y = (y - x) / 2

    Note that all "valid" diagonal coordinates will have (y + x) and (y - x)
    even.

    ## Examples:

    >>> to_cartesian_coords(0, 0)
    (0, 0)
    >>> to_cartesian_coords(1, 1)
    (1, 0)
    >>> to_cartesian_coords(-1, 1)
    (0, 1)
    >>> to_cartesian_coords(0, 2)
    (1, 1)
    >>> to_cartesian_coords(4, 2)
    (3, -1)
    """
    return (y + x) // 2, (y - x) // 2


def part1(sensors, row=2_000_000):
    """Solve part 1."""
    intervals = sorted(
        (
            sensor.x - (sensor.d - abs(row - sensor.y)),
            sensor.x + (sensor.d - abs(row - sensor.y)),
        )
        for sensor in sensors
        if sensor.d >= abs(row - sensor.y)
    )
    coverage = sum(
        last - first + 1 for first, last in reduce(collapse_interval, intervals, [])
    )
    beacons = {sensor.bx for sensor in sensors if sensor.by == row}
    return coverage - len(beacons)


def part2(sensors):
    """Solve part 2.

    Use coordinates transformed to squares and find where four squares almost
    meet. The intersection point is found by growing each square one unit.
    """
    for squares in itertools.combinations(sensors, 4):
        xs = {sq.ulx - 1 for sq in squares} & {sq.lrx + 1 for sq in squares}
        ys = {sq.uly - 1 for sq in squares} & {sq.lry + 1 for sq in squares}
        if xs and ys:
            x, y = to_cartesian_coords(xs.pop(), ys.pop())
            if all(abs(sq.x - x) + abs(sq.y - y) > sq.d for sq in sensors):
                return 4_000_000 * x + y


def slow_part2(sensors, rows=4_000_000):
    """Double down on collapsing sensor intervals per row for part two.

    Runs in about 20 seconds.
    """
    row, coverage = next(
        (row, intervals)
        for row in range(rows)
        if len(
            intervals := reduce(
                collapse_interval,
                sorted(
                    (
                        sensor.x - (sensor.d - abs(row - sensor.y)),
                        sensor.x + (sensor.d - abs(row - sensor.y)),
                    )
                    for sensor in sensors
                    if sensor.d > abs(row - sensor.y)
                ),
                [],
            )
        )
        > 1
    )
    return row + (coverage[0][1] + 1) * 4_000_000


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
