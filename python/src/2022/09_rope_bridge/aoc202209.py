"""AoC 9, 2022: Rope Bridge."""

# Standard library imports
import math
import pathlib
import shutil
import sys
import time

# Third party imports
import colorama
from colorama import Cursor, Fore, Style

colorama.init(autoreset=True)

DIRECTIONS = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}


def parse_data(puzzle_input):
    """Parse input."""
    return [step for line in puzzle_input.split("\n") for step in parse_line(line)]


def parse_line(line):
    """Parse one line of input.

    ## Example:

    >>> parse_line("R 4")
    [(1, 0), (1, 0), (1, 0), (1, 0)]
    """
    direction, number = line.split()
    return [DIRECTIONS[direction] for _ in range(int(number))]


def part1(steps):
    """Solve part 1."""
    knots = move_rope(steps, num_knots=2)
    return len(set(knots[-1]))


def part2(steps):
    """Solve part 2."""
    knots = move_rope(steps, num_knots=10)
    if "--viz" in sys.argv:
        animate(knots)
    return len(set(knots[-1]))


def move_rope(steps, num_knots):
    """Move a rope with the given number of knots.

    ## Example

    >>> steps = [(0, 1), (0, 1), (-1, 0), (0, -1), (-1, 0), (-1, 0)]
    >>> move_rope(steps, num_knots=2)
    [[(0, 0), (0, 1), (0, 2), (-1, 2), (-1, 1), (-2, 1), (-3, 1)],
     [(0, 0), (0, 0), (0, 1), (0, 1), (0, 1), (-1, 1), (-2, 1)]]
    >>> move_rope(steps, num_knots=3)
    [[(0, 0), (0, 1), (0, 2), (-1, 2), (-1, 1), (-2, 1), (-3, 1)],
     [(0, 0), (0, 0), (0, 1), (0, 1), (0, 1), (-1, 1), (-2, 1)],
     [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (-1, 1)]]
    """
    knots = [[(0, 0)] for _ in range(num_knots)]
    head = knots[0]
    for dx, dy in steps:
        hx, hy = head[-1]
        head.append((hx + dx, hy + dy))
        for knot, tail in zip(knots, knots[1:]):
            tail.append(adjust_tail(knot[-1], tail[-1]))
    return knots


def adjust_tail(head, tail):
    """Adjust the position of the tail so that it's next to the head.

    ## Examples:

    >>> adjust_tail((2, 2), (2, 2))
    (2, 2)
    >>> adjust_tail((2, -2), (0, 0))
    (1, -1)
    >>> adjust_tail((1, 1), (2, 0))
    (2, 0)
    >>> adjust_tail((4, 6), (2, 6))
    (3, 6)
    """
    (hx, hy), (tx, ty) = head, tail
    dx, dy = hx - tx, hy - ty
    return tail if max(abs(dx), abs(dy)) <= 1 else (tx + sign(dx), ty + sign(dy))


def sign(number):
    """Calculate the sign of the given number.

    ## Examples:

    >>> sign(0)
    0
    >>> sign(43)
    1
    >>> sign(-21)
    -1
    """
    return 1 if number > 0 else -1 if number < 0 else 0


def animate(knots):
    """Add an animation of the knots in the terminal."""
    sleep = 0.5 / math.sqrt(len(knots[0]))
    width, height = shutil.get_terminal_size()
    center_x, center_y = width // 2, height // 2
    camera_x, camera_y = 0, 0

    def pos(x, y):
        return Cursor.POS(center_x + x, center_y - y)

    ropes = zip(*knots)
    trace_1 = set()
    trace_9 = set()
    for (head_x, head_y), *rope in ropes:
        screen = [colorama.ansi.clear_screen()]
        trace_1.add(rope[0])
        trace_9.add(rope[8])

        # Move camera
        if abs(head_x - camera_x) > center_x - 5:
            camera_x = head_x + (center_x - 5) * sign(camera_x - head_x)
        if abs(head_y - camera_y) > center_y - 5:
            camera_y = head_y + (center_y - 5) * sign(camera_y - head_y)

        # Draw traces
        screen.append(f"{Style.NORMAL}{Fore.GREEN}")
        screen.extend(
            f"{pos(trace_x - camera_x, trace_y - camera_y)}."
            for trace_x, trace_y in trace_1
            if abs(trace_x - camera_x) <= center_x
            and abs(trace_y - camera_y) <= center_y
        )
        screen.append(f"{pos(-center_x + 2, center_y - 1)}. {len(trace_1)}")
        screen.append(f"{Style.NORMAL}{Fore.CYAN}")
        screen.extend(
            f"{pos(trace_x - camera_x, trace_y - camera_y)}o"
            for trace_x, trace_y in trace_9
            if abs(trace_x - camera_x) <= center_x
            and abs(trace_y - camera_y) <= center_y
        )
        screen.append(f"{pos(-center_x + 2, center_y - 2)}o {len(trace_9)}")

        # Draw rope
        screen.append(f"{Style.BRIGHT}{Fore.YELLOW}")
        screen.extend(
            f"{pos(knot_x - camera_x, knot_y - camera_y)}{knot}"
            for knot, (knot_x, knot_y) in list(enumerate(rope, start=1))[::-1]
        )
        screen.append(f"{pos(head_x - camera_x, head_y - camera_y)}H")
        print("".join(screen))
        time.sleep(sleep)


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
