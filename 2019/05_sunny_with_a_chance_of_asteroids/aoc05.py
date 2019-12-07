"""Sunny With A Chance of Asteroids

Advent of Code 2019, day 5
Solution by Geir Arne Hjelle, 2019-12-05 / 2019-12-07
"""
import pathlib
import sys
from aoc2019.intcode_computer import IntcodeComputer


def run_program(program, input):
    computer_state = IntcodeComputer(program, input)
    states = []
    while True:
        state = next(computer_state)
        if state is None:
            return states

        states.append(state)


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        program = [int(c) for c in file_path.read_text().strip().split(",")]

        # Part 1
        part_1 = run_program(program, input=iter([1]))
        print(f"Diagnostic code for Air Conditioner: {part_1[-1]}")

        # Part 2
        part_2 = run_program(program, input=iter([5]))
        print(f"Diagnostic code for Thermal Radiator Controller: {part_2[0]}")


if __name__ == "__main__":
    debug = print if "--debug" in sys.argv else lambda *_: None
    main(sys.argv[1:])
