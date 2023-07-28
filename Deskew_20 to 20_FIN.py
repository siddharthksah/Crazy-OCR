import os
import re
import cv2
import numpy as np
import pandas as pd
import pytesseract
from PIL import Image, ImageOps
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import rotate
from deskew import determine_skew

class IDCardOCR:

    def __init__(self, directory):
        self.directory = directory

    @staticmethod
    def rotation(rotate_image, angle):
        """
        Rotates the image by a given angle

        Parameters:
        rotate_image (cv2 image): Original image
        angle (float): Angle to rotate image

        Returns:
        rotatingimage (cv2 image): Rotated image
        """

        img_height, img_width = rotate_image.shape[:2]
        center_y, center_x = img_height // 2, img_width // 2
        rotation_matrix = cv2.getRotationMatrix2D((center_y, center_x), angle, 1.0)
        cos_val = np.abs(rotation_matrix[0][0])
        sin_val = np.abs(rotation_matrix[0][1])
        new_img_height = int((img_height * sin_val) + (img_width * cos_val))
        new_img_width = int((img_height * cos_val) + (img_width * sin_val))
        rotation_matrix[0][2] += (new_img_width / 2) - center_x
        rotation_matrix[1][2] += (new_img_height / 2) - center_y
        rotated_image = cv2.warpAffine(rotate_image, rotation_matrix, (new_img_width, new_img_height))

        return rotated_image

    def text_extractor_front_jpg(self, image_location):
        """
        Extracts text from a given image

        Parameters:
        image_location (str): File path of the image

        Returns:
        string (str): Extracted text
        """

        try:
            img = Image.open(image_location).convert("RGB")
            image = ImageOps.exif_transpose(img)
            img = np.array(image)
            img = cv2.resize(img, (1024, 768))
            config = '-l eng --oem 3 --psm 6'
            string = pytesseract.image_to_string(img, config=config)
            return string
        except Exception as e:
            print(f"An error occurred while extracting text: {e}")
            return None

    def fin_extractor_from_string(self, image_location):
        """
        Extracts the FIN from the given image

        Parameters:
        image_location (str): File path of the image

        Returns:
        FIN (str): Extracted FIN
        """

        fin = "None"
        string = self.text_extractor_front_jpg(image_location)

        if string is not None:
            store_array = string.split()
            for element in store_array:
                if re.match("^[STFG]\d{7}[A-Z]$", element):
                    fin = element
                    break

        return fin

    def rotate_and_extract_fin(self):
        """
        Rotates the image and extracts FIN

        Returns:
        FIN (str): Extracted FIN
        """

        filename = 'File1.jpg'
        image = cv2.imread(self.directory + filename)

        loop_break = 0
        for i in range(-20, 20):
            if loop_break < 2:
                rotated = self.rotation(image, i)
                image_location = self.directory + 'temp/rotated_' + str(i) + '.jpg'
                cv2.imwrite(image_location, rotated)
                fin = self.fin_extractor_from_string(image_location)
                if fin != "None":
                    loop_break += 1
        return fin


if __name__ == '__main__':
    directory = './Deskewed Cropped/'
    id_card_ocr = IDCardOCR(directory)
    print(id_card_ocr.rotate_and_extract_fin())
