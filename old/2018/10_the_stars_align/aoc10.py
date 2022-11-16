"""The Stars Align

Advent of Code 2018, day 10
Solution by Geir Arne Hjelle, 2018-12-10
"""
# Standard library imports
import re
import sys

# Third party imports
import numpy as np

debug = print if "--debug" in sys.argv else lambda *_: None


class PosVel:
    def __init__(self, posvel):
        self.numobs = len(posvel)
        self._posvel = np.array(posvel)
        self._refpos = self._posvel[:, :2]
        self._vel = self._posvel[:, 2:]

    def pos(self, time):
        return self._refpos + self._vel * time


def parse_posvel(lines):
    pattern = re.compile(
        r"position=<([- \d]+),([- \d]+)> velocity=<([- \d]+),([- \d]+)>"
    )
    posvel = list()
    for num, line in enumerate(lines, start=1):
        match = pattern.match(line)
        if match:
            posvel.append([int(g) for g in match.groups()])
        else:
            print(f"Could not read line {num}: {line}")
    return PosVel(posvel)


def search(posvel, time=0):
    prev_area = np.inf
    while True:
        pos = posvel.pos(time)
        area = np.prod(np.max(pos, axis=0) - np.min(pos, axis=0))
        debug(f"Time: {time:6d}  Area: {area:8d}")
        if area > prev_area:
            break

        prev_area = area
        time += 1

    time -= 1
    return time, posvel.pos(time)


def write(message):
    coords = {tuple(p) for p in (message - message.min(axis=0))}
    max_x, max_y = max(x for x, y in coords) + 1, max(y for x, y in coords) + 1
    return "\n".join(
        "".join("█" if (x, y) in coords else " " for x in range(max_x))
        for y in range(max_y)
    )


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue
        filename, _, t_start = filename.partition(":")
        t_start = int(t_start) if t_start else 0

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            posvel = parse_posvel(line.strip() for line in fid)
            time, message = search(posvel, t_start)
            print(f"Time: {time}")
            print(f"Message:\n{write(message)}")


if __name__ == "__main__":
    main(sys.argv[1:])
