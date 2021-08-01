import os

from PIL import Image

from console.compress_palette import *

class TestCompressPalette:
    def test_it_opens_an_image(self):
        image = Image.new('RGB', (10, 10))
        filename = 'images/test.png'
        image.save(filename)
        assert open_input_image(filename)
        os.remove(filename)

    def test_it_creates_a_new_image(self):
        image = Image.new('RGB', (10, 10))
        filename = 'images/test.png'
        assert write_output_image(image, filename)
        assert os.path.exists(filename)
        os.remove(filename)

    def test_it_fails_to_write_non_image_format(self):
        image = Image.new('RGB', (10, 10))
        filename = 'images/test.pn'
        assert not write_output_image(image, filename)
        assert not os.path.exists(filename)

    def test_it_creates_a_minimized_palette(self):
        source_image = Image.new('RGB', (10, 10))
        filename = 'images/test.png'
        (width, height) = source_image.size
        for x in range(width):
            for y in range(height):
                source_image.putpixel((x, y), (20 * y, 0, 0))
        create_palette(source_image, filename)
        assert os.path.exists(filename)
        output_palette = Image.open(filename)
        assert output_palette.size == (10, 1)
        assert output_palette.getpixel((0, 0)) == (0, 0, 0)
        assert output_palette.getpixel((2, 0)) == (40, 0, 0)
        assert output_palette.getpixel((4, 0)) == (80, 0, 0)
        assert output_palette.getpixel((6, 0)) == (120, 0, 0)
        assert output_palette.getpixel((8, 0)) == (160, 0, 0)
        output_palette.save(filename) # saving the file frees it to be deleted
        os.remove(filename)
