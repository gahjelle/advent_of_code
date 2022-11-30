"""Tests for AoC 6, 2016: Signals and Noise"""

# Standard library imports
import pathlib

# Third party imports
import aoc201606
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201606.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201606.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ["cld", "auo", "tag"]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201606.part1(example1) == "cat"


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201606.part1(example2) == "easter"


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201606.part2(example1) == "dog"


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201606.part2(example2) == "advent"
