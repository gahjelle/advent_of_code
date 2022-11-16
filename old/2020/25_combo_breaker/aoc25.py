"""Combo Breaker

Advent of Code 2020, day 25
Solution by Geir Arne Hjelle, 2020-12-25
"""

# Standard library imports
import itertools
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def find_loopsize(public_key):
    """Find loopsize corresponding to the given public key"""
    value = 1
    for candidate in itertools.count(start=1):
        value = (value * 7) % 20201227
        if value == public_key:
            return candidate


def calculate_encryption_key(public_key, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * public_key) % 20201227

    return value


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    public_keys = [int(k) for k in file_path.read_text().strip().split()]
    loop_sizes = [find_loopsize(pk) for pk in public_keys]
    encryption_key = calculate_encryption_key(public_keys[0], loop_sizes[1])
    print(f"The encryption key is {encryption_key}")


if __name__ == "__main__":
    main(sys.argv[1:])
