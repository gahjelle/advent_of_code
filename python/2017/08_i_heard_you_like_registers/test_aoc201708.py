"""Tests for AoC 8, 2017: I Heard You Like Registers"""

# Standard library imports
import pathlib

# Third party imports
import aoc201708
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201708.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201708.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        aoc201708.Instruction("b", "inc", 5, "a", ">", 1),
        aoc201708.Instruction("a", "inc", 1, "b", "<", 5),
        aoc201708.Instruction("c", "dec", -10, "a", ">=", 1),
        aoc201708.Instruction("c", "inc", -20, "c", "==", 10),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201708.part1(example1) == 1


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201708.part2(example1) == 10
