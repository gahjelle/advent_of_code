"""Tests for AoC 8, 2024: Resonant Collinearity."""

# Standard library imports
import pathlib

# Third party imports
import aoc202408
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202408.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    grid, antennas = example1
    assert grid == {(row, col) for row in range(12) for col in range(12)}
    assert antennas == {
        "0": [(1, 8), (2, 5), (3, 7), (4, 4)],
        "A": [(5, 6), (8, 8), (9, 9)],
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202408.part1(example1) == 14


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202408.part2(example1) == 34
