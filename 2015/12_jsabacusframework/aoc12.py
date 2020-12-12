"""JSAbacusFramework.io

Advent of Code 2015, day 12
Solution by Geir Arne Hjelle, 2016-12-10
"""
import json
import pathlib
import sys


def add_numbers(j_obj, ignore_red):
    try:
        return 0 + j_obj
    except TypeError:
        pass

    try:
        values = j_obj.values()
        if ignore_red and "red" in values:
            return 0
    except AttributeError:
        values = j_obj

    return sum(add_numbers(v, ignore_red) for v in values if not v == values)


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with open(file_path, mode="r") as fid:
        j_obj = json.load(fid)

    print(f"The total sum is {add_numbers(j_obj, False)}")
    print(f"The sum when ignoring red is {add_numbers(j_obj, True)}")


if __name__ == "__main__":
    main(sys.argv[1:])
