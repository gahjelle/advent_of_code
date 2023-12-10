"""Tests for AoC 10, 2023: Pipe Maze."""

# Standard library imports
import pathlib

# Third party imports
import aoc202310
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202310.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202310.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc202310.parse_data(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().rstrip()
    return aoc202310.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    start, grid = example1
    assert start == (1, 1)
    assert grid == {
        (1, 1): {(1, 2), (2, 1)},
        (1, 2): {(1, 1), (1, 3)},
        (1, 3): {(1, 2), (2, 3)},
        (2, 1): {(1, 1), (3, 1)},
        (2, 3): {(1, 3), (3, 3)},
        (3, 1): {(2, 1), (3, 2)},
        (3, 2): {(3, 1), (3, 3)},
        (3, 3): {(3, 2), (2, 3)},
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202310.part1(example1) == 4


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202310.part1(example2) == 8


def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc202310.part2(example3) == 8


def test_part2_example4(example4):
    """Test part 2 on example input."""
    assert aoc202310.part2(example4) == 10
