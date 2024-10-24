import cv2
import numpy as np
def text():
    img = np.zeros((512, 512, 3), np.uint8)
    img.fill(255)
    img = cv2.rectangle(img, (300, 200), (0, 70), (0, 180, 256), 3)
    img = cv2.putText(img, 'Hello New World', (0, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 180, 256), 5)
    cv2.imshow('JetsonNano_PutText', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
text()