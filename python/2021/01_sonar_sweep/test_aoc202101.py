"""Tests for AoC 1, 2021: Sonar Sweep."""

# Standard library imports
import pathlib

# Third party imports
import aoc202101
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202101.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202101.part1(example1) == 7


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202101.part2(example1) == 5
