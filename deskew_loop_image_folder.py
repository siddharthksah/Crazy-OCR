"""
This script reads images from a specified directory, determines the skew angle of each image,
then rotates the image to correct the skew, and saves the corrected image to another directory.

Usage: Run the script in an environment with cv2, numpy, skimage, and deskew installed.
The directories for input and output should be updated accordingly.
"""

import os
import cv2
import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import rotate
from deskew import determine_skew

# Set the directory for input images and output results
INPUT_DIR = './Cropped Image Processing/'
OUTPUT_DIR = './Deskewed Cropped/Image Processing Cropped Deskewed/'

def process_image(image_path, output_path):
    """
    Read the image, determine and correct its skew, then save to output directory.

    Args:
    image_path (str): The path of the image file to process.
    output_path (str): The path to save the processed image.
    """
    image = io.imread(image_path)
    grayscale = rgb2gray(image)
    angle = determine_skew(grayscale)
    rotated = rotate(image, angle, resize=True) * 255

    # Rotate the image 90 degrees if its width is greater than its height
    height, width = rotated.shape[:2]
    if width > height:
        rotated = cv2.rotate(rotated, cv2.ROTATE_90_COUNTERCLOCKWISE)

    io.imsave(output_path, rotated.astype(np.uint8))

def process_directory(directory):
    """
    Process all .jpg images in the specified directory.

    Args:
    directory (str): The directory containing the images.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            try:
                print(f"Processing image {filename}")
                image_path = os.path.join(directory, filename)
                output_path = os.path.join(OUTPUT_DIR, filename)
                process_image(image_path, output_path)
            except Exception as e:
                print(f"Error processing image {filename}: {e}")

if __name__ == "__main__":
    process_directory(INPUT_DIR)
