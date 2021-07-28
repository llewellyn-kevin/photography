from PIL import Image

from . import ColorTree

def get_colors(image: Image):
    """Takes an image and returns a color tree with every color present."""

    pixels = image.load()
    width, height = image.size
    colors = ColorTree()
    for y in range(height):
        for x in range(width):
            colors.append(pixels[x, y])
    return colors
