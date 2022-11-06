"""Tests for AoC 13, 2015: Knights of the Dinner Table"""

# Standard library imports
import pathlib

# Third party imports
import aoc201513
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201513.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == {
        "Alice": {"Bob": 54, "Carol": -79, "David": -2},
        "Bob": {"Alice": 83, "Carol": -7, "David": -63},
        "Carol": {"Alice": -62, "Bob": 60, "David": 55},
        "David": {"Alice": 46, "Bob": -7, "Carol": 41},
    }


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201513.part1(example1) == 330


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201513.part2(example1) == 286
