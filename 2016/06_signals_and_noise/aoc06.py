"""Signals and Noise

Advent of Code 2016, day 6
Solution by Geir Arne Hjelle, 2016-12-06
"""

# Standard library imports
import pathlib
import sys


def common_letters(words, most_common):
    return "".join(sorted(c, key=c.count, reverse=most_common)[0] for c in zip(*words))


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        words = [w.strip() for w in fid]

    print(f"Error-corrected message:    {common_letters(words, True)}")
    print(f"Modified repetition code:   {common_letters(words, False)}")


if __name__ == "__main__":
    main(sys.argv[1:])
