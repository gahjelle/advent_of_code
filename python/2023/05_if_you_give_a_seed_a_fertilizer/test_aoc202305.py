"""Tests for AoC 5, 2023: If You Give A Seed A Fertilizer."""

# Standard library imports
import pathlib

# Third party imports
import aoc202305
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202305.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1[0] == [79, 14, 55, 13]
    assert example1[1] == [
        [(98, 100, -48), (50, 98, 2)],
        [(15, 52, -15), (52, 54, -15), (0, 15, 39)],
        [(53, 61, -4), (11, 53, -11), (0, 7, 42), (7, 11, 50)],
        [(18, 25, 70), (25, 95, -7)],
        [(77, 100, -32), (45, 64, 36), (64, 77, 4)],
        [(69, 70, -69), (0, 69, 1)],
        [(56, 93, 4), (93, 97, -37)],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202305.part1(example1) == 35


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202305.part2(example1) == 46
