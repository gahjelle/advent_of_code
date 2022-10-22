"""AoC 16, 2020: Ticket Translation"""

# Standard library imports
import math
import pathlib
import sys

# Third party imports
import parse

RULE = parse.compile("{rule}: {s1:d}-{e1:d} or {s2:d}-{e2:d}")


def parse(puzzle_input):
    """Parse input"""
    rules, ticket, tickets = puzzle_input.split("\n\n")
    return {
        "rules": _parse_rules(rules),
        "ticket": _parse_tickets(ticket)[0],
        "tickets": _parse_tickets(tickets),
    }


def _parse_rules(rules):
    """Parse ticket rules

    ## Example:

    >>> _parse_rules("one: 0-1 or 4-6\\ntwo: 10-13 or 4-4")
    {'one': {0, 1, 4, 5, 6}, 'two': {4, 10, 11, 12, 13}}
    """
    return {
        m["rule"]: set(range(m["s1"], m["e1"] + 1)) | set(range(m["s2"], m["e2"] + 1))
        for rule in rules.split("\n")
        if (m := RULE.parse(rule))
    }


def _parse_tickets(tickets):
    """Parse several tickets

    ## Example:
    >>> _parse_tickets("ignored\\n1,2,3,4\\n10,15,20,99")
    [[1, 2, 3, 4], [10, 15, 20, 99]]
    """
    return [
        [int(field) for field in ticket.split(",")]
        for ticket in tickets.split("\n")[1:]
    ]


def part1(data):
    """Solve part 1"""
    valid_values = set.union(*data["rules"].values())
    return sum(
        invalid
        for ticket in data["tickets"]
        if (invalid := invalid_field(valid_values, ticket)) is not None
    )


def part2(data):
    """Solve part 2"""
    valid_values = set.union(*data["rules"].values())
    valid_tickets = [
        ticket
        for ticket in data["tickets"]
        if invalid_field(valid_values, ticket) is None
    ]

    fields = deduce_fields(data["rules"], valid_tickets)
    return math.prod(
        value
        for value, field in zip(data["ticket"], fields)
        if field.startswith("departure ")
    )


def invalid_field(valid_values, ticket):
    """Identify invalid fields on a ticket

    ## Examples:

    >>> invalid_field({1, 2, 3, 6}, [2, 4, 6])
    4
    >>> invalid_field({2, 4, 6, 8}, [2, 4, 6])
    """
    return next((field for field in ticket if field not in valid_values), None)


def deduce_fields(rules, tickets):
    """Deduce the order of the fields on the tickets

    ## Example:

    >>> deduce_fields({"a": {2, 4}, "b": {1, 3}}, [[1, 2], [3, 4]])
    ['b', 'a']
    """
    field_values = [set(field) for field in zip(*tickets)]
    possible_fields = [
        {field for field, valid in rules.items() if values & valid == values}
        for values in field_values
    ]

    fields = [None] * len(rules)
    while any(possible_fields):
        decided = {
            idx: next(iter(fields))
            for idx, fields in enumerate(possible_fields)
            if len(fields) == 1
        }
        for idx, field in decided.items():
            fields[idx] = field
            for possible in possible_fields:
                possible.discard(field)
    return fields


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
