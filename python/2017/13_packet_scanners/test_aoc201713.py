"""Tests for AoC 13, 2017: Packet Scanners"""

# Standard library imports
import pathlib

# Third party imports
import aoc201713
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201713.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201713.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == {0: 3, 1: 2, 4: 4, 6: 4}


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201713.part1(example1) == 24


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201713.part2(example1) == 10
