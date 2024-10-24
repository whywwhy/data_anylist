import cv2
import numpy as np
def image_contours():
    img = cv2.imread('shape.png')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, img_thresh = cv2.threshold(img_gray,230,255,0)
    contours, hierachy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img_contours = img.copy()
    img_contours = cv2.drawContours(img_contours, contours, -1, (51,102,255), 4)

    cv2.imshow('JetsonNano_Contours_Original', img)
    cv2.imshow('JetsonNano_Contours_Gray', img_gray)
    cv2.imshow('JetsonNano_Contours_Thresh', img_thresh)
    cv2.imshow('JetsonNano_Contours', img_contours)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_contours()