from typing import List

from .intcode import intcode
from .intcode import looping_intcodes
from .intcode import chain_intercodes


def print_image(image_array: List[int], width: int, ascii_render: bool = False,
                ascii_map: List[str] = ["█", "░"]):
    output = ""
    for i, item in enumerate(image_array):
        if i > 0 and i % width == 0:
            output += "\n"
        output += f"{str(item) if not ascii_render else ascii_map[item]}"
    return output


def find_topmost_pixel(pixel_array):
    for item in pixel_array:
        if item == 0 or item == 1:
            return item


#     return 9


def image_from_layers(layers):
    pixel_groups = list(zip(*layers))
    image_array = [find_topmost_pixel(pixel_group) for pixel_group in pixel_groups]

    return image_array
