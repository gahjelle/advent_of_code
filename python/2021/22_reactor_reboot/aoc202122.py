"""AoC 22, 2021: Reactor Reboot."""

# Standard library imports
import collections
import itertools
import pathlib
import sys
from dataclasses import dataclass

# Third party imports
import parse

STEP_PATTERN = parse.compile(
    "{onoff} x={min_x:d}..{max_x:d},y={min_y:d}..{max_y:d},z={min_z:d}..{max_z:d}"
)
_MAX_DIM = 125_000
GRID_STEP = 10_000  # Seems to give decent performance on input data
GRID_SIZE = _MAX_DIM // GRID_STEP


@dataclass(frozen=True)
class Cube:
    """Representation of 3D cube."""

    min_x: int
    max_x: int
    min_y: int
    max_y: int
    min_z: int
    max_z: int

    @property
    def grid_location(self):
        """Classify cube as belonging to a grid_location,

        Note: It's assumed that the cube only belongs to one grid_location
        """
        return (
            (self.min_x // GRID_STEP + GRID_SIZE)
            + (self.min_y // GRID_STEP + GRID_SIZE) * (2 * GRID_SIZE)
            + (self.min_z // GRID_STEP + GRID_SIZE) * (2 * GRID_SIZE) ** 2
        )

    def split_to_grid(self):
        """Split a cube into subcubes based on the grid."""
        xs = [
            (
                max(n * GRID_STEP, self.min_x),
                min((n + 1) * GRID_STEP - 1, self.max_x),
            )
            for n in range(self.min_x // GRID_STEP, self.max_x // GRID_STEP + 1)
        ]
        ys = [
            (
                max(n * GRID_STEP, self.min_y),
                min((n + 1) * GRID_STEP - 1, self.max_y),
            )
            for n in range(self.min_y // GRID_STEP, self.max_y // GRID_STEP + 1)
        ]
        zs = [
            (
                max(n * GRID_STEP, self.min_z),
                min((n + 1) * GRID_STEP - 1, self.max_z),
            )
            for n in range(self.min_z // GRID_STEP, self.max_z // GRID_STEP + 1)
        ]

        cls = self.__class__
        for (min_x, max_x), (min_y, max_y), (min_z, max_z) in itertools.product(
            xs, ys, zs
        ):
            yield cls(min_x, max_x, min_y, max_y, min_z, max_z)

    def overlaps(self, other):
        """Check if other cube overlaps this cube."""
        return (
            self.min_x <= other.max_x
            and self.max_x >= other.min_x
            and self.min_y <= other.max_y
            and self.max_y >= other.min_y
            and self.min_z <= other.max_z
            and self.max_z >= other.min_z
        )

    def union(self, other):
        """Calculate the cube that is the union of this and the other cube."""
        cls = self.__class__
        return cls(
            min_x=min(self.min_x, other.min_x),
            max_x=max(self.max_x, other.max_x),
            min_y=min(self.min_y, other.min_y),
            max_y=max(self.max_y, other.max_y),
            min_z=min(self.min_z, other.min_z),
            max_z=max(self.max_z, other.max_z),
        )

    def split(self, cubes):
        """Split cube based on edges of smaller cubes."""
        xs = sorted({cube.min_x for cube in cubes} | {cube.max_x + 1 for cube in cubes})
        ys = sorted({cube.min_y for cube in cubes} | {cube.max_y + 1 for cube in cubes})
        zs = sorted({cube.min_z for cube in cubes} | {cube.max_z + 1 for cube in cubes})

        return [
            Cube(min_x, max_x - 1, min_y, max_y - 1, min_z, max_z - 1)
            for min_x, max_x in zip(xs[:-1], xs[1:])
            for min_y, max_y in zip(ys[:-1], ys[1:])
            for min_z, max_z in zip(zs[:-1], zs[1:])
        ]

    def __len__(self):
        """Calculate the size of the cube."""
        return (
            (self.max_x - self.min_x + 1)
            * (self.max_y - self.min_y + 1)
            * (self.max_z - self.min_z + 1)
        )


def parse_data(puzzle_input):
    """Parse input."""
    return [parse_step(line) for line in puzzle_input.split("\n")]


def parse_step(line):
    """Parse one line of input into a step in the reboot procedure.

    Include an indicator on whether the step is part of initialization

    >>> parse_step("on x=-11..33,y=-6..40,z=-16..37")
    (True, 'on', Cube(min_x=-11, max_x=33, min_y=-6, max_y=40, min_z=-16, max_z=37))

    >>> parse_step("off x=-55875..-39308,y=-55098..-35781,z=30971..57698")
    (False, 'off', Cube(min_x=-55875, max_x=-39308, min_y=-55098, max_y=-35781,
                        min_z=30971, max_z=57698))
    """
    match = STEP_PATTERN.parse(line)
    init = all(abs(v) <= 50 for k, v in match.named.items() if k != "onoff")

    return (
        init,
        match["onoff"],
        Cube(
            match["min_x"],
            match["max_x"],
            match["min_y"],
            match["max_y"],
            match["min_z"],
            match["max_z"],
        ),
    )


def part1(data):
    """Solve part 1."""
    return reboot([step for init, *step in data if init])


def part2(data):
    """Solve part 2."""
    return reboot([step for _, *step in data])


def reboot(steps):
    """Reboot the reactor."""
    # Split steps into cubes in a grid
    grid = collections.defaultdict(list)
    for onoff, original_cube in steps:
        for cube in original_cube.split_to_grid():
            if onoff == "off" and cube.grid_location not in grid:
                continue
            grid[cube.grid_location].append((onoff, cube))

    # Find number of cubes inside each grid location
    num_cubes = 0
    for steps in grid.values():
        # Split each grid into a subgrid along cube edges
        _, bbox = steps[0]
        for _, cube in steps[1:]:
            bbox = bbox.union(cube)
        cubes = bbox.split([cube for _, cube in steps])

        # Carry out on-off steps on the subgrid
        step_cubes = set()
        for onoff, new_cube in steps:
            components = {cube for cube in cubes if new_cube.overlaps(cube)}
            if onoff == "on":
                step_cubes |= components
            else:
                step_cubes -= components

        num_cubes += sum(len(cube) for cube in step_cubes)
    return num_cubes


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
