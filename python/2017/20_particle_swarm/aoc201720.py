"""AoC 20, 2017: Particle Swarm."""

# Standard library imports
import collections
import itertools
import pathlib
import sys
from dataclasses import dataclass

# Third party imports
import parse

PATTERN = parse.compile(
    "p=<{px:d},{py:d},{pz:d}>, v=<{vx:d},{vy:d},{vz:d}>, a=<{ax:d},{ay:d},{az:d}>"
)


@dataclass(frozen=True)
class XYZ:
    """A class representing an X, Y, Z-tuple that support vector operations."""

    x: int
    y: int
    z: int

    def __add__(self, other):
        """Vector addition.

        ## Example:

        >>> XYZ(1, 2, 3) + XYZ(2, -4, 8)
        XYZ(x=3, y=-2, z=11)
        """
        cls = self.__class__
        return cls(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, scalar):
        """Scalar multiplication.

        ## Example:

        >>> XYZ(1, -2, 4) * 3
        XYZ(x=3, y=-6, z=12)
        """
        cls = self.__class__
        return cls(self.x * scalar, self.y * scalar, self.z * scalar)

    def __abs__(self):
        """Manhattan (L1) norm.

        ## Example:

        >>> abs(XYZ(3, -1, 7))
        11
        """
        return abs(self.x) + abs(self.y) + abs(self.z)


@dataclass(frozen=True)
class Particle:
    """A particle, represented by position, velocity and acceleration vectors."""

    pos: XYZ
    vel: XYZ
    acc: XYZ

    @classmethod
    def from_string(cls, line):
        """Parse one particle from a string.

        ## Example:

        >>> Particle.from_string("p=<395,-997,4914>, v=<-30,66,-69>, a=<1,-2,-8>")
        Particle(pos=XYZ(x=395, y=-997, z=4914), vel=XYZ(x=-30, y=66, z=-69), acc=XYZ(x=1, y=-2, z=-8))
        """
        m = PATTERN.parse(line)
        return cls(
            pos=XYZ(m["px"], m["py"], m["pz"]),
            vel=XYZ(m["vx"], m["vy"], m["vz"]),
            acc=XYZ(m["ax"], m["ay"], m["az"]),
        )

    def pos_at_t(self, t):
        """Position at time t.

        ## Example:

        >>> p = Particle(XYZ(1, 2, 3), XYZ(3, -1, 0), XYZ(-1, 0, 0))
        >>> p.pos_at_t(0)
        XYZ(x=1, y=2, z=3)
        >>> p.pos_at_t(1)
        XYZ(x=3, y=1, z=3)
        >>> p.pos_at_t(2)
        XYZ(x=4, y=0, z=3)
        >>> p.pos_at_t(5)
        XYZ(x=1, y=-3, z=3)
        """
        return self.pos + self.vel * t + self.acc * ((t + 1) * t // 2)

    def long_term_norm(self):
        """Represent distance to origin in the long term.

        Use first derivative to consider slope. Represent long term by a large t.

        ## Example:

        >>> p = Particle(XYZ(1, 2, 3), XYZ(3, -1, 0), XYZ(-1, 0, 0))
        >>> p.long_term_norm()
        999998
        """
        t = 1_000_000
        return abs(self.vel + self.acc * t)


def parse_data(puzzle_input):
    """Parse input."""
    return [Particle.from_string(line) for line in puzzle_input.split("\n")]


def part1(particles):
    """Solve part 1."""
    return min(
        (particle.long_term_norm(), idx) for idx, particle in enumerate(particles)
    )[1]


def part2(particles):
    """Solve part 2."""
    survivors = set(range(len(particles)))
    for t in itertools.count(0):
        positions = {idx: particles[idx].pos_at_t(t) for idx in survivors}
        collisions = {
            pos
            for pos, count in collections.Counter(positions.values()).items()
            if count >= 2
        }
        survivors -= {idx for idx, pos in positions.items() if pos in collisions}
        if min(abs(pos) for pos in positions.values()) > 10_000:
            return len(survivors)


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
