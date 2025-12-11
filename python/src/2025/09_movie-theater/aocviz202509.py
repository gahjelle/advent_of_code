"""AoC day 9, 2025: Movie Theater."""

import itertools
from pathlib import Path

from PIL import Image, ImageDraw

type Coordinate = tuple[int, int]

CX, CY = 800, 800
RADIUS = 760
AOC_YELLOW = (238, 214, 153)


def parse_data(puzzle_input: str) -> list[Coordinate]:
    """Parse puzzle input."""
    return [
        (int(x), int(y))
        for line in puzzle_input.splitlines()
        for x, y in [line.split(",")]
    ]


def part2(data: list[Coordinate], out_path: Path) -> None:
    """Visualize part 2."""
    draw_grid(data, out_path)


def draw_grid(data: list[Coordinate], out_path: Path) -> None:
    image = Image.new("RGB", size=(CX * 2, CY * 2), color=AOC_YELLOW)
    draw = ImageDraw.Draw(image)
    # draw.circle((CX, CY), RADIUS, fill=AOC_YELLOW)

    max_x = max(x for x, _ in data)
    max_y = max(y for _, y in data)
    print(f"{max_x = }, {max_y = }")
    for start, end in itertools.pairwise([*data, data[0]]):
        x1, y1 = to_coords(*start, max_x, max_y)
        x2, y2 = to_coords(*end, max_x, max_y)
        draw.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=1)

    for pairs in [
        (5765, 32241),
        (5267, 32241),
        (5178, 66511),
        (5649, 66511),
        (5649, 67626),
        (5642, 67626),
    ]:
        x, y = to_coords(*pairs, max_x, max_y)
        draw.circle((x, y), 5, fill=(255, 0, 0))

    image.save(out_path)


def to_coords(x: int, y: int, max_x: int, max_y: int) -> Coordinate:
    """Find coordinates of a single nail."""
    return int(x / max_x * CX * 2), int(y / max_y * CY * 2)
