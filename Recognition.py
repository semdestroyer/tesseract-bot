import numpy
import cv2
import pytesseract
import os
from PIL import Image


def findLetters(img):
    #nullpath = img
    img = cv2.imread(img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    preprocess = 'blur'
    if preprocess == 'thresh':
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif preprocess == 'blur':
       gray = cv2.medianBlur(gray, 3)
    filename = 'img/gray/{}.png'.format(os.getpid())
    cv2.imwrite(filename,gray)
    text = pytesseract.image_to_string(Image.open(filename),config='-l eng --oem 1 --psm 6')

    os.remove(filename)
    #os.remove(nullpath)
    return text

