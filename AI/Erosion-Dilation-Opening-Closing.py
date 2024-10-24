import cv2
import numpy as np
from matplotlib import pyplot as plt

def morphological_transformations():
    original = cv2.imread('d (1).png', cv2.IMREAD_GRAYSCALE)
    dot = cv2.imread('d (1).png', cv2.IMREAD_GRAYSCALE)
    hole = cv2.imread('h.png', cv2.IMREAD_GRAYSCALE)
    
    ret_o, th_o = cv2.threshold(original, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret_d, th_d = cv2.threshold(dot, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret_h, th_h = cv2.threshold(hole, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    
    dilationHole = cv2.dilate(th_h, kernel, iterations = 1)
    erosionHole = cv2.erode(dilationHole, kernel, iterations = 1)
    
    erosionDot = cv2.erode(th_d, kernel, iterations = 1)
    dilationDot = cv2.dilate(erosionDot, kernel, iterations = 1)
    
    images = [th_h, dilationHole, erosionHole, th_d, erosionDot, dilationDot]
    titles = ['h.png', 'dilationH', 'erosionH', 'd.png', 'erosionDot', 'dilationDot']
    
    fig = plt.figure()
    for i in range(6):
        plt.subplot(2, 3, i+1), plt.imshow(images[i],'gray'), plt.title(titles[i]), plt.xticks([]), plt.yticks([])
    
    # erosion = cv2.erode(th_o, kernel, iterations = 1)
    # dilation = cv2.dilate(th_h, kernel, iterations = 1)
    # opening = cv2.morphologyEx(th_d, cv2.MORPH_OPEN, kernel)
    # closing = cv2.morphologyEx(th_h, cv2.MORPH_CLOSE, kernel)
    # gradient = cv2.morphologyEx(th_o, cv2.MORPH_GRADIENT, kernel)
    # tophat = cv2.morphologyEx(th_o, cv2.MORPH_TOPHAT, kernel)
    # blackhat = cv2.morphologyEx(th_o, cv2.MORPH_BLACKHAT, kernel)
    
    # images = [th_d, erosion, opening, th_h, dilation, closing, gradient, tophat, blackhat]
    # titles = ['Dot Image', 'Erosion', 'Opening', 'Hole Image', 'Dilation', 'Closing', 'Gradient', 'Tophat', 'Blackhot']
    # fig = plt.figure()
    
    # for i in range(9):
    #     plt.subplot(3,3,i+1), plt.imshow(images[i],'gray'), plt.title(titles[i]), plt.xticks([]), plt.yticks([])
        
    plt.show()

morphological_transformations()