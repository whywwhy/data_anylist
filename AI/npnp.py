import numpy as np 
import matplotlib.pyplot as plt

def histogram_equlization(imgae):
    hist, bins = np.histogram(imgae.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf*hist.max() / cdf.max()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    equalized_iamge = cdf[image]
    return equalized_iamge 
image = plt.imread('input.jpg')

if len(image.shape) == 3:
    image = np.dot(image[...,:3], [0.299, 0.587, 0.114])
equalized_iamge = histogram_equlization(image)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(equalized_iamge, cmap='gray')
plt.title('Equlized Image')
plt.show()