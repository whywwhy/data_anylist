import cv2
import numpy as np
def rectangle():
    img = np.zeros((512, 512, 3), np.uint8)

    img.fill(0)
    img = cv2.rectangle(img, (300, 300), (500, 500), (255, 0, 0), cv2.FILLED)
    img = cv2.rectangle(img, (20, 20), (300, 300), (0, 0, 255), cv2.FILLED)

    cv2.imshow('JetsonNano_Rectangle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
rectangle()