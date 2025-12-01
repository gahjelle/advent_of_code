"""Tests for AoC 1, 2023: Trebuchet?!."""

# Standard library imports
import pathlib

# Third party imports
import aoc202301
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202301.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202301.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202301.part1(example1) == 142


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202301.part2(example1) == 142


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202301.part2(example2) == 281
