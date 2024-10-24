import cv2
import numpy as np

def dataPreprocessing():
    q1_4image = 'img/q1-4.png'

    #4
    q1_4img = cv2.imread(q1_4image, cv2.IMREAD_COLOR)
    q1_4img_resize = cv2.resize(q1_4img, (640, 480), interpolation=cv2.INTER_LINEAR)

    pts1 = np.float32([[468, 200], [540, 180], [470, 375], [540, 425]])
    pts2 = np.float32([[10, 10], [1000, 10], [10, 1000], [1000, 1000]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    q1_4img_warp = cv2.warpPerspective(q1_4img_resize, matrix, (1010, 1010))

    cv2.imshow('q1-4origin', q1_4img)
    cv2.imshow('q1-4img', q1_4img_warp)
    
    cv2.imwrite('R1-4.png', q1_4img_warp)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

dataPreprocessing()
