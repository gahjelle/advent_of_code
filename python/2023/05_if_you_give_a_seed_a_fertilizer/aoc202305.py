"""AoC 5, 2023: If You Give A Seed A Fertilizer."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input.

    Convert all ranges to use the notation [start, stop) instead of start and
    length. This makes the interval math clearer at the end.
    """
    blocks = [lines.split("\n") for lines in puzzle_input.split("\n\n")]
    seeds = [int(seed) for seed in blocks[0][0].split()[1:]]
    transforms = [
        [
            (src, src + num, dst - src)  # Map to start, stop, offset
            for dst, src, num in [[int(n) for n in line.split()] for line in lines[1:]]
        ]
        for lines in blocks[1:]
    ]
    return seeds, transforms


def part1(data):
    """Solve part 1."""
    seeds, transforms = data
    locations = plant_seed_ranges([(seed, seed + 1) for seed in seeds], transforms)
    return min(locations)[0]


def part2(data):
    """Solve part 2."""
    seeds, transforms = data
    locations = plant_seed_ranges(
        [(seed, seed + num) for seed, num in zip(seeds[::2], seeds[1::2])], transforms
    )
    return min(locations)[0]


def plant_seed_ranges(seeds, transforms, state="seed", to_state="location"):
    """Plant ranges of seeds.

    ## Example:

    >>> transforms = [[(70, 78, -50), (20, 25, 40), (44, 47, -4)]]
    >>> plant_seed_ranges([(23, 24), (46, 48), (77, 80)], transforms)
    [(63, 64), (42, 43), (47, 48), (27, 28), (78, 80)]
    """
    for transform in transforms:
        seeds = [
            new_seed
            for seed, num in seeds
            for new_seed in grow_range(seed, num, transform)
        ]

    return seeds


def grow_range(seed_start, seed_stop, transform):
    """Grow a range of seeds one stage.

    This may split the range into several ranges.

    ## Examples:

    >>> transform = [(70, 78, -50), (20, 25, 40), (44, 47, -4)]
    >>> grow_range(22, 25, transform)
    [(62, 65)]
    >>> grow_range(10, 20, transform)
    [(10, 20)]
    >>> grow_range(11, 22, transform)
    [(11, 20), (60, 62)]
    >>> grow_range(77, 80, transform)
    [(27, 28), (78, 80)]
    >>> grow_range(18, 29, transform)
    [(18, 20), (60, 65), (25, 29)]
    """
    if seed_stop <= seed_start:
        return []

    for start, stop, offset in transform:
        # Fully contained in the current interval
        if start <= seed_start < stop and start < seed_stop <= stop:
            return [(seed_start + offset, seed_stop + offset)]

        # No overlap with current interval
        if seed_stop <= start or seed_start >= stop:
            continue

        # The general case, a range needs to be split in three parts:
        # - before and after the current interval is sent of to separate processing
        # - the intersection with the current interval is handled
        return (
            grow_range(seed_start, start, transform)
            + [(max(seed_start, start) + offset, min(seed_stop, stop) + offset)]
            + grow_range(stop, seed_stop, transform)
        )

    return [(seed_start, seed_stop)]


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
