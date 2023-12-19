"""Tests for AoC 16, 2023: The Floor Will Be Lava."""

# Standard library imports
import pathlib

# Third party imports
import aoc202316
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202316.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        (0, 1): "|",
        (0, 5): "\\",
        (1, 0): "|",
        (1, 2): "-",
        (1, 4): "\\",
        (2, 5): "|",
        (2, 6): "-",
        (3, 8): "|",
        (5, 9): "\\",
        (6, 4): "/",
        (6, 6): "\\",
        (6, 7): "\\",
        (7, 1): "-",
        (7, 3): "-",
        (7, 4): "/",
        (7, 7): "|",
        (8, 1): "|",
        (8, 6): "-",
        (8, 7): "|",
        (8, 9): "\\",
        (9, 2): "/",
        (9, 3): "/",
        (9, 5): "|",
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202316.part1(example1) == 46


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202316.part2(example1) == 51
