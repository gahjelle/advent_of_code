"""Tests for AoC 17, 2015: No Such Thing as Too Much"""

# Standard library imports
import pathlib

# Third party imports
import aoc201517
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201517.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [20, 15, 10, 5, 5]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201517.part1(example1, eggnog_volume=25) == 4


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201517.part2(example1, eggnog_volume=25) == 3
