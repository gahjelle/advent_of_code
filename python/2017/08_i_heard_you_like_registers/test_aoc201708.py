"""Tests for AoC 8, 2017: I Heard You Like Registers"""

# Standard library imports
import pathlib

# Third party imports
import aoc201708
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def input1():
    puzzle_input = (PUZZLE_DIR / "input1.txt").read_text().strip()
    return aoc201708.parse(puzzle_input)


@pytest.fixture
def input2():
    puzzle_input = (PUZZLE_DIR / "input2.txt").read_text().strip()
    return aoc201708.parse(puzzle_input)


def test_parse_input1(input1):
    """Test that input is parsed properly"""
    assert input1 == [
        aoc201708.Instruction("b", "inc", 5, "a", ">", 1),
        aoc201708.Instruction("a", "inc", 1, "b", "<", 5),
        aoc201708.Instruction("c", "dec", -10, "a", ">=", 1),
        aoc201708.Instruction("c", "inc", -20, "c", "==", 10),
    ]


def test_part1_input1(input1):
    """Test part 1 on example input"""
    assert aoc201708.part1(input1) == 1


def test_part2_input1(input1):
    """Test part 2 on example input"""
    assert aoc201708.part2(input1) == 10
