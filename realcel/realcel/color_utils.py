from PIL import Image

from .color_tree import ColorTree

def get_colors(image: Image):
    """Takes an image and returns a color tree with every color present."""

    pixels = image.load()
    width, height = image.size
    colors = ColorTree()
    for y in range(height):
        for x in range(width):
            colors.append(pixels[x, y])
    return colors

def distance(color_one: tuple, color_two: tuple) -> float:
    """Finds the distance between two rgb colors.

    Colors must be given as a 3D tuple representing a point in the
    cartesian rgb color space. Consequently the distance is calculated
    by a simple cartesian distance formula. Returns a float representing
    the magnitude of the distance with precision 2.
    """

    (r1, g1, b1) = color_one
    (r2, g2, b2) = color_two
    return round(((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2) ** .5, 2)

def to_hsl(color: tuple) -> tuple:
    """Transforms a color from rgb space to hsl space.

    Color must be given as a 3D tuple representing a point in rgb space.
    Returns a 3D tuple representing a point in the hsl space.

    Saturation and luminance are given as floats representing percentages
    with a precision of 2. Hue is given as an angle in degrees between
    0 and 360 degrees with a precision of 0.
    """

    rf = color[0] / 255
    gf = color[1] / 255
    bf = color[2] / 255
    maximum = max(rf, gf, bf)
    minimum = min(rf, gf, bf)

    delta = maximum - minimum
    l = (maximum + minimum) / 2
    s = 0 if delta == 0 else delta / (1 - abs(2 * l - 1))

    if delta == 0:
        h = 0
    elif maximum == rf:
        h = 60 * (((gf - bf) / delta) % 6)
    elif maximum == gf:
        h = 60 * ((bf - rf) / delta + 2)
    else: # max is bf
        h = 60 * ((rf - gf) / delta + 4)

    return (round(h), round(s, 2), round(l, 2))

def to_rgb(color: tuple) -> tuple:
    """Converts from biconal hsl space to cartesian rgb space.

    Color must be given as a 3D tuple representing a point in hsl space.
    Returns a 3D tuple representing a point in the rgb space.

    Each value is returned as an integer with precision 0.
    """

    (h, s, l) = color
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    if h < 60:
        (rf, gf, bf) = (c, x, 0)
    elif h < 120:
        (rf, gf, bf) = (x, c, 0)
    elif h < 180:
        (rf, gf, bf) = (0, c, x)
    elif h < 240:
        (rf, gf, bf) = (0, x, c)
    elif h < 300:
        (rf, gf, bf) = (x, 0, c)
    else: # <= 360
        (rf, gf, bf) = (c, 0, x)

    return (round((rf + m) * 255),
            round((gf + m) * 255),
            round((bf + m) * 255))
