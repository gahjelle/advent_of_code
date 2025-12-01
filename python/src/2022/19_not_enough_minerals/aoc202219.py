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
    """Parse one line describing a blueprint."""
    match = PATTERN.parse(line)
    return match["id"], (
        (match["ore_ore"], 0, 0, 0),
        (match["clay_ore"], 0, 0, 0),
        (match["obsidian_ore"], match["obsidian_clay"], 0, 0),
        (match["geode_ore"], 0, match["geode_obsidian"], 0),
    )


def part1(blueprints):
    """Solve part 1."""
    total = 0
    for id, blueprint in blueprints.items():
        with Timer(logger=print if "--debug" in sys.argv else None):
            geodes = collect_geodes(blueprint, time=24)
        total += id * geodes
        if "--debug" in sys.argv:
            print(id, geodes, total)
    return total


def part2(blueprints, ids=(1, 2, 3)):
    """Solve part 2."""
    total = 1
    for id in ids:
        blueprint = blueprints[id]
        with Timer(logger=print if "--debug" in sys.argv else None):
            geodes = collect_geodes(blueprint, time=32)
        total *= geodes
        if "--debug" in sys.argv:
            print(id, geodes, total)
    return total


def collect_geodes(blueprint, time):
    """Find the maximum number of geodes."""
    queue = collections.deque([(0, (0, 0, 0, 0), (1, 0, 0, 0))])
    max_price = [max(prices[kind] for prices in blueprint) for kind in range(4)]
    (poo, _, _, _) = blueprint[ORE]
    (pco, _, _, _) = blueprint[CLAY]
    (pobo, pobc, _, _) = blueprint[OBSIDIAN]
    (pgo, _, pgob, _) = blueprint[GEODE]

    best = 0
    seen = set()

    while queue:
        t, (o, c, ob, g), (ro, rc, rob, rg) = queue.popleft()

        # Check if time is up for this particular production run
        if t == time:
            if g > best:
                best = g
            continue

        # Cap number of resources to what's possible to use in the remaining time
        # This helps keep the state space manageable
        if o > (mo := (max_price[ORE] * (time - t))):
            o = mo
        if c > (mc := (max_price[CLAY] * (time - t))):
            c = mc
        if ob > (mob := (max_price[OBSIDIAN] * (time - t))):
            ob = mob

        # Don't redo work already done
        state = (t, (o, c, ob, g), (ro, rc, rob, rg))
        if state in seen:
            continue
        seen.add(state)

        # Only produce
        if o < max_price[ORE]:
            queue.appendleft(
                (t + 1, (o + ro, c + rc, ob + rob, g + rg), (ro, rc, rob, rg))
            )
        # Produce and construct a new Ore robot
        if o >= poo and ro < max_price[ORE]:
            queue.appendleft(
                (t + 1, (o + ro - poo, c + rc, ob + rob, g + rg), (ro + 1, rc, rob, rg))
            )
        # Produce and construct a new Clay robot
        if o >= pco and rc < max_price[CLAY]:
            queue.appendleft(
                (t + 1, (o + ro - pco, c + rc, ob + rob, g + rg), (ro, rc + 1, rob, rg))
            )
        # Produce and construct a new Obsidian robot
        if o >= pobo and c >= pobc and rob < max_price[OBSIDIAN]:
            queue.appendleft(
                (
                    t + 1,
                    (o + ro - pobo, c + rc - pobc, ob + rob, g + rg),
                    (ro, rc, rob + 1, rg),
                )
            )
        # Produce and construct a new Geode robot
        if o >= pgo and ob >= pgob:
            queue.appendleft(
                (
                    t + 1,
                    (o + ro - pgo, c + rc, ob + rob - pgob, g + rg),
                    (ro, rc, rob, rg + 1),
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
