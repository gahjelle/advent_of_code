"""Tests for AoC 2, 2018: Inventory Management System."""

# Standard library imports
import pathlib

# Third party imports
import aoc201802
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201802.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201802.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201802.part1(example1) == 12


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201802.part2(example1) == "abcde"


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201802.part2(example2) == "fgij"
