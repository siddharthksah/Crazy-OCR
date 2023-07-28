"""
Filename: image_blurriness_detection.py

This script reads an image and determines its blurriness score using the Laplacian 
method. A higher score means the image is in focus, while a low score implies the 
image is blurry. The script will print 'Blurry' or 'Not blurry' based on the score.

Author: Siddharth Kumar (www.siddharthsah.com)
Last Updated: July 28, 2023
"""

import cv2
from PIL import Image
import numpy as np


def calculate_blurriness_score(image_path):
    """
    Calculates the blurriness score of the image located at the given path.

    Args:
        image_path: The path to the image file.

    Returns:
        The blurriness score as a float.
    """

    # Open the image file and convert it to RGB
    image = Image.open(image_path).convert("RGB")
    image = np.array(image)

    # Convert the image into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate laplacian of the image and return the variance
    return cv2.Laplacian(gray, cv2.CV_64F).var()


def main():
    """
    The main function of the script. It determines and prints the blurriness status 
    of the image at the given path.
    """

    # The path to the image file
    image_path = './data/front.png'

    # Calculate the blurriness score of the image
    blurriness_score = calculate_blurriness_score(image_path)

    print(f"Blurriness Score: {blurriness_score}")

    # Determine whether the image is blurry or not
    if blurriness_score > 35:
        print("Status: Not blurry")
    else:
        print("Status: Blurry")


if __name__ == "__main__":
    main()
