"""Tests for AoC 23, 2015: Opening the Turing Lock."""

# Standard library imports
import pathlib

# Third party imports
import aoc201523
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201523.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ("inc", ["b"]),
        ("jio", ["a", "+2"]),
        ("tpl", ["b"]),
        ("inc", ["b"]),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201523.part1(example1) == 4


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201523.part2(example1) == 2
