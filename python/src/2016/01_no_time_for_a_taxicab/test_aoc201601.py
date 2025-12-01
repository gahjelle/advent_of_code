"""Tests for AoC 1, 2016: No Time for a Taxicab."""

# Standard library imports
import pathlib

# Third party imports
import aoc201601
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201601.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201601.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [("R", 5), ("L", 5), ("R", 5), ("R", 3)]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201601.part1(example1) == 12


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201601.part2(example2) == 4
