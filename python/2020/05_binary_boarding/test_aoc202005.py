"""Tests for AoC 5, 2020: Binary Boarding"""

# Standard library imports
import pathlib

# Third party imports
import aoc202005
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def input1():
    puzzle_input = (PUZZLE_DIR / "input1.txt").read_text().strip()
    return aoc202005.parse(puzzle_input)


def test_parse_input1(input1):
    """Test that input is parsed properly"""
    assert input1 == [357, 567, 119, 820]


def test_part1_input1(input1):
    """Test part 1 on example input"""
    assert aoc202005.part1(input1) == 820


def test_part2():
    """Test part 2 on example input"""
    data = [3, 9, 4, 8, 5, 10, 7, 11]
    assert aoc202005.part2(data) == 6
