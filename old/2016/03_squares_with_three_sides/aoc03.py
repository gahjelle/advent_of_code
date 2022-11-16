"""Squares with Three Sides

Advent of Code 2016, day 3
Solution by Geir Arne Hjelle, 2016-12-03
"""

# Standard library imports
import pathlib
import sys

# Third party imports
import numpy as np


def count_triangles(triangles):
    return sum(np.sum(triangles, axis=1) > 2 * np.max(triangles, axis=1))


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    triangles = np.loadtxt(file_path)
    print(f"Number of possible triangles in rows:    {count_triangles(triangles)}")
    print(
        f"Number of possible triangles in columns: "
        f"{count_triangles(triangles.T.reshape(-1, 3))}"
    )


if __name__ == "__main__":
    main(sys.argv[1:])
