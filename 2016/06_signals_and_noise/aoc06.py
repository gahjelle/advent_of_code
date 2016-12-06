"""Signals and Noise

Advent of Code 2016, day 6
Solution by Geir Arne Hjelle, 2016-12-06
"""
import sys


def common_letters(words, most_common):
    return ''.join(sorted(c, key=c.count, reverse=most_common)[0] for c in zip(*words))


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            words = [w.strip() for w in fid.readlines()]

        print('Error-corrected message:    {}'.format(common_letters(words, True)))
        print('Modified repetition code:   {}'.format(common_letters(words, False)))


if __name__ == '__main__':
    main()
