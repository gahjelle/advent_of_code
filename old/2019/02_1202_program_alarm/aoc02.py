"""1202 Program Alarm

Advent of Code 2019, day 2
Solution by Geir Arne Hjelle, 2019-12-02 / 2019-12-07
"""
# Standard library imports
import itertools
import sys

# Advent of Code imports
from aoc2019.intcode_computer import IntcodeComputer

MOON = 19690720


def run_program(program, noun=12, verb=2):
    codes = program.copy()
    codes[1], codes[2] = noun, verb

    computer = IntcodeComputer(program=codes, input=None)
    computer.run()

    return computer.program[0]


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            line = next(fid)
            program = [int(c) for c in line.split(",")]

        # Part 1
        print(f"Program 1202 ended at {run_program(program)}")

        # Part 2: Attempt to calculate noun and verb
        base = run_program(program, 0, 0)
        dn = run_program(program, 1, 0) - base
        dv = run_program(program, 0, 1) - base

        if dn >= 1 and dv >= 1:
            noun = (MOON - base) // dn
            verb = (MOON - base) % dn // dv
            if (result := run_program(program, noun, verb)) == MOON:
                print(f"{noun:02d}{verb:02d} -> {result}")
                continue

        # Part 2: Brute force
        for noun, verb in itertools.product(range(100), range(100)):
            result = run_program(program, noun, verb)
            if result == MOON:
                print(f"{noun:02d}{verb:02d} -> {result}")
                break
        else:
            print(f"Did not find a valid noun and verb")


if __name__ == "__main__":
    debug = print if "--debug" in sys.argv else lambda *_: None
    main(sys.argv[1:])
