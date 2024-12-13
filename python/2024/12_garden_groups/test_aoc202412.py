"""Tests for AoC 12, 2024: Garden Groups."""

# Standard library imports
import pathlib

# Third party imports
import aoc202412
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202412.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202412.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        (0, 0): "A",
        (0, 1): "A",
        (0, 2): "A",
        (0, 3): "A",
        (1, 0): "B",
        (1, 1): "B",
        (1, 2): "C",
        (1, 3): "D",
        (2, 0): "B",
        (2, 1): "B",
        (2, 2): "C",
        (2, 3): "C",
        (3, 0): "E",
        (3, 1): "E",
        (3, 2): "E",
        (3, 3): "C",
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202412.part1(example1) == 140


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202412.part2(example1) == 80


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202412.part1(example2) == 1930


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202412.part2(example2) == 1206
