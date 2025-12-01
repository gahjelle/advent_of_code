"""AoC 12, 2019: The N-Body Problem."""

# Standard library imports
import itertools
import math
import pathlib
import sys
from dataclasses import dataclass

# Third party imports
import parse

MOON_PATTERN = parse.compile("<x={x:d}, y={y:d}, z={z:d}>")


@dataclass
class Moon:
    x: int
    y: int
    z: int
    vx: int = 0
    vy: int = 0
    vz: int = 0

    @classmethod
    def from_str(cls, line):
        """Create a Moon from a text description."""
        if match := MOON_PATTERN.parse(line):
            return cls(match["x"], match["y"], match["z"])

    def copy(self):
        """Create a copy of the Moon object."""
        cls = type(self)
        return cls(self.x, self.y, self.z, self.vx, self.vy, self.vz)

    def apply_gravity(self, other):
        """Apply gravity to moon based on other moon."""
        self.vx += 1 if self.x < other.x else -1 if self.x > other.x else 0
        self.vy += 1 if self.y < other.y else -1 if self.y > other.y else 0
        self.vz += 1 if self.z < other.z else -1 if self.z > other.z else 0

    def add_velocity(self):
        """Add velocity to position."""
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    @property
    def total_energy(self):
        """Calculate total energy for moon."""
        potential = abs(self.x) + abs(self.y) + abs(self.z)
        kinetic = abs(self.vx) + abs(self.vy) + abs(self.vz)
        return potential * kinetic


def parse_data(puzzle_input):
    """Parse input."""
    return [Moon.from_str(line) for line in puzzle_input.split("\n")]


def part1(moons, num_steps=1000):
    """Solve part 1."""
    moons = simulate(moons, num_steps=num_steps)
    return sum(moon.total_energy for moon in moons)


def part2(moons):
    """Solve part 2."""
    cycle_length = {}
    for xyz, step in find_cycles(moons):
        if xyz not in cycle_length:
            cycle_length[xyz] = step

        if len(cycle_length) == 3:
            break
    return math.lcm(*cycle_length.values())


def simulate(moons, num_steps):
    """Simulate the movement of the moons for a number of steps."""
    moons = [moon.copy() for moon in moons]
    for _ in range(num_steps):
        for moon_1, moon_2 in itertools.combinations(moons, 2):
            moon_1.apply_gravity(moon_2)
            moon_2.apply_gravity(moon_1)
        for moon in moons:
            moon.add_velocity()

    return moons


def find_cycles(moons):
    """Find the cycle length for all moons along each axis."""
    moons = [moon.copy() for moon in moons]
    seen = {"x": set(), "y": set(), "z": set()}
    for step_num in itertools.count(start=0):
        for moon_1, moon_2 in itertools.combinations(moons, 2):
            moon_1.apply_gravity(moon_2)
            moon_2.apply_gravity(moon_1)
        for moon in moons:
            moon.add_velocity()

        for xyz in "xyz":
            hash = tuple(
                (getattr(moon, xyz), getattr(moon, f"v{xyz}")) for moon in moons
            )
            if hash in seen[xyz]:
                yield xyz, step_num
            seen[xyz].add(hash)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
