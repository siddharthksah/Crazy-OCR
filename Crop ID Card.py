# importing the necessary packages
import re
import cv2
import pytesseract
import matplotlib.pyplot as plt
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance



def crop_image(image, front_back):

    def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
        # initialize the dimensions of the image to be resized and
        # grab the image size
        dim = None
        (h, w) = image.shape[:2]

        # if both the width and height are None, then return the
        # original image
        if width is None and height is None:
            return image

        # check to see if the width is None
        if width is None:
            # calculate the ratio of the height and construct the
            # dimensions
            r = height / float(h)
            dim = (int(w * r), height)

        # otherwise, the height is None
        else:
            # calculate the ratio of the width and construct the
            # dimensions
            r = width / float(w)
            dim = (width, int(h * r))

        # resize the image
        resized = cv2.resize(image, dim, interpolation = inter)

        # return the resized image
        return resized

    img = image_resize(image, width = 600)

    #img = ImageEnhance.Sharpness(img)

    plt.imshow(img)
    plt.show()

    # sharpen_filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    # img = cv2.filter2D(img, -1, sharpen_filter)



    #convert image to grayscale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #blurr image to smooth
    blurr = cv2.GaussianBlur(grey, (5,5),0)



    #finding edges
    edge = cv2.Canny(blurr, 0, 50)

    plt.imshow(edge)
    plt.show()

    #apadtive threshold and canny gave similar final output
    #threshold = cv2.adaptiveThreshold(blurr ,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    #find contours in thresholded image and sort them according to decreasing area
    contours, _ = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse= True)

    #contour approximation
    for i in contours:
        elip =  cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i,0.08*elip, True)

        if len(approx) == 4 :
            doc = approx
            break

    #draw contours
    cv2.drawContours(img, [doc], -1, (0, 255, 0), 2)

    plt.imshow(img)
    plt.show()

    #reshape to avoid errors ahead
    doc=doc.reshape((4,2))

    #create a new array and initialize
    new_doc = np.zeros((4,2), dtype="float32")

    Sum = doc.sum(axis = 1)
    new_doc[0] = doc[np.argmin(Sum)]
    new_doc[2] = doc[np.argmax(Sum)]

    Diff = np.diff(doc, axis=1)
    new_doc[1] = doc[np.argmin(Diff)]
    new_doc[3] = doc[np.argmax(Diff)]

    (tl,tr,br,bl) = new_doc

    #find distance between points and get max
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
    # plt.imshow(img2)
    # plt.show()
    #img2 = cv2.resize(img2,(600,800))

    #cv2.imwrite("edge.jpg", edge)
    #cv2.imwrite("contour.jpg", img)
    #cv2.imwrite("Scanned.jpg", img2)

    # show all images
    # cv2.imshow("Original.jpg",img)
    # cv2.imshow("Grey.jpg",grey)
    # cv2.imshow("Gaussian_Blur.jpb",blurr)
    # cv2.imshow("Canny_Edge.jpg",edge)
    # #cv2.imshow("Threshold.jpg",threshold)
    # cv2.imshow("Contours.jpg", img)
    # cv2.imshow("Scanned.jpg", img2)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    plt.imshow(img2)
    plt.show()

    #cv2.imwrite('./data/temp/front_cropped.png', img2)
    #print('Image Saved in the temp directory!')

    if front_back == "front":
        cv2.imwrite('./data/temp/front_cropped.png', img2)
    elif front_back == "back":
        cv2.imwrite('./data/temp/back_cropped.png', img2)
    else:
        print("Pass right parameters in the crop function!")

#location of the input image


#img = Image.open("./data/front.png")

img = cv2.imread("./data/output/File 1.jpg")
crop_image(img, 'front')