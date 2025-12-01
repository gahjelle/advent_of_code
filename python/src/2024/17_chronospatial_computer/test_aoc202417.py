"""Tests for AoC 17, 2024: Chronospatial Computer."""

# Standard library imports
import pathlib

# Third party imports
import aoc202417
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202417.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202417.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    memory, program = example1
    assert memory == [729, 0, 0]
    assert program == [0, 1, 5, 4, 3, 0]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202417.part1(example1) == "4,6,3,5,6,3,5,2,1,0"


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202417.part2(example2) == 117_440
