"""Not Quite Lisp

Advent of Code 2015, day 1
Solution by Geir Arne Hjelle, 2016-12-03
"""
# Standard library imports
import sys

STEPS = {"(": 1, ")": -1}


def count_floors(parens):
    return sum(STEPS[s] for s in parens)


def find_basement(parens):
    floor = 0
    for count, step in enumerate(parens, start=1):
        floor += STEPS[step]
        if floor < 0:
            return count


def main(args):
    for filename in args:
        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            for line in fid:
                parens = line.strip()
                parens_str = f"{parens[:8]}.." if len(parens) > 10 else parens

                # Part 1
                num_floors = count_floors(parens)
                print(f"{parens_str:<10s}: Santa ends at floor {num_floors}")

                # Part 2
                basement = find_basement(parens)
                print(
                    f"{parens_str:<10s}: Santa enters the basement at step {basement}\n"
                )


if __name__ == "__main__":
    main(sys.argv[1:])
