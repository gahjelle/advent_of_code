"""AoC 12, 2020: Rain Risk"""

# Standard library imports
import enum
import functools
import math
import pathlib
import sys
from dataclasses import dataclass


def parse_data(puzzle_input):
    """Parse input"""
    return [(instr[0], int(instr[1:])) for instr in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    return move(data).manhattan()


def part2(data):
    """Solve part 2"""
    return move_with_waypoint(data).manhattan()


@dataclass(frozen=True)
class Vector2D:
    x: int = 0
    y: int = 0

    def manhattan(self):
        """Calculate L1-norm of vector

        ## Examples:

        >>> Vector2D(3, 4).manhattan()
        7
        >>> Vector2D(-4, 9).manhattan()
        13
        """
        return abs(self.x) + abs(self.y)

    def rotate(self, angle):
        """Rotate a vector around the origin

        ## Examples:

        >>> Vector2D(1, 2).rotate(0)
        Vector2D(x=1, y=2)
        >>> Vector2D(1, 2).rotate(90)
        Vector2D(x=-2, y=1)
        >>> Vector2D(1, 2).rotate(180)
        Vector2D(x=-1, y=-2)
        >>> Vector2D(1, 2).rotate(270)
        Vector2D(x=2, y=-1)
        """
        cls = self.__class__
        radians = math.radians(angle)
        cos, sin = math.cos(radians), math.sin(radians)
        return cls(
            round(self.x * cos - self.y * sin), round(self.x * sin + self.y * cos)
        )

    def __add__(self, other):
        """Add two vectors together

        ## Example:

        >>> Vector2D(2, 4) + Vector2D(9, -11)
        Vector2D(x=11, y=-7)
        """
        cls = self.__class__
        return cls(self.x + other.x, self.y + other.y)

    def __mul__(self, value):
        """Multiply a vector by a scalar

        ## Example:

        >>> Vector2D(-1, 3) * 4
        Vector2D(x=-4, y=12)
        """
        cls = self.__class__
        return cls(self.x * value, self.y * value)


class Direction(enum.IntEnum):
    N = 0
    E = 90
    S = 180
    W = 270

    @functools.cached_property
    def unit(self):
        """Unit vector in the given direction

        ## Examples

        >>> Direction.N.unit
        Vector2D(x=0, y=1)
        >>> Direction.E.unit
        Vector2D(x=1, y=0)
        >>> Direction.S.unit
        Vector2D(x=0, y=-1)
        >>> Direction.W.unit
        Vector2D(x=-1, y=0)
        """
        radians = math.radians(self)
        return Vector2D(round(math.sin(radians)), round(math.cos(radians)))

    @functools.cache
    def rotate(self, angle):
        """Rotate from the given direction

        ## Examples:

        >>> Direction.N.rotate(0)
        <Direction.N: 0>
        >>> Direction.S.rotate(90)
        <Direction.E: 90>
        >>> Direction.E.rotate(180)
        <Direction.W: 270>
        >>> Direction.W.rotate(270)
        <Direction.N: 0>
        >>> Direction.W.rotate(-90)
        <Direction.N: 0>
        """
        cls = self.__class__
        return cls((self - angle) % 360)


def move(instructions, pos=Vector2D(0, 0), face=Direction.E):
    """Move boat according to instructions

    ## Example:

    >>> move([("N", 3), ("F", 5), ("R", 90), ("F", 2)])
    Vector2D(x=5, y=1)
    """
    for instruction, value in instructions:
        match instruction:
            case "N" | "E" | "S" | "W":
                pos += Direction[instruction].unit * value
            case "F":
                pos += face.unit * value
            case "R":
                face = face.rotate(-value)
            case "L":
                face = face.rotate(value)
    return pos


def move_with_waypoint(instructions, pos=Vector2D(0, 0), waypoint=Vector2D(10, 1)):
    """Move waypoint and boat according to instructions

    ## Example:

    >>> move_with_waypoint([("F", 2), ("S", 1), ("L", 90), ("F", -3)])
    Vector2D(x=20, y=-28)
    """
    for instruction, value in instructions:
        match instruction:
            case "N" | "E" | "S" | "W":
                waypoint += Direction[instruction].unit * value
            case "F":
                pos += waypoint * value
            case "R":
                waypoint = waypoint.rotate(-value)
            case "L":
                waypoint = waypoint.rotate(value)
    return pos


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
