"""Tests for AoC 2, 2021: Dive!"""

# Standard library imports
import pathlib

# Third party imports
import aoc202102
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202102.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [(5, 0), (0, 5), (8, 0), (0, -3), (0, 8), (2, 0)]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202102.part1(example1) == 150


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202102.part2(example1) == 900
