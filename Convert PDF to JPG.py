"""
Module to convert the first page of a PDF file to a JPG/PNG image.
"""

from poppler import load_from_file, PageRenderer
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt


def load_pdf(file_path):
    """
    Load the PDF file from the provided path.

    :param file_path: str, Path to the PDF file.
    :return: PDF document object
    """
    pdf_document = load_from_file(file_path)
    return pdf_document


def extract_page(pdf_document, page_num=0):
    """
    Extract the specified page from the PDF document.

    :param pdf_document: PDF document object.
    :param page_num: int, Page number to be extracted. Default is 0.
    :return: Page object
    """
    return pdf_document.create_page(page_num)


def render_page(page):
    """
    Render the specified PDF page as an image object.

    :param page: Page object.
    :return: Image object
    """
    renderer = PageRenderer()
    return renderer.render_page(page)


def convert_image_to_array(image):
    """
    Convert the image object to a numpy array.

    :param image: Image object.
    :return: ndarray, numpy array representation of the image.
    """
    return np.array(image.memoryview(), copy=False)


def convert_to_rgb(image_array):
    """
    Convert image from RGBA to RGB colorspace.

    :param image_array: ndarray, numpy array representation of the image.
    :return: Image object in RGB colorspace.
    """
    image = Image.fromarray((image_array).astype(np.uint8))
    image_rgb = image.convert('RGB')
    return image_rgb


def save_image(image, path):
    """
    Save the image to the specified path.

    :param image: Image object.
    :param path: str, Path to save the image.
    """
    image.save(path)
    print("Image exported successfully...")


def display_image(path):
    """
    Display the image using matplotlib.

    :param path: str, Path to the image file.
    """
    img = cv2.imread(path)
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    file_path = "./data/front.pdf"
    output_path = './data/PDF2JPG_front.jpg'

    pdf_doc = load_pdf(file_path)
    page = extract_page(pdf_doc)
    image = render_page(page)
    image_array = convert_image_to_array(image)
    image_rgb = convert_to_rgb(image_array)
    save_image(image_rgb, output_path)
    display_image(output_path)
