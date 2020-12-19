"""Monster Messages

Advent of Code 2020, day 19
Solution by Geir Arne Hjelle, 2020-12-19
"""
import itertools
import pathlib
import sys
from typing import NamedTuple

import parse

debug = print if "--debug" in sys.argv else lambda *_: None

_RULE_LINE = parse.compile("{id:d}: {rule}")
_RULE_VALUE = parse.compile('"{char}"')


class Rule(NamedTuple):
    values: list[str] = []
    links: list[list[int]] = []


def parse_input(rule_lines, message_lines):
    return (
        dict([parse_rule(ln) for ln in rule_lines.split("\n")]),
        message_lines.split("\n"),
    )


def parse_rule(line):
    parts = _RULE_LINE.parse(line)
    value = _RULE_VALUE.parse(parts["rule"])
    if value:
        return parts["id"], Rule(values={value["char"]})
    else:
        return (
            parts["id"],
            Rule(links=[[int(n) for n in r.split()] for r in parts["rule"].split("|")]),
        )


def simplify_rules(all_rules):
    """Resolve rules linking to other rules"""
    values = {k: r.values for k, r in all_rules.items() if r.values}
    links = {k: r.links for k, r in all_rules.items() if r.links}
    ids = {k: set.union(*[set(lnk) for lnk in r]) for k, r in links.items()}

    while links:
        for id, rules in dict(links).items():
            if ids[id] - values.keys():
                continue

            rule_values = []
            for rule in rules:
                rule_values.extend(
                    (
                        "".join(p for p in v)
                        for v in itertools.product(*(values[r] for r in rule))
                    )
                )
            values[id] = set(rule_values)
            links.pop(id)
            break  # Break to simplify loop resolution
        else:
            # No rule was resolved, there is a loop in the rules
            break
    return values, links


def satisfies_8_11(rule42, rule31, messages, loop):
    """Find candidates that satisfies the 0: 8 11 rule

    If loop == True, these will be rules of the form

        42 42 ... 42 31 31 ... 31

    where 42 is repeated at least twice and 31 is repeated at least once.
    Additionally, there needs to be at least one more 42 than 31.

    However, if loop == False, these rules are just 42 42 31, so we
    additionally enforce that there are 3 parts to the message.
    """
    assert not (rule42 & rule31), "Rules 42 and 31 are assumed to be non-overlapping"

    rule_lens = {len(v) for v in rule42 | rule31}
    assert len(rule_lens) == 1, "All 42/31 rules are assumed to have the same length"
    rule_len = rule_lens.pop()

    count_valid = 0
    for message in messages:
        chunks = [message[i : i + rule_len] for i in range(0, len(message), rule_len)]
        num_chunks = len(chunks)
        if not loop and num_chunks != 3:
            continue

        # Number of chunks matching rule 42 at the start of the message
        num_42 = len(list(itertools.takewhile(lambda c: c in rule42, chunks)))

        # Number of chunks matching rule 31 at the end of the message
        num_31 = len(list(itertools.takewhile(lambda c: c in rule31, chunks[::-1])))

        # Check that the message is valid
        if num_42 > num_31 >= 1 and num_42 + num_31 == num_chunks:
            count_valid += 1

    return count_valid


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    rules, messages = parse_input(*file_path.read_text().strip().split("\n\n"))

    # Optimize for 0: 8 11 rules
    assert rules[0].links == [[8, 11]], "Assuming special rules for 8 and 11"
    assert rules[8].links == [[42]], "Assuming 8: 42 rule"
    assert rules[11].links == [[42, 31]], "Assuming 11: 42 31 rule"

    # Part 1
    simplified_rules = rules | {
        0: Rule(values={""}),
        8: Rule(values={""}),
        11: Rule(values={""}),
    }
    values, links = simplify_rules(simplified_rules)
    assert not links, "There should not be any loops in original input"
    num_msg = satisfies_8_11(values[42], values[31], messages, loop=False)
    print(f"{num_msg} messages satisfy the original rules")

    # Part 2
    updated_rules = rules | {
        8: Rule(links=[[42], [42, 8]]),
        11: Rule(links=[[42, 31], [42, 11, 31]]),
    }
    values, links = simplify_rules(updated_rules)
    num_msg = satisfies_8_11(values[42], values[31], messages, loop=True)
    print(f"{num_msg} messages satisfy the updated rules")


if __name__ == "__main__":
    main(sys.argv[1:])
