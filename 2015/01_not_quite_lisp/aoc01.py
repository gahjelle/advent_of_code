"""Not Quite Lisp

Advent of Code 2015, day 1
Solution by Geir Arne Hjelle, 2016-12-03
"""
import sys

STEPS = {'(': 1, ')': -1}


def count_floors(parens):
    # parens.count('(') - parens.count(')')
    return sum(STEPS[s] for s in parens)


def find_basement(parens):
    floor = 0
    for count, step in enumerate(parens, start=1):
        floor += STEPS[step]
        if floor < 0:
            return count


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                parens = line.strip()
                print('{:<8s}{:2s}: Santa ends at floor {}'
                      ''.format(parens[:8], '..' if len(parens) > 8 else '', count_floors(parens)))
                print('{:<8s}{:2s}: Santa enters the basement at step {}\n'
                      ''.format(parens[:8], '..' if len(parens) > 8 else '', find_basement(parens)))


if __name__ == '__main__':
    main()
