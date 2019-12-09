"""Sensor Boost

Advent of Code 2019, day 9
Solution by Geir Arne Hjelle, 2019-12-09
"""
import pathlib
import sys

from aoc2019.intcode_computer import IntcodeComputer

debug = print if "--debug" in sys.argv else lambda *_: None


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
        program = [int(s) for s in file_path.read_text().split(",")]

        # Part 1
        part_1 = run_program(program, input=iter([1]))[0]
        print(f"The keycode is {part_1}")

        # Part 2
        part_2 = run_program(program, input=iter([2]))[0]
        print(f"The coordinates are: {part_2}")


if __name__ == "__main__":
    main(sys.argv[1:])
