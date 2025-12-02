"""AoC day 2, 2025: Gift Shop."""

from collections.abc import Generator


def parse_data(puzzle_input: str) -> list[str]:
    """Parse puzzle input."""
    return [
        str(id)
        for rng in puzzle_input.split(",")
        for start, end in [rng.split("-")]
        for id in range(int(start), int(end) + 1)
    ]


def part1(data: list[str]) -> int:
    """Solve part 1."""
    return sum(int(id) for id in is_silly(data))


def part2(data: list[str]) -> int:
    """Solve part 2."""
    return sum(int(id) for id in is_super_silly(data))


def is_silly(ids: list[str]) -> Generator[str]:
    """Identify silly IDs."""
    for id in ids:
        length = len(id)
        if length % 2:
            continue
        first = id[: length // 2]
        second = id[length // 2 :]
        if first == second:
            yield id


def is_super_silly(ids: list[str]) -> Generator[str]:
    """Identify super silly IDs."""
    for id in ids:
        length = len(id)
        for n in range(1, length // 2 + 1):
            if length % n:
                continue
            first = id[:n]
            super_silly = True
            for idx in range(n, length, n):
                second = id[idx : idx + n]
                if first != second:
                    super_silly = False
                    break
            if super_silly:
                yield id
                break
