"""Tests for AoC 8, 2021: Seven Segment Search"""

# Standard library imports
import pathlib

# Third party imports
import aoc202108
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202108.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert len(example1) == 10
    assert example1[0] == {
        "input": [
            "be",
            "abcdefg",
            "bcdefg",
            "acdefg",
            "bceg",
            "cdefg",
            "abdefg",
            "bcdef",
            "abcdf",
            "bde",
        ],
        "output": ["abcdefg", "bcdef", "bcdefg", "bceg"],
    }


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202108.part1(example1) == 26


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202108.part2(example1) == 61_229
