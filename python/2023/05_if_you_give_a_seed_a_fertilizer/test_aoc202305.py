"""Tests for AoC 5, 2023: If You Give A Seed A Fertilizer."""

# Standard library imports
import pathlib

# Third party imports
import aoc202305
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202305.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1[0] == [79, 14, 55, 13]
    assert example1[1] == {
        ("seed", "soil"): [[50, 98, 2], [52, 50, 48]],
        ("soil", "fertilizer"): [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
        ("fertilizer", "water"): [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
        ("water", "light"): [[88, 18, 7], [18, 25, 70]],
        ("light", "temperature"): [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
        ("temperature", "humidity"): [[0, 69, 1], [1, 0, 69]],
        ("humidity", "location"): [[60, 56, 37], [56, 93, 4]],
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202305.part1(example1) == 35


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202305.part2(example1) == 46
