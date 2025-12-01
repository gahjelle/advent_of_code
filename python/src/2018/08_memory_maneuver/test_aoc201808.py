"""Tests for AoC 8, 2018: Memory Maneuver."""

# Standard library imports
import pathlib

# Third party imports
import aoc201808
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201808.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ({1: ({}, [10, 11, 12]), 2: ({1: ({}, [99])}, [2])}, [1, 1, 2])


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201808.part1(example1) == 138


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201808.part2(example1) == 66
