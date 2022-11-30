"""Tests for AoC 5, 2021: Hydrothermal Venture"""

# Standard library imports
import pathlib

# Third party imports
import aoc202105
import pytest

# from aoc202105 import Line

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202105.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202105.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [[2, 0, 0, 2], [0, 2, 2, 2], [0, 0, 0, 2], [0, 0, 2, 2]]

    # assert example1 == [
    #     Line("diagonal", x1=0, y1=2, x2=2, y2=0),
    #     Line("horisontal", x1=0, y1=2, x2=2, y2=2),
    #     Line("vertical", x1=0, y1=0, x2=0, y2=2),
    #     Line("diagonal", x1=0, y1=0, x2=2, y2=2),
    # ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202105.part1(example1) == 1


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc202105.part1(example2) == 5


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202105.part2(example1) == 4


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc202105.part2(example2) == 12
