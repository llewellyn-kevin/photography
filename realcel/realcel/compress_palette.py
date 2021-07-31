import argparse
from PIL import Image
from palette import get_colors
# from realcel.palette import get_colors

def open_input_image(input_name: str) -> Image:
    """Open the given input image and return an image object handling any errors."""

    image = Image.open(input_name)
    return image

def write_output_image(output_image: Image, output_name: str) -> bool:
    """Writes the output image to the user's file system."""

    try:
        output_image.save(output_name)
        return True
    except OSError:
        return False

def create_palette(input_image: Image, output_target: str) -> bool:
    """Creates a new image with every color from output and saves to the system."""

    colors = get_colors(input_image).to_list()
    output_image = Image.new('RGB', (len(colors), 1))
    for index, color in enumerate(colors):
        output_image.putpixel((index, 0), color)
    return write_output_image(output_image, output_target)

def succeed(outputted_image: str):
    """Notify the user that the process has succeeded."""

    print(f'Success! Created a palette: {outputted_image}')

def fail():
    """Notify the user that the process has failed."""

    print('Unable to create palette.')

if __name__ == "__main__":
    """Main loop for this script. Parses the args and starts the process."""

    parser = argparse.ArgumentParser(description = 'Script to take an input image, find every color, and return a palette of one pixel per color.')
    parser.add_argument('input', help = 'the path and name for the input file from which the palette should be made')
    parser.add_argument('output', help = 'the path and name for the output file that should be generated')
    args = parser.parse_args()

    source_image = open_input_image(args.input)
    succeed(args.output) if create_palette(source_image, args.output) else fail()
