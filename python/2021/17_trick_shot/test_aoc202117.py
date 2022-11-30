"""Tests for AoC 17, 2021: Trick Shot"""

# Standard library imports
import pathlib

# Third party imports
import aoc202117
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202117.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202117.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == ((20, 30), (-10, -5))


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202117.part1(example1) == 45


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc202117.part1(example2) == 15


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202117.part2(example1) == 112


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc202117.part2(example2) == 10
