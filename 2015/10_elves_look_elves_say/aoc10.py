"""Elves Look, Elves Say

Advent of Code 2015, day 10
Solution by Geir Arne Hjelle, 2016-12-06
"""
import itertools
import sys


def look_and_say(sequence, repeat):
    next_seq = ''.join(str(len(list(g[1]))) + g[0] for g in itertools.groupby(sequence))
    if repeat > 1:
        return [len(next_seq)] + look_and_say(next_seq, repeat-1)

    return [len(next_seq)]


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                seed = line.strip()
                lengths = look_and_say(seed, repeat=50)
                print('Length after 40 iterations: {}'.format(lengths[39]))
                print('Length after 50 iterations: {}'.format(lengths[49]))


if __name__ == '__main__':
    main()
