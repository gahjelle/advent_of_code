"""Slam Shuffle

Advent of Code 2019, day 22
Solution by Geir Arne Hjelle, 2019-12-22
"""
import pathlib
import sys

import parse

debug = print if "--debug" in sys.argv else lambda *_: None


def deal_into_new_stack(card_pos):
    return -card_pos - 1


def cut_cards(card_pos, num):
    return card_pos - num


def deal_with_increment(card_pos, num):
    return card_pos * num


COMMANDS = {
    parse.compile("deal into new stack"): deal_into_new_stack,
    parse.compile("cut {num:d}"): cut_cards,
    parse.compile("deal with increment {num:d}"): deal_with_increment,
}


def update_num_cards(shuffles, default):
    pattern = parse.compile("use {num:d} cards")

    num_cards = default
    for shuffle in shuffles:
        result = pattern.parse(shuffle)
        if result:
            num_cards = result.named["num"]

    return num_cards


def translate_shuffles(shuffles):
    commands = []
    for shuffle in shuffles:
        debug(shuffle)
        for pattern, command in COMMANDS.items():
            result = pattern.parse(shuffle)
            if result:
                commands.append((command, result.named))
    return commands


def as_linear(commands):
    maps = {}
    for card in range(2):
        card_pos = card
        for command, args in commands:
            card_pos = command(card_pos, **args)
        maps[card] = card_pos

    return maps[1] - maps[0], maps[0]


def geom_sum(a, n, m):
    """Calculate $S_n = a^{n-1} + ... + a + 1 mod m$

    Use $S_n = (a^n - 1) / (a - 1) mod m = (a^n - 1) * (a - 1)^{-1} mod m$.
    For the inverse, Fermat's little theorem implies that
    $(a - 1)^{-1} mod m = (a - 1)^{m-2} mod m$, so that
    $S_n = (a^n - 1) mod m * (a - 1)^{m-2} mod m$
    """
    return ((pow(a, n, m) - 1) * pow(a - 1, m - 2, m)) % m


def shuffle_deck(coeffs, card, num_cards, repeats, inverse=False):
    a, b = [c % num_cards for c in coeffs]
    if inverse:
        # y(c) = ac + b => ŷ(p) = âp - âb with ^ as inverse
        a_inv = pow(a, -1, num_cards)
        a, b = a_inv % num_cards, (-a_inv * b) % num_cards

    a_n = pow(a, repeats, num_cards)
    s_n = geom_sum(a, repeats, num_cards)
    debug(card, a, b, a_n, s_n)

    return (a_n * card + s_n * b) % num_cards


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        shuffles = file_path.read_text().strip().split("\n")
        commands = translate_shuffles(shuffles)
        coeffs = as_linear(commands)
        debug(coeffs)

        # Part 1
        num_cards = update_num_cards(shuffles, default=10007)
        card = 2019 % num_cards
        part_1 = shuffle_deck(coeffs, card=card, num_cards=num_cards, repeats=1)
        print(f"Card {card} is in position {part_1}")

        # Part 2
        num_cards = update_num_cards(shuffles, default=119315717514047)
        card_pos = 2020 % num_cards
        part_2 = shuffle_deck(
            coeffs,
            card=card_pos,
            num_cards=num_cards,
            repeats=101741582076661,
            inverse=True,
        )
        print(f"Card {part_2} is in position {card_pos}")


if __name__ == "__main__":
    main(sys.argv[1:])
