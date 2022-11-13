"""AoC 18, 2015: Like a GIF For Your Yard"""

# Standard library imports
import pathlib
import sys

import numpy as np


def parse(puzzle_input):
    """Parse input"""
    return [[light == "#" for light in row] for row in puzzle_input.split("\n")]


def part1(data, num_steps=100):
    """Solve part 1"""
    lights = np.array(data, dtype=np.uint8)
    for _ in range(num_steps):
        lights = animate_step(lights)
    return np.sum(lights)


def part2(data, num_steps=100):
    """Solve part 2"""
    lights = keep_corners_on(np.array(data, dtype=np.uint8))
    for _ in range(num_steps):
        lights = keep_corners_on(animate_step(lights))
    return np.sum(lights)


def keep_corners_on(lights):
    """Make sure corner lights are on.

    ## Example:

    >>> lights = np.array([[1, 1, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0]])
    >>> keep_corners_on(lights)
    array([[1, 1, 0, 1],
           [1, 0, 0, 1],
           [1, 0, 1, 1]])
    """
    corners = np.zeros_like(lights)
    corners[0, 0] = corners[0, -1] = corners[-1, 0] = corners[-1, -1] = 1
    return lights | corners


def animate_step(lights):
    """Animate one step of the light show.

    ## Example:

        #..#    2320    ##..
        ##.. -> 3443 -> #..#
        #.##    2421    #.#.

    >>> lights = np.array([[1, 0, 0, 1], [1, 1, 0, 0], [1, 0, 1, 1]])
    >>> animate_step(lights)
    array([[1, 1, 0, 0],
           [1, 0, 0, 1],
           [1, 0, 1, 0]])
    """
    num_rows, num_cols = lights.shape
    with_buffer = np.zeros((num_rows + 2, num_cols + 2), dtype=np.uint8)
    with_buffer[1:-1, 1:-1] = lights
    neighbors = (
        with_buffer[:-2, :-2]
        + with_buffer[1:-1, :-2]
        + with_buffer[2:, :-2]
        + with_buffer[:-2, 1:-1]
        + with_buffer[2:, 1:-1]
        + with_buffer[:-2, 2:]
        + with_buffer[1:-1, 2:]
        + with_buffer[2:, 2:]
    )
    return (lights & ((neighbors == 2) | (neighbors == 3))) | (~lights & neighbors == 3)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
