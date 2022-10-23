"""Tests for AoC 5, 2019: Sunny with a Chance of Asteroids"""

# Standard library imports
import pathlib

# Third party imports
import aoc201905
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201905.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201905.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [3, 0, 4, 0, 99]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201905.part1(example1) == 1


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201905.part2(example1) == 5
