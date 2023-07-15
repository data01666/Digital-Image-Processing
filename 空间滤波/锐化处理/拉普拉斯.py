import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

def laplacian_operator(image):
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)
    sharpened = cv2.addWeighted(image, 0.25, laplacian, 0.75, 0)
    return laplacian, sharpened

image = cv2.imread('Cameraman.bmp', 0)
laplacian, sharpened = laplacian_operator(image)

fig, axs = plt.subplots(1, 3, figsize=(12, 4))
axs[0].imshow(image, cmap='gray')
axs[0].set_title('原图')
axs[1].imshow(laplacian, cmap='gray')
axs[1].set_title('拉普拉斯图像')
axs[2].imshow(sharpened, cmap='gray')
axs[2].set_title('锐化增强图像')
plt.show()
