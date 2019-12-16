"""Settlers of the North Pole

Advent of Code 2018, day 18
Solution by Geir Arne Hjelle, 2018-12-19
"""
import sys

import colorama
import numpy as np

colorama.init(autoreset=True)
debug = print if "--debug" in sys.argv else lambda *_: None

OPEN = 1
TREE = 2
YARD = 3


def parse_input(fid):
    def translate(line):
        return [{".": OPEN, "|": TREE, "#": YARD}[c] for c in line]

    return np.array([translate(c) for c in [l.strip() for l in fid]])


def grow(init_area, num_gen):
    offset = 2
    area = np.zeros(tuple(s + 2 * offset for s in init_area.shape))
    area[offset:-offset, offset:-offset] = init_area
    len_x, len_y = area.shape

    patterns = dict()
    gen = 0
    while gen < num_gen:
        if "--draw" in sys.argv:
            print_area(area[offset:-offset, offset:-offset], gen)

        hash = tuple(area.flatten().tolist())
        if hash in patterns:
            step = gen - patterns[hash]
            num_steps = (num_gen - gen) // step
            gen += num_steps * step
            patterns.clear()
        patterns[hash] = gen

        prev_area = area.copy()
        for x in range(offset, len_x - offset):
            for y in range(offset, len_y - offset):
                acre = prev_area[y - 1 : y + 2, x - 1 : x + 2].copy()
                acre[1, 1] = 0

                # OPEN -> TREE
                if area[y, x] == OPEN:
                    if np.sum(acre == TREE) >= 3:
                        area[y, x] = TREE

                # TREE -> YARD
                elif area[y, x] == TREE:
                    if np.sum(acre == YARD) >= 3:
                        area[y, x] = YARD

                # YARD -> OPEN
                elif area[y, x] == YARD:
                    if np.sum(acre == YARD) == 0 or np.sum(acre == TREE) == 0:
                        area[y, x] = OPEN
        gen += 1

    if "--draw" in sys.argv:
        print_area(area[offset:-offset, offset:-offset], num_gen)
    return value(area[offset:-offset, offset:-offset])


def value(area):
    return np.sum(area == TREE) * np.sum(area == YARD)


def print_area(area, gen):
    translate = {
        OPEN: f"{colorama.Fore.BLUE}.",
        TREE: f"{colorama.Fore.GREEN}▲",
        YARD: f"{colorama.Fore.YELLOW}▩",
    }

    area_map = "\n".join("".join(translate[c] for c in row) for row in area)
    print(f"{colorama.Cursor.POS(1, 5)}Generation {gen}\n{area_map}")


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            area = parse_input(fid)

            # Part 1
            num_mins = 10
            value = grow(area.copy(), num_mins)
            print(f"Value after {num_mins:,} minutes is {value}")

            # Part 2
            num_mins = 1_000_000_000
            value = grow(area.copy(), num_mins)
            print(f"Value after {num_mins:,} minutes is {value}")


if __name__ == "__main__":
    main(sys.argv[1:])
