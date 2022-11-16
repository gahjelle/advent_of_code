"""

Advent of Code 2018, day
Solution by Geir Arne Hjelle, 2018-12-
"""
# Standard library imports
import sys


def main():
    for filename in sys.argv[1:]:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            for line in fid:
                print(line.strip())


if __name__ == "__main__":
    debug = print if "--debug" in sys.argv else lambda *_: None
    main()
