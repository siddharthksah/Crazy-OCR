"""
This module processes an image and crops the area of interest. 
It uses image processing techniques such as edge and contour detection.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    Function to resize an image while keeping the aspect ratio intact.

    :param image: np.array, Original Image
    :param width: int, Width that the image is resized to
    :param height: int, Height that the image is resized to
    :param inter: cv2 interpolation method, Default is cv2.INTER_AREA
    :return: np.array, Resized image
    """
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized


def process_image(img):
    """
    Process image to detect the contour of interest.

    :param img: np.array, Original Image
    :return: np.array, Image with the contour of interest cropped.
    """
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurr = cv2.GaussianBlur(grey, (5,5),0)
    edge = cv2.Canny(blurr, 0, 50)

    contours, _ = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for i in contours:
        elip =  cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i,0.08*elip, True)

        if len(approx) == 4 :
            doc = approx
            break

    cv2.drawContours(img, [doc], -1, (0, 255, 0), 2)

    return doc, img


def reshape_and_transform(doc, img):
    """
    Reshaping and transforming the image based on contours.

    :param doc: np.array, Contour
    :param img: np.array, Image
    :return: np.array, Reshaped and Transformed Image
    """
    doc=doc.reshape((4,2))
    new_doc = np.zeros((4,2), dtype="float32")

    Sum = doc.sum(axis = 1)
    new_doc[0] = doc[np.argmin(Sum)]
    new_doc[2] = doc[np.argmax(Sum)]

    Diff = np.diff(doc, axis=1)
    new_doc[1] = doc[np.argmin(Diff)]
    new_doc[3] = doc[np.argmax(Diff)]

    (tl,tr,br,bl) = new_doc
    dist1 = np.linalg.norm(br-bl)
    dist2 = np.linalg.norm(tr-tl)
    maxLen = max(int(dist1),int(dist2))
    dist3 = np.linalg.norm(tr-br)
    dist4 = np.linalg.norm(tl-bl)
    maxHeight = max(int(dist3), int(dist4))

    dst = np.array([[0,0],[maxLen-1, 0],[maxLen-1, maxHeight-1], [0, maxHeight-1]], dtype="float32")
    N = cv2.getPerspectiveTransform(new_doc, dst)
    warp = cv2.warpPerspective(img, N, (maxLen, maxHeight))
    img2 = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)

    return img2


def crop_image(image_path, output_path):
    """
    Main function to crop an image.

    :param image_path: str, Path to the image to be cropped
    :param output_path: str, Path to save the cropped image
    """
    try:
        img = cv2.imread(image_path)
    except Exception as e:
        print(f"Error: Unable to read image file: {image_path}. Exception: {str(e)}")
        return

    img = image_resize(img, width=600)
    doc, img = process_image(img)
    img2 = reshape_and_transform(doc, img)

    try:
        cv2.imwrite(output_path, img2)
        print(f"Image Saved at {output_path}")
    except Exception as e:
        print(f"Error: Unable to save image file: {output_path}. Exception: {str(e)}")
        return


if __name__ == "__main__":
    input_path = "./data/output/File 1.jpg"
    output_path_front = './data/temp/front_cropped.png'
    crop_image(input_path, output_path_front)
