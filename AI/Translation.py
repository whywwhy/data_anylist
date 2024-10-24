import cv2
import numpy as np
def image_translation():
    img = cv2.imread('gangbao.png', cv2.IMREAD_COLOR)
    img = cv2.rectangle(img, (100, 255), (40, 60), (255, 255, 255), 1)
    rows, cols = img.shape[:2]

    M = np.float32([[1, 0, 40], [0, 1, 60]])
    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow('JetsonNano_Original', img)
    cv2.imshow('JetsonNano_Translation', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
image_translation()