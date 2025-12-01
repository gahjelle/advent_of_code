"""Tests for AoC 10, 2022: Cathode-Ray Tube."""

# Standard library imports
import pathlib

# Third party imports
import aoc202210
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202210.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202210.parse_data(puzzle_input)


@pytest.fixture
def input_data():
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().rstrip()
    return aoc202210.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [1, 1, 1, 4, 4, -1, -1]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202210.part1(example1) == 0


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202210.part1(example2) == 13_140


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202210.part2(example2, return_screen=True) == (
        "##..##..##..##..##..##..##..##..##..##..\n"
        "###...###...###...###...###...###...###.\n"
        "####....####....####....####....####....\n"
        "#####.....#####.....#####.....#####.....\n"
        "######......######......######......####\n"
        "#######.......#######.......#######....."
    )


def test_part2_input_data(input_data):
    """Test part 2 on example input."""
    assert aoc202210.part2(input_data) == "EFGERURE"
