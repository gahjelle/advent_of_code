"""Tractor Beam

Advent of Code 2019, day 19
Solution by Geir Arne Hjelle, 2019-12-19
"""
# Standard library imports
import functools
import itertools
import pathlib
import sys

# Third party imports
import numpy as np

# Advent of Code imports
from aoc2019.intcode_computer import IntcodeComputer

debug = print if "--debug" in sys.argv else lambda *_: None


def generate_beam(program, size, angles=(0, np.degrees(90)), offset=(0, 0)):
    size_x, size_y = size
    dx, dy = offset
    min_rad, max_rad = angles
    beam = np.zeros(size, dtype=np.uint8)

    for x, y in itertools.product(range(size_x), range(size_y)):
        angle = np.arctan2(y + dy, x + dx)
        if min_rad <= angle <= max_rad:
            beam[y, x] = check_position(program, x + dx, y + dy)

    return beam


def check_position(program, x, y):
    return next(IntcodeComputer(program, input=iter([x, y])))


def estimate_angles(beam):
    # Avoid emitter
    beam = beam.copy()
    beam[0, 0] = 0

    # Find angles
    y, x = np.where(beam == 1)
    angles = np.arctan2(y, x)

    # Add a small buffer
    buffer = np.radians(0.1)
    return np.min(angles) - buffer, np.max(angles) + buffer


def find_square(program, angles, size):
    pos = functools.partial(check_position, program)

    # x and y follows the upper edge of the beam
    min_rad, max_rad = angles
    radius = size / (max_rad - min_rad) * np.sqrt(2)
    x = int(np.cos(min_rad) * radius)
    y = int(np.sin(min_rad) * radius)
    while pos(x, y):
        y -= 1

    # Check square corners, move on to the next x-coordinate
    dxy = size - 1
    while True:
        while not pos(x, y):
            y += 1
        debug(f"Checking {x, y}")

        if pos(x - dxy, y) and pos(x - dxy, y + dxy) and pos(x, y + dxy):
            break
        x += 1

    return x - dxy, y


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        program = [int(s) for s in file_path.read_text().split(",")]

        # Use smaller program to estimate angles
        beam = generate_beam(program, size=(25, 25))
        angles = estimate_angles(beam)

        # Part 1
        beam_1 = generate_beam(program, size=(50, 50), angles=angles)
        print(f"{np.sum(beam_1) + 1:.0f} points affected by the beam")

        # Part 2
        size = 100
        pos = find_square(program, angles, size=size)
        square_id = pos[0] * 10000 + pos[1]
        print(f"The closest {size}x{size} square is {square_id}")


if __name__ == "__main__":
    main(sys.argv[1:])
