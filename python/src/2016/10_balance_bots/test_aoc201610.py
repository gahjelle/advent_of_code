"""Tests for AoC 10, 2016: Balance Bots."""

# Standard library imports
import pathlib

# Third party imports
import aoc201610
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201610.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ({2: [5, 2], 1: [3]}, {2: (1, 0), 1: (1001, 0), 0: (1002, 1000)})


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201610.part1(example1, chips=(2, 3)) == 1


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201610.part2(example1) == 30
