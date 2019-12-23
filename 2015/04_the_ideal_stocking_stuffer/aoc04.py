"""The Ideal Stocking Stuffer

Advent of Code 2015, day 4
Solution by Geir Arne Hjelle, 2016-12-03
"""
import hashlib
import itertools
import sys


def find_md5_number(key, num_zeros, offset=1):
    prefix = "0" * num_zeros

    for counter in itertools.count(start=offset, step=1):
        md5 = hashlib.md5()
        md5.update(bytes(key + str(counter), encoding="utf-8"))

        if md5.hexdigest().startswith(prefix):
            return counter


def main(args):
    for filename in args:
        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            for line in fid:
                key = line.strip()

                # Part 1
                part_1 = find_md5_number(key, num_zeros=5)
                print(f"{key} - 5 zeros: {part_1}")

                # Part 2
                part_2 = find_md5_number(key, num_zeros=6, offset=part_1)
                print(f"{key} - 6 zeros: {part_2}")


if __name__ == "__main__":
    main(sys.argv[1:])
