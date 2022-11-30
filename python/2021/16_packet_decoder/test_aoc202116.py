"""Tests for AoC 16, 2021: Packet Decoder"""

# Standard library imports
import pathlib

# Third party imports
import aoc202116
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202116.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202116.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc202116.parse_data(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().strip()
    return aoc202116.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == "110100101111111000101000"


def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert example2 == "00100100000000000110111101000101001010010001001000000000"


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202116.part1(example1) == 6


def test_part1_example3(example3):
    """Test part 1 on example input"""
    assert aoc202116.part1(example3) == 16


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc202116.part2(example2) == 10 * 20


def test_part2_example4(example4):
    """Test part 2 on example input"""
    assert aoc202116.part2(example4) == 1
