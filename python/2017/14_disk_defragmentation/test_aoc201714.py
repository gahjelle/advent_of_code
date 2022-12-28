"""Tests for AoC 14, 2017: Disk Defragmentation."""

# Standard library imports
import pathlib

# Third party imports
import aoc201714
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201714.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == "flqrgnkx"


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201714.part1(example1) == 8108


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201714.part2(example1) == 1242
