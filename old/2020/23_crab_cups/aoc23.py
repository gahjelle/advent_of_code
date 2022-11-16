"""Crab Cups

Advent of Code 2020, day 23
Solution by Geir Arne Hjelle, 2020-12-23
"""

# Standard library imports
import itertools
import math
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def circular_dict(cups_iter):
    cups = {}
    current_cups, next_cups = itertools.tee(cups_iter, 2)
    first_cup = next(next_cups)

    for current_cup, next_cup in zip(current_cups, next_cups):
        cups[current_cup] = next_cup
    cups[next_cup] = first_cup

    return first_cup, cups, next_cup


def move(ptr, cups, num_moves):
    max_cup = max(cups)

    for _ in range(num_moves):
        pick_ups = {cups[ptr], cups[cups[ptr]], pick_up := cups[cups[cups[ptr]]]}
        target = ptr - 1 if ptr > 1 else max_cup
        while target in pick_ups:
            target = target - 1 if target > 1 else max_cup

        cups[ptr], cups[target], cups[pick_up] = cups[pick_up], cups[ptr], cups[target]
        ptr = cups[ptr]

    return cups


def label_cups(cups):
    cup_list = []

    ptr = cups[1]
    while ptr != 1:
        cup_list.append(ptr)
        ptr = cups[ptr]

    return "".join(str(n) for n in cup_list)


def friends_of_1(cups):
    return cups[1], cups[cups[1]]


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    first_cup, cups, last_cup = circular_dict(
        int(c) for c in file_path.read_text().strip()
    )

    # Part 1
    part_1 = move(first_cup, dict(cups), 100)
    print(f"After 100 moves, the cups are {label_cups(part_1)}")

    # Part 2
    first, many_cups, last = circular_dict(range(len(cups) + 1, 1_000_000 + 1))
    many_cups.update(cups)
    many_cups[last_cup] = first
    many_cups[last] = first_cup

    part_2 = move(first_cup, many_cups, 10_000_000)
    print(f"After 10 million moves: {math.prod(friends_of_1(part_2))}")


if __name__ == "__main__":
    main(sys.argv[1:])
