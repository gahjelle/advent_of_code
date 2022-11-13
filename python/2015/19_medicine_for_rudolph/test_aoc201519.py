"""Tests for AoC 19, 2015: Medicine for Rudolph"""

# Standard library imports
import pathlib

# Third party imports
import aoc201519
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201519.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == (
        "HOHOHO",
        [("e", "H"), ("e", "O"), ("H", "HO"), ("H", "OH"), ("O", "HH")],
    )


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201519.part1(example1) == 7


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201519.part2(example1) == 6
