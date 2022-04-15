import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import rotate
import cv2
# importing the necessary packages
import os
import re
import cv2
import pytesseract
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import pandas as pd

from deskew import determine_skew


# this functions take the front image of the ID card and returns a string of all the text information in the image
def textExtractorfront_jpg(image_location):
    # you can use both jpg and png file formats here
    #img = cv2.imread(image_location)

    img = Image.open(image_location).convert("RGB")

    image = ImageOps.exif_transpose(img)

    img = np.array(image)

    # plt.imshow(img)
    # plt.show()

    # img = Image.open('./Original Images/File91.jpg')

    img = cv2.resize(img, (1024, 768))

    # def rotate(image, center=None, scale=1.0):
    #     angle = 360 - int(re.search('(?<=Rotate: )\d+', pytesseract.image_to_osd(image)).group(0))
    #     (h, w) = image.shape[:2]
    #
    #     if center is None:
    #         center = (w / 2, h / 2)
    #
    #     # Perform the rotation
    #     M = cv2.getRotationMatrix2D(center, angle, scale)
    #     rotated = cv2.warpAffine(image, M, (w, h))
    #
    #     return rotated
    #
    # img = rotate(img)

    # rot_data = pytesseract.image_to_osd(img, );
    # print("[OSD] " + rot_data)
    # rot = re.search('(?<=Rotate: )\d+', rot_data).group(0)
    #
    # angle = float(rot)
    # if angle > 0:
    #     angle = 360 - angle
    # print("[ANGLE] " + str(angle))
    #
    # (h, w) = img.shape[:2]
    # center = (w // 2, h // 2)
    # M = cv2.getRotationMatrix2D(center, angle, 1.0)
    # img = cv2.warpAffine(img, M, (w, h),
    #                          flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    #print(pytesseract.image_to_osd(img, config='--psm 0'))



    # plt.imshow(img)
    # plt.show()

    #img = cv2.imread('front.jpg')


    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #config = ('-l eng --oem 1 --psm 3')

    #string = (pytesseract.image_to_string(img, config= config))
    # string = (pytesseract.image_to_string(img))

    config = '-l eng --oem 3 --psm 6'

    string = (pytesseract.image_to_string(img, config=config))


    #print(string)

    return string


# this functions uses a regex to find the FIN  in the string returned from the textExtractorfront_jpg function and returns the FIN
def FIN_ExtractorFromString(image_location):

    FIN = "None"
    # getting the string of text from the image
    string = textExtractorfront_jpg(image_location)
    #print(string)

    # converting this string into an array by splitting it with the space
    store_array = string.split()

    # we do an element wise search to find which element in the array matches with regex of a FIN, this regex will work for both local and foreigner FIN
    for element in store_array:

        m = re.match("^[STFG]\d{7}[A-Z]$", element)

        # See if success.
        if m:
            # print(element)
            FIN = element

        else:
            pass
            # print("No FIN found!")

    return FIN


def rotation(rotateImage, angle):
    # Taking image height and width
    imgHeight, imgWidth = rotateImage.shape[0], rotateImage.shape[1]

    # Computing the centre x,y coordinates
    # of an image
    centreY, centreX = imgHeight // 2, imgWidth // 2

    # Computing 2D rotation Matrix to rotate an image
    rotationMatrix = cv2.getRotationMatrix2D((centreY, centreX), angle, 1.0)

    # Now will take out sin and cos values from rotationMatrix
    # Also used numpy absolute function to make positive value
    cosofRotationMatrix = np.abs(rotationMatrix[0][0])
    sinofRotationMatrix = np.abs(rotationMatrix[0][1])

    # Now will compute new height & width of
    # an image so that we can use it in
    # warpAffine function to prevent cropping of image sides
    newImageHeight = int((imgHeight * sinofRotationMatrix) +
                         (imgWidth * cosofRotationMatrix))
    newImageWidth = int((imgHeight * cosofRotationMatrix) +
                        (imgWidth * sinofRotationMatrix))

    # After computing the new height & width of an image
    # we also need to update the values of rotation matrix
    rotationMatrix[0][2] += (newImageWidth / 2) - centreX
    rotationMatrix[1][2] += (newImageHeight / 2) - centreY

    # Now, we will perform actual image rotation
    rotatingimage = cv2.warpAffine(
        rotateImage, rotationMatrix, (newImageWidth, newImageHeight))

    return rotatingimage


# filename = 'File 1.jpg'
#
# image = io.imread('./data/output/' + filename)
# grayscale = rgb2gray(image)
# angle = determine_skew(grayscale)
# rotated = rotate(image, angle, resize=True) * 255
# height, width = rotated.shape[:2]
# # print(height)
# # print(width)
# if width > height:
#     io.imsave('./data/output/deskewed/temp/' + filename, rotated.astype(np.uint8))
#     image = rotated
# else:
#     image = cv2.rotate(rotated, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
#     io.imsave('./data/output/deskewed/temp/' + filename, image.astype(np.uint8))
# #print('Done!')

directory = './Deskewed Cropped/'

# #array = []
# filenameArray = []
# FINArray = []
# IsFINCorrect = []

# for filename in os.listdir(directory):
#
#     if filename.endswith(".jpg"):
#         #do smth

        #print(filename)

        #image = cv2.imread(directory + filename)
        # import numpy as np
        # import argparse
        # import imutils
        # import cv2
        # import matplotlib.pyplot as plt

        # Load and display original image
image = cv2.imread(directory + 'File1.jpg')

# Determine the center of the image
# OpenCV allows you to specify any arbitrary point to rotate around,
# here we'll use the image center

loopBreak = 0

for i in range(-20, 20):

    if loopBreak < 2:

        rotated = rotation(image, i)

        # (h, w) = image.shape[:2]
        # center = (w // 2, h // 2)
        #
        # # Build the rotation matrix around the center, 45 degrees clockwise,
        # # without changing the scale
        # # cv2.warpAffine applies the transformation
        # #print(i)
        # angleToRotate = i
        # M = cv2.getRotationMatrix2D(center, angleToRotate, 1.0)
        # rotated = cv2.warpAffine(image, M, (w, h))
        # cv2.imshow("Rotated by 45 Degrees", rotated)
        # cv2.waitKey(0)

        # plt.imshow(rotated)
        # plt.show()

        #image = rotated
        image_location = './Deskewed Cropped/temp/'+ 'rotated_' + str(i) + '.jpg'
        print(image_location)
        cv2.imwrite('./Deskewed Cropped/temp/'+ 'rotated_' + str(i) + '.jpg', rotated)

        FIN = FIN_ExtractorFromString(image_location)
        print(FIN)

        #sometimes we get FIN but '' instead of, keep turning the image 2 more degrees solves this program
        if FIN != "None":
            loopBreak = loopBreak + 1

    # if (FIN == ""):
    #     break

# if FIN == '':
#     IsFINCorrect.append('1')
# else:
#     IsFINCorrect.append('0')
#
# filenameArray.append(filename)
# FINArray.append(FIN)

print(FIN)







# if __name__ == '__main__':
#     print(FIN_ExtractorFromString())



#array = np.array(array)
# filenameArray = np.array(filenameArray)
# FINArray = np.array(FINArray)
# IsFINCorrect = np.array(IsFINCorrect)
#
# df = pd.DataFrame({"Filename" : filenameArray, "FIN": FINArray, "Correct FIN?": IsFINCorrect})
# df.to_csv("./Deskewed Cropped/result_Deskewed_Cropped_Rotated.csv", index=False)
# print('Done!')