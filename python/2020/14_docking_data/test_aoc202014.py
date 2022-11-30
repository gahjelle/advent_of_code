"""Tests for AoC 14, 2020: Docking Data."""

# Standard library imports
import pathlib

# Third party imports
import aoc202014
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202014.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202014.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 8, 11),
        ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 7, 101),
        ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 8, 0),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202014.part1(example1) == 165


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202014.part2(example2) == 208
