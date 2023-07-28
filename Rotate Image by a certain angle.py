"""
filename: image_rotation.py

This is an open-source Python script for image processing using OpenCV. 
The script reads an image, determines its center, and then rotates the image around this center point.

Author: Siddharth Kumar (www.siddharthsah.com)
Last Updated: July 28, 2023
"""

import argparse
import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path):
    """
    Loads an image from the specified file path.

    Args:
        image_path (str): The file path of the image to load.

    Returns:
        ndarray: The loaded image.
    """
    try:
        return cv2.imread(image_path)
    except IOError as e:
        print(f"IOError: {e}")
        print(f"Could not read file at path: {image_path}")
        return None

def rotate_image(image, angle):
    """
    Rotates an image by the specified angle around its center point.

    Args:
        image (ndarray): The image to rotate.
        angle (float): The angle by which to rotate the image.

    Returns:
        ndarray: The rotated image.
    """
    if image is not None:
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h))
        return rotated
    else:
        print("Image is None, cannot perform rotation.")
        return None

def display_image(image):
    """
    Displays an image using matplotlib.

    Args:
        image (ndarray): The image to display.
    """
    if image is not None:
        plt.imshow(image)
        plt.show()
    else:
        print("Image is None, cannot display image.")

def main():
    """
    The main function to execute the image processing.
    """
    image_path = './data/output/deskewed/File 1.jpg'
    image = load_image(image_path)

    angle_to_rotate = -20
    rotated_image = rotate_image(image, angle_to_rotate)

    display_image(rotated_image)

if __name__ == "__main__":
    main()
