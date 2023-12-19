"""Tests for AoC 19, 2023: Aplenty."""

# Standard library imports
import pathlib

# Third party imports
import aoc202319
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202319.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == (
        {
            "px": [("a", "<", 2006, "qkq"), ("m", ">", 2090, "A"), ("", "", 0, "rfg")],
            "pv": [("a", ">", 1716, "R"), ("", "", 0, "A")],
            "lnx": [("m", ">", 1548, "A"), ("", "", 0, "A")],
            "rfg": [("s", "<", 537, "gd"), ("x", ">", 2440, "R"), ("", "", 0, "A")],
            "qs": [("s", ">", 3448, "A"), ("", "", 0, "lnx")],
            "qkq": [("x", "<", 1416, "A"), ("", "", 0, "crn")],
            "crn": [("x", ">", 2662, "A"), ("", "", 0, "R")],
            "in": [("s", "<", 1351, "px"), ("", "", 0, "qqz")],
            "qqz": [("s", ">", 2770, "qs"), ("m", "<", 1801, "hdj"), ("", "", 0, "R")],
            "gd": [("a", ">", 3333, "R"), ("", "", 0, "R")],
            "hdj": [("m", ">", 838, "A"), ("", "", 0, "pv")],
        },
        [
            {"x": 787, "m": 2655, "a": 1222, "s": 2876},
            {"x": 1679, "m": 44, "a": 2067, "s": 496},
            {"x": 2036, "m": 264, "a": 79, "s": 2244},
            {"x": 2461, "m": 1339, "a": 466, "s": 291},
            {"x": 2127, "m": 1623, "a": 2188, "s": 1013},
        ],
    )


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202319.part1(example1) == 19_114


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202319.part2(example1) == 167_409_079_868_000
