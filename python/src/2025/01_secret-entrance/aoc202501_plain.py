"""AoC 1, 2025: Secret Entrance."""


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
        click = 1 if turn > 0 else -1
        for _ in range(abs(turn)):
            dial += click
            count += (dial % 100) == 0
    return count
