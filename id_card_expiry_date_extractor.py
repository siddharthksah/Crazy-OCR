"""
Filename: id_card_expiry_date_extractor.py

This script extracts the expiry date from the back image of an ID card. The image
is converted to grayscale and optical character recognition (OCR) is used to extract
all the text information. Then, a regular expression (regex) is used to find the 
expiry date in the format dd-mm-yyyy.

Author: Siddharth Kumar (www.siddharthsah.com)
Last Updated: July 28, 2023
"""

import re
import cv2
import pytesseract

def text_extractor_back_jpg(image_path):
    """
    Reads an image, converts it to grayscale, and extracts all text information.

    Args:
        image_path: Path to the image file.

    Returns:
        A string containing all the text information in the image.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image couldn't be read, check the path: {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray)


def expiry_extractor_from_string(text):
    """
    Uses a regex to find the expiry date in the extracted text.

    Args:
        text: A string of text extracted from an image.

    Returns:
        The expiry date found in the text.
    """
    # Split the text into an array of words
    words = text.split()

    # Search for the expiry date in the array of words
    for word in words:
        match = re.match("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$", word)
        if match:
            return word  # Return the expiry date

    # If no expiry date was found, return None
    return None


def main():
    """
    Main function that reads the back image of an ID card, extracts the text, 
    and finds the expiry date.
    """
    image_path = 'back.jpg'
    text = text_extractor_back_jpg(image_path)
    expiry_date = expiry_extractor_from_string(text)

    if expiry_date:
        print(f"Expiry date found: {expiry_date}")
    else:
        print("No expiry date found in the ID card image.")


if __name__ == '__main__':
    main()
