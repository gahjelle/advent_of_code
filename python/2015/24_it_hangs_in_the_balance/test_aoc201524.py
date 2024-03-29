"""Tests for AoC 24, 2015: It Hangs in the Balance."""

# Standard library imports
import pathlib

# Third party imports
import aoc201524
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201524.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [11, 10, 9, 8, 7, 5, 4, 3, 2, 1]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201524.part1(example1) == 99


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201524.part2(example1) == 44
