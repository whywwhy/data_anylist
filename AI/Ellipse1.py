import cv2
import numpy as np
def ellipse():
    img = np.zeros((512, 512, 3), np.uint8)
    img.fill(0)
    img = cv2.ellipse(img, (200, 256), (50, 100),130, 90, 360, (0, 255, 255), -1)
    img = cv2.ellipse(img, (300, 100), (50, 100), 45, 0, 270, (0, 0, 255), -1)
    cv2.imshow('JetsonNano_Ellipse', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

ellipse()