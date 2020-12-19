"""Squares with Three Sides

Advent of Code 2016, day 3
Solution by Geir Arne Hjelle, 2016-12-03
"""

# Standard library imports
import sys

# Third party imports
import numpy as np


def count_triangles(triangles):
    return sum(np.sum(triangles, axis=1) > 2 * np.max(triangles, axis=1))


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        triangles = np.loadtxt(filename)
        print('Number of possible triangles in rows:    {}'.format(count_triangles(triangles)))
        print('Number of possible triangles in columns: {}'.format(count_triangles(triangles.T.reshape(-1, 3))))


if __name__ == '__main__':
    main()
