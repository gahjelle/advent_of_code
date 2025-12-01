"""Tests for AoC 20, 2023: Pulse Propagation."""

# Standard library imports
import pathlib

# Third party imports
import aoc202320
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202320.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202320.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        "broadcaster": ("", ["a", "b", "c"]),
        "a": ("%", ["b"]),
        "b": ("%", ["c"]),
        "c": ("%", ["inv"]),
        "inv": ("&", ["a"]),
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202320.part1(example1) == 32_000_000


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202320.part1(example2) == 11_687_500
