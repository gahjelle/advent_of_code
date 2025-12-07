"""AoC day 7, 2025: Laboratories."""

import collections

type Column = int
type Splitters = list[set[Column]]


def parse_data(puzzle_input: str) -> tuple[Column, Splitters]:
    """Parse puzzle input."""
    grid = {
        (row, col): char
        for row, line in enumerate(puzzle_input.splitlines())
        for col, char in enumerate(line)
        if char in "S^"
    }
    maxrow, _ = max(grid)
    _, scol = next(pos for pos, char in grid.items() if char == "S")
    return 0, [
        {c - scol for (r, c), char in grid.items() if r == row and char == "^"}
        for row in range(maxrow + 1)
        if any(r == row and char == "^" for (r, _), char in grid.items())
    ]


def part1(data: tuple[Column, Splitters]) -> int:
    """Solve part 1."""
    start, splitters = data
    beams = {start}
    num_splits = 0
    for line in splitters:
        num_splits += len(beams & line)
        beams = (beams - line) | {
            beam for split in (beams & line) for beam in [split - 1, split + 1]
        }
    return num_splits


def part2(data: tuple[Column, Splitters]) -> int:
    """Solve part 2."""
    # sourcery skip: dict-assign-update-to-union
    start, splitters = data
    beams = collections.Counter([start])
    for line in splitters:
        new_beams = collections.Counter(
            {beam: num for beam, num in beams.items() if beam not in line}
        )
        for beam in set(beams) & line:
            new_beams.update({beam - 1: beams[beam], beam + 1: beams[beam]})
        beams = new_beams
    return sum(beams.values())
