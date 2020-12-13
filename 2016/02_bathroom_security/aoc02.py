"""Bathroom Security

Advent of Code 2016, day 2
Solution by Geir Arne Hjelle, 2016-12-03
"""
import pathlib
import sys

# Keypad for first part:     1 2 3
#                            4 5 6
#                            7 8 9
#
KEYPAD_1 = {
    1: {"D": 4, "R": 2},
    2: {"D": 5, "R": 3, "L": 1},
    3: {"D": 6, "L": 2},
    4: {"U": 1, "D": 7, "R": 5},
    5: {"U": 2, "D": 8, "R": 6, "L": 4},
    6: {"U": 3, "D": 9, "L": 5},
    7: {"U": 4, "R": 8},
    8: {"U": 5, "R": 9, "L": 7},
    9: {"U": 6, "L": 8},
}

# Keypad for second part:           1
#                                 2 3 4
#                               5 6 7 8 9
#                                 A B C
#                                   D
#
KEYPAD_2 = {
    1: {"D": 3},
    2: {"D": 6, "R": 3},
    3: {"U": 1, "D": 7, "R": 4, "L": 2},
    4: {"D": 8, "L": 3},
    5: {"R": 6},
    6: {"U": 2, "D": "A", "R": 7, "L": 5},
    7: {"U": 3, "D": "B", "R": 8, "L": 6},
    8: {"U": 4, "D": "C", "R": 9, "L": 7},
    9: {"L": 8},
    "A": {"U": 6, "R": "B"},
    "B": {"U": 7, "D": "D", "R": "C", "L": "A"},
    "C": {"U": 8, "L": "B"},
    "D": {"U": "B"},
}


def find_code(fid, keypad):
    key = 5
    code = []
    for line in fid:
        for instruction in line.strip():
            key = keypad[key].get(instruction, key)
        code.append(str(key))
    return "".join(code)


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        print(f"Keypad 1: {find_code(fid, KEYPAD_1)}")

    with file_path.open(mode="r") as fid:
        print(f"Keypad 2: {find_code(fid, KEYPAD_2)}")


if __name__ == "__main__":
    main(sys.argv[1:])
