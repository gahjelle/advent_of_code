"""Elves Look, Elves Say

Advent of Code 2015, day 10
Solution by Geir Arne Hjelle, 2016-12-06
"""
import pathlib
import itertools
import sys


def look_and_say(sequence):
    while True:
        sequence = "".join(
            str(len(list(g[1]))) + g[0] for g in itertools.groupby(sequence)
        )
        yield sequence


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        for line in fid:
            lengths = [len(s) for s in itertools.islice(look_and_say(line.strip()), 50)]
            print(f"Length of {line.strip()} after 40 iterations: {lengths[39]}")
            print(f"Length of {line.strip()} after 50 iterations: {lengths[49]}")


if __name__ == "__main__":
    main(sys.argv[1:])
