"""AoC day 2, 2025: Gift Shop."""


def parse_data(puzzle_input: str) -> dict[str, int]:
    """Parse puzzle input."""
    return {
        str(id): id
        for rng in puzzle_input.split(",")
        for start, end in [rng.split("-")]
        for id in range(int(start), int(end) + 1)
    }


def part1(data: dict[str, int]) -> int:
    """Solve part 1."""
    return sum(id for str_id, id in data.items() if is_invalid(str_id))


def part2(data: dict[str, int]) -> int:
    """Solve part 2."""
    return sum(id for str_id, id in data.items() if is_really_invalid(str_id))


def is_invalid(id: str) -> bool:
    """Check if an ID is invalid.

    An invalid ID is an ID which is made only of some sequence of digits
    repeated twice.

    ## Examples:

    >>> is_invalid("33")
    True
    >>> is_invalid("6464")
    True
    >>> is_invalid("646464")
    False
    """
    return id[: len(id) // 2] * 2 == id


def is_really_invalid(id: str) -> bool:
    """Check if an ID is really invalid.

    An ID is invalid if it is made only of some sequence of digits repeated at
    least twice.

    ## Examples:

    >>> is_really_invalid("33333")
    True
    >>> is_really_invalid("6464")
    True
    >>> is_really_invalid("646464")
    True
    >>> is_really_invalid("1231231234")
    False
    """
    return any(
        len(id) % n == 0 and id[:n] * (len(id) // n) == id
        for n in range(1, len(id) // 2 + 1)
    )
