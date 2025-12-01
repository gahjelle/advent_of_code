"""Tests for AoC 2, 2024: Red-Nosed Reports."""

# Standard library imports
import pathlib

# Third party imports
import aoc202402
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202402.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202402.part1(example1) == 2


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202402.part2(example1) == 4
