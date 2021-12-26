"""Tests for AoC 25, 2021: Sea Cucumber"""

# Standard library imports
import pathlib

# Third party imports
import aoc202125
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202125.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    num_rows, num_cols, easts, souths = example1
    assert num_rows == 9
    assert num_cols == 10
    assert len(easts) == 23
    assert len(souths) == 26
    assert not easts & souths
    assert (8, 9) in easts
    assert (0, 0) in souths
    assert (5, 5) not in easts | souths


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202125.part1(example1) == 58
