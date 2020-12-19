"""Space Police

Advent of Code 2019, day 11
Solution by Geir Arne Hjelle, 2019-12-11
"""
# Standard library imports
import enum
import itertools
import pathlib
import sys
from dataclasses import dataclass, field

# Advent of Code imports
from aoc2019.intcode_computer import IntcodeComputer

debug = print if "--debug" in sys.argv else lambda *_: None


class Heading(enum.Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


TURN_LEFT = {
    Heading.UP: Heading.LEFT,
    Heading.DOWN: Heading.RIGHT,
    Heading.LEFT: Heading.DOWN,
    Heading.RIGHT: Heading.UP,
}

TURN_RIGHT = {
    Heading.UP: Heading.RIGHT,
    Heading.DOWN: Heading.LEFT,
    Heading.LEFT: Heading.UP,
    Heading.RIGHT: Heading.DOWN,
}


@dataclass
class Robot:
    x: int
    y: int
    heading: Heading
    colors: dict = field(default_factory=dict, repr=False)

    def turn(self, turn_code):
        if turn_code == 0:
            self.heading = TURN_LEFT[self.heading]
        else:
            self.heading = TURN_RIGHT[self.heading]

    def step(self):
        dx, dy = self.heading.value
        self.x += dx
        self.y += dy

    def paint(self, program, start):
        computer = IntcodeComputer(program, input=itertools.chain(start, self))
        while True:
            color = next(computer)
            if color is None:
                break
            debug(f"Paint {self.x, self.y} with {['black', 'white'][color]}")

            self.colors[(self.x, self.y)] = color
            self.turn(next(computer))
            self.step()

        return self.colors

    def __iter__(self):
        return self

    def __next__(self):
        return self.colors.get((self.x, self.y), 0)


def paint_ship(program, start=0):
    robot = Robot(0, 0, Heading.UP)
    return robot.paint(program, start=iter([start]))


def draw_painting(colors):
    pixel_map = {0: " ", 1: "█"}

    x_coords, y_coords = zip(*colors)
    x_start, x_end = min(x_coords), max(x_coords) + 1
    y_start, y_end = max(y_coords), min(y_coords) - 1

    for y in range(y_start, y_end, -1):
        print("".join(pixel_map[colors.get((x, y), 0)] for x in range(x_start, x_end)))


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        program = [int(s) for s in file_path.read_text().split(",")]

        # Part 1
        part_1 = paint_ship(program)
        print(f"Painted {len(part_1)} panels")

        # Part 2
        part_2 = paint_ship(program, start=1)
        print(f"Starting from white, painted the following:")
        draw_painting(part_2)


if __name__ == "__main__":
    main(sys.argv[1:])
