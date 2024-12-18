"""AoC 14, 2024: Restroom Redoubt."""

# Standard library imports
import math
import pathlib
import sys
from collections import Counter

# Third party imports
import colorama
import parse

colorama.init()
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
    """Solve part 2.

    Use that the horizontal and vertical positions will be periodical with
    periods width and height.
    """
    # Find when most robots come together vertically and horizontally
    max_x = sec_x = max_y = sec_y = 0
    for num_seconds in range(max(width, height)):
        num_x = Counter(x for (x, _), _ in robots).most_common(1)[0][1]
        if num_x > max_x:
            max_x, sec_x = num_x, num_seconds
        num_y = Counter(y for (_, y), _ in robots).most_common(1)[0][1]
        if num_y > max_y:
            max_y, sec_y = num_y, num_seconds
        robots = move(robots, 1, width, height)

    # Find when the vertical and horizontal blips overlap
    christmas_tree = next(
        sec
        for sec in range(sec_x, width * height, width)
        if (sec - sec_y) % height == 0
    )

    # Animate the robots
    if "--show" in sys.argv:
        for num_seconds in range(max(width, height) + 1, christmas_tree + 1):
            robots = move(robots, 1, width, height)
            show(robots, width, height)
            print(num_seconds)
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


def show(robots, width, height):
    grid = Counter(pos for pos, _ in robots)
    print(colorama.Cursor.POS(x=1, y=1))
    for row in range(height):
        for col in range(width):
            print(grid.get((col, row), " "), end="")
        print()


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
