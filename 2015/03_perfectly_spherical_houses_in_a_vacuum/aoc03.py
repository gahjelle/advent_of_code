"""Perfectly Spherical Houses In A Vacuum

Advent of Code 2015, day 3
Solution by Geir Arne Hjelle, 2016-12-03
"""
import itertools
import sys

MOVES = {
    "^": lambda p: (p[0], p[1] + 1),
    "v": lambda p: (p[0], p[1] - 1),
    ">": lambda p: (p[0] + 1, p[1]),
    "<": lambda p: (p[0] - 1, p[1]),
}


def count_houses(directions, num_santas):
    positions = [(0, 0)] * num_santas
    houses = {positions[0]}

    for direction, santa in zip(directions, itertools.cycle(range(num_santas))):
        positions[santa] = MOVES[direction](positions[santa])
        houses.add(positions[santa])

    return len(houses)


def main(args):
    for filename in args:
        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            for line in fid:
                directions = line.strip()
                dir_str = f"{directions[:8]}.." if len(directions) > 10 else directions

                # Part 1
                part_1 = count_houses(directions, num_santas=1)
                print(
                    f"{dir_str:<10}: {part_1} houses receive at least one present "
                    f"from 1 santa"
                )

                # Part 2
                part_2 = count_houses(directions, num_santas=2)
                print(
                    f"{dir_str:<10}: {part_2} houses receive at least one present "
                    f"from 2 santas"
                )


if __name__ == "__main__":
    main(sys.argv[1:])
