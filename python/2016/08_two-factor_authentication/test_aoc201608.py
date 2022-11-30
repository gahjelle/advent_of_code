"""Tests for AoC 8, 2016: Two-Factor Authentication"""

# Standard library imports
import pathlib

# Third party imports
import aoc201608
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201608.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ("rect", 3, 2),
        ("rotate_column", 1, 1),
        ("rotate_row", 0, 4),
        ("rotate_column", 1, 1),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201608.part1(example1, rows=3, cols=7) == 6
