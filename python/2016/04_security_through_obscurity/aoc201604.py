"""AoC 4, 2016: Security Through Obscurity."""

# Standard library imports
import collections
import functools
import pathlib
import sys
from string import ascii_lowercase
from typing import NamedTuple

import parse

PATTERN = parse.compile("{message}-{sector_id:d}[{checksum}]")


class Room(NamedTuple):
    """Description of a room."""

    message: str
    sector_id: int
    checksum: str


def parse_data(puzzle_input):
    """Parse input."""
    return [
        Room(m["message"], m["sector_id"], m["checksum"])
        for line in puzzle_input.split("\n")
        if (m := PATTERN.parse(line))
    ]


def part1(rooms):
    """Solve part 1."""
    return sum(
        room.sector_id for room in rooms if checksum(room.message) == room.checksum
    )


def part2(rooms, target="north"):
    """Solve part 2."""
    return next(
        (
            (room.sector_id, decrypted)
            for room in rooms
            if (
                (decrypted := decrypt(room.message, target))
                and checksum(room.message) == room.checksum
            )
        ),
        None,
    )


def checksum(message):
    """Calculate checksum of message.

    The checksum is the five most common letters in the encrypted name, in
    order, with ties broken by alphabetization.

    ## Examples:

    >>> checksum("advent-of-code")
    'deoac'
    >>> checksum("not-a-real-room")
    'oarel'
    """
    return "".join(
        char
        for _, char in sorted(
            (-count, char)
            for char, count in collections.Counter(message.replace("-", "")).items()
        )[:5]
    )


@functools.cache
def cipher(shift):
    """Create a table for rotating letters in a shift cipher.

    ## Examples:

    >>> cipher(1)  # doctest: +ELLIPSIS
    {45: 32, 97: 98, 98: 99, 99: 100, 100: 101, ..., 121: 122, 122: 97}
    >>> cipher(24)  # doctest: +ELLIPSIS
    {45: 32, 97: 121, 98: 122, 99: 97, 100: 98, ..., 121: 119, 122: 120}
    """
    return str.maketrans("-", " ") | str.maketrans(
        ascii_lowercase,
        ascii_lowercase[shift:] + ascii_lowercase[:shift],
    )


def decrypt(message, target):
    """Decrypt a message while looking for a target phrase.

    ## Examples:

    >>> decrypt("christmas-is-coming", "aoc")
    >>> decrypt("uh-cgjlymmcpy-aoc", "impressive")
    'an impressive gui'
    >>> decrypt("qzmt-zixmtkozy-ivhz", "encrypted")
    'very encrypted name'
    >>> decrypt("aoc", "g")
    'esg'
    """
    for shift in range(1, 26):
        if target in (decrypted := message.translate(cipher(shift))):
            return decrypted


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
