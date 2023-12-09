"""Tests for AoC 9, 2023: Mirage Maintenance."""

# Standard library imports
import pathlib

# Third party imports
import aoc202309
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202309.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202309.part1(example1) == 114


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202309.part2(example1) == 2
