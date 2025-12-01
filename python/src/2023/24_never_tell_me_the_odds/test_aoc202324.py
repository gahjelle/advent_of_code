"""Tests for AoC 24, 2023: Never Tell Me The Odds."""

# Standard library imports
import pathlib

# Third party imports
import aoc202324
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202324.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        [19, 13, 30, -2, 1, -2],
        [18, 19, 22, -1, -1, -2],
        [20, 25, 34, -2, -2, -4],
        [12, 31, 28, -1, -2, -1],
        [20, 19, 15, 1, -5, -3],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202324.part1(example1, 7, 27) == 2


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202324.part2(example1) == 47
