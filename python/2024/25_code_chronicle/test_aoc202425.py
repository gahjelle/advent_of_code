"""Tests for AoC 25, 2024: Code Chronicle."""

# Standard library imports
import pathlib

# Third party imports
import aoc202425
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202425.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    keys, locks = example1
    assert keys == [[5, 0, 2, 1, 3], [4, 3, 4, 0, 2], [3, 0, 2, 0, 1]]
    assert locks == [[0, 5, 3, 4, 3], [1, 2, 0, 5, 3]]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202425.part1(example1) == 3
