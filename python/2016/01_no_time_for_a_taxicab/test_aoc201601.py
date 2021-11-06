"""Tests for AoC 1, 2016: No Time for a Taxicab"""

# Standard library imports
import pathlib

# Third party imports
import aoc201601
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def input1():
    puzzle_input = (PUZZLE_DIR / "input1.txt").read_text().strip()
    return aoc201601.parse(puzzle_input)


@pytest.fixture
def input2():
    puzzle_input = (PUZZLE_DIR / "input2.txt").read_text().strip()
    return aoc201601.parse(puzzle_input)


def test_parse_input1(input1):
    """Test that input is parsed properly"""
    assert input1 == [("R", 5), ("L", 5), ("R", 5), ("R", 3)]


def test_part1_input1(input1):
    """Test part 1 on example input"""
    assert aoc201601.part1(input1) == 12


def test_part2_input2(input2):
    """Test part 2 on example input"""
    assert aoc201601.part2(input2) == 4
