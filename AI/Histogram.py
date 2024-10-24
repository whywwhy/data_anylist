import cv2
import numpy as np
from matplotlib import pyplot as plt

def histogram():
    img1 = cv2.imread('gary-img.png')
    img2 = cv2.imread('bao.png')
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    def cvt(i):
        b, g, r = cv2.split(i)
        i = cv2.merge([r, g, b])
        return i
    
    img1 = cvt(img1)
    img2 = cvt(img2)

    h1, w1 = img1_gray.shape[:2]
    h2, w2 = img2_gray.shape[:2]

    his1_for = np.zeros(256)
    his2_for = np.zeros(256)
    his1_odd = np.zeros(256)
    his2_odd = np.zeros(256)
    hist1_mid = np.zeros(256)
    hist2_mid = np.zeros(256)

    for y in range(h1):
        for x in range(w1):
            i = img1_gray[y, x]
            his1_for[i] += 1
            if x % 2 != 0 and y % 2 != 0:
                his1_odd[i] += 1

    for y in range(h2):
        for x in range(w2):
            i = img2_gray[y, x]
            his2_for[i] += 1
            if x % 2 != 0 and y % 2 != 0:
                his2_odd[i] += 1

    h1s = h1//5
    h1e = int(h1*(4/5))
    w1s = 0
    w1e = int(w1*(4/5))

    h2s = h2//5
    h2e = int(h2*(4/5))
    w2s = 0
    w2e = int(w2*(4/5))

    for y in range(h1s, h1e):
        for x in range(w1s, w1e):
            hist1_mid[img1_gray[y, x]] += 1
    
    for y in range(h2s, h2e):
        for x in range(w2s, w2e):
            hist2_mid[img2_gray[y, x]] += 1

            ###짱배채희###
            #(wle>=wls and wls<=wle) and (h1s<=h1)

    # for y in range(h1):
    #     for x in range(w1):
    #         i = img1_gray[y, x]
    #         his1_for[i] += 1
    #         if x %2 == 1 and y%2==1:
    #             his1_odd[i]+=1
    #         if h1s>=x and (h1e<=y and y<=w1s):
    #             hist1_mid[i]+=1
                

    fig = plt.figure()

    hist1 = cv2.calcHist([img1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([img2_gray], [0], None, [256], [0, 256])
    
    plt.subplot(621), plt.imshow(img1), plt.title('Image_A'), plt.xticks([]), plt.yticks([])
    plt.subplot(622), plt.imshow(img2), plt.title('Image_B'), plt.xticks([]), plt.yticks([])

    plt.subplot(623), plt.plot(hist1), plt.xlim([0, 256])
    plt.subplot(624), plt.plot(hist2), plt.xlim([0, 256])
    
    plt.subplot(625), plt.plot(his1_for), plt.xlim([0, 256])
    plt.subplot(626), plt.plot(his2_for), plt.xlim([0, 256])
    
    plt.subplot(627), plt.plot(his1_odd), plt.xlim([0, 256])
    plt.subplot(628), plt.plot(his2_odd), plt.xlim([0, 256])

    plt.subplot(629), plt.plot(hist1_mid), plt.xlim([0, 256])
    plt.subplot(6, 2, 10), plt.plot(hist2_mid), plt.xlim([0, 256])

    plt.subplot(6, 2, 11), plt.imshow(img1[h1s:h1e, w1s:w1e]), plt.title('Image_A Zoomed'), plt.xticks([]), plt.yticks([])
    plt.subplot(6, 2, 12), plt.imshow(img2[h2s:h2e, w2s:w2e]), plt.title('Image_B Zoomed'), plt.xticks([]), plt.yticks([])

    plt.tight_layout()
    plt.show()

histogram()
