"""Tests for AoC 16, 2024: Reindeer Maze."""

# Standard library imports
import pathlib

# Third party imports
import aoc202416
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202416.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202416.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc202416.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    grid, start, target = example1
    assert grid == {
        (1, 1): ".",
        (1, 2): ".",
        (1, 3): ".",
        (2, 1): "E",
        (2, 3): "S",
        (3, 1): ".",
        (3, 2): ".",
        (3, 3): ".",
    }
    assert start == (2, 3)
    assert target == (2, 1)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202416.part1(example1) == 3004


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202416.part2(example1) == 8


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202416.part1(example2) == 7_036


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202416.part2(example2) == 45


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc202416.part1(example3) == 11_048


def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc202416.part2(example3) == 64
