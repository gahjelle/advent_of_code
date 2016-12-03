"""Probably a Fire Hazard

Advent of Code 2015, day 6
Solution by Geir Arne Hjelle, 2016-12-03
"""
import sys
import numpy as np


def _parse_line(line):
    words = line.strip().split()
    corner1 = tuple(int(c) for c in words[-3].split(','))
    corner2 = tuple(int(c) + 1 for c in words[-1].split(','))
    rows = slice(corner1[0], corner2[0])
    cols = slice(corner1[1], corner2[1])
    command = '_'.join(words[:-3])

    return command, rows, cols


def count_lights(fid):
    lights = np.zeros((1000, 1000), dtype=bool)
    for line in fid:
        command, rows, cols = _parse_line(line)
        globals()[command](lights, rows, cols)

    return np.sum(lights)


def calculate_brightness(fid):
    lights = np.zeros((1000, 1000), dtype=int)
    for line in fid:
        command, rows, cols = _parse_line(line)
        globals()['elvish_' + command](lights, rows, cols)

    return np.sum(lights)


def turn_on(lights, rows, cols):
    lights[rows, cols] = True


def toggle(lights, rows, cols):
    lights[rows, cols] = ~lights[rows, cols]


def turn_off(lights, rows, cols):
    lights[rows, cols] = False


def elvish_turn_on(lights, rows, cols):
    lights[rows, cols] += 1


def elvish_toggle(lights, rows, cols):
    lights[rows, cols] += 2


def elvish_turn_off(lights, rows, cols):
    lights[rows, cols] -= 1
    lights[rows, cols][lights[rows, cols] < 0] = 0


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))

        with open(filename, mode='r') as fid:
            print('{} lights are lit'.format(count_lights(fid)))

        with open(filename, mode='r') as fid:
            print('Total brightness is {}'.format(calculate_brightness(fid)))


if __name__ == '__main__':
    main()
