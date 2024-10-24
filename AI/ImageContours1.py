import cv2
import numpy as np

def image_contours():
    original = cv2.imread('d (1).png', cv2.IMREAD_GRAYSCALE)
    dot = cv2.imread('d (1).png', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('d (1).png') 
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, th_d = cv2.threshold(dot, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    ret, img_thresh = cv2.threshold(img_gray, 230, 255, 0)

    erosionDot = cv2.erode(th_d, kernel, iterations=2)
    dilationDot = cv2.dilate(erosionDot, kernel, iterations=2)

    a = cv2.absdiff(dilationDot, img_thresh)
    
    ddd = cv2.absdiff(th_d, dilationDot)

    contours, hierachy = cv2.findContours(ddd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img_contours = img.copy()
    img_contours = cv2.drawContours(img_contours, contours, -1, (51,102,255), 4)

    cv2.imshow('d (1).png', img_contours)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_contours()
