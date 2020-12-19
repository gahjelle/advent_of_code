"""Corruption Checksum

Advent of code 2017, day 2
Solution by Geir Arne Hjelle, 2017-12-02
"""
# Standard library imports
import sys

# Third party imports
import numpy as np


def read_spreadsheet(filename):
    sheet = []
    with open(filename, mode="r") as fid:
        for line in fid:
            sheet.append([int(n) for n in line.strip().split()])

    return sheet


def calculate_rowsum(sheet):
    return sum(max(row) - min(row) for row in sheet)


def calculate_divisible_sum(sheet):
    total = 0
    for row in sheet:
        div = np.array([[divmod(r, c)[0] for c in row] for r in row])
        mod = np.array([[divmod(r, c)[1] for c in row] for r in row])
        mod += np.eye(len(mod), dtype=int)
        total += div[mod == 0][0]
    return total


def main(args):
    for filename in args:
        print(f"\n{filename}:")
        sheet = read_spreadsheet(filename)
        print(calculate_rowsum(sheet))
        print(calculate_divisible_sum(sheet))


if __name__ == "__main__":
    main(sys.argv[1:])
