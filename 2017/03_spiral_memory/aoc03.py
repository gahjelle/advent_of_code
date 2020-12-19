"""Spiral Memory

Advent of Code 2017, day 3
Solution by Geir Arne Hjelle, 2017-12-03
"""
# Standard library imports
import sys

# Third party imports
import numpy as np


def calculate_steps(square):
    """Fast calculation, jump to correct circle/band of spiral"""
    circle = np.ceil((np.sqrt(square) - 1) / 2)
    corner = (2 * circle + 1) ** 2  # Lower-right corner is (2n + 1)^2
    steps = 2 * circle
    while corner > square:
        if corner - square <= circle:
            return steps - (corner - square)
        elif corner - square <= 2 * circle:
            return steps - (2 * circle - corner + square)
        corner -= 2 * circle

    return steps


def spiral_steps(number):
    """Slow calculation, fill in spiral, locate number"""
    size = np.ceil((np.sqrt(number) - 1) / 2)
    spiral, irow, icol = fill_in_spiral(number, size, lambda s: np.max(s) + 1)
    location = [i[0] - c // 2 for i, c in zip(np.where(spiral == number), spiral.shape)]

    return np.sum(np.abs(location))


def spiral_sum(number):
    # Use that at each turn the number more than doubles
    size = np.ceil(np.log2(number + 1) / 4)
    spiral, irow, icol = fill_in_spiral(number, size, lambda s: np.sum(s))

    return int(spiral[irow, icol])


def fill_in_spiral(number, size, method):
    # Allocate a spiral that will be big enough
    spiral = np.zeros((2 + int(2 * size + 1),) * 2)

    # Initialize
    irow, icol = [s // 2 for s in spiral.shape]  # Start in the middle
    drow, dcol = 0, 1  # Pointing right
    spiral[irow, icol] = 1

    # Fill in numbers until we find one bigger than the given number
    while True:
        if spiral[irow, icol] > number:
            return spiral, irow, icol
        irow += drow
        icol += dcol
        spiral[irow, icol] = method(spiral[irow - 1 : irow + 2, icol - 1 : icol + 2])

        # Should we turn?
        if spiral[irow - dcol, icol + drow] < 1:
            drow, dcol = -dcol, drow


def main(args):
    for filename in args:
        print("\n{}:".format(filename))
        with open(filename, mode="r") as fid:
            for line in fid:
                square = int(line.strip())

                # Part 1
                steps = calculate_steps(square)
                print(f"Square {square} is {steps:.0f} steps away")

                # Part 2
                first = spiral_sum(square)
                print(f"{first} is the first value larger than {square}\n")


if __name__ == "__main__":
    main(sys.argv[1:])
