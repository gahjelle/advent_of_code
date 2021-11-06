"""Tests for AoC 1, 2019: The Tyranny of the Rocket Equation"""

# Standard library imports
import pathlib

# Third party imports
import aoc201901
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def input1():
    puzzle_input = (PUZZLE_DIR / "input1.txt").read_text().strip()
    return aoc201901.parse(puzzle_input)


def test_parse_input1(input1):
    """Test that input is parsed properly"""
    assert input1 == [12, 14, 1969, 100756]


def test_part1_input1(input1):
    """Test part 1 on example input"""
    assert aoc201901.part1(input1) == 2 + 2 + 654 + 33583


def test_part2_input1(input1):
    """Test part 2 on example input"""
    assert aoc201901.part2(input1) == 2 + 2 + 966 + 50346
