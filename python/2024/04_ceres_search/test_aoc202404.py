"""Tests for AoC 4, 2024: Ceres Search."""

# Standard library imports
import pathlib

# Third party imports
import aoc202404
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202404.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202404.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        (0, 0): "A",
        (0, 1): "A",
        (0, 2): "X",
        (0, 3): "A",
        (0, 4): "A",
        (0, 5): "A",
        (1, 0): "A",
        (1, 1): "S",
        (1, 2): "A",
        (1, 3): "M",
        (1, 4): "X",
        (1, 5): "M",
        (2, 0): "A",
        (2, 1): "A",
        (2, 2): "A",
        (2, 3): "A",
        (2, 4): "A",
        (2, 5): "A",
        (3, 0): "X",
        (3, 1): "M",
        (3, 2): "A",
        (3, 3): "S",
        (3, 4): "A",
        (3, 5): "S",
        (4, 0): "A",
        (4, 1): "X",
        (4, 2): "A",
        (4, 3): "A",
        (4, 4): "A",
        (4, 5): "A",
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202404.part1(example1) == 4


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202404.part1(example2) == 18


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202404.part2(example1) == 1


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202404.part2(example2) == 9
