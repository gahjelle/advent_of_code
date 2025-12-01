"""Tests for AoC 22, 2021: Reactor Reboot."""

# Standard library imports
import pathlib

# Third party imports
import aoc202122
import pytest
from aoc202122 import Cube

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202122.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202122.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc202122.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        (True, "on", Cube(10, 12, 10, 12, 10, 12)),
        (True, "on", Cube(11, 13, 11, 13, 11, 13)),
        (True, "off", Cube(9, 11, 9, 11, 9, 11)),
        (True, "on", Cube(10, 10, 10, 10, 10, 10)),
        (False, "on", Cube(621, 760, 251, 486, -280, -69)),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202122.part1(example1) == 39


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202122.part1(example2) == 590_784


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc202122.part1(example3) == 474_140


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202122.part2(example1) == 39 + 140 * 236 * 212


def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc202122.part2(example3) == 2_758_514_936_282_235
