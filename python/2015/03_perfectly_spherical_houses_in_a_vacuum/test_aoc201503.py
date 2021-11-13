"""Tests for AoC 3, 2015: Perfectly Spherical Houses in a Vacuum"""

# Standard library imports
import pathlib

# Third party imports
import aoc201503
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201503.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201503.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [(0, 1), (1, 0), (0, -1), (-1, 0)]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201503.part1(example1) == 4


def test_part1_example2(example2):
    """Test part 2 on example input"""
    assert aoc201503.part1(example2) == 2


def test_part2_example1(example1):
    """Test part 1 on example input"""
    assert aoc201503.part2(example1) == 3


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc201503.part2(example2) == 11
