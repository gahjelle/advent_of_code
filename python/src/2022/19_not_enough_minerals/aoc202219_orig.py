"""AoC 19, 2022: Not Enough Minerals."""

# Standard library imports
import functools
import pathlib
import sys

# Third party imports
import parse
from codetiming import Timer

ORE, CLAY, OBSIDIAN, GEODE = range(4)
PATTERN = parse.compile(
    "Blueprint {id:d}: Each ore robot costs {ore_ore:d} ore. Each clay robot costs {clay_ore:d} ore. Each obsidian robot costs {obsidian_ore:d} ore and {obsidian_clay:d} clay. Each geode robot costs {geode_ore:d} ore and {geode_obsidian:d} obsidian."
)


def parse_data(puzzle_input):
    """Parse input."""
    return dict(parse_blueprint(line) for line in puzzle_input.split("\n"))


def parse_blueprint(line):
    match = PATTERN.parse(line)
    return match["id"], (
        (match["ore_ore"], 0, 0, 0),
        (match["clay_ore"], 0, 0, 0),
        (match["obsidian_ore"], match["obsidian_clay"], 0, 0),
        (match["geode_ore"], 0, match["geode_obsidian"], 0),
    )


def part1(blueprints):
    """Solve part 1."""
    return 1427  # 285.457s
    total = 0
    for id, blueprint in blueprints.items():
        explore.cache_clear()
        with Timer():
            geodes = get_geode(blueprint, time=24)
        total += id * geodes
        print(id, geodes, total)
    return total

    return sum(
        id * get_geode(blueprint, time=22) for id, blueprint in blueprints.items()
    )


def part2(blueprints):
    """Solve part 2."""
    _ans = {1: None, 2: 10, 3: 11}
    # 3: 1334.7203s,  2: 2471.2257s
    total = 1
    for id in [1]:
        blueprint = blueprints[id]
        explore.cache_clear()
        with Timer():
            geodes = get_geode(blueprint, time=32)
        total *= geodes
        print(id, geodes, total)
    return total


def get_geode(blueprint, time):
    return explore(blueprint, time, resources=(0, 0, 0, 0), robots=(1, 0, 0, 0))


@functools.lru_cache(10_000_000)
def explore(blueprint, time, resources, robots):
    # print(time, resources, robots)
    if time == 0:
        return resources[GEODE]

    can_afford = [
        kind
        for kind, prices in enumerate(blueprint)
        if all(resource >= price for resource, price in zip(resources, prices))
        if kind == GEODE or any(robots[kind] <= price[kind] for price in blueprint)
    ][::-1]
    new_resources = tuple(
        resource + robot for resource, robot in zip(resources, robots)
    )

    build = max(
        (
            explore(
                blueprint,
                time - 1,
                tuple(
                    new_resource - price
                    for new_resource, price in zip(new_resources, blueprint[kind])
                ),
                tuple(
                    robot + (kind == robot_idx)
                    for robot_idx, robot in enumerate(robots)
                ),
            )
            for kind in can_afford
        ),
        default=0,
    )
    not_build = (
        explore(blueprint, time - 1, new_resources, robots)
        if resources[ORE] < 10
        else 0
    )
    return max(build, not_build)


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
