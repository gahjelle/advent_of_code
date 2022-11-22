"""AoC 1, 2016: No Time for a Taxicab"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [(step[0], int(step[1:])) for step in puzzle_input.split(", ")]


class AlreadyVisited(Exception):
    """Note that a position has already been visited"""


class EasterBunnyPath:
    turns = {
        "N": {"R": "E", "L": "W"},
        "E": {"R": "S", "L": "N"},
        "S": {"R": "W", "L": "E"},
        "W": {"R": "N", "L": "S"},
    }
    units = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}

    def __init__(self, position=(0, 0), direction="N", raise_at_first_crossing=False):
        """Initialize"""
        self.position = position
        self.direction = direction
        self.raise_at_first_crossing = raise_at_first_crossing
        self.seen = {self.position}

    def walk(self, steps):
        """Walk the given steps"""
        for turn, num_steps in steps:
            self.direction = self.turns[self.direction][turn]
            for _ in range(num_steps):
                self.step()

    def step(self):
        """Take a step"""
        px, py = self.position
        dx, dy = self.units[self.direction]
        self.position = (px + dx, py + dy)

        if self.raise_at_first_crossing and self.position in self.seen:
            raise AlreadyVisited(self.position)

        self.seen.add(self.position)

    @property
    def distance(self):
        """Calculate the taxicab distance"""
        px, py = self.position
        return abs(px) + abs(py)


def part1(data):
    """Solve part 1"""
    path = EasterBunnyPath()
    path.walk(data)

    return path.distance


def part2(data):
    """Solve part 2"""
    path = EasterBunnyPath(raise_at_first_crossing=True)
    try:
        path.walk(data)
    except AlreadyVisited:
        return path.distance


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
