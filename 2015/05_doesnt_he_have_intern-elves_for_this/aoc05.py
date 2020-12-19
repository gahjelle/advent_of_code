"""Doesn't He Have Intern-Elves For This?

Advent of Code 2015, day 5
Solution by Geir Arne Hjelle, 2016-12-03
"""
# Standard library imports
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def find_nice_strings_1(strings):
    return [
        s.strip()
        for s in strings
        if check_vowels(s) and check_double(s) and check_naughty(s)
    ]


def find_nice_strings_2(strings):
    return [s.strip() for s in strings if check_twice(s) and check_repeats(s)]


def check_vowels(string):
    """Check if string contains at least three vowels
    """
    return sum(string.count(v) for v in "aeiou") >= 3


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
    return not any(s in string for s in {"ab", "cd", "pq", "xy"})


def check_twice(string):
    """Check if string contains a pair of any two letters that appears at least
       twice without overlapping
    """
    for i in range(len(string) - 2):
        c, r = string[i : i + 2], string[i + 2 :]
        if c in r:
            return True
    return False


def check_repeats(string):
    """Check if string contains at least one letter which repeats with exactly
       one letter between
    """
    for c1, c2 in zip(string[:-2], string[2:]):
        if c1 == c2:
            return True
    return False


def main(args):
    for filename in args:
        if filename.startswith("-"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            strings = fid.readlines()

        # Part 1
        nice_strings = find_nice_strings_1(strings)
        print(f"{len(nice_strings)} strings are nice according to the old rules")
        debug(", ".join(sorted(nice_strings)))

        # Part 2
        nice_strings = find_nice_strings_2(strings)
        print(f"{len(nice_strings)} strings are nice according to the new rules")
        debug(", ".join(sorted(nice_strings)))


if __name__ == "__main__":
    main(sys.argv[1:])
