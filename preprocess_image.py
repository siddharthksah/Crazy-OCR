from PIL import Image
import cv2
import pytesseract
import matplotlib.pyplot as plt

#read the image
image = cv2.imread('./data/back.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

gray = cv2.medianBlur(gray, 3)

text = pytesseract.image_to_string(gray)

print(text)

#show image
plt.imshow(gray)
plt.show()

