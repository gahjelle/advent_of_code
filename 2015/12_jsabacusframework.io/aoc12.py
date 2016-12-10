"""JSAbacusFramework.io

Advent of Code 2015, day 12
Solution by Geir Arne Hjelle, 2016-12-10
"""
import json
import sys


def add_numbers(j_obj, ignore_red):
    try:
        return 0 + j_obj
    except TypeError:
        pass

    try:
        values = j_obj.values()
        if ignore_red and 'red' in values:
            return 0
    except AttributeError:
        values = j_obj

    return sum(add_numbers(v, ignore_red) for v in values if not v == values)


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            j_obj = json.load(fid)

        print('The total sum is {}'.format(add_numbers(j_obj, False)))
        print('The sum when ignoring red is {}'.format(add_numbers(j_obj, True)))


if __name__ == '__main__':
    main()
