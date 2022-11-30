"""Tests for AoC 10, 2020: Adapter Array"""

# Standard library imports
import pathlib

# Third party imports
import aoc202010
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202010.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202010.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc202010.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202010.part1(example1) == 35


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc202010.part1(example2) == 220


def test_part1_example3(example3):
    """Test part 1 on example input"""
    assert aoc202010.part1(example3) == 42


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202010.part2(example1) == 8


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc202010.part2(example2) == 19_208


def test_part2_example3(example3):
    """Test part 2 on example input"""
    assert aoc202010.part2(example3) == 1_053
