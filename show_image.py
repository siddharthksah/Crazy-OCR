"""
filename: image_to_text.py

An open-source Python script to read an image and display it using the Python Imaging Library (PIL)
and OpenCV, with the additional capability to extract text from the image using PyTesseract.

Author: Siddharth Kumar (www.siddharthsah.com)
Last Updated: July 28, 2023
"""

import cv2
from PIL import Image
import pytesseract
import os

def read_image(file_path):
    """
    This function reads an image file from the specified path.

    Args:
        file_path (str): The path to the image file.

    Returns:
        Image: A PIL Image object.
    """
    try:
        im = Image.open(file_path)
        return im
    except IOError as e:
        print(f"IOError: {e}")
        print(f"File {file_path} cannot be opened.")
        return None

def display_image(image):
    """
    This function displays the specified image.

    Args:
        image (Image): A PIL Image object.
    """
    if image is not None:
        image.show()
    else:
        print("Cannot display the image as the Image object is None.")

def main():
    """
    The main function to execute the image reading and displaying.
    """
    # Define the image file path
    image_file_path = "./data/front.jpg"

    # Read the image from the file
    image = read_image(image_file_path)

    # Display the image
    display_image(image)

# This is a standard Python practice. If this file (image_to_text.py) is being imported from 
# another module, it prevents the following code block from being run. However, if it is run 
# as a standalone script, the code block is executed.
if __name__ == "__main__":
    main()
