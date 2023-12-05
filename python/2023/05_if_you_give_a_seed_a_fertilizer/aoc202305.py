"""AoC 5, 2023: If You Give A Seed A Fertilizer."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    blocks = [lines.split("\n") for lines in puzzle_input.split("\n\n")]
    seeds = [int(seed) for seed in blocks[0][0].split()[1:]]
    maps = {}
    for lines in blocks[1:]:
        names = tuple(lines[0].split()[0].split("-")[:3:2])
        maps[names] = [[int(n) for n in line.split()] for line in lines[1:]]

    return seeds, maps


def part1(data):
    """Solve part 1."""
    seeds, maps = data
    locations = plant_seeds([(seed, 1) for seed in seeds], maps)
    return min(seed for seed, _ in locations)


def part2(data):
    """Solve part 2."""
    seeds, maps = data
    locations = plant_seeds(list(zip(seeds[::2], seeds[1::2])), maps)
    return min(seed for seed, _ in locations)


def plant_seeds(seeds, maps, state="seed", to_state="location"):
    """Plant seeds.

    ## Example:

    >>> maps = {("seed", "location"): [[20, 70, 8], [60, 20, 5], [40, 44, 3]]}
    >>> plant_seeds([(23, 1), (46, 2), (77, 3)], maps)
    [(63, 1), (42, 1), (47, 1), (27, 1), (78, 2)]
    """
    transforms = dict(maps.keys())
    while state != to_state:
        next_state = transforms[state]
        seeds = [
            new_seed
            for seed, num in seeds
            for new_seed in grow_seed(seed, num, maps[state, next_state])
        ]
        state = next_state

    return seeds


def grow_seed(seed, num_seeds, tables):
    """Grow a group of seeds one stage.

    This may split the group into several groups.

    Note: This currently doesn't properly support splitting when "coming from
    below". For example, something like (11, 11) would not be correctly split at
    20. However, these situations do not seem to happen with the full tables.

    ## Examples:

    >>> tables = [[20, 70, 8], [60, 20, 5], [40, 44, 3]]
    >>> grow_seed(22, 3, tables)
    [(62, 3)]
    >>> grow_seed(10, 10, tables)
    [(10, 10)]
    >>> grow_seed(77, 3, tables)
    [(27, 1), (78, 2)]
    """
    for destination, source, num in tables:
        if source <= seed < source + num:
            if num_seeds <= source + num - seed:
                return [(destination + (seed - source), num_seeds)]
            else:
                return [
                    (destination + (seed - source), source + num - seed)
                ] + grow_seed(source + num, seed + num_seeds - source - num, tables)
    return [(seed, num_seeds)]


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
