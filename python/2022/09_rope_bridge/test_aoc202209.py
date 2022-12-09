"""Tests for AoC 9, 2022: Rope Bridge."""

# Standard library imports
import pathlib

# Third party imports
import aoc202209
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202209.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202209.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        (1, 0),
        (1, 0),
        (1, 0),
        (1, 0),
        (0, 1),
        (0, 1),
        (0, 1),
        (0, 1),
        (-1, 0),
        (-1, 0),
        (-1, 0),
        (0, -1),
        (1, 0),
        (1, 0),
        (1, 0),
        (1, 0),
        (0, -1),
        (-1, 0),
        (-1, 0),
        (-1, 0),
        (-1, 0),
        (-1, 0),
        (1, 0),
        (1, 0),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202209.part1(example1) == 13


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202209.part1(example2) == 88


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202209.part2(example1) == 1


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202209.part2(example2) == 36
