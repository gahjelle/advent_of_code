"""Tests for AoC 9, 2020: Encoding Error"""

# Standard library imports
import pathlib

# Third party imports
import aoc202009
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202009.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == (
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    )


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202009.part1(example1, preamble=5) == 127


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202009.part2(example1, preamble=5) == 62
