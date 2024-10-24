import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_rotation():
    img = cv2.imread('gary-img.png', cv2.IMREAD_COLOR)
    w, h, c = img.shape
    img = cv2.rectangle(img, (0, 0), (w-1, h-1), (255, 255, 255), 1)
    rows, cols = img.shape[:2]

    M = cv2.getRotationMatrix2D((cols/2, rows/2), 145, 0.5)
    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow('JetsonNano_Original', img)
    cv2.imshow('JetsonNano_Rotation', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_rotation() 