import cv2
import numpy as np
def circle():
    img = np.zeros((512, 512, 3), np.uint8)
    img.fill(0)
    img = cv2.circle(img, (300, 300), 100, (0, 255, 255), 3)
    img = cv2.circle(img, (200, 300), 130, (0, 0, 255), 7)
    img = cv2.circle(img, (400, 300), 80, (255, 0, 0), -1)
    cv2.imshow('JetsonNano_Circle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

circle()