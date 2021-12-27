"""AoC 10, 2017: Knot Hash"""

# Standard library imports
import collections
import functools
import pathlib
import sys


class CircleList(collections.UserList):
    """A list which wraps around"""

    def __getitem__(self, key):
        """Handle keys that wrap around

        >>> circle = CircleList(range(4))
        >>> circle[5]
        1

        >>> circle[3:6]
        [3, 0, 1]
        """
        size = len(self.data)
        if isinstance(key, int):
            return self.data[key % size]
        elif isinstance(key, slice):
            start, stop, step = key.indices(size)
            if stop == key.stop:
                return self.data[key]
            else:
                return self.data[start:stop:step] + self.data[: key.stop % size : step]

    def __setitem__(self, key, value):
        """Handle keys that wrap around

        >>> circle = CircleList(range(4))
        >>> circle[6] = 66
        >>> circle
        [0, 1, 66, 3]

        >>> circle[3:5] = [333, 444]
        >>> circle
        [444, 1, 66, 333]
        """
        size = len(self.data)
        if isinstance(key, int):
            self.data[key % size] = value
        elif isinstance(key, slice):
            start, stop, step = key.indices(size)
            if stop == key.stop:
                self.data[key] = value
            else:
                first = (stop - start) // step
                self.data[key] = value[:first]
                self.data[: key.stop % size : step] = value[first:]

    def reverse(self, index, length):
        """Reverse length number of elements starting at the given index

        >>> circle = CircleList(range(4))
        >>> circle.reverse(2, 3)
        >>> circle
        [2, 1, 0, 3]
        """
        self[index : index + length] = self[index : index + length][::-1]


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


def part1(data, circle_length=256):
    """Solve part 1"""
    lengths = [int(number) for number in data.split(",")]
    circle = CircleList(range(circle_length))
    first, second, *_ = tie_knots(circle, lengths)
    return first * second


def part2(data, circle_length=256):
    """Solve part 2"""
    lengths = input_to_lengths(data)
    circle = CircleList(range(circle_length))
    sparse_hash = tie_knots(circle, lengths, num_rounds=64)
    dense_hash = sparse_to_dense_hash(sparse_hash)
    return as_hex(dense_hash)


def input_to_lengths(input):
    """Convert input to their ASCII codes, add fixed suffix

    >>> input_to_lengths("1,2,3")
    [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]
    """
    return [ord(char) for char in input] + [17, 31, 73, 47, 23]


def tie_knots(circle, lengths, num_rounds=1):
    """Tie knots on a circular list

    0: [0]  1   2   3   --> ([0]) 1   2   3   -->  [0]  1   2   3
    1:  0  [1]  2   3   -->   0 ([1]  2   3)  -->   0  [3]  2   1
    2:  0  [3]  2   1   -->   0 ([3]  2)  1   -->   0  [2]  3   1
       ---
    3:  0  [2]  3   1   -->   0 ([2]) 3   1   -->   0  [2]  3   1
    4:  0  [2]  3   1   -->   0 ([2]  3   1)  -->   0  [1]  3   2
    5: [0]  1   3   2   --> ([0]  1)  3   2   -->  [1]  0   3   2

    >>> tie_knots(CircleList([0, 1, 2, 3]), [1, 3, 2])
    [0, 2, 3, 1]

    >>> tie_knots(CircleList([0, 1, 2, 3]), [1, 3, 2], num_rounds=2)
    [1, 0, 3, 2]
    """
    current_position = 0
    skip_size = 0
    for _ in range(num_rounds):
        for length in lengths:
            circle.reverse(current_position, length)
            current_position = (current_position + length + skip_size) % len(circle)
            skip_size += 1

    return circle.data


def sparse_to_dense_hash(sparse_hash):
    """Calculate dense from sparse hash

    >>> sparse_to_dense_hash([n % 15 for n in range(256)])
    [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15]
    """
    return [
        functools.reduce(lambda x, y: x ^ y, sparse_hash[idx : idx + 16])
        for idx in range(0, len(sparse_hash), 16)
    ]


def as_hex(hash):
    """Represent hash as a hexadecimal number

    >>> as_hex([64, 7, 255])
    '4007ff'
    """
    return "".join(hex(number).replace("0x", "00")[-2:] for number in hash)


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
