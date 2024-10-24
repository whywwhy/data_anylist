import cv2
from matplotlib import pyplot as plt

def matplotlib():
    img = cv2.imread('sunny.png', cv2.IMREAD_COLOR)

    fig = plt.figure()
    # fig.canvas.set_window_title('JetsonNano_Matplot')
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    fig = plt.figure()
    # fig.canvas.set_window_title('JetsonNano_Matplot')
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])
    plt.imshow(img2)
    plt.xticks([])
    plt.yticks([])
    plt.show()

matplotlib()