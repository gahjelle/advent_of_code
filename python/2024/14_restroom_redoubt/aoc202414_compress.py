"""AoC 14, 2024: Restroom Redoubt."""

# Standard library imports
import collections
import itertools
import math
import pathlib
import sys
import zlib

# Third party imports
import matplotlib.pyplot as plt
import parse
from rich.progress import track

ROBOT_PATTERN = parse.compile("p={px:d},{py:d} v={vx:d},{vy:d}")


def parse_data(puzzle_input):
    """Parse input."""
    return [
        ((m["px"], m["py"]), (m["vx"], m["vy"]))
        for line in puzzle_input.split("\n")
        if (m := ROBOT_PATTERN.parse(line))
    ]


def part1(robots, width=101, height=103):
    """Solve part 1."""
    return math.prod(count_quadrants(move(robots, 100, width, height), width, height))


def part2(robots, width=101, height=103):
    """Solve part 2."""
    compressed = {}
    for num_seconds in track(range(width * height), description="Compressing ..."):
        compressed[num_seconds] = len(
            zlib.compress(grid_as_str(robots, width, height).encode("utf-8"))
        )
        robots = move(robots, 1, width, height)
    if "--show" in sys.argv:
        plot(*list(zip(*compressed.items())))
    _, christmas_tree = min((entropy, sec) for sec, entropy in compressed.items())
    return christmas_tree


def move(robots, num_seconds, width, height):
    """Move robots for the given number of seconds."""
    if num_seconds == 0:
        return robots

    return move(
        [
            (((px + vx) % width, (py + vy) % height), (vx, vy))
            for (px, py), (vx, vy) in robots
        ],
        num_seconds - 1,
        width,
        height,
    )


def count_quadrants(robots, width, height):
    mid_x, mid_y = width // 2, height // 2
    return [
        sum((px < mid_x) and (py < mid_y) for (px, py), _ in robots),
        sum((px < mid_x) and (py > mid_y) for (px, py), _ in robots),
        sum((px > mid_x) and (py < mid_y) for (px, py), _ in robots),
        sum((px > mid_x) and (py > mid_y) for (px, py), _ in robots),
    ]


def grid_as_str(robots, width, height):
    positions = collections.Counter(pos for pos, _ in robots)
    return "".join(
        str(positions.get((col, row), " "))
        for row, col in itertools.product(range(height), range(width))
    )


def plot(x, y):
    """Plot the compression data"""
    plt.scatter(x, y)
    plt.show()


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.startswith("-"):
            continue
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
