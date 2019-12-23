"""Probably a Fire Hazard

Advent of Code 2015, day 6
Solution by Geir Arne Hjelle, 2016-12-03 / 2019-12-23
"""
import sys
import numpy as np

import parse

PATTERN = parse.compile("{command} {row_1:d},{col_1:d} through {row_2:d},{col_2:d}")
COMMANDS = {}


def register(func):
    COMMANDS[func.__name__] = func
    return func


def _parse_line(line):
    info = PATTERN.parse(line.strip()).named
    command = info["command"].replace(" ", "_")
    rows = slice(info["row_1"], info["row_2"] + 1)
    cols = slice(info["col_1"], info["col_2"] + 1)

    return command, rows, cols


def count_lights(commands):
    lights = np.zeros((1000, 1000), dtype=bool)
    for command, rows, cols in commands:
        COMMANDS[command](lights, rows, cols)
    return np.sum(lights)


def calculate_brightness(commands):
    lights = np.zeros((1000, 1000), dtype=int)
    for command, rows, cols in commands:
        COMMANDS["elvish_" + command](lights, rows, cols)
    return np.sum(lights)


@register
def turn_on(lights, rows, cols):
    lights[rows, cols] = True


@register
def toggle(lights, rows, cols):
    lights[rows, cols] = ~lights[rows, cols]


@register
def turn_off(lights, rows, cols):
    lights[rows, cols] = False


@register
def elvish_turn_on(lights, rows, cols):
    lights[rows, cols] += 1


@register
def elvish_toggle(lights, rows, cols):
    lights[rows, cols] += 2


@register
def elvish_turn_off(lights, rows, cols):
    lights[rows, cols] -= 1
    lights[rows, cols][lights[rows, cols] < 0] = 0


def main(args):
    for filename in args:
        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            commands = [_parse_line(ln) for ln in fid]

        # Part 1
        lights = count_lights(commands)
        print(f"{lights} lights are lit")

        # Part 2
        brightness = calculate_brightness(commands)
        print(f"Total brightness is {brightness}")


if __name__ == "__main__":
    main(sys.argv[1:])
