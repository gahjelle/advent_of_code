"""Space Image Format

Advent of Code 2019, day 8
Solution by Geir Arne Hjelle, 2019-12-08
"""
# Standard library imports
import pathlib
import sys

# Third party imports
import numpy as np

debug = print if "--debug" in sys.argv else lambda *_: None


def create_image(text, width=25, height=6):
    img = np.array([int(s) for s in text])
    return img.reshape(-1, height, width)


def count(image):
    num_layers = image.shape[0]
    num_zeros = np.sum(image.reshape(num_layers, -1) == 0, axis=1)
    min_layer = np.argmin(num_zeros)

    return np.sum(image[min_layer] == 1) * np.sum(image[min_layer] == 2)


def decode(image):
    pixel_map = {0: " ", 1: "█"}

    msg = image[0]
    for layer in image[1:]:
        idx = msg == 2
        msg[idx] = layer[idx]

    return "\n".join("".join(pixel_map[c] for c in layer) for layer in msg)


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        image = create_image(file_path.read_text().strip())
        print(f"Checksum: {count(image)}")
        print(f"Message:\n{decode(image)}")


if __name__ == "__main__":
    main(sys.argv[1:])
