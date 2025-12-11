"""AoC day 9, 2025: Movie Theater."""

import collections
import itertools

type Coordinate = tuple[int, int]
type CoordinateMapping = dict[int, int]
type PuzzleData = tuple[
    list[Coordinate], list[Coordinate], CoordinateMapping, CoordinateMapping
]
type Grid = set[Coordinate]


def parse_data(puzzle_input: str) -> PuzzleData:
    """Parse puzzle input.

    Use compressed coordinates. Use col, row for original coordinates and c, r
    for compressed coordinates.
    """
    corners = [
        (int(col), int(row))
        for line in puzzle_input.splitlines()
        for col, row in [line.split(",")]
    ]

    c2col = dict(enumerate(sorted({col for col, _ in corners})))
    col2c = {col: c for c, col in c2col.items()}
    r2row = dict(enumerate(sorted({row for _, row in corners})))
    row2r = {row: r for r, row in r2row.items()}

    return corners, [(col2c[col], row2r[row]) for col, row in corners], c2col, r2row


def part1(data: PuzzleData) -> int:
    """Solve part 1."""
    red, *_ = data

    max_area = 0
    for idx, (row, col) in enumerate(red):
        for row2, col2 in red[idx + 1 :]:
            if (area := calculate_area(row, col, row2, col2)) > max_area:
                max_area = area
    return max_area


def part2(data: PuzzleData) -> int:
    """Solve part 2.

    NOTE: Currently very slow (~5 mins)
    """
    _, red, c2col, r2row = data
    green = flood_fill(create_polygon(red))

    max_area = 0
    for idx, (col, row) in enumerate(red):
        for col2, row2 in red[idx + 1 :]:
            min_c, max_c = min(col, col2), max(col, col2)
            min_r, max_r = min(row, row2), max(row, row2)
            if (
                area := calculate_area(c2col[col], r2row[row], c2col[col2], r2row[row2])
            ) > max_area:
                num_green = len(
                    [
                        (c, r)
                        for c, r in green
                        if min_c <= c <= max_c and min_r <= r <= max_r
                    ]
                )
                if num_green == calculate_area(col, row, col2, row2):
                    print(area, c2col[col], r2row[row], c2col[col2], r2row[row2])
                    max_area = area
    return max_area


def create_polygon(corners: list[Coordinate]) -> Grid:
    """Draw a polygon based on the corners."""
    grid = set()
    for (x1, y1), (x2, y2) in itertools.pairwise([*corners, corners[0]]):
        dx = -1 if x1 > x2 else 0 if x1 == x2 else 1
        dy = -1 if y1 > y2 else 0 if y1 == y2 else 1
        if dx:
            y = y1
            for x in range(x1, x2 + dx, dx):
                grid.add((x, y))
        if dy:
            x = x1
            for y in range(y1, y2 + dy, dy):
                grid.add((x, y))
    return grid


def flood_fill(grid: Grid) -> Grid:
    """Use flood fill to find all coordinates inside the polygon."""
    # Find a good start candidate
    start = (0, 0)
    for col in itertools.count():
        first_row = {r for c, r in grid if c == col}
        next_row = {r for c, r in grid if c == col + 1}
        if candidates := first_row - next_row:
            start = (col + 1, candidates.pop())
            break

    # Flood fill the grid
    queue = collections.deque([start])
    flood = set()
    while queue:
        x, y = pos = queue.popleft()
        if pos in flood:
            continue
        flood.add(pos)

        for nx, ny in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
            if (nx, ny) in grid or (nx, ny) in flood:
                continue
            queue.append((nx, ny))
    return grid | flood


def calculate_area(x1: int, y1: int, x2: int, y2: int) -> int:
    """Calculate the area of the box with the given corners.

    ## Example:

    >>> calculate_area(2, 5, 9, 7)
    24
    >>> calculate_area(11, 7, 7, 1)
    35
    >>> calculate_area(7, 3, 2, 3)
    6
    >>> calculate_area(2, 5, 11, 1)
    50
    """
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


def display_grid(red: list[Coordinate]) -> None:
    """Display a grid in the console."""
    green = flood_fill(create_polygon(red))

    num_cols = max(col for col, _ in red) + 1
    num_rows = max(row for _, row in red) + 1
    for row in range(num_rows):
        for col in range(num_cols):
            print(
                "#" if (col, row) in red else "." if (col, row) in green else " ",
                end="",
            )
        print()
