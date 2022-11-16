"""Lobby Layout

Advent of Code 2020, day 24
Solution by Geir Arne Hjelle, 2020-12-24
"""

# Standard library imports
import pathlib
import sys
from collections import Counter

# Third party imports
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

debug = print if "--debug" in sys.argv else lambda *_: None

FLOORSIZE = 250
INSTRUCTIONS = {
    "e": (2, 0),
    "w": (-2, 0),
    "ne": (1, -1),
    "se": (1, 1),
    "nw": (-1, -1),
    "sw": (-1, 1),
}


def parse_tile(line):
    """Parse instructions for one tile"""
    buffer = ""
    instructions = []
    for char in line:
        if buffer + char in INSTRUCTIONS:
            instructions.append(INSTRUCTIONS[buffer + char])
            buffer = ""
        else:
            buffer = char
    return np.array(instructions)


def get_floor(tiles):
    floor = np.zeros((FLOORSIZE, FLOORSIZE), dtype=int)
    for tile in tiles:
        floor[tile] = 1

    floor = np.concatenate(
        [np.concatenate([floor, floor]), np.concatenate([floor, floor])], axis=1
    )[
        FLOORSIZE // 2 : FLOORSIZE // 2 + FLOORSIZE,
        FLOORSIZE // 2 : FLOORSIZE // 2 + FLOORSIZE,
    ]

    if "--draw" in sys.argv:
        draw(floor)

    return floor


def draw(floor):
    plt.imshow(floor)
    plt.show()


def step(floor):
    current = floor.copy()
    neighbors = (
        current[:-4, 1:-1]
        + current[4:, 1:-1]
        + current[3:-1, :-2]
        + current[3:-1, 2:]
        + current[1:-3, :-2]
        + current[1:-3, 2:]
    )

    # Any black tile with zero or more than 2 black tiles immediately adjacent
    # to it is flipped to white.
    floor[2:-2, 1:-1][
        (current[2:-2, 1:-1] == 1) & ((neighbors == 0) | (neighbors > 2))
    ] = 0

    # Any white tile with exactly 2 black tiles immediately adjacent to it is
    # flipped to black.
    floor[2:-2, 1:-1][(current[2:-2, 1:-1] == 0) & (neighbors == 2)] = 1

    return floor


def animate(floor, num_days=100):
    if "--draw" in sys.argv:
        fig, ax = plt.subplots(figsize=(15, 15))
        floors = [step(floor).copy() for _ in range(num_days)]

        def draw_floor(day):
            ax.imshow(floors[day])
            ax.set_title(f"Day {day + 1}: {floors[day].sum()} tiles")

        _ = FuncAnimation(fig, draw_floor, frames=range(num_days), interval=100)
        plt.show()
    else:
        for _ in range(num_days):
            floor = step(floor)

    return floor


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    instructions = [parse_tile(ln) for ln in file_path.read_text().strip().split("\n")]

    # Part 1
    tiles = Counter([tuple(instr.sum(axis=0)) for instr in instructions])
    black = [t for t, c in tiles.items() if c % 2]
    print(f"There are {len(black)} black tiles")

    # Part 2
    floor = animate(get_floor(black), num_days=100)
    print(f"There are {floor.sum()} black tiles after 100 days")


if __name__ == "__main__":
    main(sys.argv[1:])
