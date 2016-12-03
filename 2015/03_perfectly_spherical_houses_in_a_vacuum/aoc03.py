"""Perfectly Spherical Houses In A Vacuum

Advent of Code 2015, day 3
Solution by Geir Arne Hjelle, 2016-12-03
"""
import itertools
import sys

MOVES = {'^': lambda p: (p[0], p[1] + 1),
         'v': lambda p: (p[0], p[1] - 1),
         '>': lambda p: (p[0] + 1, p[1]),
         '<': lambda p: (p[0] - 1, p[1]),
         }


def count_houses(directions, num_santas):
    positions = [(0, 0)] * num_santas
    houses = {positions[0]}

    for direction, santa in zip(directions, itertools.cycle(range(num_santas))):
        positions[santa] = MOVES[direction](positions[santa])
        houses.add(positions[santa])

    return len(houses)


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                directions = line.strip()
                print('{:<8s}{:2s}: {} houses receive at least one present from 1 santa'
                      ''.format(directions[:8], '..' if len(directions) > 8 else '', count_houses(directions, 1)))
                print('{:<8s}{:2s}: {} houses receive at least one present from 2 santas'
                      ''.format(directions[:8], '..' if len(directions) > 8 else '', count_houses(directions, 2)))


if __name__ == '__main__':
    main()
