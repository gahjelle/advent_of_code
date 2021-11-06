"""AoC 18, 2020: Operation Order"""

# Standard library imports
import pathlib
import re
import sys

PARENS = re.compile(r"(\([^)(]*?\))")
SIMPLE_EXPRESSION = re.compile(r"(?P<arg1>\d+) (?P<op>[+*]) (?P<arg2>\d+)")
PLUS_EXPRESSION = re.compile(r"(?P<arg1>\d+) \+ (?P<arg2>\d+)")


def evaluate_line(line, calculator):
    """Simplify parentheses using calculator to evaluate values"""
    while parens := PARENS.search(line):
        expression = parens.group()
        value = calculator(expression[1:-1])
        line = line.replace(expression, str(value))

    return int(line)


def evaluate_left_to_right(expression):
    """Evaluate left to right"""
    while subexpression := SIMPLE_EXPRESSION.search(expression):
        value = evaluate_simple_expression(**subexpression.groupdict())
        expression = expression.replace(subexpression.group(), str(value), 1)

    return int(expression)


def evaluate_plus_first(expression):
    """Evaluate plusses first"""
    while subexpression := PLUS_EXPRESSION.search(expression):
        value = evaluate_simple_expression(op="+", **subexpression.groupdict())
        expression = expression.replace(subexpression.group(), str(value), 1)

    return evaluate_left_to_right(expression)


def evaluate_simple_expression(arg1, op, arg2):
    """Evaluate a simple expression with only two arguments and an operator"""
    if op == "+":
        return int(arg1) + int(arg2)
    elif op == "*":
        return int(arg1) * int(arg2)


def parse(puzzle_input):
    """Parse input"""
    return [f"({ln})" for ln in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    return sum(evaluate_line(line, evaluate_left_to_right) for line in data)


def part2(data):
    """Solve part 2"""
    return sum(evaluate_line(line, evaluate_plus_first) for line in data)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
