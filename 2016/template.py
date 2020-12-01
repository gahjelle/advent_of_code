"""

Advent of Code 2016, day 
Solution by Geir Arne Hjelle, 2016-12-
"""
import sys


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                print(line.strip())


if __name__ == '__main__':
    main()
