# importing the necessary packages
import re
import cv2
import pytesseract

#this functions take the back image of the ID card and returns a string of all the text information in the image
def textExtractorback_jpg():
    img = cv2.imread('back.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    string = (pytesseract.image_to_string(gray))

    return string

#this functions uses a regex to find the Expiry date in the string returned from the textExtractorback_jpg function and returns the Expiry
def Expiry_ExtractorFromString():

    #getting the string of text from the image
    string = textExtractorback_jpg()

    #converting this string into an array by splitting it with the space
    store_array = string.split()

    # print(store_array)
    # we do an element wise search to find which element in the array matches with regex of a DOB, it should be in the dd-mm-yyyy format
    for element in store_array:

        m = re.match("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$", element)

        # See if success.

        # this automatically selects the later date which is the expiry date
        # there are two dates on the back of the ID card, the first one is date of issue, as the algorithm runs left to right, it overwrites the date of issue
        if m:
            # print(element)
            expiry = element

        else:
            # print("No DOB found!")
            pass

    return expiry


if __name__ == '__main__':
    print(Expiry_ExtractorFromString())
