"""Chronal Charge

Advent of Code 2018, day 11
Solution by Geir Arne Hjelle, 2018-12-11
"""
# Standard library imports
import itertools
import sys

# Third party imports
import numpy as np

debug = print if "--debug" in sys.argv else lambda *_: None
SIZE = 300


def calculate_grid(serial_id):
    rng = np.arange(SIZE) + 1
    x, y = np.meshgrid(rng, rng)
    rack_id = x + 10

    return (rack_id * (rack_id * y + serial_id) // 100) % 10 - 5


def total_sum(grid, window):
    offset = window - 1
    total = np.zeros((SIZE - offset, SIZE - offset))
    for dx, dy in itertools.product(range(window), range(window)):
        total += grid[dy : SIZE - offset + dy, dx : SIZE - offset + dx]

    max_sum = int(np.max(total))
    y, x = np.where(total == max_sum)
    return max_sum, x[0] + 1, y[0] + 1


def all_windows(grid):
    # This can be made much faster by calculating the sums incrementally
    # instead of constantly redoing the sums
    sums = list()
    for window in range(1, SIZE + 1):
        max_sum, x, y = total_sum(grid, window)
        if max_sum < 0:
            break  # Stop early
        sums.append((max_sum, x, y, window))

    return max(sums)


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            ids = [int(line) for line in fid]
        for serial_id in ids:
            grid = calculate_grid(serial_id)
            max_sum, x, y = total_sum(grid, window=3)
            print(f"Serial ID: {serial_id:<5d}      {x},{y} (sum: {max_sum})")

            max_sum, x, y, window = all_windows(grid)
            print(f"       Best window:   {x},{y},{window} (sum: {max_sum})")


if __name__ == "__main__":
    main(sys.argv[1:])
