"""Tests for AoC 19, 2024: Linen Layout."""

# Standard library imports
import pathlib

# Third party imports
import aoc202419
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202419.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    towels, patterns = example1
    assert towels == frozenset(["r", "wr", "b", "g", "bwu", "rb", "gb", "br"])
    assert patterns == [
        "brwrr",
        "bggr",
        "gbbr",
        "rrbgbr",
        "ubwu",
        "bwurrg",
        "brgr",
        "bbrgwb",
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202419.part1(example1) == 6


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202419.part2(example1) == 16
