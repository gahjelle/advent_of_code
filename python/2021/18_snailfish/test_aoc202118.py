"""Tests for AoC 18, 2021: Snailfish"""

# Standard library imports
import pathlib

# Third party imports
import aoc202118
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202118.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202118.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        [(1, 1), (1, 1)],
        [(1, 2), (1, 2)],
        [(1, 3), (1, 3)],
        [(1, 4), (1, 4)],
        [(2, 1), (2, 2), (3, 3), (3, 4), (2, 5)],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202118.part1(example1) == 1027


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc202118.part1(example2) == 4140


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202118.part2(example1) == 469


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc202118.part2(example2) == 3993
