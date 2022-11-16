"""Ticket translation

Advent of Code 2020, day 16
Solution by Geir Arne Hjelle, 2020-12-16
"""
# Standard library imports
import math
import pathlib
import sys

# Third party imports
import parse

debug = print if "--debug" in sys.argv else lambda *_: None

_RULES_PATTERN = parse.compile("{field}: {s1:d}-{e1:d} or {s2:d}-{e2:d}")


def parse_rules(text):
    rules = {}
    for rule in text.split("\n"):
        if match := _RULES_PATTERN.parse(rule):
            rules[match["field"]] = set(
                list(range(match["s1"], match["e1"] + 1))
                + list(range(match["s2"], match["e2"] + 1))
            )

    return rules


def parse_tickets(text):
    return [[int(t) for t in ln.split(",")] for ln in text.split("\n")[1:]]


def discard_invalid_tickets(rules, tickets):
    return [t for t in tickets if not set(t) - set.union(*rules.values())]


def possible_fields(rules, tickets, fields):
    for ticket in tickets:
        for column, value in enumerate(ticket):
            for field in list(fields[column]):
                if value not in rules[field]:
                    fields[column].remove(field)
    return fields


def decide_fields(rules, tickets):
    fields = possible_fields(
        rules, tickets, {n: set(rules.keys()) for n in range(len(rules))}
    )

    # Find fields using that each field corresponds to one column
    while max(len(f) for f in fields.values()) > 1:
        for column, col_fields in list(fields.items()):
            if len(col_fields) > 1:
                continue
            col_field = list(col_fields).pop()
            for other_column, other_fields in fields.items():
                if col_field in other_fields and other_column != column:
                    other_fields.remove(col_field)

    return {list(f)[0]: c for c, f in fields.items()}


def recreate_ticket(rules, tickets, ticket):
    valid_tickets = discard_invalid_tickets(rules, tickets)
    fields = decide_fields(rules, valid_tickets)
    ticket_fields = {f: ticket[idx] for f, idx in fields.items()}
    debug(ticket_fields)

    return ticket_fields


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    rules_text, ticket_text, tickets_text = file_path.read_text().strip().split("\n\n")
    rules = parse_rules(rules_text)
    tickets = parse_tickets(tickets_text)

    # Part 1
    error_rate = sum(
        f for t in tickets for f in t if f not in set.union(*rules.values())
    )
    print(f"Your error rate is {error_rate}")

    # Part 2
    ticket = recreate_ticket(rules, tickets, parse_tickets(ticket_text)[0])
    departure = math.prod(v for f, v in ticket.items() if f.startswith("departure "))
    print(f"Departure is at {departure}")


if __name__ == "__main__":
    main(sys.argv[1:])
