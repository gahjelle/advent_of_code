"""Tests for AoC 6, 2019: Universal Orbit Map."""

# Standard library imports
import pathlib

# Third party imports
import aoc201906
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201906.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201906.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        "COM": [],
        "B": ["B"],
        "C": ["B", "C"],
        "G": ["B", "G"],
        "D": ["B", "C", "D"],
        "H": ["B", "G", "H"],
        "E": ["B", "C", "D", "E"],
        "I": ["B", "C", "D", "I"],
        "F": ["B", "C", "D", "E", "F"],
        "J": ["B", "C", "D", "E", "J"],
        "K": ["B", "C", "D", "E", "J", "K"],
        "L": ["B", "C", "D", "E", "J", "K", "L"],
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201906.part1(example1) == 42


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201906.part2(example2) == 4
