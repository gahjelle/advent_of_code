"""Rain Risk

Advent of Code 2020, day 12
Solution by Geir Arne Hjelle, 2020-12-16
"""
# Standard library imports
import enum
import pathlib
import sys
from dataclasses import dataclass, field
from typing import Callable, ClassVar, NamedTuple

# Third party imports
import parse

debug = print if "--debug" in sys.argv else lambda *_: None

_INSTRUCTION = parse.compile("{action:1}{value:d}")


class Action(NamedTuple):
    method: Callable
    params: list

    def __repr__(self):
        return f"{self.method}({', '.join(str(p) for p in self.params)})"


class Instruction(NamedTuple):
    action: Action
    value: int


class Bearing(enum.IntEnum):
    NORTH = 0
    EAST = 90
    SOUTH = 180
    WEST = 270

    @property
    def char(self):
        """Get character representing bearing"""
        return self.name[0]

    def __add__(self, dvalue):
        value = (self.value + dvalue) % 360
        return getattr(
            self, {v: n for n, v in self.__class__.__members__.items()}[value]
        )


class Position(NamedTuple):
    lat: int
    lon: int
    bearing: Bearing = Bearing.EAST


@dataclass
class Ship:
    position: Position = field(init=False)
    instructions: list = field(default_factory=list)
    actions: ClassVar[dict] = {}

    def __post_init__(self):
        """Initialize position"""
        self.compiled = [
            Instruction(self.actions[n["action"]], n["value"])
            for i in self.instructions
            for n in [_INSTRUCTION.parse(i)]
        ]
        self.position = Position(0, 0, Bearing.EAST)

    def reset(self):
        """Reset position"""
        self.__post_init__()

    def sail(self):
        """Sail according to all instructions"""
        self.reset()
        for instruction in self.compiled:
            self.execute(instruction)
        print(self)

    def execute(self, instruction, log=True):
        """Execute one instruction"""
        action, value = instruction
        getattr(self, action.method)(value, *action.params)
        if log:
            debug(f"{str(instruction):<50} {self.position}")

    def distance(self, to=Position(0, 0)):
        """Calculate Manhattan distance to other position"""
        return sum(abs(p - t) for p, t in zip(self.position[:2], to[:2]))

    def __str__(self):
        pos = self.position
        return (
            f"The ship is at ({pos.lat}, {pos.lon}), "
            f"distance to origin: {self.distance()}"
        )


class ShipModel1(Ship):
    actions = {
        "N": Action("move", (1, 0)),
        "E": Action("move", (0, 1)),
        "S": Action("move", (-1, 0)),
        "W": Action("move", (0, -1)),
        "L": Action("turn", (-1,)),
        "R": Action("turn", (1,)),
        "F": Action("forward", ()),
    }

    def move(self, multiplier, dlat, dlon):
        """Move the ship, keep the bearing"""
        pos = self.position
        self.position = Position(
            pos.lat + dlat * multiplier, pos.lon + dlon * multiplier, pos.bearing
        )

    def turn(self, multiplier, dbearing):
        """Turn the ship, keep the position"""
        pos = self.position
        self.position = Position(pos.lat, pos.lon, pos.bearing + dbearing * multiplier)

    def forward(self, steps):
        """Move the ship forward"""
        self.execute(
            Instruction(self.actions[self.position.bearing.char], steps), log=False
        )


class ShipModel2(Ship):
    actions = {
        "N": Action("move_waypoint", (1, 0)),
        "E": Action("move_waypoint", (0, 1)),
        "S": Action("move_waypoint", (-1, 0)),
        "W": Action("move_waypoint", (0, -1)),
        "L": Action("rotate_waypoint", (-1,)),
        "R": Action("rotate_waypoint", (1,)),
        "F": Action("forward", ()),
    }
    rotations = {
        90: (lambda lat, lon: (-lon, lat)),
        180: (lambda lat, lon: (-lat, -lon)),
        270: (lambda lat, lon: (lon, -lat)),
    }

    def __post_init__(self):
        super().__post_init__()
        self.waypoint = Position(1, 10)

    def move_waypoint(self, multiplier, dlat, dlon):
        """Move the waypoint"""
        wpt = self.waypoint
        self.waypoint = Position(
            wpt.lat + dlat * multiplier, wpt.lon + dlon * multiplier
        )

    def rotate_waypoint(self, multiplier, dangle):
        """Rotate the waypoint"""
        wpt = self.waypoint
        self.waypoint = Position(*self.rotations[(dangle * multiplier) % 360](*wpt[:2]))

    def forward(self, steps):
        """Move the ship towards the waypoint"""
        pos, wpt = self.position, self.waypoint
        self.position = Position(pos.lat + wpt.lat * steps, pos.lon + wpt.lon * steps)


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    instructions = file_path.read_text().strip().split("\n")

    # Part 1
    ship = ShipModel1(instructions)
    ship.sail()

    # Part 2
    ship = ShipModel2(instructions)
    ship.waypoint = Position(1, 10)
    ship.sail()


if __name__ == "__main__":
    main(sys.argv[1:])
