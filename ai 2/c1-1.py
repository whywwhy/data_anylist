import cv2

def dataPreprocessing():
    q1_1image = 'img/q1-1.png'

    # 1
    q1_1img = cv2.imread(q1_1image, cv2.IMREAD_COLOR)
    q1_1img = cv2.resize(q1_1img, (256, 256), interpolation=cv2.INTER_LINEAR)

    cv2.imshow('q1-1img', q1_1img)
    
    cv2.imwrite('R1-1.png', q1_1img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

dataPreprocessing()
