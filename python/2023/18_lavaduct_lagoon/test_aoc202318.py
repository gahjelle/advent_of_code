"""Tests for AoC 18, 2023: Lavaduct Lagoon."""

# Standard library imports
import pathlib

# Third party imports
import aoc202318
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202318.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ("R", 6, "70c710"),
        ("D", 5, "0dc571"),
        ("L", 2, "5713f0"),
        ("D", 2, "d2c081"),
        ("R", 2, "59c680"),
        ("D", 2, "411b91"),
        ("L", 5, "8ceee2"),
        ("U", 2, "caa173"),
        ("L", 1, "1b58a2"),
        ("U", 2, "caa171"),
        ("R", 2, "7807d2"),
        ("U", 3, "a77fa3"),
        ("L", 2, "015232"),
        ("U", 2, "7a21e3"),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202318.part1(example1) == 62


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202318.part2(example1) == 952_408_144_115
