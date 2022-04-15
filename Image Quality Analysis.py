import cv2
from PIL import Image
import numpy as np

#image = cv2.imread('./data/front.png')  # read the image


image_path = './data/front.png'


image = Image.open(image_path).convert("RGB")
image = np.array(image)

def blurriness(image):
    # converting the image into the grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # calculate laplacian of the image
    return cv2.Laplacian(image, cv2.CV_64F).var()

print(blurriness(image))

if blurriness(image) > 35:
    print("Not blurry")
else:
    print("Blurry")

