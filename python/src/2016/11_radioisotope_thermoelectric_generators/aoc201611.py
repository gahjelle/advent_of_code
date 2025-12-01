"""AoC 11, 2016: Radioisotope Thermoelectric Generators."""

# Standard library imports
import heapq
import itertools
import pathlib
import re
import sys

PATTERN_CHIP = re.compile(r"a (\w+)-compatible microchip")
PATTERN_GEN = re.compile(r"a (\w+) generator")


def parse_data(puzzle_input):
    """Parse input."""
    isotopes = {"": 0}
    return tuple(
        tuple(sorted(parse_floor(line, isotopes))) for line in puzzle_input.split("\n")
    )


def parse_floor(floor, isotopes):
    """Parse items on one floor.

    ## Example:

    >>> parse_floor(
    ...     "The first floor contains a santa generator "
    ...     "and a bunny-compatible microchip.", {"": 0}
    ... )
    [1, -2]
    """
    for match in itertools.chain(
        PATTERN_GEN.findall(floor), PATTERN_CHIP.findall(floor)
    ):
        if match not in isotopes:
            isotopes[match] = max(isotopes.values()) + 1
    return (
        []
        + [isotopes[match] for match in PATTERN_GEN.findall(floor)]
        + [-isotopes[match] for match in PATTERN_CHIP.findall(floor)]
    )


def part1(floors):
    """Solve part 1."""
    return move_to_assembly(floors)


def part2(floors):
    """Solve part 2."""
    floors = (tuple(sorted(floors[0] + (-99, -98, 98, 99))), *floors[1:])
    return move_to_assembly(floors)


def move_to_assembly(floors, elevator=0):
    """Move all microchips and generators to the target floor for assembly.

    ## Example:

    >>> move_to_assembly(((1,), (-1,), (), ()))
    3
    """
    queue = [(0, (elevator, floors))]
    steps = {(elevator, floors): 0}

    while queue:
        _, current = heapq.heappop(queue)

        # Are we done?
        _, floors = current
        if not any(floors[:-1]):
            return steps[current]

        # Add potential moves to queue
        for moved, num_top in generate_moves(*current):
            if moved in steps and steps[moved] <= steps[current] + 1:
                continue
            steps[moved] = steps[current] + 1
            heapq.heappush(
                queue,
                (
                    # Prioritize moves towards the top floor
                    steps[moved] - num_top * 100,
                    moved,
                ),
            )
    return None


def generate_moves(elevator, floors):
    """Generate possible moves."""
    floor = floors[elevator]
    for floor_num in [elevator + d for d in (1, -1) if 0 <= elevator + d < 4]:
        for moves in itertools.chain(
            itertools.combinations(floor, 2), itertools.combinations(floor, 1)
        ):
            new_floors = list(floors)
            new_floors[elevator] = tuple(item for item in floor if item not in moves)
            new_floors[floor_num] = tuple(sorted(floors[floor_num] + moves))
            if is_valid(new_floors[elevator]) and is_valid(new_floors[floor_num]):
                yield (floor_num, tuple(new_floors)), len(new_floors[-1])


def is_valid(floor):
    """Check that the current situation doesn't lead to meltdown.

    Microchips (>0) can not be on the same floor as a different generator (<0)
    unless it's connected to its own generator (<0).

    ## Examples:

    >>> is_valid((-1, 2))      # HM, LG
    False
    >>> is_valid((-2, -1, 1))  # LM, HM, HG
    False
    >>> is_valid((-1, 1, 2))   # HM, HG, LG
    True
    """
    if not floor or floor[-1] < 0:
        return True

    return all(-chip in floor for chip in floor if chip < 0)


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
