"""Tests for AoC 1, 2017: Inverse Captcha"""

# Standard library imports
import pathlib

# Third party imports
import aoc201701
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().strip()
    return aoc201701.parse_data(puzzle_input)


@pytest.fixture
def example7():
    puzzle_input = (PUZZLE_DIR / "example7.txt").read_text().strip()
    return aoc201701.parse_data(puzzle_input)


@pytest.fixture
def example9():
    puzzle_input = (PUZZLE_DIR / "example9.txt").read_text().strip()
    return aoc201701.parse_data(puzzle_input)


def test_parse_example7(example7):
    """Test that input is parsed properly"""
    assert example7 == [1, 2, 3, 4, 2, 5]


def test_part1_example4(example4):
    """Test part 1 on example input"""
    assert aoc201701.part1(example4) == 9


def test_part2_example9(example9):
    """Test part 2 on example input"""
    assert aoc201701.part2(example9) == 4
