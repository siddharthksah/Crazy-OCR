# THIS CODE CONVERTS THE FIRST PAGE 0F A PDF FILE TO JPG/PNG IMAGE
#importing the necessary packages
from poppler import load_from_file, PageRenderer
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt

#path of the file goes here
pdf_document = load_from_file("./data/front.pdf")
#extracting the first page from the PDF file
page_1 = pdf_document.create_page(0)

#creatigng the rendering object and rendering the PDF page to an image object
renderer = PageRenderer()
image = renderer.render_page(page_1)

#converting the image to a numpy array
a = np.array(image.memoryview(), copy=False)

#converting the numpy array to image object and the uint8 data type contains all whole numbers from 0 to 255
im1 = Image.fromarray((a).astype(np.uint8))

#converting the image from RGBA to RGB colorspace
im1 = im1.convert('RGB')

#converting the color space from BGR to RGB
b, g, r = im1.split()
im1 = Image.merge("RGB", (r, g, b))

#saving the image in either jpg or png format in the root directory
im1.save('./data/PDF2JPG_front.jpg')
#im1.save('PDF2PNG.png')
print("Image exported successfully...")

img = cv2.imread('./data/PDF2JPG_front.jpg')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img)
plt.show()





