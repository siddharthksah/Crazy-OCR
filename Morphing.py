import cv2 as cv
from itertools import cycle
from common import draw_str
from PIL import Image
import numpy as np
import os

#read more about morphing here https://northstar-www.dartmouth.edu/doc/idl/html_6.2/Morphing.html

# image_path = './data/front.jpg'
#
# image = Image.open(image_path)
# image = np.array(image)

fn = './data/front.jpg'
image = cv.imread(fn)

modes = ['erode/dilate', 'open/close', 'blackhat/tophat', 'gradient']
str_modes = ['ellipse', 'rect', 'cross']

# modes = ['erode']
#
# str_modes = ['ellipse']

# cur_mode = next(modes)
# print(cur_mode)
# cur_str_mode = next(str_modes)
# print(cur_str_mode)


def update(dummy=None):

    count = 0

    for cur_mode in modes:
        for cur_str_mode in str_modes:
            for i in range(12, 20):
                sz = i
                for j in range(1, 10):
                    iters = j
                    count = count + 1
                    opers = cur_mode.split('/')
                    #print(opers)
                    if len(opers) > 1:
                        sz = sz - 10
                        op = opers[sz > 0]
                        sz = abs(sz)
                    else:
                        op = opers[0]
                    sz = sz * 2 + 1
                    #print(sz)
                    str_name = 'MORPH_' + cur_str_mode.upper()
                    oper_name = 'MORPH_' + op.upper()
                    st = cv.getStructuringElement(getattr(cv, str_name), (sz, sz))
                    res = cv.morphologyEx(image, getattr(cv, oper_name), st, iterations=iters)

                    draw_str(res, (10, 20), 'mode: ' + cur_mode)
                    draw_str(res, (10, 40), 'operation: ' + oper_name)
                    draw_str(res, (10, 60), 'structure: ' + str_name)
                    draw_str(res, (10, 80), 'ksize: %d  iters: %d' % (sz, iters))

                    cv.imwrite("./output_try/" + "frame%d.jpg" % count, res)
                    print(count)

                    # dirname = "{}_{}_{}_{}_{}".format(sz, iters, cur_mode, oper_name, str_name)
                    #
                    # root = os.getcwd()  # or whatever root folder you want
                    # dirpath = os.path.join(root, "output", dirname)
                    #
                    # # print(dirpath)
                    #
                    # cv.imwrite(dirpath + '.jpg', res)
                    # print('Saved')


update()
print("Done, all images saved!")