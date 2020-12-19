"""High-Entropy Passphrases

Advent of Code 2017, day 4
Solution by Geir Arne Hjelle, 2017-12-04
"""
# Standard library imports
import sys


def count_valid(list_of_passphrases):
    return sum(len(set(p)) == len(p) for p in list_of_passphrases)


def sort_passphrases(list_of_passphrases):
    return [
        ["".join(sorted(letters)) for letters in words] for words in list_of_passphrases
    ]


def main(args):
    for filename in args:
        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            passphrases = [line.strip().split() for line in fid]

        # Part 1
        simple = count_valid(passphrases)
        print(f"{simple} valid phrases with simple policy")

        # Part 2
        anagram = count_valid(sort_passphrases(passphrases))
        print(f"{anagram} valid phrases with anagram policy")


if __name__ == "__main__":
    main(sys.argv[1:])
