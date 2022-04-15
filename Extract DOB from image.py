#importing the necessary packages
import re
import cv2
import pytesseract


#this functions take the front image of the ID card and returns a string of all the text information in the image
def textExtractorfront_jpg():
    img = cv2.imread('./output/5_1.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    string = (pytesseract.image_to_string(gray))

    return string


#this functions uses a regex to find the DOB in the string returned from the textExtractorfront_jpg function and returns the DOB
def DOB_ExtractorFromString():

    #getting the string of text from the image
    string = textExtractorfront_jpg()

    #converting this string into an array by splitting it with the space
    store_array = string.split()

    # we do an element wise search to find which element in the array matches with regex of a DOB, it should be in the dd-mm-yyyy format
    for element in store_array:

        m = re.match("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$", element)

        # See if success.
        if m:
            # print(element)
            DOB = element

        else:
            # print("No DOB found!")
            pass

    return DOB


if __name__ == '__main__':
    print(DOB_ExtractorFromString())
