"""Monitoring Station

Advent of Code 2019, day 10
Solution by Geir Arne Hjelle, 2019-12-10
"""
import math
import pathlib
import sys

import numpy as np

debug = print if "--debug" in sys.argv else lambda *_: None


def read_asteroids(text):
    rows = text.split()
    asteroids = {
        (x, y) for y, row in enumerate(rows) for x, c in enumerate(row) if c == "#"
    }
    width, height = len(rows[0]), len(rows)
    return asteroids, (width, height)


def count_locations(asteroids, size):
    map = np.zeros(size, dtype=int)
    for x, y in asteroids:
        map[x, y] = count_los(x, y, asteroids)

    return map


def count_los(x, y, asteroids):
    return len([1 for tx, ty in asteroids if in_sight(x, y, tx, ty, asteroids)])


def in_sight(x, y, to_x, to_y, asteroids):
    if to_x == x and to_y == y:
        return False

    dx, dy = to_x - x, to_y - y
    steps = math.gcd(dx, dy)
    step_x, step_y = dx / steps, dy / steps
    for step in range(1, steps):
        if (x + step * step_x, y + step * step_y) in asteroids:
            return False
    return True


def sort_by_angle(asteroids, x, y):
    asteroids.remove((x, y))
    return sorted(
        asteroids,
        key=lambda p: (
            np.arctan2(p[0] - x, y - p[1]) % (2 * math.pi),  # angle
            -abs(p[0] - x) - abs(p[1] - y),  # distance
        ),
    )


def vaporize(asteroids, x, y):
    vaporized = []
    while asteroids:
        debug(f"{len(asteroids)} asteroids left to vaporize")
        for to_x, to_y in asteroids.copy():
            if in_sight(x, y, to_x, to_y, asteroids):
                asteroids.remove((to_x, to_y))
                vaporized.append((to_x, to_y))
                debug(f"{len(vaporized):>5}: Blasting {to_x, to_y}")
    return vaporized


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        asteroids, size = read_asteroids(file_path.read_text())

        # Part 1
        map = count_locations(asteroids, size)
        x, y = np.unravel_index(map.argmax(), map.shape)
        print(f"Best location is {x, y} seeing {map[x, y]} asteroids")

        # Part 2
        asteroids = sort_by_angle(asteroids, x, y)
        order = vaporize(asteroids, x, y)
        idx = min(len(order), 200)
        print(f"The {idx}th asteroid to be blasted is {order[idx - 1]}")


if __name__ == "__main__":
    main(sys.argv[1:])
