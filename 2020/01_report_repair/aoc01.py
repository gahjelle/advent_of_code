"""Report Repair

Advent of Code 2020, day 1
Solution by Geir Arne Hjelle, 2020-12-01
"""
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def find_adders(numbers, target=2020):
    """Find two numbers that add up to target"""
    lookup = set(numbers)

    for first in numbers:
        if (target - first) in lookup and first != target - first:
            return first, target - first

    return None, None


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")

        with file_path.open(mode="r") as fid:
            numbers = [int(line) for line in fid]

        # Part 1
        first, second = find_adders(numbers)
        print(f"{first} + {second} = 2020, and their product is {first * second}")

        # Part 2
        for idx, first in enumerate(numbers):
            second, third = find_adders(numbers[idx + 1 :], 2020 - first)
            if second and third:
                print(
                    f"{first} + {second} + {third} = 2020, "
                    f"and their product is {first * second * third}"
                )
                break


if __name__ == "__main__":
    main(sys.argv[1:])
