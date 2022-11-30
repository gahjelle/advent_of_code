"""Tests for AoC 13, 2020: Shuttle Search"""

# Standard library imports
import pathlib

# Third party imports
import aoc202013
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202013.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == {
        "time": 939,
        "bus_ids": [(7, 0), (13, 1), (59, 4), (31, 6), (19, 7)],
    }


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202013.part1(example1) == 295


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202013.part2(example1) == 1_068_781
