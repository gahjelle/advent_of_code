"""Tests for AoC 7, 2023: Camel Cards."""

# Standard library imports
import pathlib

# Third party imports
import aoc202307
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202307.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ("32T3K", 765),
        ("T55J5", 684),
        ("KK677", 28),
        ("KTJJT", 220),
        ("QQQJA", 483),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202307.part1(example1) == 6440


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202307.part2(example1) == 5905
