"""Tests for AoC 5, 2017: A Maze of Twisty Trampolines, All Alike"""

# Standard library imports
import pathlib

# Third party imports
import aoc201705
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201705.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201705.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [0, 3, 0, 1, -3]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201705.part1(example1) == 5


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201705.part2(example1) == 10
