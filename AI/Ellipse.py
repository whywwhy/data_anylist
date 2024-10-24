import cv2
import numpy as np
def ellipse():
    img = np.zeros((512, 512, 3), np.uint8)
    img.fill(0)
    img = cv2.ellipse(img, (156, 200), (100, 100), 0, 30, 330, (0, 255, 255), -1)
    img = cv2.circle(img, (300, 200), 10, (0, 0, 255), -1)
    img = cv2.circle(img, (350, 200), 10, (0, 255, 0), -1)
    img = cv2.circle(img, (400, 200), 10, (255, 0, 0), -1)
    img = cv2.putText(img, 'PAC-MAN', (135, 400), cv2.FONT_HERSHEY_PLAIN, 3, (0, 180, 256), 5)
    cv2.imshow('JetsonNano_Ellipse', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

ellipse()