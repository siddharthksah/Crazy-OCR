"""
Module to create a collage from a collection of images.
"""

from PIL import Image
import os


def make_collage(directory, output_path, cols=10, rows=10, width=10240, height=7680, debug=False):
    """
    Function to create a collage from images in a specified directory.

    :param directory: str, Path to directory containing images.
    :param output_path: str, Path to save the generated collage.
    :param cols: int, Number of columns in the collage. Default is 10.
    :param rows: int, Number of rows in the collage. Default is 10.
    :param width: int, Width of the collage. Default is 10240.
    :param height: int, Height of the collage. Default is 7680.
    :param debug: bool, Flag to print debug information. Default is False.
    """
    thumbnail_width = width // cols
    thumbnail_height = height // rows
    size = thumbnail_width, thumbnail_height
    new_im = Image.new('RGB', (width, height))
    ims = []

    # Get list of files in directory
    files = os.listdir(directory)

    # Check if enough images to fill collage
    if len(files) < cols * rows:
        print("Error: Not enough images in directory to fill collage.")
        return

    for filename in files:
        if filename.endswith(".jpg"):
            try:
                im = Image.open(os.path.join(directory, filename))
                im.thumbnail(size)
                ims.append(im)
            except IOError:
                print(f"Error: Unable to open image file {filename}. Skipping...")

    i = 0
    x = 0
    y = 0

    for col in range(cols):
        for row in range(rows):
            if debug:
                print(i, x, y)
            new_im.paste(ims[i], (x, y))
            i += 1
            y += thumbnail_height
        x += thumbnail_width
        y = 0

    try:
        new_im.save(output_path)
        print(f"Collage saved successfully at {output_path}")
    except IOError:
        print("Error: Unable to save collage.")


if __name__ == "__main__":
    input_dir = "./Deskewed Cropped/temp/"
    output_path = "./Deskewed Cropped/temp/collage.png"

    make_collage(input_dir, output_path, debug=True)
