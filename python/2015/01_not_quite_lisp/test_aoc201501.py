"""Tests for AoC 1, 2015: Not Quite Lisp"""

# Standard library imports
import pathlib

# Third party imports
import aoc201501
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def input1():
    puzzle_input = (PUZZLE_DIR / "input1.txt").read_text().strip()
    return aoc201501.parse(puzzle_input)


@pytest.fixture
def input2():
    puzzle_input = (PUZZLE_DIR / "input2.txt").read_text().strip()
    return aoc201501.parse(puzzle_input)


@pytest.fixture
def input3():
    puzzle_input = (PUZZLE_DIR / "input3.txt").read_text().strip()
    return aoc201501.parse(puzzle_input)


@pytest.fixture
def input4():
    puzzle_input = (PUZZLE_DIR / "input4.txt").read_text().strip()
    return aoc201501.parse(puzzle_input)


def test_parse_input1(input1):
    """Test that input is parsed properly"""
    assert input1 == [1, 1, -1, -1]


def test_part1_input1(input1):
    """Test part 1 on example input"""
    assert aoc201501.part1(input1) == 0


def test_part1_input2(input2):
    """Test part 1 on example input"""
    assert aoc201501.part1(input2) == 3


def test_part1_input3(input3):
    """Test part 1 on example input"""
    assert aoc201501.part1(input3) == -3


def test_part2_input4(input4):
    """Test part 2 on example input"""
    assert aoc201501.part2(input4) == 5
