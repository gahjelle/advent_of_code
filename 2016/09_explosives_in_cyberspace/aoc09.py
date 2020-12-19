"""Explosives in Cyberspace

Advent of Code 2016, day 9
Solution by Geir Arne Hjelle, 2016-12-09
"""
# Standard library imports
import itertools
import sys


def find_length(string, iterate):
    s_iter = iter(string)
    for c in s_iter:
        if c != '(':
            yield 1
            continue

        counter, repeats = [int(n) for n in ''.join(itertools.takewhile(lambda c: c != ')', s_iter)).split('x')]
        data = itertools.islice(s_iter, counter)
        yield repeats * (sum(find_length(data, True)) if iterate else len(list(data)))


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                string = line.strip()
                print('{:<40s} - Method one: {}'.format(string[:40], sum(find_length(string, False))))
                print('{:<40s} - Method two: {}'.format(string[:40], sum(find_length(string, True))))


if __name__ == '__main__':
    main()
