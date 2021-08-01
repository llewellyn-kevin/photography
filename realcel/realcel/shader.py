from PIL import Image

from realcel.color_utils import to_hsl, to_rgb

def generate_auto_shadow_palette(base_color: tuple, tint: int, gradient_width: int) -> Image:
    """Takes a base color, picks a shadow, and generates a gradient between the two.

    Arguments:
    base_color      --  The original color that should be transformed.
    tint            --  How much lightness should be subtracted from base color to
                        get the shadow color. Given as a percentage representing
                        lightness.
    gradient_width  --  How many pixels wide the transition between the two
                        colors should be. The total image will be 100px wide,
                        so this is the percentage of the image that will be
                        a transition area. Should be between 0 and 98 inclusive.
    """

    assert gradient_width >= 0 and gradient_width <= 98

    (base_h, base_s, base_l) = to_hsl(base_color)
    shadow_h, shadow_s, shadow_l = base_h, base_s, base_l - (tint / 100)
    shadow_color = to_rgb((shadow_h, shadow_s, shadow_l))

    output_image = Image.new('RGB', (100, 1))

    gradient_start = 50 - gradient_width // 2
    gradient_end = 50 + gradient_width // 2
    gradient_step = tint / 100 if gradient_width == 0 else tint / gradient_width / 100

    for x in range(gradient_start):
        output_image.putpixel((x, 0), base_color)
    for i, x in enumerate(range(gradient_start, gradient_end)):
        output_image.putpixel((x, 0), to_rgb((base_h, base_s, base_l - gradient_step * i)))
    for x in range(gradient_end, 100):
        output_image.putpixel((x, 0), shadow_color)

    return output_image
