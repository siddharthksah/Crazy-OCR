"""
A script to correct the skew in an image file and save the corrected image. 
If the image's width is more than its height after correction, the image is 
rotated by 90 degrees counter-clockwise.

This script uses numpy, skimage, cv2 and deskew python libraries.

Usage: 
1. Replace the `filename` with your file's name.
2. Replace the input and output file paths as per your directory structure.
3. Run the script in a Python environment with necessary libraries installed.

Author: Siddharth Kumar (www.siddharthsah.com)
"""

import os
import cv2
import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import rotate
from deskew import determine_skew

def deskew_and_rotate(filename):
    """
    Function to correct the skew in the image and save the corrected image.

    Args:
        filename (str): The filename of the image to correct.

    Returns:
        None
    """
    try:
        input_path = os.path.join('./data/output/', filename)
        output_path = os.path.join('./data/output/deskewed/', filename)

        # Load image and convert to grayscale
        image = io.imread(input_path)
        grayscale = rgb2gray(image)

        # Determine skew angle and rotate image to correct skew
        angle = determine_skew(grayscale)
        rotated = rotate(image, angle, resize=True) * 255

        # Rotate the image 90 degrees counter-clockwise if width is more than height
        height, width = rotated.shape[:2]
        if width > height:
            rotated = cv2.rotate(rotated, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # Save corrected image
        io.imsave(output_path, rotated.astype(np.uint8))

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    filename = 'File 1.jpg'
    deskew_and_rotate(filename)
    print('Done!')
