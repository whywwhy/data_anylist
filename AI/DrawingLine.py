# import cv2
# import numpy as np
# def line():
#     img = np.zeros((512, 512, 3), np.uint8)
#     img.fill(255)
#     img = cv2.line(img, (300, 0), (100, 511), (0, 255, 0), 5)
#     cv2.imshow('JetsonNano_Line', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows() 

# line()

import cv2
import numpy as np
def line():
    img = np.zeros((512, 512, 3), np.uint8)

    img.fill(0)
    img = cv2.line(img, (256, 0), (256, 511), (255, 0, 0), 10)
    img = cv2.line(img, (0, 256), (511, 256), (0, 0, 256), 5)

    cv2.imshow('JetsonNano_Line', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

line()
