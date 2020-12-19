"""I Was Told There Would Be No Math

Advent of Code 2015, day 2
Solution by Geir Arne Hjelle, 2016-12-03
"""
# Standard library imports
import sys


def calculate(fid):
    wrapping = list()
    ribbon = list()

    for line in fid:
        w, h, d = sorted([int(n) for n in line.split("x")])
        wrap_area = 2 * (w * h + w * d + h * d) + w * h
        ribbon_length = 2 * (w + h) + w * h * d
        wrapping.append(wrap_area)
        ribbon.append(ribbon_length)

    return wrapping, ribbon


def main(args):
    for filename in args:
        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            wrapping, ribbon = calculate(fid)
            print(
                f"In total, the elves need {sum(wrapping)} ft² of wrapping paper "
                f"and {sum(ribbon)} ft of ribbon"
            )


if __name__ == "__main__":
    main(sys.argv[1:])
