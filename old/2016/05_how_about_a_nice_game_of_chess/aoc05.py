"""How About a Nice Game of Chess?

Advent of Code 2016, day 5
Solution by Geir Arne Hjelle, 2016-12-05
"""

# Standard library imports
import hashlib
import itertools
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def find_md5_numbers(key, num_numbers=8, num_zeros=5):
    output = list()
    prefix = "0" * num_zeros
    for counter in itertools.count(start=1, step=1):
        md5 = hashlib.md5()
        md5.update(bytes(f"{key}{counter}", encoding="utf-8"))

        digest = md5.hexdigest()
        if digest.startswith(prefix):
            output.append(digest[num_zeros])
            debug(f"{counter:10d} {digest} {''.join(output)}")

            if len(output) >= num_numbers:
                return "".join(output)


def find_md5_with_positions(key, num_numbers=8, num_zeros=5):
    hex_letters = "0123456789abcdef"
    output = ["_"] * num_numbers + [None] * (16 - num_numbers)
    prefix = "0" * num_zeros
    for counter in itertools.count(start=1, step=1):
        md5 = hashlib.md5()
        md5.update(bytes(f"{key}{counter}", encoding="utf-8"))

        digest = md5.hexdigest()
        if digest.startswith(prefix):
            idx = hex_letters.index(digest[num_zeros])
            if output[idx] == "_":
                output[idx] = digest[num_zeros + 1]
                debug(f"{counter:10d} {digest} {''.join(output[:num_numbers])}")

            if not output.count("_"):
                return "".join(output[:num_numbers])


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        for line in fid:
            door_id = line.strip()
            print(f"{door_id} - first door:  {find_md5_numbers(door_id)}")
            print(f"{door_id} - second door: {find_md5_with_positions(door_id)}")


if __name__ == "__main__":
    main(sys.argv[1:])
