"""

Advent of Code 2020, day
Solution by Geir Arne Hjelle, 2020-12-
"""
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        text = file_path.read_text()
        print(text)


if __name__ == "__main__":
    main(sys.argv[1:])
