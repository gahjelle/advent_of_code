"""Tests for AoC 7, 2022: No Space Left On Device."""

# Standard library imports
import pathlib

# Third party imports
import aoc202207
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202207.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202207.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        "a": {"e": {"i": 584}, "f": 29_116, "g": 2_557, "h.lst": 62_596},
        "b.txt": 14_848_514,
        "c.dat": 8_504_156,
        "d": {"d.ext": 5_626_152, "d.log": 8_033_020, "j": 4_060_174, "k": 7_214_296},
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202207.part1(example1) == 95_437


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202207.part2(example1) == 24_933_642
