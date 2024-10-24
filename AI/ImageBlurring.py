import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_blurring():
    img = cv2.imread('gary-img.png', cv2.IMREAD_COLOR)
    b, g, r = cv2.split(img)
    img = cv2.merge([r, g, b])

    dst_1 = cv2.blur(img, (7, 7))
    dst_2 = cv2.GaussianBlur(img, (5, 5), 0)
    dst_3 = cv2.medianBlur(img, 9)
    dst_4 = cv2.bilateralFilter(img, 9, 75, 75)

    images = [img, dst_1, dst_2, dst_3, dst_4]
    titles = ['ORIGINAL', 'BLUR(7X7)', 'GAUSSIAN BLUR(5X5)', 'MEDIAN BLUR', 'BILATERAL']
              
    fig = plt.figure()
    # fig.canvas.set_window_title("JetsonNano_Blurring")
    for i in range(5):
        plt.subplot(3, 2, i+1), plt.imshow(images[i]), plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show() 

image_blurring()