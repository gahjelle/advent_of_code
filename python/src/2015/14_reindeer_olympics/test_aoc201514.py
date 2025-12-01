"""Tests for AoC 14, 2015: Reindeer Olympics."""

# Standard library imports
import pathlib

# Third party imports
import aoc201514
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201514.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {"Comet": (14, 10, 127, 137), "Dancer": (16, 11, 162, 173)}


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201514.part1(example1, time=1000) == 1120


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201514.part2(example1, time=1000) == 689
