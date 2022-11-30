"""Tests for AoC 2, 2017: Corruption Checksum."""

# Standard library imports
import pathlib

# Third party imports
import aoc201702
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201702.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201702.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201702.part1(example1) == 18


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201702.part2(example2) == 9
