"""Tests for AoC 8, 2015: Matchsticks"""

# Standard library imports
import pathlib

# Third party imports
import aoc201508
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201508.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201508.part1(example1) == 12


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201508.part2(example1) == 19
