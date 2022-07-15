"""Tests for AoC 6, 2017: Memory Reallocation"""

# Standard library imports
import pathlib

# Third party imports
import aoc201706
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201706.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == (0, 2, 7, 0)


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201706.part1(example1) == 5


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201706.part2(example1) == 4