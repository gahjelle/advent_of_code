"""How About a Nice Game of Chess?

Advent of Code 2016, day 5
Solution by Geir Arne Hjelle, 2016-12-05
"""
# Standard library imports
import hashlib
import itertools
import sys


def find_md5_numbers(key, num_numbers, num_zeros):
    output = list()
    for counter in itertools.count(start=1, step=1):
        md5 = hashlib.md5()
        md5.update(bytes(key + str(counter), encoding='utf-8'))

        digest = md5.hexdigest()
        if digest.startswith('0' * num_zeros):
            output.append(digest[num_zeros])
            print('{:10d} {} {}'.format(counter, digest, ''.join(output)))

        if len(output) >= num_numbers:
            return ''.join(output)


def find_md5_with_positions(key, num_numbers, num_zeros):
    hex_letters = '0123456789abcdef'
    output = ['_'] * num_numbers + [None] * (16 - num_numbers)
    for counter in itertools.count(start=1, step=1):
        md5 = hashlib.md5()
        md5.update(bytes(key + str(counter), encoding='utf-8'))

        digest = md5.hexdigest()
        if digest.startswith('0' * num_zeros):
            idx = hex_letters.index(digest[num_zeros])
            if output[idx] == '_':
                output[idx] = digest[num_zeros + 1]
                print('{:10d} {} {}'.format(counter, digest, ''.join(output[:num_numbers])))

        if not output.count('_'):
            return ''.join(output[:num_numbers])


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                print('{} - first door:  {}'.format(line.strip(),
                                                    find_md5_numbers(line.strip(), 8, 5)))

        with open(filename, mode='r') as fid:
            for line in fid:
                print('{} - second door: {}'.format(line.strip(),
                                                    find_md5_with_positions(line.strip(), 8, 5)))


if __name__ == '__main__':
    main()
