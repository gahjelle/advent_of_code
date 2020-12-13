"""Memory Reallocation

Advent of Code 2017, day 6
Solution by Geir Arne Hjelle, 2017-12-06
"""
import sys
import numpy as np

debug = print if "--debug" in sys.argv else lambda *_: None


def redistribute(memory):
    seen = dict()
    num_banks = len(memory)

    while memory.tobytes() not in seen:
        debug(memory)
        seen[memory.tobytes()] = len(seen)

        idx_max = np.argmax(memory)
        num_blocks = memory[idx_max]
        memory[idx_max] = 0

        adder, num_blocks = divmod(num_blocks, num_banks)
        memory += adder
        while num_blocks > 0:
            idx_max = (idx_max + 1) % num_banks
            memory[idx_max] += 1
            num_blocks -= 1

    return len(seen), len(seen) - seen[memory.tobytes()]


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue

        print("\n{}:".format(filename))
        with open(filename, mode="r") as fid:
            for line in fid:
                memory = np.array([int(n) for n in line.strip().split()])
                part_1, part_2 = redistribute(memory)
                print(f"Using {part_1} redistribution cycles, {part_2} in loop")


if __name__ == "__main__":
    main(sys.argv[1:])
