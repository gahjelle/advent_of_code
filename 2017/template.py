"""

Advent of Code 2017, day
Solution by Geir Arne Hjelle, 2017-12-
"""
import sys


def main():
    for filename in sys.argv[1:]:
        if filename.startswith('--'):
            continue

        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                print(line.strip())


if __name__ == '__main__':
    debug = print if '--debug' in sys.argv else lambda *_: None
    main()
