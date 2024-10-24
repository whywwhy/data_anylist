import cv2
import numpy as np

image = cv2.imread('bao.png')

height, width, _ = image.shape

gray_iamge = np.zeros((height,width), dtype = np.uint8)

for y in range(0, height):
    
    for x in range(0, width):
        
        blue, green, red = image[y, x]
        gray_value = int(0.2989 * red + 0.5870 * green + 0.1140 * blue)
        
        if gray_value > 100:
            gray_iamge[y, x] = 255
        else:
            gray_iamge[y, x] = 0
        
cv2.imwrite('bao.jpg', gray_iamge)
cv2.imshow('Gray Image', gray_iamge)

cv2.waitKey(0)
cv2.destroyAllWindows