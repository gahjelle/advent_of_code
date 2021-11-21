"""Tests for AoC 1, 2018: Chronal Calibration"""

# Standard library imports
import pathlib

# Third party imports
import aoc201801
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201801.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201801.parse(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc201801.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [1, -2, 3, 1]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201801.part1(example1) == 3


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201801.part2(example1) == 2


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc201801.part2(example2) == 10


def test_part2_example3(example3):
    """Test part 2 on example input"""
    assert aoc201801.part2(example3) == 0
