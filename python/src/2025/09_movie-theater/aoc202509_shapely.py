"""AoC day 9, 2025: Movie Theater."""

from shapely import Polygon, box

type Coordinate = tuple[int, int]


def parse_data(puzzle_input: str) -> list[Coordinate]:
    """Parse puzzle input."""
    return [
        (int(row), int(col))
        for line in puzzle_input.splitlines()
        for row, col in [line.split(",")]
    ]


def part1(data: list[Coordinate]) -> int:
    """Solve part 1."""
    corners = sorted(data)

    max_area = 0
    for idx, (row, col) in enumerate(corners):
        for row2, col2 in corners[idx + 1 :]:
            if (area := (row2 - row + 1) * abs(col2 - col + 1)) > max_area:
                max_area = area
    return max_area


def part2(data: list[Coordinate]) -> int:
    """Solve part 2."""
    # up_x, up_y = 94564, 48699
    # low_x, low_y = 94564, 50077
    polygon = Polygon(data + [data[0]])
    # print(polygon)
    # min_up_y = min(y for x, y in data if x >= up_x)
    # max_low_y = max(y for x, y in data if x >= low_x)
    # print(min_up_y, max_low_y)

    max_area = 0
    for x1, y1 in data:
        for x2, y2 in data:  # [(94564, 48699), (94564, 50077)]:
            if (area := (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)) > max_area:
                rect = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
                # print(rect, polygon.contains(rect))
                if polygon.contains(rect):
                    # print(x1, y1, x2, y2, area)
                    max_area = area

    return max_area
