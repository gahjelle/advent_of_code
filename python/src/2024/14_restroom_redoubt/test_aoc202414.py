"""Tests for AoC 14, 2024: Restroom Redoubt."""

# Standard library imports
import pathlib

# Third party imports
import aoc202414
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202414.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ((0, 4), (3, -3)),
        ((6, 3), (-1, -3)),
        ((10, 3), (-1, 2)),
        ((2, 0), (2, -1)),
        ((0, 0), (1, 3)),
        ((3, 0), (-2, -2)),
        ((7, 6), (-1, -3)),
        ((3, 0), (-1, -2)),
        ((9, 3), (2, 3)),
        ((7, 3), (-1, 2)),
        ((2, 4), (2, -3)),
        ((9, 5), (-3, -3)),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202414.part1(example1, width=11, height=7) == 12
