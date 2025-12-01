"""Tests for AoC 10, 2018: The Stars Align."""

# Standard library imports
import pathlib

# Third party imports
import aoc201810
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201810.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ((9, 1), (0, 2)),
        ((7, 0), (-1, 0)),
        ((3, -2), (-1, 1)),
        ((6, 10), (-2, -1)),
        ((2, -4), (2, 2)),
        ((-6, 10), (2, -2)),
        ((1, 8), (1, -1)),
        ((1, 7), (1, 0)),
        ((-3, 11), (1, -2)),
        ((7, 6), (-1, -1)),
        ((-2, 3), (1, 0)),
        ((-4, 3), (2, 0)),
        ((10, -3), (-1, 1)),
        ((5, 11), (1, -2)),
        ((4, 7), (0, -1)),
        ((8, -2), (0, 1)),
        ((15, 0), (-2, 0)),
        ((1, 6), (1, 0)),
        ((8, 9), (0, -1)),
        ((3, 3), (-1, 1)),
        ((0, 5), (0, -1)),
        ((-2, 2), (2, 0)),
        ((5, -2), (1, 2)),
        ((1, 4), (2, 1)),
        ((-2, 7), (2, -2)),
        ((3, 6), (-1, -1)),
        ((5, 0), (1, 0)),
        ((-6, 0), (2, 0)),
        ((5, 9), (1, -2)),
        ((14, 7), (-2, 0)),
        ((-3, 6), (2, -1)),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201810.part1(example1) == "HI"


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201810.part2(example1) == 3
