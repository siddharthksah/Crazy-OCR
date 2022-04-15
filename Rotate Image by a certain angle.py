import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt


# Load and display original image
image = cv2.imread('./data/output/deskewed/File 1.jpg')


# Determine the center of the image
# OpenCV allows you to specify any arbitrary point to rotate around,
# here we'll use the image center
(h, w) = image.shape[:2]
center = (w//2, h//2)

# Build the rotation matrix around the center, 45 degrees clockwise,
# without changing the scale
# cv2.warpAffine applies the transformation
angleToRotate = -20
M = cv2.getRotationMatrix2D(center, angleToRotate, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("Rotated by 45 Degrees", rotated)
# cv2.waitKey(0)

plt.imshow(rotated)
plt.show()


