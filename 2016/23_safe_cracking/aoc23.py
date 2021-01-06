"""Safe Cracking

Advent of Code 2016, day 23
Solution by Geir Arne Hjelle, 2021-01-06
"""

# Standard library imports
import math
import pathlib
import sys

# Advent of Code imports
from aoc2016.assembunny import AssembunnyComputer

debug = print if "--debug" in sys.argv else lambda *_: None


def simplify(instructions, a):
    """Simplify code that calculates factorial"""
    factorial_code = (
        "cpy a b\ndec b\ncpy a d\ncpy 0 a\ncpy b c\ninc a\ndec c\njnz c -2\ndec d\n"
        "jnz d -5\ndec b\ncpy b c\ncpy c d\ndec d\ninc c\njnz d -2\ntgl c\n"
        "cpy -16 c\njnz 1 c"
    )
    simplified_factorial_code = (
        f"cpy {math.factorial(a)} a\ncpy 6 c\ntgl c\ninc d\ntgl c\ninc d\ntgl c"
    )

    return instructions.replace(factorial_code, simplified_factorial_code)


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    instructions = file_path.read_text()

    # Part 1
    registers = AssembunnyComputer(instructions, a=7).run()
    print(f"{registers['a']} should be sent to the safe")

    # Part 2
    registers = AssembunnyComputer(simplify(instructions, a=12)).run()
    print(f"{registers['a']} should actually be sent to the safe")


if __name__ == "__main__":
    main(sys.argv[1:])
