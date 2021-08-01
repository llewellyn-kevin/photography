from realcel.shader import *

class TestShader:
    def test_it_generates_a_shadow(self):
        highlight = (66, 135, 245)
        shadow = (8, 62, 150)
        gradient = generate_auto_shadow_palette(highlight, 30, 0)

        assert gradient.getpixel((0, 0)) == highlight
        assert gradient.getpixel((99, 0)) == shadow

    def test_it_can_have_no_gradient(self):
        highlight = (66, 135, 245)
        shadow = (8, 62, 150)
        gradient = generate_auto_shadow_palette(highlight, 30, 0)

        assert gradient.getpixel((49, 0)) == highlight
        assert gradient.getpixel((50, 0)) == shadow

    def test_it_creates_a_gradient_with_the_correct_width(self):
        highlight = (66, 135, 245)
        shadow = (8, 62, 150)
        wide_hightlight = (0, 97, 255)
        wide_shadow = (0, 0, 0)

        narrow = generate_auto_shadow_palette(highlight, 30, 5)
        wide = generate_auto_shadow_palette(wide_hightlight, 50, 98)

        # Check boundries
        assert narrow.getpixel((47, 0)) == highlight
        assert narrow.getpixel((53, 0)) == shadow
        assert wide.getpixel((0, 0)) == wide_hightlight
        assert wide.getpixel((99, 0)) == wide_shadow

        # Check gradients
        for x in range(49, 52):
            pixel = narrow.getpixel((x, 0))
            assert pixel != highlight and pixel != shadow
        for x in range(1, 99):
            pixel = narrow.getpixel((x, 0))
            assert pixel != wide_hightlight and pixel != wide_shadow
