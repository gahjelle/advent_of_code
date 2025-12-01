"""AoC 2017: Knot hash."""

# Standard library imports
import collections
import functools


class CircleList(collections.UserList):
    """A list which wraps around."""

    def __getitem__(self, key):
        """Handle keys that wrap around.

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
        """Handle keys that wrap around.

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
        """Reverse length number of elements starting at the given index.

        >>> circle = CircleList(range(4))
        >>> circle.reverse(2, 3)
        >>> circle
        [2, 1, 0, 3]
        """
        self[index : index + length] = self[index : index + length][::-1]

    def tie_knots(self, lengths, num_rounds=1):
        """Tie knots on a circular list.

        ## Example:

        With [1, 3, 2]

        0: [0]  1   2   3   --> ([0]) 1   2   3   -->  [0]  1   2   3
        1:  0  [1]  2   3   -->   0 ([1]  2   3)  -->   0  [3]  2   1
        2:  0  [3]  2   1   -->   0 ([3]  2)  1   -->   0  [2]  3   1
        ---
        3:  0  [2]  3   1   -->   0 ([2]) 3   1   -->   0  [2]  3   1
        4:  0  [2]  3   1   -->   0 ([2]  3   1)  -->   0  [1]  3   2
        5: [0]  1   3   2   --> ([0]  1)  3   2   -->  [1]  0   3   2

        >>> CircleList([0, 1, 2, 3]).tie_knots([1, 3, 2])
        [0, 2, 3, 1]

        >>> CircleList([0, 1, 2, 3]).tie_knots([1, 3, 2], num_rounds=2)
        [1, 0, 3, 2]
        """
        current_position = 0
        skip_size = 0
        for _ in range(num_rounds):
            for length in lengths:
                self.reverse(current_position, length)
                current_position = (current_position + length + skip_size) % len(self)
                skip_size += 1

        return self.data


def hash_list(keys, circle_length=256, num_rounds=1):
    """Perform a basic knot hash on a list of numbers.

    ## Example:

    >>> hash_list([2, 4, 1], circle_length=5)
    [2, 0, 1, 4, 3]
    """
    return CircleList(range(circle_length)).tie_knots(keys, num_rounds)


def hash_string(key_string, circle_length=256, num_rounds=64):
    """Perform a regular knot hash on a key string.

    ## Example:

    >>> hash_string("AoC 2017")
    '33efeb34ea91902bb2f59c9920caa6cd'
    """
    keys = input_to_lengths(key_string)
    sparse_hash = CircleList(range(circle_length)).tie_knots(keys, num_rounds)
    return as_hex(sparse_to_dense_hash(sparse_hash))


def input_to_lengths(key_string):
    """Convert a key string to its ASCII codes, add fixed suffix.

    >>> input_to_lengths("1,2,3")
    [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]
    """
    return [ord(char) for char in key_string] + [17, 31, 73, 47, 23]


def sparse_to_dense_hash(sparse_hash):
    """Calculate dense from sparse hash.

    >>> sparse_to_dense_hash([n % 15 for n in range(256)])
    [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15]
    """
    return [
        functools.reduce(lambda x, y: x ^ y, sparse_hash[idx : idx + 16])
        for idx in range(0, len(sparse_hash), 16)
    ]


def as_hex(hash):
    """Represent hash as a hexadecimal number.

    >>> as_hex([64, 7, 255])
    '4007ff'
    """
    return "".join(hex(number).replace("0x", "00")[-2:] for number in hash)
