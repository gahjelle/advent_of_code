"""Tests for AoC 25, 2015: Let It Snow."""

# Standard library imports
import pathlib

# Third party imports
import aoc201525
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201525.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == (5, 6)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201525.part1(example1) == 31663883
