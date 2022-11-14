"""Tests for AoC 22, 2015: Wizard Simulator 20XX"""

# Standard library imports
import pathlib

# Third party imports
import aoc201522
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201522.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201522.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == aoc201522.Boss(hit_points=13, damage=8)


def test_part1_example1(example1):
    """Test part 1 on example input"""
    cost, attacks = aoc201522.part1(example1, hit_points=10, mana=250)
    assert cost == 226
    assert attacks == ["poison", "missile"]


def test_part1_example2(example2):
    """Test part 1 on example input"""
    cost, attacks = aoc201522.part1(example2, hit_points=10, mana=250)
    assert cost == 641
    assert attacks == ["recharge", "shield", "drain", "poison", "missile"]


def test_part2_example1(example1):
    """Test part 2 on example input"""
    cost, attacks = aoc201522.part2(example1, hit_points=10, mana=350)
    assert cost == 339
    assert attacks == ["shield", "poison", "missile"]


def test_part2_example2(example2):
    """Test part 2 on example input"""
    cost, attacks = aoc201522.part2(example2, hit_points=10, mana=350)
    assert cost == 754
    assert attacks == ["shield", "recharge", "drain", "shield", "poison", "missile"]
