"""The Ideal Stocking Stuffer

Advent of Code 2015, day 4
Solution by Geir Arne Hjelle, 2016-12-03
"""
import hashlib
import itertools
import sys


def find_md5_number(key, num_zeros):
    for counter in itertools.count(start=1, step=1):
        md5 = hashlib.md5()
        md5.update(bytes(key + str(counter), encoding='utf-8'))

        if md5.hexdigest().startswith('0' * num_zeros):
            return counter


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                print('{} - 5 zeros: {}'.format(line.strip(), find_md5_number(line.strip(), 5)))
                print('{} - 6 zeros: {}'.format(line.strip(), find_md5_number(line.strip(), 6)))

if __name__ == '__main__':
    main()
