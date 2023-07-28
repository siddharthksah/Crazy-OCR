# id_card_data_extraction.py

import os
import re
from typing import Tuple, List

import cv2
import numpy as np
import pandas as pd
import pytesseract
from PIL import Image, ImageOps
from deskew import determine_skew
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import rotate

# Global constants
DIRECTORY = './Deskewed Cropped/'
OUTPUT_CSV = "./Deskewed Cropped/result_Deskewed_Cropped_Rotated_100to100.csv"
IMG_DIM = (1024, 768)
PYTESSERACT_CONFIG = '-l eng --oem 3 --psm 6'


def preprocess_image(image_location: str) -> np.array:
    """
    Preprocess the image to be ready for tesseract

    :param image_location: Path to the image file
    :return: Processed image as a numpy array
    """
    img = Image.open(image_location).convert("RGB")
    image = ImageOps.exif_transpose(img)
    img = np.array(image)
    img = cv2.resize(img, IMG_DIM)
    return img


def text_extractor(image_location: str) -> str:
    """
    Extract the text from an image

    :param image_location: Path to the image file
    :return: Extracted text as a string
    """
    img = preprocess_image(image_location)
    string = pytesseract.image_to_string(img, config=PYTESSERACT_CONFIG)
    return string


def fin_extractor(image_location: str) -> str:
    """
    Extract the FIN from the text extracted from the image

    :param image_location: Path to the image file
    :return: Extracted FIN as a string
    """
    string = text_extractor(image_location)
    store_array = string.split()

    for element in store_array:
        if re.match("^[STFG]\d{7}[A-Z]$", element):
            return element

    return "None"


def rotate_image(image: np.array, angle: float) -> np.array:
    """
    Rotate the image

    :param image: Image as a numpy array
    :param angle: Angle to rotate the image
    :return: Rotated image as a numpy array
    """
    img_height, img_width = image.shape[:2]
    centre_y, centre_x = img_height // 2, img_width // 2
    rotation_matrix = cv2.getRotationMatrix2D((centre_y, centre_x), angle, 1.0)
    cos_val = np.abs(rotation_matrix[0][0])
    sin_val = np.abs(rotation_matrix[0][1])

    new_image_height = int((img_height * sin_val) + (img_width * cos_val))
    new_image_width = int((img_height * cos_val) + (img_width * sin_val))

    rotation_matrix[0][2] += (new_image_width / 2) - centre_x
    rotation_matrix[1][2] += (new_image_height / 2) - centre_y

    rotating_image = cv2.warpAffine(image, rotation_matrix, (new_image_width, new_image_height))
    return rotating_image


def process_images() -> Tuple[np.array, np.array, np.array]:
    """
    Process all images in a directory

    :return: Filenames, FINs, and correctness as numpy arrays
    """
    filenames = []
    fins = []
    is_fin_correct = []

    for filename in os.listdir(DIRECTORY):
        if filename.endswith(".jpg"):
            image_path = os.path.join(DIRECTORY, filename)
            image = cv2.imread(image_path)
            for i in range(-100, 100):
                rotated = rotate_image(image, i)
                temp_path = f'./Deskewed Cropped/temp/rotated_{i}.jpg'
                cv2.imwrite(temp_path, rotated)

                fin = fin_extractor(temp_path)
                if fin == "":
                    break

            is_fin_correct.append('1' if fin == '' else '0')
            filenames.append(filename)
            fins.append(fin)

    return np.array(filenames), np.array(fins), np.array(is_fin_correct)


def main():
    try:
        filenames, fins, is_fin_correct = process_images()
        df = pd.DataFrame({"Filename": filenames, "FIN": fins, "Correct FIN?": is_fin_correct})
        df.to_csv(OUTPUT_CSV, index=False)
        print('Done!')

    except Exception as e:
        print(f"Error encountered: {str(e)}")
        raise e


if __name__ == '__main__':
    main()
