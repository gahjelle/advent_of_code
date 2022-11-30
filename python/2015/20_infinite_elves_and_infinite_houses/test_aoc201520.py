"""Tests for AoC 20, 2015: Infinite Elves and Infinite Houses"""

# Standard library imports
import pathlib

# Third party imports
import aoc201520
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201520.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201520.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == 260


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201520.part1(example1) == 12


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201520.part2(example1, max_houses=3) == 16
