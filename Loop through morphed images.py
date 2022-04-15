from PIL import Image
import cv2
import pytesseract
import matplotlib.pyplot as plt
import re
import pandas as pd
import numpy as np
import os
directory = './data/output/deskewed'

array = []
filenameArray = []
FINArray = []

for filename in os.listdir(directory):

    if filename.endswith(".jpg"):
        #do smth

        #print(filename)

        image = cv2.imread('./data/output/deskewed/' + filename)

        #print(image)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        gray = cv2.medianBlur(gray, 3)

        text = pytesseract.image_to_string(gray)

        FIN = "None"
        # getting the string of text from the image
        string = text
        # print(string)

        # converting this string into an array by splitting it with the space
        store_array = string.split()

        # we do an element wise search to find which element in the array matches with regex of a FIN, this regex will work for both local and foreigner FIN
        for element in store_array:

            m = re.match("^[STFG]\d{7}[A-Z]$", element)

            # See if success.
            if m:
                # print(element)
                FIN = element


            else:
                #FINArray.append("None")
                pass

                # print("No FIN found!")
        FINArray.append(FIN)



        filenameArray.append(filename)

        array.append(len(text))

        #print(text)
    else:
        pass

array = np.array(array)
filenameArray = np.array(filenameArray)
FINArray = np.array(FINArray)

df = pd.DataFrame({"Filename" : filenameArray, "Length of characters detected" : array, "FIN": FINArray})
df.to_csv("./data/output/deskewed/submission.csv", index=False)
print('Done!')
