"""AoC 17, 2021: Trick Shot

Model the trajectory using the formulas:

  x(t) = (x0 + 0.5)t - 0.5t², t <= x0
  y(t) = (y0 + 0.5)t - 0.5t²

These can be derived by noting that there is a constant acceleration a(t) = -1.
This implies that speed is v(t) = C - t. Integrating this, gives position
p(t) = Ct - 0.5t² + D. The constants can be decided by looking at time steps
t = 0 and t = 1: p(0) = 0 gives D = 0, and then p(1) = v0 gives C = v0 + 0.5.

Note that y'(t) = 0 when t = y0 + 0.5 which means that the trajectory is at its
highest at timesteps t = y0 and t = y0 + 1.

We can write y(t) = 0.5t(2y0 + 1 - t), which can be used to find when y(t) = 0.
Trivially, x(0) = 0 and y(0) = 0. Additionally, y(t) = 0 for t = 2y0 + 1. At the
previous time step y(2y0) = y0, and at the next time step y(2y0 + 2) = -y0 - 1.
"""

# Standard library imports
import math
import pathlib
import sys

# Third party imports
import parse

AREA_PATTERN = parse.compile(
    "target area: x={x_min:d}..{x_max:d}, y={y_min:d}..{y_max:d}"
)


def parse(puzzle_input):
    """Parse input"""
    area = AREA_PATTERN.parse(puzzle_input)
    return ((area["x_min"], area["x_max"]), (area["y_min"], area["y_max"]))


def part1(data):
    """Solve part 1"""
    _, (min_y, max_y) = data
    y0 = highest_y0(min_y, max_y)

    return position(y0, t=y0)


def part2(data):
    """Solve part 2"""
    x_range, y_range = data
    return len(valid_initials(*x_range, *y_range))


def position(v0, t):
    """Calculate position based on initial speed and time step"""
    return int((v0 + 0.5) * t - 0.5 * t**2)


def highest_y0(min_y, max_y):
    """Find the highest initial y that crosses the target area

    If the target area is below ground, the highest shot will touch the bottom
    of the target area at the first step below zero, y(2y0 + 2) = -y0 - 1:

        -y0 - 1 = min_y  <=>  y0 = -min_y - 1

    If the target area is above ground, the highest shot will touch the top
    of the target area at the last step above zero, y(2y0) = y0.

        y0 = max_y

    >>> highest_y0(-10, -5)
    9

    >>> highest_y0(4, 5)
    5

    >>> highest_y0(-2, 2)
    2
    """
    return max(-min_y - 1, max_y)


def all_valid_x0(min_x, max_x):
    """Calculate valid values for initial x speed

    The x position stops increasing at t = x0. The maximum x position is
    therefore given by x(x0) = (x0 + 0.5)x0 - 0.5 x0² = 0.5(x0² + x0).

    Find minimum x0 such x0² + x0 - 2 min_x >= 0 using the quadratic formula.

        x0 >= 0.5(-1 ± √(1 - 8 min_x))

    Maximum x0 is the highest x0 such that x(1) <= max_x, that is x0 = max_x

    >>> all_valid_x0(20, 30)
    range(6, 31)
    """
    min_valid = math.ceil((-1 + math.sqrt(1 + 8 * min_x)) / 2)
    return range(min_valid, max_x + 1)


def valid_t(x0, min_x, max_x, min_y, max_y):
    """Calculate time steps when x is within range, given initial x"""
    t_first = math.ceil((2 * x0 + 1 - math.sqrt((2 * x0 + 1) ** 2 - 8 * min_x)) / 2)
    if x0 < (-1 + math.sqrt(1 + 8 * max_x)) / 2:
        t_last = 2 * max(-min_y, max_y)
    else:
        t_last = math.floor((2 * x0 + 1 - math.sqrt((2 * x0 + 1) ** 2 - 8 * max_x)) / 2)

    return range(t_first, t_last + 1)


def valid_y0(t, min_y, max_y):
    """Find valid values for initial y for given t"""
    y_first = math.ceil((min_y - (t - t**2) / 2) / t)
    y_last = math.floor((max_y - (t - t**2) / 2) / t)

    return range(y_first, y_last + 1)


def valid_initials(min_x, max_x, min_y, max_y):
    """Calculate valid values for initial y for each given initial x"""
    initials = []
    for x0 in all_valid_x0(min_x, max_x):
        for t in valid_t(x0, min_x, max_x, min_y, max_y):
            initials.extend([(x0, y0) for y0 in valid_y0(t, min_y, max_y)])

    return set(initials)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
