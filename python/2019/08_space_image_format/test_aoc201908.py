"""Tests for AoC 8, 2019: Space Image Format."""

# Standard library imports
import pathlib

# Third party imports
import aoc201908
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201908.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201908.part1(example1, width=3, height=2) == 1
