from PIL import Image
import os

#write the number of columns and rows you want in your collage
cols = 10
rows = 10

#define the ouput image size
width = 10240
height = 7680


thumbnail_width = width//cols
thumbnail_height = height//rows
size = thumbnail_width, thumbnail_height
new_im = Image.new('RGB', (width, height))
ims = []

#this is the directory from where all the images will be taken, please make sure your images are either .jpg or .png for it make
#basically all the images inside this folder will be used to create the collage
directory = './Deskewed Cropped/temp/'

for filename in os.listdir(directory):
    #if filename.endswith(".jpg" or ".png"):
    if filename.endswith(".jpg"):
        im = Image.open(directory + filename)
        im.thumbnail(size)
        ims.append(im)

i = 0
x = 0
y = 0
for col in range(cols):
    for row in range(rows):
        print(i, x, y)
        new_im.paste(ims[i], (x, y))
        i += 1
        y += thumbnail_height
    x += thumbnail_width
    y = 0

# the collage in this case will be saved in the root directory with the name 'collage.jpg'
new_im.save("./Deskewed Cropped/temp/collage.png")


