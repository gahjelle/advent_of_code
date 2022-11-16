"""Firewall Rules

Advent of Code 2016, day 20
Solution by Geir Arne Hjelle, 2017-05-28
"""

# Standard library imports
import pathlib
import sys


def read_blacklist(fid):
    return sorted(
        (int(first), int(last))
        for first, last in [line.strip().split("-") for line in fid]
    )


def find_lowest(blacklist):
    lowest = 0

    for first, last in blacklist:
        if first > lowest:
            return lowest
        if last >= lowest:
            lowest = last + 1

    return lowest


def count_allowed(blacklist):
    count = 0
    lowest = 0

    for first, last in blacklist:
        if first > lowest:
            count += first - lowest
        if last >= lowest:
            lowest = last + 1

    return count, lowest - 1  # Does not account for any IPs at the end of the interval


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        blacklist = read_blacklist(fid)
        print(f"Lowest available IP: {find_lowest(blacklist)}")

        count, lowest = count_allowed(blacklist)
        print(f"Number of available IPs: {count} (up to {lowest})")


if __name__ == "__main__":
    main(sys.argv[1:])
