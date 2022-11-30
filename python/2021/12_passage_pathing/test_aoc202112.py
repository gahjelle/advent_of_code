"""Tests for AoC 12, 2021: Passage Pathing."""

# Standard library imports
import pathlib

# Third party imports
import aoc202112
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202112.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202112.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc202112.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        "start": ["A", "b"],
        "A": ["start", "c", "b", "end"],
        "b": ["start", "A", "d", "end"],
        "c": ["A"],
        "d": ["b"],
        "end": ["A", "b"],
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202112.part1(example1) == 10


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202112.part1(example2) == 19


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc202112.part1(example3) == 226


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202112.part2(example1) == 36


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202112.part2(example2) == 103


def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc202112.part2(example3) == 3509
