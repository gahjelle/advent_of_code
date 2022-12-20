"""Tests for AoC 20, 2022: Grove Positioning System."""

# Standard library imports
import pathlib

# Third party imports
import aoc202220
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202220.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [(0, 1), (1, 2), (2, -3), (3, 3), (4, -2), (5, 0), (6, 4)]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202220.part1(example1) == 3


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202220.part2(example1) == 1_623_178_306
