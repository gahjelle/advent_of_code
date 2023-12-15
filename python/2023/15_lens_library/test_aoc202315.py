"""Tests for AoC 15, 2023: Lens Library."""

# Standard library imports
import pathlib

# Third party imports
import aoc202315
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202315.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        "rn=1",
        "cm-",
        "qp=3",
        "cm=2",
        "qp-",
        "pc=4",
        "ot=9",
        "ab=5",
        "pc-",
        "pc=6",
        "ot=7",
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202315.part1(example1) == 1320


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202315.part2(example1) == 145
