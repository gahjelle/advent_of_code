"""Tests for AoC 6, 2015: Probably a Fire Hazard."""

# Standard library imports
import pathlib

# Third party imports
import aoc201506
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201506.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201506.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ("turn_on", slice(0, 1000), slice(0, 1000)),
        ("toggle", slice(0, 1), slice(0, 1000)),
        ("turn_off", slice(499, 501), slice(499, 501)),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201506.part1(example1) == 1_000_000 + (0 - 1000) - 4


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201506.part1(example2) == 9 + (1 - 3) - 2 + (3 - 1)


def test_part2_example2(example2):
    """Test part 2 on example input.

      0123        0123        0123        0123        0123
    0 0000      0 1110      0 1110      0 1110      0 1130
    1 0000  ->  1 1110  ->  1 3332  ->  1 3222  ->  1 3242
    2 0000      2 1110      2 1110      2 1000      2 1020
    3 0000      3 0000      3 0000      3 0000      3 0020
    """
    assert aoc201506.part2(example2) == 21
