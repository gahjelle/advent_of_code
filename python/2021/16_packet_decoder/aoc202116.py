"""AoC 16, 2021: Packet Decoder"""

from __future__ import annotations

# Standard library imports
import itertools
import math
import pathlib
import sys
from dataclasses import dataclass


@dataclass
class Literal:
    version: int
    value: int

    @classmethod
    def from_str(cls, version, packet_data):
        """Parse a literal from a binary string"""
        bits = []
        while True:
            more_groups, next_group = packet_data[0], packet_data[1:5]
            packet_data = packet_data[5:]
            bits.append(next_group)
            if more_groups == "0":
                break

        return cls(version=version, value=int("".join(bits), base=2)), packet_data

    def get_version(self):
        """Get version of literal"""
        return self.version

    def evaluate(self):
        """Get value of literal"""
        return self.value


@dataclass
class Operator:
    version: int
    operator: int
    sub_packets: list[Literal | Operator]

    @classmethod
    def from_str(cls, version, operator, packet_data):
        """Parse an operator from a binary string"""
        length_type = packet_data[0]
        if length_type == "0":
            num = int(packet_data[1:16], base=2)
            packet_data = packet_data[16:]
            packet_data, left_over = packet_data[:num], packet_data[num:]
        elif length_type == "1":
            num = int(packet_data[1:12], base=2)
            packet_data, left_over = packet_data[12:], ""

        sub_packets = []
        for packet_num in itertools.count(1):
            sub_packet, packet_data = parse_packet(packet_data)
            sub_packets.append(sub_packet)

            if not packet_data or packet_num == num:
                break

        return cls(version, operator, sub_packets), left_over or packet_data

    def get_version(self):
        """Get version of operator

        The version of an operator is its internal version plus the sum of the versions
        of all its subpackets.

        >>> Operator(1, operator=0, sub_packets=[
        ...     Literal(2, value=3),
        ...     Literal(3, value=10),
        ...     Literal(4, value=1),
        ... ]).get_version()
        10
        """
        return self.version + sum(packet.get_version() for packet in self.sub_packets)

    def evaluate(self):
        """Evaluate the operator based on operator type

        Packets with type ID 0 are sum packets - their value is the sum of the values of
        their sub-packets. If they only have a single sub-packet, their value is the
        value of the sub-packet.

        >>> Operator(0, operator=0, sub_packets=[
        ...     Literal(0, value=3),
        ...     Literal(0, value=10),
        ...     Literal(0, value=1),
        ... ]).evaluate()
        14

        Packets with type ID 1 are product packets - their value is the result of
        multiplying together the values of their sub-packets. If they only have a single
        sub-packet, their value is the value of the sub-packet.

        >>> Operator(0, operator=1, sub_packets=[
        ...     Literal(0, value=3),
        ...     Literal(0, value=10),
        ... ]).evaluate()
        30
        """
        match self.operator:
            case 0:
                return sum(packet.evaluate() for packet in self.sub_packets)
            case 1:
                return math.prod(packet.evaluate() for packet in self.sub_packets)
            case 2:
                return min(packet.evaluate() for packet in self.sub_packets)
            case 3:
                return max(packet.evaluate() for packet in self.sub_packets)
            case 5:
                first, second = self.sub_packets
                return 1 if first.evaluate() > second.evaluate() else 0
            case 6:
                first, second = self.sub_packets
                return 1 if first.evaluate() < second.evaluate() else 0
            case 7:
                first, second = self.sub_packets
                return 1 if first.evaluate() == second.evaluate() else 0


def parse_data(puzzle_input):
    """Parse input"""
    num_bits = 4 * len(puzzle_input)
    return bin(int(puzzle_input, base=16))[2:].zfill(num_bits)


def part1(data):
    """Solve part 1"""
    packet, _ = parse_packet(data)
    return packet.get_version()


def part2(data):
    """Solve part 2"""
    packet, _ = parse_packet(data)
    return packet.evaluate()


def parse_packet(packet):
    """Parse a packet, return packet and left over packet string

    >>> parse_packet("110100101111111000101000")
    (Literal(version=6, value=2021), '000')

    >>> parse_packet("00111000000000000110111101000101001010010001001000000000")
    (Operator(version=1, operator=6, sub_packets=[Literal(version=6, value=10),
                                                  Literal(version=2, value=20)]),
     '0000000')
    """
    version = int(packet[:3], base=2)
    packet_type = int(packet[3:6], base=2)
    packet_data = packet[6:]

    if packet_type == 4:
        return Literal.from_str(version=version, packet_data=packet_data)
    else:
        return Operator.from_str(
            version=version, operator=packet_type, packet_data=packet_data
        )


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
