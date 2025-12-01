"""Tests for AoC 3, 2016: Squares With Three Sides."""

# Standard library imports
import pathlib

# Third party imports
import aoc201603
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201603.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [[5, 10, 25], [5, 12, 13], [12, 13, 8]]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201603.part1(example1) == 2


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201603.part2(example1) == 1
