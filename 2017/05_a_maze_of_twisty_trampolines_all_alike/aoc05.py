"""A Maze of Twisty Trampolines, All Alike

Advent of Code 2017, day 5
Solution by Geir Arne Hjelle, 2017-12-05
"""
import sys


def do_jumps(jumps, threshold=None):
    current = 0
    num_jumps = len(jumps)
    num_steps = 0

    while 0 <= current < num_jumps:
        debug(jumps, current)
        jump = jumps[current]
        if threshold is None or jump < threshold:
            jumps[current] += 1
        else:
            jumps[current] -= 1
        current += jump
        num_steps += 1

    return num_steps


def print_jumps(jumps, current):
    jump_str = [f"({j})" if i == current else f" {j} " for i, j in enumerate(jumps)]
    print(" ".join(jump_str))


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            jumps = [int(n) for n in fid]
            print(f"Reached the exit in {do_jumps(jumps[:])} steps")
            print(f"With weird rule, used {do_jumps(jumps[:], 3)} steps")


debug = print_jumps if "--debug" in sys.argv else lambda *_: None

if __name__ == "__main__":
    main(sys.argv[1:])
