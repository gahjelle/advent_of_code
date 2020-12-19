"""

Advent of Code 2016, day
Solution by Geir Arne Hjelle, 2020-12-
"""
# Standard library imports
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    text = file_path.read_text()
    print(text)


if __name__ == "__main__":
    main(sys.argv[1:])
