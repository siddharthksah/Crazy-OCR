import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import rotate
import cv2

from deskew import determine_skew

filename = 'File 1.jpg'

image = io.imread('./data/output/' + filename)
grayscale = rgb2gray(image)
angle = determine_skew(grayscale)
rotated = rotate(image, angle, resize=True) * 255
height, width = rotated.shape[:2]
# print(height)
# print(width)
if width > height:
    io.imsave('./data/output/deskewed/' + filename, rotated.astype(np.uint8))
else:
    image = cv2.rotate(rotated, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    io.imsave('./data/output/deskewed/' + filename, image.astype(np.uint8))
print('Done!')
