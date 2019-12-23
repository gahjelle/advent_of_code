"""Category Six

Advent of Code 2019, day 23
Solution by Geir Arne Hjelle, 2019-12-23
"""
import collections
import pathlib
import sys
from dataclasses import dataclass, field

from aoc2019.intcode_computer import IntcodeComputer

NAT_ADDRESS = 255
debug = print if "--debug" in sys.argv else lambda *_: None


@dataclass
class NIC:
    address: int
    queue: collections.deque = field(default_factory=collections.deque, init=False)
    idle: bool = False

    def __post_init__(self):
        self.queue.append(self.address)

    def __next__(self):
        if self.queue:
            return self.queue.popleft()
        else:
            self.idle = True
            return -1

    def send(self, x, y):
        self.idle = False
        self.queue.extend([x, y])


@dataclass
class NAT:
    address: int
    memory: tuple = field(default=(None, None), init=False)
    network: dict = field(repr=False)
    stack: list = field(default_factory=list, init=False, repr=False)

    def send(self, x, y):
        self.memory = (x, y)

    def network_idle(self):
        for computer in self.network.values():
            if not computer.input.idle:
                return False
        return True

        # Have we seen any packets
        return bool(self.stack)

    def resume_network(self):
        address = 0
        x, y = self.memory
        if x is None or y is None:
            return

        if self.stack and self.stack[-1] == self.memory:
            return self.memory

        debug(f"NAT sending to {address}: {x}, {y}")
        self.stack.append((x, y))
        self.network[address].input.send(x, y)


def run_network(intcode, computers, use_nat=False):
    network = {a: IntcodeComputer(intcode, input=NIC(a)) for a in computers}
    inputs = {a: network[a].input for a in computers}
    outputs = {a: collections.deque() for a in computers}
    monitor = {} if use_nat else {NAT_ADDRESS}
    if use_nat:
        nat = inputs[NAT_ADDRESS] = NAT(NAT_ADDRESS, network)

    # Boot and run computers
    while True:
        for computer in computers:
            output = network[computer].step()
            if output is None:
                continue

            debug(f"Receiving from {computer}: {output}")
            outputs[computer].append(output)
            if len(outputs[computer]) < 3:
                continue

            address = outputs[computer].popleft()
            x = outputs[computer].popleft()
            y = outputs[computer].popleft()
            debug(f"Sending to {address}: {x}, {y}")
            if address in monitor:
                return address, x, y
            inputs[address].send(x, y)

        if use_nat and nat.network_idle():
            response = nat.resume_network()
            if response is not None:
                return response


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        intcode = [int(s) for s in file_path.read_text().split(",")]

        # Part 1
        address, x, y = run_network(intcode, computers=range(50))
        print(f"The first packet sent to {address} is {y}")

        # Part 2
        x, y = run_network(intcode, computers=range(50), use_nat=True)
        print(f"The first repeated packet sent by the NAT is {y}")


if __name__ == "__main__":
    main(sys.argv[1:])
