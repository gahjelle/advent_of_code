"""Inverse Captcha

Advent of Code 2017, day 1
Solution by Geir Arne Hjelle, 2017-12-01
"""
import sys


def calculate_next_captcha(line):
    digits = line + line[0]
    return sum([int(a) for a, b in zip(digits[:-1], digits[1:]) if a == b])


def calculate_halfway_captcha(line):
    num_dig = len(line)
    digits = line * 2
    return sum([int(a) for a, b in zip(digits[:num_dig], digits[num_dig//2:])
                if a == b])


def main():
    for filename in sys.argv[1:]:
        print(f'\n{filename}:')
        with open(filename, mode='r') as fid:
            for line in fid:
                digits = line.strip()
                digits_repr = digits if len(digits) < 9 else digits[:6] + '...'
                print('{:<10} {:6d} {:6d}'
                      ''.format(digits_repr,
                                calculate_next_captcha(digits),
                                calculate_halfway_captcha(digits)))


if __name__ == '__main__':
    main()
