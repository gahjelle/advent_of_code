"""Timing is everything

Advent of Code 2016, day 15
Solution by Geir Arne Hjelle, 2016-12-15
"""

# Standard library imports
import itertools
import pathlib
import sys


def read_disc(line):
    tokens = line.strip().split()
    num_pos = int(tokens[3])
    pos = (int(tokens[-1].strip(".")) + int(tokens[1].strip("#"))) % num_pos
    return num_pos, pos


def find_time_to_drop(discs):
    return next(itertools.dropwhile(lambda t: not tick(t, discs), itertools.count(1)))


def tick(time, discs):
    return not any((p + time) % n for n, p in discs)


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        discs = [read_disc(d) for d in fid]
        print(f"The capsule can be dropped at time {find_time_to_drop(discs)}")
        print(
            "With the extra disc, the capsule can be dropped at time "
            f"{find_time_to_drop(discs + [(11, len(discs) + 1)])}"
        )


if __name__ == "__main__":
    main(sys.argv[1:])
