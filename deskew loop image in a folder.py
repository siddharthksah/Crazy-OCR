import os
import cv2
import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import rotate

from deskew import determine_skew

directory = './Cropped Image Processing/'



for filename in os.listdir(directory):

    if filename.endswith(".jpg"):
        print(filename)
        #do smth

        #print(filename)

        # image = cv2.imread('./output/' + filename)

        #print(image)
        image = io.imread(directory + filename)
        grayscale = rgb2gray(image)
        angle = determine_skew(grayscale)
        rotated = rotate(image, angle, resize=True) * 255

        height, width = rotated.shape[:2]
        # print(height)
        # print(width)

        if width > height :
            io.imsave('./Cropped Image Processing/Image Processing Cropped Deskewed/' + filename, rotated.astype(np.uint8))
        else:
            image = cv2.rotate(rotated, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
            io.imsave('./Deskewed Cropped/Image Processing Cropped Deskewed/' + filename, image.astype(np.uint8))






