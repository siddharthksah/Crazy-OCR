"""
Filename: morphology_operations.py

This Python script is designed to perform morphology operations (like erode/dilate, 
open/close, blackhat/tophat, and gradient) on an image. It can be useful in various 
image processing tasks such as noise reduction, image enhancement etc.

The script uses OpenCV to perform these operations and display the processed images 
in real time.

Author: Siddharth Kumar (www.siddharthsah.com)
Last Updated: July 28, 2023
"""

import sys
from itertools import cycle
import cv2 as cv

# Function to perform the morphological operations
def perform_morphology(img, cur_mode, cur_str_mode):
    """
    Perform morphology operations on the image and show the result.

    Args:
        img: The input image.
        cur_mode: Current morphology mode.
        cur_str_mode: Current structure mode.
    """
    sz = cv.getTrackbarPos('op/size', 'morphology')
    iters = cv.getTrackbarPos('iters', 'morphology')

    opers = cur_mode.split('/')
    if len(opers) > 1:
        sz = sz - 10
        op = opers[sz > 0]
        sz = abs(sz)
    else:
        op = opers[0]
    sz = sz*2+1

    str_name = 'MORPH_' + cur_str_mode.upper()
    oper_name = 'MORPH_' + op.upper()
    st = cv.getStructuringElement(getattr(cv, str_name), (sz, sz))
    res = cv.morphologyEx(img, getattr(cv, oper_name), st, iterations=iters)

    cv.imshow('morphology', res)

# Load the image
def load_image(file_path):
    """
    Load an image from the specified file path.

    Args:
        file_path: The file path to the image.

    Returns:
        Loaded image or None if the image file could not be loaded.
    """
    img = cv.imread(file_path)
    if img is None:
        print('Failed to load image file:', file_path)
    else:
        return img

# The main function
def main():
    """
    The main function that executes the image processing and morphological operations.
    """
    try:
        img_file_path = sys.argv[1]
    except:
        img_file_path = './data/front.jpg'

    img = load_image(img_file_path)

    if img is None:
        sys.exit(1)

    cv.imshow('original', img)

    modes = cycle(['erode/dilate', 'open/close', 'blackhat/tophat', 'gradient'])
    str_modes = cycle(['ellipse', 'rect', 'cross'])

    cur_mode = next(modes)
    cur_str_mode = next(str_modes)

    cv.namedWindow('morphology')
    cv.createTrackbar('op/size', 'morphology', 12, 20, lambda x: perform_morphology(img, cur_mode, cur_str_mode))
    cv.createTrackbar('iters', 'morphology', 1, 10, lambda x: perform_morphology(img, cur_mode, cur_str_mode))

    perform_morphology(img, cur_mode, cur_str_mode)

    while True:
        ch = cv.waitKey()
        if ch == 27:  # ESC key to exit
            break
        if ch == ord('1'):
            cur_mode = next(modes)
            perform_morphology(img, cur_mode, cur_str_mode)
        if ch == ord('2'):
            cur_str_mode = next(str_modes)
            perform_morphology(img, cur_mode, cur_str_mode)

    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
