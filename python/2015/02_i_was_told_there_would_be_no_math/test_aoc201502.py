"""Tests for AoC 2, 2015: I Was Told There Would Be No Math"""

# Standard library imports
import pathlib

# Third party imports
import aoc201502
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def input1():
    puzzle_input = (PUZZLE_DIR / "input1.txt").read_text().strip()
    return aoc201502.parse(puzzle_input)


def test_parse_input1(input1):
    """Test that input is parsed properly"""
    assert input1 == [aoc201502.Present(2, 3, 4), aoc201502.Present(1, 1, 10)]


def test_part1_input1(input1):
    """Test part 1 on example input"""
    assert aoc201502.part1(input1) == 58 + 43


def test_part2_input1(input1):
    """Test part 2 on example input"""
    assert aoc201502.part2(input1) == 34 + 14
