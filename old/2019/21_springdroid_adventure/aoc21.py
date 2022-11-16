"""Springdroid Adventure

Advent of Code 2019, day 21
Solution by Geir Arne Hjelle, 2019-12-21
"""
# Standard library imports
import pathlib
import sys

# Advent of Code imports
from aoc2019.intcode_computer import IntcodeComputer

debug = print if "--debug" in sys.argv else lambda *_, **__: None


def run_springdroid(intcode, program):
    droid = IntcodeComputer(intcode, input=iter(program))
    while True:
        output = next(droid)
        if output is None:
            break
        if output > 127:
            return output
        debug(chr(output), end="", flush=True)


def prepare(program):
    commands = [
        f"{c.partition('--')[0].strip()}\n" for c in program.strip().split("\n")
    ]
    return [ord(c) for c in "".join(commands)]


PROGRAM_1 = """
    NOT A J  -- HOLE at A              @.??#
    NOT B T
    OR T J   -- ... or HOLE at B       @?.?#
    NOT C T
    OR T J   -- ... or HOLE at C       @??.#
    AND D J  -- ... and GROUND at D
    WALK
"""


PROGRAM_2 = """
    NOT A J  -- HOLE at A                  @.??#?????
    NOT B T
    OR T J   -- ... or HOLE at B           @?.?#?????
    NOT C T  -- ... or (HOLE at C
    AND H T  --         and GROUND at H)   @??.#???#?
    OR T J
    AND D J  -- ... and GROUND at D
    RUN
"""


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        intcode = [int(s) for s in file_path.read_text().split(",")]

        # Part 1
        part_1 = run_springdroid(intcode, prepare(PROGRAM_1))
        print(f"Damage: {part_1}")

        # Part 2
        part_2 = run_springdroid(intcode, prepare(PROGRAM_2))
        print(f"Damage: {part_2}")


if __name__ == "__main__":
    main(sys.argv[1:])
