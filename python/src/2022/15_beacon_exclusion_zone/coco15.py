# Standard library imports
import pathlib

# Third party imports
from codetiming import Timer


def main(puzzle_input, row, max_coord):
    data = parse(puzzle_input)
    solution1 = part1(data, row)
    solution2 = part2(data, max_coord)

    return solution1, solution2


@Timer(text="parse(): {milliseconds:.3f} ms")
def parse(puzzle_input: str):
    """Parse input"""
    return [
        [
            tuple(int(loc[2:]) for loc in pair.split(", "))
            for pair in line.strip("Sensor at ").split(": closest beacon is at ")
        ]
        for line in puzzle_input.splitlines()
    ]


@Timer(text="part1(): {milliseconds:.3f} ms")
def part1_(data, row):
    """Solve part 1.

    How many locations at the given row are covered by sensors but don't contain
    a beacon?

    1. Find min and max columns covered by any sensor at specific row
    2. For each column between min and max, check if it's covered by a sensor
    3. If it doesn't contain a beacon, increment a counter
    4. Return total number of positions that don't contain a beacon
    """
    sensors = [sensor for sensor, _ in data]
    beacons = {beacon for _, beacon in data}
    distances = [manhattan(sensor, beacon) for sensor, beacon in data]
    max_distance = max(distances)

    min_col = min(sensor[0] - max_distance for sensor in sensors)
    max_col = max(sensor[0] + max_distance for sensor in sensors)

    squares_where_beacon_cant_be = 0
    for col in range(min_col, max_col):
        if col % 100_000 == 0:  # Progress indicator
            print(f"Current at {col = :,} ({max_col = :,})")
        if any(
            manhattan((col, row), sensor) <= distance and (col, row) not in beacons
            for sensor, distance in zip(sensors, distances)
        ):
            squares_where_beacon_cant_be += 1

    return squares_where_beacon_cant_be


@Timer(text="part1(): {milliseconds:.3f} ms")
def part1(data, row):
    sensors = [sensor for sensor, _ in data]
    distances = [manhattan(sensor, beacon) for sensor, beacon in data]
    ranges = [
        coverage
        for sensor, distance in zip(sensors, distances)
        if (coverage := get_coverage(sensor, distance, row)) is not None
    ]
    sensor_coverage = sum(
        range_max - range_min for range_min, range_max in merge_ranges(ranges)
    )
    beacons_in_row = {b_col for _, (b_col, b_row) in data if b_row == row}

    return sensor_coverage - len(beacons_in_row)


@Timer(text="part2(): {milliseconds:.3f} ms")
def part2_(data, max_coord):
    """Solve part 2.

    Whats the only position that's not covered by any sensor in the search
    space? The search space is a square where the x and y coordinates are
    between 0 and max_coord.

    For each row, check if it has a hole in the coverage. To check a row,
    calculate the range each sensor covers, merge those ranges, and check if
    there is a column that isn't covered.

    Return the tuning frequency of the coordinate that isn't covered, where the
    distress beacon must be!
    """
    sensors = [sensor for sensor, _ in data]
    distances = [manhattan(sensor, beacon) for sensor, beacon in data]

    for row in range(max_coord):
        if row % 100_000 == 0:  # Progress indicator
            print(f"{row:,} rows out of {max_coord:,} inspected")
        ranges = [
            coverage
            for sensor, distance in zip(sensors, distances)
            if (coverage := get_coverage(sensor, distance, row)) is not None
        ]
        rng_union = merge_ranges(ranges)

        if len(rng_union) > 1:
            return rng_union[0][1] * 4_000_000 + row  # Tuning frequency


@Timer(text="part2(): {milliseconds:.3f} ms")
def part2(data, max_coord):
    """Solve part 2."""
    rotated = [
        (x + y, x - y, manhattan((x, y), (b_x, b_y))) for (x, y), (b_x, b_y) in data
    ]

    for x1, _, d1 in rotated:
        for _, y2, d2 in rotated:
            r_x = x1 - d1 - 1
            r_y = y2 - d2 - 1
            if all(manhattan((r_x, r_y), (x, y)) > d for x, y, d in rotated):
                x = (r_x + r_y) // 2
                y = (r_x - r_y) // 2
                if 0 <= x <= max_coord and 0 <= y <= max_coord:
                    return x, y, 4_000_000 * x + y

    n = 0
    for x1, _, d1 in rotated:
        for x2, _, d2 in rotated:
            for _, y3, d3 in rotated:
                for _, y4, d4 in rotated:
                    n += 1
                    if x1 - d1 - 1 == x2 + d2 + 1 and y3 - d3 - 1 == y4 + d4 + 1:
                        r_x = x1 - d1 - 1
                        r_y = y3 - d3 - 1
                        if all(
                            manhattan((r_x, r_y), (x, y)) > d for x, y, d in rotated
                        ):
                            x = (r_x + r_y) // 2
                            y = (r_x - r_y) // 2

                            return x, y, 4_000_000 * x + y

    # Third party imports
    import IPython

    IPython.embed()


def manhattan(p1, p2):
    """Get manhattan distance between two points

    ..........
    ....#.....
    ...###....
    ..##P##...
    ...###....
    ....#.....
    ..........
    """
    x = abs(p2[0] - p1[0])
    y = abs(p2[1] - p1[1])

    return x + y


def get_coverage(sensor, distance, row):
    """Get range of columns covered by a sensor in a row.

    Paramilliseconds:
      - sensor: (int, int), location of sensor
      - distance: int, manhattan distance to nearest beacon
      - row: int, the target row

    ## Example

      0123456789
    0 ..........
    1 ....#.....
    2 ...###....
    3 ..##P##...
    4 ...###.... < this row
    5 ....#.....
    6 ..........

    >>> get_coverage((4, 3), 2, row=4)
    (3, 6)
    """
    s_x, s_y = sensor
    if abs(s_y - row) > distance:
        return None
    side = abs(abs(s_y - row) - distance)
    return (s_x - side, s_x + side + 1)


def merge_ranges(ranges):
    """Merge ranges.

    Example:

    -3 -2 -1  0  1  2  3  4  5  6  7  8

                       |-----|
        |-----------|
                          |--------|

    Merge results in:

        |-----------|  |-----------|

    >>> merge_ranges([(3, 5), (-2, 2), (4, 7)])
    [(-2, 2), (3, 7)]
    """
    first, *ranges = sorted(ranges)
    non_overlapping = [first]

    for r in ranges:
        if r[0] <= non_overlapping[-1][1]:
            non_overlapping[-1] = (
                min(r[0], non_overlapping[-1][0]),
                max(r[1], non_overlapping[-1][1]),
            )
        else:
            non_overlapping.append(r)

    return non_overlapping


if __name__ == "__main__":
    sample_input = pathlib.Path("example1.txt").read_text().strip()
    solution1, solution2 = main(sample_input, row=10, max_coord=20)
    print(f"SAMPLE:\n\t{solution1 = }\n\t{solution2 = }\n")

    main_input = pathlib.Path("input.txt").read_text().strip()
    solution1, solution2 = main(main_input, row=2_000_000, max_coord=4_000_000)
    print(f"MAIN:\n\t{solution1 = }\n\t{solution2 = }")

"""
    The sensor diamonds become squares aligned to the axis in diagonal
    coordinates:

       A          E B A
      BCD          F C
     EFGHI   ->   J G D
      JKL          K H
       M          M L I


  H = (1, 0) -> (1, 1)
  K = (0, 1) -> (-1, 1)
      
  (x, y)
    = x(1, 0) + y(0, 1) -> x(1, 1) + y(-1, 1)
                         = (x-y, x+y)

  A = (0, -2)  -> (2, -2)
  L = (1, 1) -> (0, 2)      
"""

"""


"""
