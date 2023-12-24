"""AoC 24, 2023: Never Tell Me The Odds."""

# Standard library imports
import pathlib
import sys

# Third party imports
import sympy


def parse_data(puzzle_input):
    """Parse input."""
    return [
        [int(p) for p in line.replace("@", ",").split(",")]
        for line in puzzle_input.split("\n")
    ]


def part1(hailstones, min_xy=200_000_000_000_000, max_xy=400_000_000_000_000):
    """Solve part 1."""

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    num_in_area = 0
    for idx1, (x1, y1, _, dx1, dy1, _) in enumerate(hailstones):
        for x2, y2, _, dx2, dy2, _ in hailstones[idx1 + 1 :]:
            div = det((dy1, dy2), (dx1, dx2))
            if div == 0:
                continue  # Lines don't intersect

            d1 = det((x1, y1), (x1 + dx1, y1 + dy1))
            d2 = det((x2, y2), (x2 + dx2, y2 + dy2))
            x = det((d1, d2), (dx1, dx2)) / div
            y = det((d1, d2), (dy1, dy2)) / div
            t1 = (x - x1) / dx1
            t2 = (x - x2) / dx2

            if t1 >= 0 and t2 >= 0 and min_xy <= x <= max_xy and min_xy <= y <= max_xy:
                num_in_area += 1
    return num_in_area


def part2(hailstones):
    """Solve part 2."""
    x, y, z, dx, dy, dz, t1, t2, t3 = sympy.symbols("x, y, z, dx, dy, dz, t1, t2, t3")
    x1, y1, z1, dx1, dy1, dz1 = hailstones[0]
    x2, y2, z2, dx2, dy2, dz2 = hailstones[1]
    x3, y3, z3, dx3, dy3, dz3 = hailstones[2]

    equations = [
        x1 - x + (dx1 - dx) * t1,
        y1 - y + (dy1 - dy) * t1,
        z1 - z + (dz1 - dz) * t1,
        x2 - x + (dx2 - dx) * t2,
        y2 - y + (dy2 - dy) * t2,
        z2 - z + (dz2 - dz) * t2,
        x3 - x + (dx3 - dx) * t3,
        y3 - y + (dy3 - dy) * t3,
        z3 - z + (dz3 - dz) * t3,
    ]

    X, Y, Z, *_ = sympy.solve(equations, [x, y, z, dx, dy, dz, t1, t2, t3])[0]
    return X + Y + Z


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
