"""Tests for AoC 24, 2019: Planet of Discord."""

# Standard library imports
import pathlib

# Third party imports
import aoc201924
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201924.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {(0, 4), (1, 0), (1, 3), (2, 0), (2, 3), (2, 4), (3, 2), (4, 0)}


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201924.part1(example1) == 2_129_920


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201924.part2(example1, minutes=10) == 99
