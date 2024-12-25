"""AoC 24, 2024: Crossed Wires."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    memory, gates = puzzle_input.split("\n\n")
    return {
        key: int(value)
        for line in memory.split("\n")
        for key, value in [line.split(": ")]
    }, {
        output: (operation, input1, input2)
        for line in gates.split("\n")
        for input1, operation, input2, _, output in [line.split()]
    }


def part1(data):
    """Solve part 1."""
    initial_memory, gates = data
    memory = calculate_gates(gates, initial_memory)
    return read_as_bin(memory, prefix="z")


def part2(data):
    """Solve part 2.

    The swaps were found by manually inspecting the tree of operations. Use
    --show to display.
    """
    initial_memory, gates = data
    if "--show" in sys.argv:
        for gate in [gate for gate in gates if gate.startswith("z")]:
            draw_graph(gates, gate)

    swaps = [("z06", "hwk"), ("qmd", "tnt"), ("z31", "hpc"), ("z37", "cgr")]
    for first, second in swaps:
        gates = swap(gates, first, second)

    memory = calculate_gates(gates, initial_memory)
    x = read_as_bin(initial_memory, prefix="x")
    y = read_as_bin(initial_memory, prefix="y")
    z = read_as_bin(memory, prefix="z")
    assert z == x + y, f"gates need to be swapped: {x} + {y} != {z}"

    return ",".join(sorted(gate for gates in swaps for gate in gates))


def swap(gates, first, second):
    """Swap two gates."""
    return gates | {first: gates[second], second: gates[first]}


def calculate_gates(gates, memory):
    """Run the calculation through all the gates."""
    while gates:
        new_gates = {}
        for output, (operation, input1, input2) in gates.items():
            if input1 not in memory or input2 not in memory:
                new_gates = new_gates | {output: (operation, input1, input2)}
                continue
            if operation == "AND":
                memory = memory | {output: memory[input1] & memory[input2]}
            elif operation == "XOR":
                memory = memory | {output: memory[input1] ^ memory[input2]}
            elif operation == "OR":
                memory = memory | {output: memory[input1] | memory[input2]}
            else:
                raise ValueError(f"{operation}")
        if gates == new_gates:
            break
        gates = new_gates
    return memory


def read_as_bin(memory, prefix):
    """Read a binary number from a memory."""
    number = [
        (gate, value) for gate, value in memory.items() if gate.startswith(prefix)
    ]
    return int(
        "0" + "".join(str(value) for _, value in sorted(number, reverse=True)),
        base=2,
    )


def draw_graph(gates, node, prefix=""):
    """Draw a graph of operations, starting at the given node."""
    gate = gates.get(node)
    if gate is None:
        return
    operation, input1, input2 = gate
    print(f"{prefix}{node} <- {input1} {operation} {input2}")

    gate1 = gates.get(input1)
    gate2 = gates.get(input2)
    pnum = (len(prefix) // 2) % 10
    if gate1 is None or gate2 is None or gate1 < gate2:
        draw_graph(gates, input1, f"{prefix}{pnum} ")
        draw_graph(gates, input2, f"{prefix}{pnum} ")
    else:
        draw_graph(gates, input2, f"{prefix}{pnum} ")
        draw_graph(gates, input1, f"{prefix}{pnum} ")


def count_graph(gates, node):
    """Count how deep the graph is, starting at the given node."""
    gate = gates.get(node)
    if gate is None:
        return 1
    _operation, input1, input2 = gate
    return count_graph(gates, input1) + count_graph(gates, input2)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.startswith("-"):
            continue
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
