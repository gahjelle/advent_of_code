"""Crossed Wires

Advent of Code 2019, day 3
Solution by Geir Arne Hjelle, 2019-12-03
"""
import pathlib
import sys

from shapely import geometry


def find_intersections(commands):
    line_1, line_2 = [find_line(cmd) for cmd in commands]
    intersections = line_1.intersection(line_2)

    # Count steps by projecting along each line
    return [
        (int(p.x), int(p.y), int(steps))
        for p in intersections
        if (steps := line_1.project(p) + line_2.project(p)) > 0
    ]


def find_line(commands):
    point = geometry.Point(0, 0)
    points = [point]
    for command in commands:
        dir = command[0]
        step = int(command[1:])
        if dir == "R":
            point = geometry.Point(point.x + step, point.y)
        elif dir == "U":
            point = geometry.Point(point.x, point.y + step)
        elif dir == "L":
            point = geometry.Point(point.x - step, point.y)
        elif dir == "D":
            point = geometry.Point(point.x, point.y - step)
        points.append(point)

    return geometry.LineString(points)


def manhattan(coords):
    x, y, *_ = coords
    return abs(x) + abs(y)


def steps(coords):
    return coords[-1]


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        text = file_path.read_text().strip()
        commands = [ln.split(",") for ln in text.split("\n")]
        points = find_intersections(commands)

        # Part 1
        closest = min(points, key=manhattan)
        print(
            f"Closest intersection at {closest[:2]}: Distance = {manhattan(closest)}"
        )

        # Part 2
        first = min(points, key=steps)
        print(
            f"First intersection at {first[:2]}: Distance = {steps(first)}"
        )


if __name__ == "__main__":
    debug = print if "--debug" in sys.argv else lambda *_: None
    main(sys.argv[1:])
