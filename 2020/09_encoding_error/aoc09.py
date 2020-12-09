"""Encoding Error

Advent of Code 2020, day 9
Solution by Geir Arne Hjelle, 2020-12-09
"""
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def find_adders(numbers, target):
    """Find two numbers that add up to target"""
    lookup = set(numbers)

    for first in numbers:
        if (target - first) in lookup and first != target - first:
            return first, target - first


def check_numbers(numbers, preamble):
    """Check numbers for first error in encoding"""
    for idx in range(preamble, len(numbers)):
        if not find_adders(numbers[idx - preamble : idx], numbers[idx]):
            return numbers[idx]


def find_contiguous(numbers, target):
    """Find a contiguous run of numbers that add up to target"""
    idx = len(numbers) - 1
    while idx > 1:
        for run_length in range(2, idx):
            run_sum = sum(numbers[idx - run_length : idx])
            if run_sum > target:
                break
            elif run_sum == target:
                return numbers[idx - run_length : idx]
        idx -= 1


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        preamble = int(next(fid))
        numbers = [int(num) for num in fid]

    # Part 1
    invalid = check_numbers(numbers, preamble)
    print(f"{invalid} is not the sum of any pair of the preceding {preamble} numbers")

    # Part 2
    run = find_contiguous(numbers, target=invalid)
    print(f"{min(run) + max(run)} is an exploitable weakness")


if __name__ == "__main__":
    main(sys.argv[1:])
