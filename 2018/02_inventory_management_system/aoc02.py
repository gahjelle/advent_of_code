"""Inventory Management System

Advent of Code 2018, day 2
Solution by Geir Arne Hjelle, 2018-12-03
"""
from collections import Counter
import itertools
import sys


def contains_count(count, ids):
    return sum(count in Counter(id).values() for id in ids)


def almost_equal(ids):
    for str1, str2 in itertools.product(ids, repeat=2):
        if string_dist(str1, str2) == 1:
            break
    else:
        raise ValueError("Could not find two almost equal strings")

    return "".join(c1 for c1, c2 in zip(str1, str2) if c1 == c2)


def string_dist(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))


def main():
    for filename in sys.argv[1:]:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            ids = [l.strip() for l in fid]
            checksum = contains_count(2, ids) * contains_count(3, ids)
            print(f"Checksum: {checksum}")

            common_letters = almost_equal(ids)
            print(f"Common letters: {common_letters}")


if __name__ == "__main__":
    debug = print if "--debug" in sys.argv else lambda *_: None
    main()
