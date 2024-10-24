import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_binarization():
    img = cv2.imread('gangbao.png', cv2.IMREAD_GRAYSCALE)
    th = 150
    th_max = 255
    
    ret_1, thresh_1 = cv2.threshold(img, th, th_max, cv2.THRESH_BINARY)
    ret_2, thresh_2 = cv2.threshold(img, th, th_max, cv2.THRESH_BINARY_INV)
    ret_3, thresh_3 = cv2.threshold(img, th, th_max, cv2.THRESH_TRUNC)
    ret_4, thresh_4 = cv2.threshold(img, th, th_max, cv2.THRESH_TOZERO)
    ret_5, thresh_5 = cv2.threshold(img, th, th_max, cv2.THRESH_TOZERO_INV)
              
    titles = ['ORIGINAL', 'BINARY', "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
    images = [img, thresh_1, thresh_2, thresh_3, thresh_4, thresh_5]
    fig = plt.figure()
    # fig.canvas.set_window_title("JetsonNano_Thresholding")
    order = [0, 2, 4, 1, 3, 5]
    
    for i in range(6):
        plt.subplot(3, 2, order[i]+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
    
image_binarization()