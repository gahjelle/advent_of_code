"""Tests for AoC 7, 2021: The Treachery of Whales"""

# Standard library imports
import collections
import pathlib

# Third party imports
import aoc202107
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202107.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == collections.Counter([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202107.part1(example1) == 37


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202107.part2(example1) == 168
