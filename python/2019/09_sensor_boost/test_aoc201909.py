"""Tests for AoC 9, 2019: Sensor Boost."""

# Standard library imports
import pathlib

# Third party imports
import aoc201909
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201909.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201909.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc201909.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        109,
        1,
        204,
        -1,
        1001,
        100,
        1,
        100,
        1008,
        100,
        16,
        101,
        1006,
        101,
        0,
        99,
    ]


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201909.part1(example2) == 1_219_070_632_396_864


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc201909.part1(example3) == 1_125_899_906_842_624
