import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

def sobel_operator(image):
    gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_x = cv2.convertScaleAbs(gradient_x)
    gradient_y = cv2.convertScaleAbs(gradient_y)
    magnitude = cv2.addWeighted(gradient_x, 0.5, gradient_y, 0.5, 0)
    return gradient_x, gradient_y, magnitude

image = cv2.imread('Cameraman.bmp', 0)
gradient_x, gradient_y, magnitude = sobel_operator(image)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].imshow(image, cmap='gray')
axs[0, 0].set_title('原图')
axs[0, 1].imshow(gradient_x, cmap='gray')
axs[0, 1].set_title('水平梯度')
axs[1, 0].imshow(gradient_y, cmap='gray')
axs[1, 0].set_title('竖直梯度')
axs[1, 1].imshow(magnitude, cmap='gray')
axs[1, 1].set_title('梯度图像')
plt.tight_layout()
plt.show()
