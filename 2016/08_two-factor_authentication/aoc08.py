"""Two-Factor Authentication

Advent of Code 2016, day 8
Solution by Geir Arne Hjelle, 2016-12-08
"""

# Standard library imports
import pathlib
import sys

# Third party imports
import numpy as np


def set_up_lights(fid):
    lights = np.zeros((6, 50), dtype=bool)
    for line in fid:
        tokens = line.strip().split()
        if line.startswith("init "):  # for testing
            cols, rows = [int(c) for c in tokens[1].split("x")]
            lights = np.zeros((rows, cols), dtype=bool)
        elif line.startswith("rect "):
            cols, rows = [int(c) for c in tokens[1].split("x")]
            lights[:rows, :cols] = True
        elif line.startswith("rotate column x="):
            col = int(tokens[2][2:])
            offset = int(tokens[4])
            lights[:, col] = np.hstack((lights[-offset:, col], lights[:-offset, col]))
        elif line.startswith("rotate row y="):
            row = int(tokens[2][2:])
            offset = int(tokens[4])
            lights[row, :] = np.hstack((lights[row, -offset:], lights[row, :-offset]))

    return lights


def display_lights(lights):
    for row in lights:
        print("    |" + "".join(("#" if light else " " for light in row)) + "|")


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        lights = set_up_lights(fid)
    print(f"{np.sum(lights)} lights are lit")
    display_lights(lights)


if __name__ == "__main__":
    main(sys.argv[1:])
