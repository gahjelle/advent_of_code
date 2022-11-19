"""Tests for AoC 7, 2015: Some Assembly Required"""

# Standard library imports
import pathlib

# Third party imports
import aoc201507
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201507.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == {
        "x": ("SET", 123),
        "y": ("OR", "b", "x"),
        "d": ("AND", "x", "y"),
        "e": ("OR", "x", "y"),
        "f": ("LSHIFT", "x", 2),
        "g": ("RSHIFT", "y", 2),
        "h": ("NOT", "x"),
        "i": ("NOT", "y"),
        "a": ("SET", "g"),
        "b": ("SET", 666),
    }


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201507.part1(example1) == 190


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201507.part2(example1) == 63
