"""Tests for AoC 1, 2020: Report Repair"""

# Standard library imports
import pathlib

# Third party imports
import aoc202001
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def input1():
    puzzle_input = (PUZZLE_DIR / "input1.txt").read_text().strip()
    return aoc202001.parse(puzzle_input)


def test_parse_input1(input1):
    """Test that input is parsed properly"""
    assert input1 == [1721, 979, 366, 299, 675, 1456]


def test_part1_input1(input1):
    """Test part 1 on example input"""
    assert aoc202001.part1(input1) == 514579


def test_part2_input1(input1):
    """Test part 2 on example input"""
    assert aoc202001.part2(input1) == 241861950
