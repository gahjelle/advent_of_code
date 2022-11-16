"""Alchemical Reduction

Advent of Code 2018, day 5
Solution by Geir Arne Hjelle, 2018-12-05
"""
# Standard library imports
import sys

# Third party imports
import numpy as np

debug = print if "--debug" in sys.argv else lambda *_: None
REDUCED = -999


def to_numbers(polymer):
    nums = np.array([ord(c) - 96 for c in polymer])
    nums[nums < 0] = -(nums[nums < 0] + 32)
    return nums


def to_polymer(nums):
    nums[nums < 0] = -(nums[nums < 0] + 32)
    return "".join(chr(n) for n in nums + 96)


def reduce(polymer):
    nums = to_numbers(polymer)
    while True:
        # debug(to_polymer(nums.copy()))
        sums = nums[1:] + nums[:-1]
        if not np.any(sums == 0):
            break

        idx = np.where(sums == 0)[0]
        idx_reduce = idx[np.concatenate(([True], np.diff(idx) != 1))]
        nums[idx_reduce] = REDUCED
        nums[idx_reduce + 1] = REDUCED
        nums = nums[nums != REDUCED]

    return to_polymer(nums)


def test_all(polymer):
    lens = dict()
    for unit in sorted(set(polymer.lower())):
        lens[unit] = len(reduce("".join(c for c in polymer if not c.lower() == unit)))
        debug(f"{unit}: {lens[unit]}")
    return lens


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            for line in fid:
                polymer = line.strip()
                reduced = reduce(polymer)
                print(f"Length of reduced polymer: {len(reduced)}")

                lens = test_all(polymer)
                shortest = min(lens, key=lambda x: lens[x])
                print(f"Length of shortest polymer: {lens[shortest]} ({shortest})")


if __name__ == "__main__":
    main(sys.argv[1:])
