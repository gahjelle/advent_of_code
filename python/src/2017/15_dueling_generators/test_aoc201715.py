"""Tests for AoC 15, 2017: Dueling Generators."""

# Standard library imports
import pathlib

# Third party imports
import aoc201715
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201715.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == (65, 8921)


def test_part1_small_example1(example1):
    """Test part 1 on example input."""
    assert aoc201715.part1(example1, num_rounds=40_000) == 3


def test_part2_small_example1(example1):
    """Test part 2 on example input."""
    assert aoc201715.part2(example1, num_rounds=5_000, min_num=40_000) == 1


@pytest.mark.skip(reason="slow")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201715.part1(example1) == 588


@pytest.mark.skip(reason="slow")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201715.part2(example1) == 309
