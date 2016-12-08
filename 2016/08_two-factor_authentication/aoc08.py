"""Two-Factor Authentication

Advent of Code 2016, day 8
Solution by Geir Arne Hjelle, 2016-12-08
"""
import sys
import numpy as np


def set_up_lights(fid):
    lights = np.zeros((6, 50), dtype=bool)
    for line in fid:
        tokens = line.strip().split()
        if line.startswith('init '):    # for testing
            cols, rows = [int(c) for c in tokens[1].split('x')]
            lights = np.zeros((rows, cols), dtype=bool)
        elif line.startswith('rect '):
            cols, rows = [int(c) for c in tokens[1].split('x')]
            lights[:rows, :cols] = True
        elif line.startswith('rotate column x='):
            col = int(tokens[2][2:])
            offset = int(tokens[4])
            lights[:, col] = np.hstack((lights[-offset:, col], lights[:-offset, col]))
        elif line.startswith('rotate row y='):
            row = int(tokens[2][2:])
            offset = int(tokens[4])
            lights[row, :] = np.hstack((lights[row, -offset:], lights[row, :-offset]))

    return lights


def display_lights(lights):
    for row in lights:
        print('    |' + ''.join(('#' if l else ' ' for l in row)) + '|')


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            lights = set_up_lights(fid)
        print('{} lights are lit'.format(np.sum(lights)))
        display_lights(lights)

if __name__ == '__main__':
    main()
