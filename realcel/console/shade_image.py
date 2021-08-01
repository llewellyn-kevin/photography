import argparse

from PIL import Image

from realcel.color_utils import get_colors, find_closest_color

def create_shaded_image(input_image: Image, input_palette: Image, output_target: str) -> bool:
    """Replaces all the colors in an image, with the closest color from the given palette."""

    palette_colors = get_colors(input_palette).to_list()
    (width, height) = input_image.size
    output_image = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            source_color = input_image.getpixel((x, y))
            converted_color = find_closest_color(source_color, palette_colors)
            output_image.putpixel((x, y), converted_color)
    try:
        output_image.save(output_target)
        return True
    except ValueError:
        return False

def succeed(outputted_image: str):
    """Notify the user that the process has succeeded."""

    print(f'Success! Created an image: {outputted_image}')

def fail():
    """Notify the user that the process has failed."""

    print('Unable to create new image.')

if __name__ == "__main__":
    """Main loop for this script. Parses the args and starts the process."""

    parser = argparse.ArgumentParser(description = 'Script to take an input image, find every color, and return a palette of one pixel per color.')
    parser.add_argument('input', help = 'the path and name for the input file from which the palette should be made')
    parser.add_argument('palette', help = 'the path and name for the color palette that should be selected from')
    parser.add_argument('output', help = 'the path and name for the output file that should be generated')
    args = parser.parse_args()

    source_image = Image.open(args.input)
    palette_image = Image.open(args.palette)
    succeed(args.output) if create_shaded_image(source_image, palette_image, args.output) else fail()
