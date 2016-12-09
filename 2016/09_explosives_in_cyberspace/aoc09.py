"""Explosives in Cyberspace

Advent of Code 2016, day 9
Solution by Geir Arne Hjelle, 2016-12-09
"""
import itertools
import sys


def find_length(string, iterate):
    length = 0
    s_iter = iter(string.strip())
    for c in s_iter:
        if c != '(':
            length += 1
            continue

        counter, repeats = [int(n) for n in ''.join(itertools.takewhile(lambda c: c != ')', s_iter)).split('x')]
        data = ''.join(itertools.islice(s_iter, counter))
        length += repeats * (find_length(data, True) if iterate else len(data))

    return length



def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                print('{:<40s} - Method one: {}'.format(line.strip()[:40], find_length(line, False)))
                print('{:<40s} - Method two: {}'.format(line.strip()[:40], find_length(line, True)))


if __name__ == '__main__':
    main()
