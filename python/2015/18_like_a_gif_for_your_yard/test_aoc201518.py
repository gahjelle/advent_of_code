"""Tests for AoC 18, 2015: Like a GIF For Your Yard"""

# Standard library imports
import pathlib

# Third party imports
import aoc201518
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201518.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        [False, True, False, True, False, True],
        [False, False, False, True, True, False],
        [True, False, False, False, False, True],
        [False, False, True, False, False, False],
        [True, False, True, False, False, True],
        [True, True, True, True, False, False],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201518.part1(example1, num_steps=4) == 4


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201518.part2(example1, num_steps=5) == 17
