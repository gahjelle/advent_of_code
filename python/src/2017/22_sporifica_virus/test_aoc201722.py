"""Tests for AoC 22, 2017: Sporifica Virus."""

# Standard library imports
import pathlib

# Third party imports
import aoc201722
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201722.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ((1, 1), {(0, 2), (1, 0)})


def test_part1_example1_short(example1):
    """Test part 1 on example input."""
    assert aoc201722.part1(example1, num_bursts=70) == 41


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201722.part1(example1) == 5_587


def test_part2_example1_short(example1):
    """Test part 2 on example input."""
    assert aoc201722.part2(example1, num_bursts=100) == 26


@pytest.mark.skip(reason="slow")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201722.part2(example1) == 2_511_944
