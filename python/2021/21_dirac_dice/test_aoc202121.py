"""Tests for AoC 21, 2021: Dirac Dice"""

# Standard library imports
import pathlib

# Third party imports
import aoc202121
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202121.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == (4, 8)


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202121.part1(example1) == 739_785


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202121.part2(example1) == 444_356_092_776_315
