"""Doesn't He Have Intern-Elves For This?

Advent of Code 2015, day 5
Solution by Geir Arne Hjelle, 2016-12-03
"""
import sys


def find_nice_strings_1(fid):
    return [s.strip() for s in fid if check_vowels(s) and check_double(s) and check_naughty(s)]


def find_nice_strings_2(fid):
    return [s.strip() for s in fid if check_twice(s) and check_repeats(s)]


def check_vowels(string):
    """Check if string contains at least three vowels
    """
    return sum(string.count(v) for v in 'aeiou') >= 3


def check_double(string):
    """Check if string contains at least one letter that appears twice in a row
    """
    for c1, c2 in zip(string[:-1], string[1:]):
        if c1 == c2:
            return True
    return False


def check_naughty(string):
    """Check that string does not contain the strings 'ab', 'cd', 'pq', or 'xy'
    """
    return not any(s in string for s in ('ab', 'cd', 'pq', 'xy'))


def check_twice(string):
    """Check if string contains a pair of any two letters that appears at least twice without overlapping
    """
    for i in range(len(string) - 2):
        l, c, r = string[:i], string[i:i+2], string[i+2:]
        if c in l or c in r:
            return True
    return False


def check_repeats(string):
    """Check if string contains at least one letter which repeats with exactly one letter between
    """
    for c1, c2 in zip(string[:-2], string[2:]):
        if c1 == c2:
            return True
    return False


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            nice_strings = find_nice_strings_1(fid)
            print('{} strings are nice according to the old rules\n  ({})'
                  ''.format(len(nice_strings), ', '.join(nice_strings)))

        with open(filename, mode='r') as fid:
            nice_strings = find_nice_strings_2(fid)
            print('{} strings are nice according to the new rules\n  ({})'
                  ''.format(len(nice_strings), ', '.join(nice_strings)))


if __name__ == '__main__':
    main()
