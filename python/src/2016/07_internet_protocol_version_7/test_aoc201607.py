"""Tests for AoC 7, 2016: Internet Protocol Version 7."""

# Standard library imports
import pathlib

# Third party imports
import aoc201607
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201607.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201607.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        (["abba", "qrst"], ["mnop"]),
        (["abcd", "xyyx"], ["bddb"]),
        (["aaaa", "tyui"], ["qwer"]),
        (["ioxxoj", "zxcvbn"], ["asdfgh"]),
        (["aoc", "easter", "noon"], ["gah", "bunny"]),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201607.part1(example1) == 3


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201607.part2(example2) == 3
