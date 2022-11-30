"""Tests for AoC 12, 2020: Rain Risk."""

# Standard library imports
import pathlib

# Third party imports
import aoc202012
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202012.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [("F", 10), ("N", 3), ("F", 7), ("R", 90), ("F", 11)]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202012.part1(example1) == 25


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202012.part2(example1) == 286
