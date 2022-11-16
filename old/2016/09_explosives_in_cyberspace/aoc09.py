"""Explosives in Cyberspace

Advent of Code 2016, day 9
Solution by Geir Arne Hjelle, 2016-12-09
"""
# Standard library imports
import itertools
import pathlib
import sys


def find_length(string, iterate):
    s_iter = iter(string)
    for c in s_iter:
        if c != "(":
            yield 1
            continue

        counter, repeats = [
            int(n)
            for n in "".join(itertools.takewhile(lambda c: c != ")", s_iter)).split("x")
        ]
        data = itertools.islice(s_iter, counter)
        yield repeats * (sum(find_length(data, True)) if iterate else len(list(data)))


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with open(file_path, mode="r") as fid:
        for line in fid:
            string = line.strip()
            print(f"{string[:40]:<40s} - Method one: {sum(find_length(string, False))}")
            print(f"{string[:40]:<40s} - Method two: {sum(find_length(string, True))}")


if __name__ == "__main__":
    main(sys.argv[1:])
