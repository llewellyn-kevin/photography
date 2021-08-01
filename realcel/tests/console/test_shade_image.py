import os

from PIL import Image

from console.shade_image import create_shaded_image

class TestShadeImage:
    def test_it_creates_a_shaded_image(self):
        image = Image.new('RGB', (20, 3))
        for x in range(20):
            image.putpixel((x, 0), (10 * x + 10, 0, 0))
            image.putpixel((x, 1), (0, 10 * x + 10, 0))
            image.putpixel((x, 2), (0, 0, 10 * x + 10))

        palette = Image.new('RGB', (1, 3))
        palette.putpixel((0, 0), (255, 0, 0))
        palette.putpixel((0, 1), (0, 255, 0))
        palette.putpixel((0, 2), (0, 0, 255))

        filename = 'images/test_output.png'

        assert create_shaded_image(image, palette, filename)
        assert os.path.exists(filename)

        new_image = Image.open(filename)
        assert new_image.size == (20, 3)
        for x in range(20):
            assert new_image.getpixel((x, 0)) == (255, 0, 0)
            assert new_image.getpixel((x, 1)) == (0, 255, 0)
            assert new_image.getpixel((x, 2)) == (0, 0, 255)
        new_image.save(filename)
        os.remove(filename)

    def test_it_fails_to_create_image_with_bad_format(self):
        image = Image.new('RGB', (20, 3))
        palette = Image.new('RGB', (1, 3))
        assert not create_shaded_image(image, palette, 'images/test_output.pn')
