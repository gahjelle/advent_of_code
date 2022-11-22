"""AoC 11, 2021: Dumbo Octopus"""

# Standard library imports
import itertools
import pathlib
import sys
import time

# Third party imports
import colorama
import numpy as np
from colorama import Cursor

colorama.init()


def parse(puzzle_input):
    """Parse input"""
    return np.array(
        [[int(energy) for energy in line] for line in puzzle_input.split("\n")]
    )


def part1(data):
    """Solve part 1"""
    energy, num_flashes = data, 0
    for _ in range(100):
        energy, num_flashes = step(energy, num_flashes)

    return num_flashes


def part2(data):
    """Solve part 2"""
    for count in itertools.count(1):
        data, _ = step(data)
        if "--viz" in sys.argv:
            visualize(data)
        if np.all(data == 0):
            return count


def step(energies, num_flash=0):
    """Do one step on energy levels"""
    new_energies = energies + 1
    has_not_flashed = np.ones_like(energies, dtype=bool)

    while np.any(new_energies[has_not_flashed] > 9):
        to_flash = (new_energies > 9) & (has_not_flashed)

        new_energies[:-1, :-1] += to_flash[1:, 1:]
        new_energies[:, :-1] += to_flash[:, 1:]
        new_energies[1:, :-1] += to_flash[:-1, 1:]
        new_energies[:-1, :] += to_flash[1:, :]
        new_energies[1:, :] += to_flash[:-1, :]
        new_energies[:-1, 1:] += to_flash[1:, :-1]
        new_energies[:, 1:] += to_flash[:, :-1]
        new_energies[1:, 1:] += to_flash[:-1, :-1]

        has_not_flashed &= ~to_flash
        num_flash += np.sum(to_flash)

    new_energies[new_energies > 9] = 0
    return new_energies, num_flash


def visualize(data):
    """Show flashing energy levels"""
    markers = "# ._o*øO0@"
    for col, line in enumerate(data):
        for row, energy in enumerate(line):
            print(f"{Cursor.POS(col + 1, row + 5)}{markers[energy]}")
    time.sleep(0.05)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.startswith("-"):
            continue

        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
