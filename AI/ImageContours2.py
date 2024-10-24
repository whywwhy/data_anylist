import cv2
import numpy as np 

def ddddd():
    img = cv2.imread('d (1).png', cv2.IMREAD_COLOR) 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, threshhold = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    erosion = cv2.erode(threshhold, kernel, iterations=2)
    dilation = cv2.dilate(erosion, kernel, iterations=2) 

    minusthresh = cv2.absdiff(threshhold, dilation)

    contours, hierachy = cv2.findContours(threshhold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    
    ddd = cv2.absdiff(threshhold, dilation)

    contours, hierachy = cv2.findContours(ddd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img_contours = img.copy()
    img_contours = cv2.drawContours(img_contours, contours, -1, (51,160,255), 4)
    img_bounding_box = img.copy()
    # for contours in contours:
    #     x, y, w, h = cv2.boundingRect(contours)
    #     bounding_rect = cv2.rectangle(img_bounding_box, (x, y), (x+w, y+h), (0, 0, 255), 1)
        

    for i in range(len(contours)):
        x1, y1, w1, h1 = cv2.boundingRect(contours[i])
        bounding_rect = cv2.rectangle(img_bounding_box, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 1)
        bounding_rect = cv2.putText(bounding_rect, f"{cv2.contourArea(contours[i])}", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)


    cv2.imshow('img', img) 
    cv2.imshow('img_gray', img_gray)
    cv2.imshow('threshhold', threshhold)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('wow', minusthresh)
    cv2.imshow('contour', img_contours)
    cv2.imshow('bounding_rect', bounding_rect)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
ddddd() 