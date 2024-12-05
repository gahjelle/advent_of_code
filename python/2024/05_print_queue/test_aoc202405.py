"""Tests for AoC 5, 2024: Print Queue."""

# Standard library imports
import pathlib

# Third party imports
import aoc202405
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202405.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    rules, updates = example1
    assert rules == {
        13: {97, 61, 29, 47, 75, 53},
        29: {75, 97, 53, 61, 47},
        53: {47, 75, 61, 97},
        61: {97, 47, 75},
        47: {97, 75},
        75: {97},
        97: set(),
    }
    assert updates == [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202405.part1(example1) == 143


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202405.part2(example1) == 123
