"""No time for a Taxi Cab

Advent of Code 2016, day 1
Solution by Geir Arne Hjelle, 2016-12-03
"""
import pathlib
import sys

TURNS = {
    "N": {"R": "E", "L": "W"},
    "E": {"R": "S", "L": "N"},
    "S": {"R": "W", "L": "E"},
    "W": {"R": "N", "L": "S"},
}

MOVES = {
    "N": lambda p: (p[0], p[1] + 1),
    "E": lambda p: (p[0] + 1, p[1]),
    "S": lambda p: (p[0], p[1] - 1),
    "W": lambda p: (p[0] - 1, p[1]),
}


def find_distance(instructions):
    position = (0, 0)
    direction = "N"
    visited = set()

    for instruction in instructions:
        turn = instruction[0]
        distance = int(instruction[1:])
        direction = TURNS[direction][turn]
        for _ in range(distance):
            position = MOVES[direction](position)
            if position in visited:
                print(
                    "Already visited {} which is {} blocks away"
                    "".format(position, sum(abs(c) for c in position))
                )
            visited.add(position)

    print(
        "Ended at {} which is {} blocks away"
        "".format(position, sum(abs(c) for c in position))
    )


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        for line in fid:
            find_distance(i.strip() for i in line.split(","))


if __name__ == "__main__":
    main(sys.argv[1:])
