"""Memory Reallocation

Advent of Code 2017, day 6
Solution by Geir Arne Hjelle, 2017-12-06
"""
import sys
import numpy as np


def redistribute(memory):
    seen = dict()
    num_banks = len(memory)

    while memory.tostring() not in seen:
        debug(memory)
        seen[memory.tostring()] = len(seen)

        idx_max = np.argmax(memory)
        num_blocks = memory[idx_max]
        memory[idx_max] = 0

        adder, num_blocks = divmod(num_blocks, num_banks)
        memory += adder
        while num_blocks > 0:
            idx_max = (idx_max + 1) % num_banks
            memory[idx_max] += 1
            num_blocks -= 1

    return len(seen), len(seen) - seen[memory.tostring()]


def main():
    for filename in sys.argv[1:]:
        if filename.startswith('--'):
            continue

        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                memory = np.array([int(n) for n in line.strip().split()])
                print('Using {} redistribution cycles, {} in loop'.format(*redistribute(memory)))


if __name__ == '__main__':
    debug = print if '--debug' in sys.argv else lambda *_: None
    main()