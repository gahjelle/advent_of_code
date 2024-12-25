"""Tests for AoC 24, 2024: Crossed Wires."""

# Standard library imports
import pathlib

# Third party imports
import aoc202424
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202424.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202424.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    memory, gates = example1
    assert memory == {"x00": 1, "x01": 1, "x02": 1, "y00": 0, "y01": 1, "y02": 0}
    assert gates == {
        "z00": ("AND", "x00", "y00"),
        "z01": ("XOR", "x01", "y01"),
        "z02": ("OR", "x02", "y02"),
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202424.part1(example1) == 4


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202424.part1(example2) == 2024
