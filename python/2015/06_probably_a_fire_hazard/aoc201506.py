"""AoC 6, 2015: Probably a Fire Hazard"""

# Standard library imports
import pathlib
import sys

import numpy as np
import parse

PARSER = parse.compile("{cmd} {uly:d},{ulx:d} through {lry:d},{lrx:d}")
FUNCTIONS = {"flick": {}, "adjust": {}}


def register(kind):
    """Register a command to flick or adjust the lights."""

    def _register(func):
        """Store function in dict for later use."""
        FUNCTIONS[kind][func.__name__.partition("_")[-1]] = func
        return func

    return _register


def parse_data(puzzle_input):
    """Parse input"""
    return [parse_instruction(line) for line in puzzle_input.split("\n")]


def parse_instruction(line):
    """Parse one instruction.

    ## Examples:

    >>> parse_instruction("turn on 0,0 through 999,999")
    ('turn_on', slice(0, 1000, None), slice(0, 1000, None))
    >>> parse_instruction("toggle 0,0 through 999,0")
    ('toggle', slice(0, 1, None), slice(0, 1000, None))
    >>> parse_instruction("turn off 499,499 through 500,500")
    ('turn_off', slice(499, 501, None), slice(499, 501, None))
    """
    match = PARSER.parse(line)
    return (
        match["cmd"].replace(" ", "_"),
        slice(match["ulx"], match["lrx"] + 1),
        slice(match["uly"], match["lry"] + 1),
    )


def part1(instructions):
    """Solve part 1"""
    return np.sum(flick_lights(instructions, FUNCTIONS["flick"], dtype=bool))


def part2(instructions):
    """Solve part 2"""
    return np.sum(flick_lights(instructions, FUNCTIONS["adjust"], dtype=int))


def flick_lights(instructions, functions, dtype):
    """Flick the lights according to the given instructions"""
    lights = np.zeros((1000, 1000), dtype=dtype)
    for command, rows, cols in instructions:
        functions[command](lights, rows, cols)
    return lights


@register("flick")
def flick_turn_on(lights, rows, cols):
    """Turn on lights."""
    lights[rows, cols] = True


@register("flick")
def flick_turn_off(lights, rows, cols):
    """Turn off lights."""
    lights[rows, cols] = False


@register("flick")
def flick_toggle(lights, rows, cols):
    """Toggle lights."""
    lights[rows, cols] = ~lights[rows, cols]


@register("adjust")
def adjust_turn_on(lights, rows, cols):
    """Increase brightness by 1."""
    lights[rows, cols] += 1


@register("adjust")
def adjust_turn_off(lights, rows, cols):
    """Decrease brightness by 1 down to a minimum of 0."""
    lights[rows, cols] -= np.minimum(1, lights[rows, cols])


@register("adjust")
def adjust_toggle(lights, rows, cols):
    """Increase brightness by 2."""
    lights[rows, cols] += 2


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
