"""Tests for AoC 2, 2023: Cube Conundrum."""

# Standard library imports
import pathlib

# Third party imports
import aoc202302
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202302.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202302.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        1: [(4, 0, 3), (1, 2, 6), (0, 2, 0)],
        2: [(0, 2, 1), (1, 3, 4), (0, 1, 1)],
        3: [(20, 8, 6), (4, 13, 5), (1, 5, 0)],
        4: [(3, 1, 6), (6, 3, 0), (14, 3, 15)],
        5: [(6, 3, 1), (1, 2, 2)],
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202302.part1(example1) == 8


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202302.part2(example1) == 2286
