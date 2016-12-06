"""Elves Look, Elves Say

Advent of Code 2015, day 10
Solution by Geir Arne Hjelle, 2016-12-06
"""
import itertools
import sys


def look_and_say(sequence):
    while True:
        sequence = ''.join(str(len(list(g[1]))) + g[0] for g in itertools.groupby(sequence))
        yield sequence


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                lengths = [len(s) for s in itertools.islice(look_and_say(line.strip()), 50)]
                print('Length of {} after 40 iterations: {}'.format(line.strip(), lengths[39]))
                print('Length of {} after 50 iterations: {}'.format(line.strip(), lengths[49]))


if __name__ == '__main__':
    main()
