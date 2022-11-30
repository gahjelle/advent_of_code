"""Tests for AoC 10, 2015: Elves Look, Elves Say"""

# Standard library imports
import pathlib

# Third party imports
import aoc201510
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201510.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == "1"


def test_part1_example1(example1):
    """Test part 1 on example input

    1 -> 11 -> 21 -> 1211 -> 111221 -> 312211
    """
    assert aoc201510.part1(example1, num_steps=5) == 6


def test_part2_example1(example1):
    """Test part 2 on example input

    ... -> 312211 -> 13112221 -> 1113213211 -> 31131211131221
    """
    assert aoc201510.part2(example1, num_steps=8) == 14
