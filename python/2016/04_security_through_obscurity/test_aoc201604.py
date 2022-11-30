"""Tests for AoC 4, 2016: Security Through Obscurity"""

# Standard library imports
import pathlib

# Third party imports
import aoc201604
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201604.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201604.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ("aaaaa-bbb-z-y-x", 123, "abxyz"),
        ("a-b-c-d-e-f-g-h", 987, "abcde"),
        ("not-a-real-room", 404, "oarel"),
        ("totally-real-room", 200, "decoy"),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201604.part1(example1) == 1514


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201604.part2(example1) is None


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201604.part2(example2, "northern") == (281, "northern lights")
