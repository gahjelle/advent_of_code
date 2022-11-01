"""Tests for AoC 2, 2016: Bathroom Security"""

# Standard library imports
import pathlib

# Third party imports
import aoc201602
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201602.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        [(0, 1), (-1, 0), (-1, 0)],
        [(1, 0), (1, 0), (0, -1), (0, -1), (0, -1)],
        [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 0)],
        [(0, 1), (0, 1), (0, 1), (0, 1), (0, -1)],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201602.part1(example1) == "1985"


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201602.part2(example1) == "5DB3"
