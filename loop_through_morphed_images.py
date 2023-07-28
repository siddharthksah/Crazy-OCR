"""
This is an open-source Python script for processing text from images using pytesseract. 
The script reads images, extracts text, detects a specific pattern in the text and 
compiles the results into a Pandas DataFrame which is then exported as a CSV file.

Author: Siddharth Kumar (www.siddharthsah.com)
Last Updated: July 28, 2023
"""

import cv2
import os
import re
import numpy as np
import pandas as pd
import pytesseract
from PIL import Image

def process_image(filename):
    """
    Processes an image to extract text and a specific pattern.

    Args:
        filename (str): The filename of the image to process.

    Returns:
        tuple: A tuple containing the filename, length of characters detected, and 
               the specific pattern detected (if any).
    """
    image = cv2.imread(f'./data/output/deskewed/{filename}')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)

    text = pytesseract.image_to_string(gray)

    # Detecting specific pattern in text
    fin = "None"
    for element in text.split():
        if re.match("^[STFG]\d{7}[A-Z]$", element):
            fin = element
            break

    return filename, len(text), fin

def compile_results(directory):
    """
    Processes all images in a given directory and compiles the results into a DataFrame.

    Args:
        directory (str): The directory containing the images to process.

    Returns:
        DataFrame: A DataFrame containing the results of the processing.
    """
    results = []
    
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            result = process_image(filename)
            results.append(result)
    
    df = pd.DataFrame(results, columns=["Filename", "Length of characters detected", "FIN"])
    
    return df

def main():
    """
    The main function to execute the image processing and result compilation.
    """
    directory = './data/output/deskewed'

    df = compile_results(directory)
    df.to_csv("./data/output/deskewed/submission.csv", index=False)
    print('Done!')

if __name__ == "__main__":
    main()
