"""AoC 19, 2022: Not Enough Minerals."""

# Standard library imports
import collections
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


def part1(blueprints, time=24):
    """Solve part 1."""
    total = 0
    for id, blueprint in blueprints.items():
        with Timer(logger=print if "--debug" in sys.argv else None):
            geodes = get_geode(blueprint, total_time=time)
        total += id * geodes
        if "--debug" in sys.argv:
            print(id, geodes, total)
    return total


def part2(blueprints, time=32):
    """Solve part 2."""
    if len(blueprints) < 3:
        return 0
    total = 1
    for id in [1, 2, 3]:
        blueprint = blueprints[id]
        with Timer(logger=print if "--debug" in sys.argv else None):
            geodes = get_geode(blueprint, total_time=time)
        total *= geodes
        if "--debug" in sys.argv:
            print(id, geodes, total)
    return total


def get_geode(blueprint, total_time):
    queue = collections.deque([(0, (0, 0, 0, 0), (1, 0, 0, 0))])
    max_ore_price = max(prices[ORE] for prices in blueprint)
    best = 0

    while queue:
        time, resources, robots = queue.popleft()
        if time == total_time:
            if resources[GEODE] > best:
                best = resources[GEODE]
                if "--debug" in sys.argv:
                    print(best)
            continue

        new_resources = tuple(
            resource + robot for resource, robot in zip(resources, robots)
        )
        if resources[ORE] < max_ore_price:
            queue.appendleft((time + 1, new_resources, robots))
        for kind, prices in enumerate(blueprint):
            if any(resource < price for resource, price in zip(resources, prices)):
                continue
            if kind != GEODE and all(robots[kind] > price[kind] for price in blueprint):
                continue
            queue.appendleft(
                (
                    time + 1,
                    tuple(
                        new_resource - price
                        for new_resource, price in zip(new_resources, blueprint[kind])
                    ),
                    tuple(
                        robot + (kind == robot_idx)
                        for robot_idx, robot in enumerate(robots)
                    ),
                )
            )

    return best


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.startswith("-"):
            continue
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
