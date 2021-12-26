"""Tests for AoC 23, 2021: Amphipod"""

# Standard library imports
import pathlib

# Third party imports
import aoc202123
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202123.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202123.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == ["BCBD", "ADCA"]


@pytest.mark.skip(reason="slow")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202123.part1(example1) == 12_521


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc202123.part1(example2) == 114


@pytest.mark.skip(reason="slow")
def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202123.part2(example1) == 44_169
