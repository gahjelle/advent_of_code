"""Tests for AoC 9, 2016: Explosives in Cyberspace."""

# Standard library imports
import pathlib

# Third party imports
import aoc201609
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201609.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201609.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == "X(8x2)(3x3)ABCY"


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201609.part1(example1) == 18


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201609.part2(example1) == 20


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201609.part2(example2) == 445
