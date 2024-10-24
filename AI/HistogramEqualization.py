import cv2
import numpy as np
from matplotlib import pyplot as plt
def histogram_equlization():
    img = cv2.imread('cat.png',0)
    eqhist = cv2.equalizeHist(img)

    hist1 = cv2.calcHist([img],[0],None, [256],[0,256])
    hist2 = cv2.calcHist([eqhist],[0],None, [256],[0,256])

    fig = plt.figure()
    # fig.canvas.set_window_title('JetsonNano_Histogram_Equlization')

    plt.subplot(221), plt.imshow(img, 'gray')
              
    plt.subplot(222), plt.imshow(eqhist, 'gray')
    plt.title('Histogram Equlization'), plt.xticks([]), plt.yticks([])
              
    plt.subplot(223), plt.plot(hist1), plt.xlim([0,256])
    plt.subplot(224), plt.plot(hist2), plt.xlim([0,256])

    plt.show()

histogram_equlization()