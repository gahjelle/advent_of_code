"""Leonardo's Monorail

Advent of Code 2016, day 12
Solution by Geir Arne Hjelle, 2016-12-12
"""

# Standard library imports
import pathlib
import sys

# Advent of Code imports
from aoc2016.assembunny import AssembunnyComputer


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    instructions = file_path.read_text()

    registers = AssembunnyComputer(instructions).run()
    print(f"The value of a is {registers['a']} after running the assembunny code")

    registers = AssembunnyComputer(instructions, c=1).run()
    print(f"Initializing c to 1 gives a value of {registers['a']} for a")


if __name__ == "__main__":
    main(sys.argv[1:])
