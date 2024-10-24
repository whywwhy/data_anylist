import cv2
import numpy as np

def image_binary():
    img = cv2.imread('duck.png', cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    cv2.imshow("JetsonNano_Original", img)
    cv2.imshow("JetsonNano_Binary", dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_binary()