"""Tests for AoC 17, 2017: Spinlock."""

# Standard library imports
import pathlib

# Third party imports
import aoc201717
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201717.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == 3


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201717.part1(example1) == 638


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201717.part2(example1) == 1_222_153
