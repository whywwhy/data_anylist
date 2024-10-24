import cv2

def dataPreprocessing():
    q1_2image = 'img/q1-2.png'

    #2
    q1_2img = cv2.imread(q1_2image, cv2.IMREAD_COLOR)
    q1_2img = cv2.resize(q1_2img, (640, 480), interpolation=cv2.INTER_LINEAR)

    b, g, r = cv2.split(q1_2img)
    q1_2img_blur = cv2.blur(r, (9, 9))

    cv2.imshow('q1-2img', q1_2img_blur)
    
    cv2.imwrite('R1-2.png', q1_2img_blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

dataPreprocessing()
