# ocr_image_processing.py

"""
This script reads an image, applies pre-processing steps for Optical Character Recognition (OCR),
extracts text from the processed image using Tesseract and displays the processed image.
"""

# Import necessary libraries
import cv2
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt


def image_preprocessing(image_path):
    """
    Pre-process an image for OCR using Tesseract.
    
    Parameters:
    image_path (str): Path to the image file.

    Returns:
    image_gray (OpenCV Mat): Thresholded and blurred grayscale image.
    """
    try:
        # Load image
        image = cv2.imread(image_path)

        # Convert image to grayscale
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding for binarization
        image_gray = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Apply median blur to reduce noise
        image_gray = cv2.medianBlur(image_gray, 3)

        return image_gray
    except Exception as e:
        print(f"Error in processing the image: {e}")
        return None


def extract_text_from_image(image):
    """
    Extract text from a given image using Tesseract.
    
    Parameters:
    image (OpenCV Mat): Image to extract text from.

    Returns:
    text (str): Extracted text.
    """
    try:
        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error in extracting text from image: {e}")
        return None


def display_image(image, title):
    """
    Display an image using matplotlib.

    Parameters:
    image (OpenCV Mat): Image to display.
    title (str): Title for the image window.
    """
    try:
        plt.imshow(image, cmap='gray')
        plt.title(title)
        plt.show()
    except Exception as e:
        print(f"Error in displaying the image: {e}")


if __name__ == "__main__":
    # Define image path
    img_path = './data/back.jpg'
    
    # Preprocess image
    processed_img = image_preprocessing(img_path)
    
    # Check if image processing was successful
    if processed_img is not None:
        # Extract text
        extracted_text = extract_text_from_image(processed_img)
        
        # Check if text extraction was successful
        if extracted_text is not None:
            print(f"Extracted Text: \n{extracted_text}")
            
            # Display image
            display_image(processed_img, 'Processed Image')
        else:
            print("Text Extraction Failed.")
    else:
        print("Image Processing Failed.")
