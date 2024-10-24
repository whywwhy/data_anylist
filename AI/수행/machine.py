import cv2
import numpy as np  

def machine():
    img = cv2.imread('수행/img.png', cv2.IMREAD_COLOR) 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, threshhold = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    threshhold_color = cv2.cvtColor(threshhold, cv2.COLOR_GRAY2BGR)
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    cv2.imshow('img', img) 
    cv2.imshow('img_gray', img_gray) 
    cv2.imshow('threshhold', threshhold_color)

    cv2.imwrite('2.png', threshhold_color)

    cv2.waitKey(0)
    cv2.destroyAllWindows() 
machine()    