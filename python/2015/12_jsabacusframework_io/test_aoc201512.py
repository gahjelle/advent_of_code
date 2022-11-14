"""Tests for AoC 12, 2015: JSAbacusFramework.io"""

# Standard library imports
import pathlib

# Third party imports
import aoc201512
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201512.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201512.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [1, {"c": "red", "b": 2}, 3]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201512.part1(example1) == 6


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc201512.part1(example2) == 21


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201512.part2(example1) == 4


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc201512.part2(example2) == 6
