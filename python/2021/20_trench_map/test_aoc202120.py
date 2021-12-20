"""Tests for AoC 20, 2021: Trench Map"""

# Standard library imports
import pathlib

# Third party imports
import aoc202120
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202120.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert len(example1.enhancer) == 512
    assert example1.grid == {
        (0, 0),
        (0, 3),
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 4),
        (3, 2),
        (4, 2),
        (4, 3),
        (4, 4),
    }


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202120.part1(example1) == 35


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202120.part2(example1) == 3351
