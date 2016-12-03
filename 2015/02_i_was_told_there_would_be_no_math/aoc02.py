"""I Was Told There Would Be No Math

Advent of Code 2015, day 2
Solution by Geir Arne Hjelle, 2016-12-03
"""
import sys


def calculate(fid):
    wrapping = list()
    ribbon = list()

    for line in fid:
        w, h, d = sorted([int(n) for n in line.split('x')])
        wrap_area = 2 * (w * h + w * d + h * d) + w * h
        ribbon_length = 2 * (w + h) + w * h * d
        wrapping.append(wrap_area)
        ribbon.append(ribbon_length)

        # print('{:<10s}: The elves need {:5d} ft² of wrapping paper and {:5d} ft of ribbon'
        #       ''.format(line.strip(), wrap_area, ribbon_length))

    return wrapping, ribbon

def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            wrapping, ribbon = calculate(fid)
            print('In total, the elves need {} ft² of wrapping paper and {} ft of ribbon'
                  ''.format(sum(wrapping), sum(ribbon)))


if __name__ == '__main__':
    main()
