"""Tests for AoC 16, 2017: Permutation Promenade."""

# Standard library imports
import pathlib

# Third party imports
import aoc201716
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201716.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [("s", 1, 0), ("x", 3, 4), ("p", "e", "b")]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201716.part1(example1, num_programs=5) == "baedc"


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201716.part2(example1, num_programs=5) == "abcde"
