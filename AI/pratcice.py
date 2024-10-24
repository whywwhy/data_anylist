import cv2
import numpy as np 

def ddd():
    img = cv2.imread('star.png', cv2.IMREAD_COLOR) 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, threshhold = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    erosion = cv2.erode(threshhold, kernel, iterations=2)
    dilation = cv2.dilate(erosion, kernel, iterations=2) 

    minusthresh = cv2.absdiff(threshhold, dilation)

    contours, hierachy = cv2.findContours(threshhold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    cv2.imshow('img', img) 
    cv2.imshow('img_gray', img_gray)
    cv2.imshow('threshhold', threshhold)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows() 

ddd()