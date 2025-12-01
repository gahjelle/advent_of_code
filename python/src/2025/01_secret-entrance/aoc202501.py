"""AoC day 1, 2025: Secret Entrance."""


def parse_data(puzzle_input: str) -> list[int]:
    """Parse puzzle input."""
    return [
        int(line.replace("L", "-").replace("R", ""))
        for line in puzzle_input.split("\n")
    ]


def part1(data: list[int]) -> int:
    """Solve part 1."""
    dial = 50
    count = 0
    for turn in data:
        dial += turn
        count += (dial % 100) == 0
    return count


def part2(data: list[int]) -> int:
    """Solve part 2."""
    dial = 50
    count = 0
    for turn in data:
        prev_dial = dial
        dial = (dial + turn) % 100
        count += (
            abs(dial - prev_dial - turn) // 100  # Number of "point at zeros"
            - (prev_dial == 0 and turn < 0)  # Be careful when moving left to and from 0
            + (dial == 0 and turn < 0)
        )
    return count
