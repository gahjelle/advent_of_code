"""AoC day 5, 2025: Cafeteria."""


def parse_data(puzzle_input: str) -> tuple[list[range], list[int]]:
    """Parse puzzle input."""
    ranges, ids = puzzle_input.split("\n\n")
    return [
        range(int(start), int(stop) + 1)
        for line in ranges.splitlines()
        for start, stop in [line.split("-")]
    ], [int(line) for line in ids.splitlines()]


def part1(data: tuple[list[range], list[int]]) -> int:
    """Solve part 1."""
    ranges, ids = data
    return sum(any(id in rng for rng in ranges) for id in ids)


def part2(data: tuple[list[range], list[int]]) -> int:
    """Solve part 2."""
    ranges, _ = data
    return sum(len(rng) for rng in remove_overlaps(ranges))


def remove_overlaps(ranges: list[range]) -> list[range]:
    """Remove overlaps between ranges.

    Doesn't merge adjacent ranges.

    ## Example

        012345678901234567890
         |---|
                |--------|
                  |---|
                    |-------|

    >>> ranges = [range(1, 6), range(8, 18), range(10, 15), range(12, 21)]
    >>> remove_overlaps(ranges)
    [range(1, 6), range(8, 18), range(18, 21)]
    """
    new_ranges = []
    prev_stop = -1
    for rng in sorted(ranges, key=lambda rng: rng.start):
        start = max(rng.start, prev_stop)
        if rng.stop <= start:
            continue
        new_ranges.append(range(start, rng.stop))
        prev_stop = rng.stop
    return new_ranges
