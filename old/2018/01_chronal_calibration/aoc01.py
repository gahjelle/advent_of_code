"""Chronal Calibration

Advent of Code 2018, day 1
Solution by Geir Arne Hjelle, 2018-12-03
"""
# Standard library imports
import itertools
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def first_repeat(changes):
    total = 0
    seen = {total}
    for change in itertools.cycle(changes):
        total += change
        if total in seen:
            return total
        seen.add(total)


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            changes = [int(l) for l in fid]
            print(f"Resulting freq: {sum(changes)}")
            print(f"First repeat:   {first_repeat(changes)}")


if __name__ == "__main__":
    main(sys.argv[1:])
