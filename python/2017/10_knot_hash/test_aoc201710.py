"""Tests for AoC 10, 2017: Knot Hash"""

# Standard library imports
import pathlib

# Third party imports
import aoc201710
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201710.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201710.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == "3,4,1,5"


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201710.part1(example1, circle_length=5) == 12


def test_part2_empty_string():
    """Test part 2 on example input"""
    assert aoc201710.part2("") == "a2582a3a0e66e6e86e3812dcb672a272"


def test_part2_aoc_string():
    """Test part 2 on example input"""
    assert aoc201710.part2("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"


def test_part2_123_string():
    """Test part 2 on example input"""
    assert aoc201710.part2("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"


def test_part2_124_string():
    """Test part 2 on example input"""
    assert aoc201710.part2("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"
