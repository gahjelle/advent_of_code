"""Tests for AoC 18, 2020: Operation Order"""

# Standard library imports
import pathlib

# Third party imports
import aoc202018
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202018.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1[:2] == ["(1 + 2 * 3 + 4 * 5 + 6)", "(1 + (2 * 3) + (4 * (5 + 6)))"]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202018.part1(example1) == 71 + 51 + 26 + 437 + 12240 + 13632


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202018.part2(example1) == 231 + 51 + 46 + 1445 + 669060 + 23340
