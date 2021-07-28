from random import randint

from PIL import Image

import realcel.palette as palette

class TestPalette:
    def test_it_finds_a_color_in_an_image(self):
        # Generate an image with a single red pixel
        image = Image.new('RGB', (1, 1))
        image.putpixel((0, 0), (255, 0, 0))

        # Check if the colors in the image are found
        tree = palette.get_colors(image)
        assert(tree.has((255, 0, 0)))


    def test_it_finds_one_instance_of_every_color_in_an_image(self):
        # Generate an image with 2 each of 5 random colors
        width, height = 2, 5
        image = Image.new('RGB', (width, height))
        colors = []
        for _ in range(5):
            colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
        for y in range(height):
            for x in range(width):
                image.putpixel((x, y), colors[y])

        # Check if the colors in the image are found
        tree = palette.get_colors(image)
        for color in colors:
            assert(tree.has(color))
