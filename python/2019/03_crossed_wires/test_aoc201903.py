"""Tests for AoC 3, 2019: Crossed Wires"""

# Standard library imports
import pathlib

# Third party imports
import aoc201903
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201903.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201903.parse(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc201903.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == (
        (
            [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
            + [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (7, 5)]
            + [(6, 5), (5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (3, 2)]
        ),
        (
            [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
            + [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (6, 6)]
            + [(6, 5), (6, 4), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3)]
        ),
    )


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201903.part1(example1) == 6


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc201903.part1(example2) == 159


def test_part1_example3(example3):
    """Test part 1 on example input"""
    assert aoc201903.part1(example3) == 135


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201903.part2(example1) == 30


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc201903.part2(example2) == 610


def test_part2_example3(example3):
    """Test part 2 on example input"""
    assert aoc201903.part2(example3) == 410
