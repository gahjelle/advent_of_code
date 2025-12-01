"""Tests for AoC 6, 2018: Chronal Coordinates."""

# Standard library imports
import pathlib

# Third party imports
import aoc201806
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201806.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201806.part1(example1) == 17


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201806.part2(example1, 32) == 16
