"""AoC day 3, 2025: Lobby."""


def parse_data(puzzle_input: str) -> list[str]:
    """Parse puzzle input."""
    return puzzle_input.splitlines()


def part1(data: list[str]) -> int:
    """Solve part 1."""
    return sum(max_joltage(bank, 2) for bank in data)


def part2(data: list[str]) -> int:
    """Solve part 2."""
    return sum(max_joltage(bank, 12) for bank in data)


def max_joltage(bank: str, num_batteries: int) -> int:
    """Find the maximum joltage using num_batteries.

    ## Examples

    >>> max_joltage("982184912317983", 4)
    9998
    >>> max_joltage("1029", 2)
    29
    >>> max_joltage("234234234234278", 12)
    434234234278
    """
    n = num_batteries
    digits = []
    batteries = bank[:]
    while n > 0:
        n -= 1
        battery = max(batteries[:-n] if n else batteries)
        digits.append(battery)
        idx = batteries.index(battery)
        batteries = batteries[idx + 1 :]
    return int("".join(digits))
