"""Tests for AoC 11, 2018: Chronal Charge."""

# Standard library imports
import pathlib

# Third party imports
import aoc201811
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201811.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == 18


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201811.part1(example1, grid_size=50) == "33,45"


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201811.part2(example1, grid_size=50) == "35,32,13"
