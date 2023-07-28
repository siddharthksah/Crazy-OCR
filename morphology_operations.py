"""
filename: morphology_operations.py

This is an open-source Python script for morphological operations on an image using OpenCV. 
The script applies a variety of operations with different settings and saves the result.

Author: Siddharth Kumar (www.siddharthsah.com)
Last Updated: July 28, 2023
"""

import cv2
import numpy as np
import os
from itertools import cycle
from common import draw_str
from PIL import Image

def apply_operations(image):
    """
    Applies a variety of morphological operations to the given image and saves the result.

    Args:
        image (np.array): The image to perform operations on.
    """
    # Define operation modes and structuring element modes
    modes = ['erode/dilate', 'open/close', 'blackhat/tophat', 'gradient']
    str_modes = ['ellipse', 'rect', 'cross']

    # Initialize a count for naming output images
    count = 0

    for cur_mode in modes:
        for cur_str_mode in str_modes:
            for i in range(12, 20):
                sz = i
                for j in range(1, 10):
                    iters = j
                    count += 1
                    opers = cur_mode.split('/')
                    
                    if len(opers) > 1:
                        sz -= 10
                        op = opers[sz > 0]
                        sz = abs(sz)
                    else:
                        op = opers[0]
                    sz = sz * 2 + 1
                    
                    str_name = 'MORPH_' + cur_str_mode.upper()
                    oper_name = 'MORPH_' + op.upper()
                    st = cv2.getStructuringElement(getattr(cv2, str_name), (sz, sz))
                    res = cv2.morphologyEx(image, getattr(cv2, oper_name), st, iterations=iters)

                    # Drawing operation details on the result image
                    draw_str(res, (10, 20), 'mode: ' + cur_mode)
                    draw_str(res, (10, 40), 'operation: ' + oper_name)
                    draw_str(res, (10, 60), 'structure: ' + str_name)
                    draw_str(res, (10, 80), 'ksize: %d  iters: %d' % (sz, iters))

                    # Saving the result image
                    cv2.imwrite("./output_try/" + "frame%d.jpg" % count, res)
                    print(f"Image {count} saved")

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

def main():
    """
    The main function to execute the image processing.
    """
    image_path = './data/front.jpg'
    image = load_image(image_path)

    # Applying operations if image is successfully loaded
    if image is not None:
        apply_operations(image)
        print("Done, all images saved!")
    else:
        print("Image loading failed. Operations not applied.")

if __name__ == "__main__":
    main()
