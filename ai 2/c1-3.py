import cv2

def dataPreprocessing():
    q1_3image = 'img/q1-3.png'

    #3
    q1_3img = cv2.imread(q1_3image, cv2.IMREAD_COLOR)
    q1_3img = cv2.resize(q1_3img, (640, 480), interpolation=cv2.INTER_LINEAR)
    
    q1_3img_hsv = cv2.cvtColor(q1_3img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(q1_3img_hsv)
    q1_3img_blur = cv2.medianBlur(h, 3)

    cv2.imshow('q1-3img', q1_3img_blur)

    cv2.imwrite('R1-3.png', q1_3img_blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

dataPreprocessing()
