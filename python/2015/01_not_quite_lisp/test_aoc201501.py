"""Tests for AoC 1, 2015: Not Quite Lisp"""

# Standard library imports
import pathlib

# Third party imports
import aoc201501
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201501.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201501.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc201501.parse_data(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().strip()
    return aoc201501.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [1, 1, -1, -1]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201501.part1(example1) == 0


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc201501.part1(example2) == 3


def test_part1_example3(example3):
    """Test part 1 on example input"""
    assert aoc201501.part1(example3) == -3


def test_part2_example4(example4):
    """Test part 2 on example input"""
    assert aoc201501.part2(example4) == 5
