"""Tests for AoC 7, 2017: Recursive Circus"""

# Standard library imports
import pathlib

# Third party imports
import aoc201707
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201707.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    tree, weights = example1
    assert len(tree) == len(weights) == 13
    assert tree["pbga"] == set()
    assert tree["fwft"] == {"ktlj", "cntj", "xhth"}
    assert weights["cntj"] == 57
    assert weights["ugml"] == 68


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201707.part1(example1) == "tknk"


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201707.part2(example1) == 60
