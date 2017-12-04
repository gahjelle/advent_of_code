"""High-Entropy Passphrases

Advent of Code 2017, day 4
Solution by Geir Arne Hjelle, 2017-12-04
"""
import sys


def count_valid(list_of_passphrases):
    return sum([len(set(p)) == len(p) for p in list_of_passphrases])


def sort_passphrases(list_of_passphrases):
    return [[''.join(sorted(letters)) for letters in words]
            for words in list_of_passphrases]


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            passphrases = [line.strip().split() for line in fid]
        print('{} valid phrases with simple policy'
              ''.format(count_valid(passphrases)))
        print('{} valid phrases with anagram policy'
              ''.format(count_valid(sort_passphrases(passphrases))))


if __name__ == '__main__':
    main()
